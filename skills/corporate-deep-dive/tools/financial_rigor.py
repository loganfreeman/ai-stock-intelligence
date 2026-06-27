#!/usr/bin/env python3
"""Dependency-free financial sanity checks for equity research skills."""

from __future__ import annotations

import argparse
import json
import math
import sys
import urllib.request
from decimal import Decimal, InvalidOperation
from pathlib import Path


def decimal(value: object) -> Decimal:
    try:
        return Decimal(str(value).replace(",", "").strip())
    except (InvalidOperation, AttributeError) as exc:
        raise argparse.ArgumentTypeError(f"invalid decimal: {value}") from exc


def load_json(path_or_url: str) -> object:
    if path_or_url.startswith(("http://", "https://")):
        with urllib.request.urlopen(path_or_url, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    return json.loads(Path(path_or_url).read_text(encoding="utf-8"))


def percent(numerator: Decimal, denominator: Decimal) -> Decimal | None:
    if denominator == 0:
        return None
    return (numerator / denominator) * Decimal("100")


def audit(args: argparse.Namespace) -> int:
    data = load_json(args.input)
    if not isinstance(data, dict):
        raise SystemExit("audit input must be a JSON object")

    metrics = data.get("metrics", data)
    if not isinstance(metrics, dict):
        raise SystemExit("metrics must be a JSON object")

    warnings: list[str] = []
    output: dict[str, object] = {"checks": {}, "warnings": warnings}

    revenue = maybe_decimal(metrics.get("revenue"))
    net_income = maybe_decimal(metrics.get("net_income"))
    operating_income = maybe_decimal(metrics.get("operating_income"))
    free_cash_flow = maybe_decimal(metrics.get("free_cash_flow"))
    cash = maybe_decimal(metrics.get("cash"))
    debt = maybe_decimal(metrics.get("debt"))
    shares = maybe_decimal(metrics.get("shares_outstanding"))
    price = maybe_decimal(metrics.get("share_price"))
    market_cap = maybe_decimal(metrics.get("market_cap"))

    checks: dict[str, object] = output["checks"]  # type: ignore[assignment]

    if revenue is not None and revenue <= 0:
        warnings.append("revenue is zero or negative")

    if revenue and operating_income is not None:
        checks["operating_margin_pct"] = to_float(percent(operating_income, revenue))

    if revenue and net_income is not None:
        checks["net_margin_pct"] = to_float(percent(net_income, revenue))

    if market_cap is None and shares is not None and price is not None:
        market_cap = shares * price
        checks["computed_market_cap"] = to_float(market_cap)

    if market_cap is not None and free_cash_flow is not None:
        checks["fcf_yield_pct"] = to_float(percent(free_cash_flow, market_cap))
        if free_cash_flow <= 0:
            warnings.append("free cash flow is zero or negative")

    if cash is not None and debt is not None:
        checks["net_cash"] = to_float(cash - debt)

    sources = data.get("sources")
    if isinstance(sources, list):
        output["source_reconciliation"] = reconcile_sources(sources, Decimal(str(args.tolerance)))

    print(json.dumps(output, indent=2, sort_keys=True))
    return 1 if warnings and args.strict else 0


def maybe_decimal(value: object) -> Decimal | None:
    if value in (None, ""):
        return None
    return decimal(value)


def to_float(value: Decimal | None) -> float | None:
    if value is None:
        return None
    return float(value)


def reconcile_sources(sources: list[object], tolerance: Decimal) -> dict[str, object]:
    by_metric: dict[str, list[tuple[str, Decimal]]] = {}
    for source in sources:
        if not isinstance(source, dict):
            continue
        name = str(source.get("name", "unnamed"))
        values = source.get("metrics", {})
        if not isinstance(values, dict):
            continue
        for metric, value in values.items():
            parsed = maybe_decimal(value)
            if parsed is not None:
                by_metric.setdefault(metric, []).append((name, parsed))

    result: dict[str, object] = {}
    for metric, values in by_metric.items():
        nums = [item[1] for item in values]
        low = min(nums)
        high = max(nums)
        spread = Decimal("0") if high == 0 else abs(high - low) / abs(high)
        result[metric] = {
            "sources": [{"name": name, "value": to_float(value)} for name, value in values],
            "within_tolerance": spread <= tolerance,
            "spread_pct": to_float(spread * Decimal("100")),
        }
    return result


def reverse_dcf(args: argparse.Namespace) -> int:
    market_cap = decimal(args.market_cap)
    fcf = decimal(args.fcf)
    years = int(args.years)
    terminal_multiple = decimal(args.terminal_multiple)
    discount_rate = decimal(args.discount_rate)

    if fcf <= 0:
        raise SystemExit("fcf must be positive")
    if years <= 0:
        raise SystemExit("years must be positive")

    implied_growth = solve_growth(
        target=float(market_cap),
        fcf=float(fcf),
        years=years,
        terminal_multiple=float(terminal_multiple),
        discount_rate=float(discount_rate),
    )

    result = {
        "market_cap": to_float(market_cap),
        "starting_fcf": to_float(fcf),
        "years": years,
        "terminal_multiple": to_float(terminal_multiple),
        "discount_rate_pct": float(discount_rate * Decimal("100")),
        "implied_annual_fcf_growth_pct": implied_growth * 100,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def solve_growth(target: float, fcf: float, years: int, terminal_multiple: float, discount_rate: float) -> float:
    low = -0.90
    high = 1.00
    for _ in range(160):
        mid = (low + high) / 2
        value = present_value(fcf, mid, years, terminal_multiple, discount_rate)
        if value < target:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def present_value(fcf: float, growth: float, years: int, terminal_multiple: float, discount_rate: float) -> float:
    total = 0.0
    current = fcf
    for year in range(1, years + 1):
        current *= 1 + growth
        total += current / math.pow(1 + discount_rate, year)
    terminal_value = current * terminal_multiple
    total += terminal_value / math.pow(1 + discount_rate, years)
    return total


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Financial rigor checks for value investing research.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    audit_parser = subparsers.add_parser("audit", help="Audit a JSON metric bundle.")
    audit_parser.add_argument("--input", required=True, help="Path or HTTPS URL to JSON data.")
    audit_parser.add_argument("--tolerance", default="0.02", help="Source reconciliation tolerance as a decimal.")
    audit_parser.add_argument("--strict", action="store_true", help="Exit non-zero when warnings are present.")
    audit_parser.set_defaults(func=audit)

    dcf_parser = subparsers.add_parser("reverse-dcf", help="Solve implied FCF growth from market cap.")
    dcf_parser.add_argument("--market-cap", required=True)
    dcf_parser.add_argument("--fcf", required=True)
    dcf_parser.add_argument("--years", default="10")
    dcf_parser.add_argument("--terminal-multiple", default="15")
    dcf_parser.add_argument("--discount-rate", default="0.10")
    dcf_parser.set_defaults(func=reverse_dcf)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
