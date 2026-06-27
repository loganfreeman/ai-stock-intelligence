---
name: earnings-reviewer
description: Reviews quarterly or annual earnings for a public company with deterministic deltas, accounting checks, guidance changes, and a concise value-investing verdict.
use_when: The user asks to analyze an earnings release, 10-Q, 10-K, shareholder letter, conference call transcript, or quarterly/annual financial update for a public company.
---

# Earnings Reviewer

Use this skill for fast, evidence-bound earnings analysis. Prioritize what changed versus the prior period, prior year, management guidance, and the long-term thesis.

## Inputs

Gather:
- Company, ticker, fiscal period, filing date, and reporting currency.
- Current earnings release or filing.
- Comparable prior quarter and prior-year period.
- Prior guidance and updated guidance.
- Consensus expectations only when the user asks or the source is available.

## Tool Usage

Use `tools/delta_analyzer.py` when current and comparison metrics are available as JSON:

```bash
python3 skills/earnings-reviewer/tools/delta_analyzer.py --current current.json --prior prior.json --year-ago year_ago.json
```

The tool uses only the Python standard library. If Python is unavailable, calculate the deltas manually and state that the script was not run.

## Review Workflow

1. **Data Audit**: Verify revenue, operating income, net income, EPS, free cash flow, margins, cash, debt, and share count.
2. **Delta Table**: Show quarter-over-quarter and year-over-year changes in absolute and percentage terms.
3. **Quality of Earnings**: Separate recurring operations from one-time items, accounting changes, working-capital swings, and stock-based compensation.
4. **Guidance and Tone**: Compare prior guidance to actuals and updated guidance. Identify changes in language, demand signals, pricing, backlog, churn, or supply constraints.
5. **Thesis Impact**: Decide whether the quarter strengthens, weakens, or leaves unchanged the long-term investment thesis.
6. **Verdict**: Use `Pass`, `Fail`, or `Gray Zone`; do not output conversational stock-pick language.

## Output Contract

Return Markdown with exactly these sections:

```markdown
# Earnings Review: <Company> (<Ticker>) <Fiscal Period>

## Data Audit
| Metric | Current | Prior quarter | Year ago | Source | Confidence |

## Delta Table
| Metric | QoQ change | YoY change | Interpretation |

## Quality of Earnings

## Guidance and Management Tone

## Inversion Triggers

## Thesis Impact
Verdict: Strengthened/Weakened/Unchanged

## Absolute Verdict Matrix
| Dimension | Pass | Fail | Gray Zone | Notes |

## Research Verdict
Verdict: Pass/Fail/Gray Zone
Confidence: High/Medium/Low
```

Keep the report compact. Prefer clear deltas and disconfirming evidence over broad commentary.
