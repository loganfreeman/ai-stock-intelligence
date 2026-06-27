#!/usr/bin/env python3
"""Dependency-free earnings delta analyzer."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path


def decimal(value: object) -> Decimal | None:
    if value in (None, ""):
        return None
    try:
        return Decimal(str(value).replace(",", "").strip())
    except (InvalidOperation, AttributeError):
        return None


def load_metrics(path: str) -> dict[str, Decimal]:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise SystemExit(f"{path} must contain a JSON object")
    metrics = raw.get("metrics", raw)
    if not isinstance(metrics, dict):
        raise SystemExit(f"{path} metrics must be a JSON object")
    parsed = {}
    for key, value in metrics.items():
        number = decimal(value)
        if number is not None:
            parsed[key] = number
    return parsed


def format_delta(current: Decimal, comparison: Decimal | None) -> dict[str, float | None]:
    if comparison is None:
        return {"absolute": None, "percent": None}
    absolute = current - comparison
    pct = None if comparison == 0 else (absolute / abs(comparison)) * Decimal("100")
    return {"absolute": float(absolute), "percent": None if pct is None else float(pct)}


def analyze(args: argparse.Namespace) -> int:
    current = load_metrics(args.current)
    prior = load_metrics(args.prior) if args.prior else {}
    year_ago = load_metrics(args.year_ago) if args.year_ago else {}

    output: dict[str, object] = {"metrics": {}}
    metrics: dict[str, object] = output["metrics"]  # type: ignore[assignment]

    for key in sorted(current):
        value = current[key]
        metrics[key] = {
            "current": float(value),
            "qoq": format_delta(value, prior.get(key)),
            "yoy": format_delta(value, year_ago.get(key)),
        }

    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare current earnings metrics against prior periods.")
    parser.add_argument("--current", required=True, help="Current-period JSON metrics.")
    parser.add_argument("--prior", help="Prior-quarter JSON metrics.")
    parser.add_argument("--year-ago", help="Prior-year-period JSON metrics.")
    return parser


def main() -> int:
    return analyze(build_parser().parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
