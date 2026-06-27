---
name: corporate-deep-dive
description: Executes an adversarial value-investing research dialectic on a public equity ticker using Buffett, Munger, Yongping, and Li Lu personas.
use_when: The user requests fundamental equity research, investment evaluations, competitive moat analysis, management quality analysis, valuation, or long-term risk assessment on a specific company or stock ticker.
---

# Corporate Deep Dive

Use this skill for public-equity research where the user wants a durable business-quality judgment rather than a short-term price call.

## Context Assembly

1. Identify the company, ticker, exchange, reporting currency, and user time horizon.
2. Use current primary sources when possible: latest 10-K/20-F, latest 10-Q/6-K, earnings release, investor presentation, proxy, and company investor relations pages.
3. Read the investor reference files only after this skill triggers:
   - `references/buffett.md` for owner earnings, moat durability, and capital allocation.
   - `references/munger.md` for incentives, inversion, and business-model fragility.
   - `references/yongping.md` for consumer value, pricing restraint, and long-term product truth.
   - `references/lilu.md` for circle of competence, downside protection, and long compounding.
4. If numeric data is supplied or extracted, validate it with `tools/financial_rigor.py` before relying on it.

## Data Discipline

- Separate verified facts from estimates and judgments.
- Cite exact filing periods and source dates.
- If sources disagree, show the discrepancy in the Data Audit and use the most conservative reasonable interpretation.
- Do not invent financial figures. If a number cannot be verified, mark it `unverified`.
- Do not issue a buy/sell recommendation. Produce research verdicts only.

## Tool Usage

Run the financial tool for deterministic checks when data is available:

```bash
python3 skills/corporate-deep-dive/tools/financial_rigor.py audit --input data/company_metrics.json
python3 skills/corporate-deep-dive/tools/financial_rigor.py reverse-dcf --market-cap 100000000000 --fcf 5000000000 --years 10 --terminal-multiple 15 --discount-rate 0.10
```

The tool uses only the Python standard library. If the runtime cannot execute Python, do the same calculations manually and state that the script could not be run.

## Dialectic Workflow

1. **Data Audit**: Build a compact evidence table covering revenue, operating income, net income, free cash flow, cash, debt, shares, market cap, return on capital, and segment mix.
2. **Base Business Map**: Explain how the company makes money, what customers value, what must remain true, and where economics could break.
3. **Four Investor Lenses**: Produce independent assessments using the reference profiles. Each lens must include:
   - Core thesis.
   - Disconfirming evidence.
   - One decisive question.
   - Verdict: `Pass`, `Fail`, or `Gray Zone`.
4. **Inversion Triggers**: List conditions that would make the bullish case wrong, including accounting, competition, regulation, capital allocation, and customer behavior.
5. **Valuation Reality Check**: Compare market expectations with owner earnings, free cash flow yield, reinvestment runway, and reverse DCF assumptions.
6. **Team Lead Synthesis**: Reconcile disagreements between lenses and produce the final verdict matrix.

## Output Contract

Return Markdown with exactly these sections:

```markdown
# Corporate Deep Dive: <Company> (<Ticker>)

## Data Audit
| Metric | Current value | Period | Source | Confidence |

## Business Map

## Buffett Lens
Verdict: Pass/Fail/Gray Zone

## Munger Lens
Verdict: Pass/Fail/Gray Zone

## Yongping Lens
Verdict: Pass/Fail/Gray Zone

## Li Lu Lens
Verdict: Pass/Fail/Gray Zone

## Inversion Triggers

## Valuation Reality Check

## Absolute Verdict Matrix
| Dimension | Pass | Fail | Gray Zone | Notes |

## Research Verdict
Verdict: Pass/Fail/Gray Zone
Confidence: High/Medium/Low
What would change my mind:
```

Keep the conclusion blunt and evidence-bound. Avoid promotional language, conversational filler, and ambiguous stock-pick phrasing.
