# AI Stock Intelligence Skills

Open Agent Skills converted from [`xbtlin/ai-berkshire`](https://github.com/xbtlin/ai-berkshire), an AI-era value-investing research framework.

The repository mirrors every markdown skill in the upstream `skills/` directory as a standalone Agent Skill folder containing `SKILL.md`, making the workflows portable across OpenAI Codex, Claude Code, GitHub Copilot, Cursor, and other Agent Skills-compatible tools.

## Converted Skills

| Skill | Use case |
| --- | --- |
| `bottleneck-hunter` | Finds investable public companies created by second- and third-order supply-chain bottlenecks behind major physical supertrends. |
| `deep-company-series` | Builds a serialized deep-company research plan and article/report sequence for a public or private company. |
| `dyp-ask` | Analyzes a company through Duan Yongping-style product truth, customer value, pricing restraint, and long-term compounding questions. |
| `earnings-review` | Reviews a company earnings release or filing with value-investing discipline, data verification, deltas, and thesis-impact judgment. |
| `earnings-team` | Runs a multi-agent earnings-review team workflow that assigns specialist reviewers and synthesizes their findings. |
| `financial-data` | Collects, audits, reconciles, and structures financial data for public-company research workflows. |
| `industry-funnel` | Funnels an industry from broad universe to high-quality investable candidates using moat, economics, and valuation filters. |
| `industry-research` | Performs industry-level research, structure mapping, value-chain analysis, competitive dynamics, and investable-company identification. |
| `investment-checklist` | Applies a disciplined value-investing checklist to a company, including business quality, management, risk, and valuation gates. |
| `investment-research` | Produces a full value-investing research report for a company using Buffett, Munger, Duan Yongping, and Li Lu perspectives. |
| `investment-team` | Runs the multi-agent value-investing team dialectic and synthesizes specialist investor-persona conclusions. |
| `management-deep-dive` | Researches management quality, incentives, capital allocation, culture, governance, and evidence of owner-orientation. |
| `news-pulse` | Scans recent company, industry, and macro news for signal versus noise and investment-thesis impact. |
| `portfolio-review` | Reviews a portfolio through position sizing, thesis drift, risk concentration, valuation, and opportunity-cost lenses. |
| `private-company-research` | Researches a private company using available public sources, industry context, business model analysis, and risk checks. |
| `quality-screen` | Screens companies for high-quality business characteristics, durability, returns on capital, and reinvestment runway. |
| `thesis-tracker` | Tracks an investment thesis over time with milestones, disconfirming evidence, kill criteria, and review cadence. |
| `wechat-article` | Converts investment research into a structured long-form WeChat-style article while preserving evidence and nuance. |

## Install

Clone this repository and copy the skills into your agent skills directory:

```bash
git clone https://github.com/your-username/ai-stock-intelligence.git
cp -r ai-stock-intelligence/skills/* ~/.codex/skills/
```

For project-local usage, add the repository as a submodule and point your agent runtime at the `skills/` folder:

```bash
git submodule add https://github.com/your-username/ai-stock-intelligence.git .agents/skills/ai-stock-intelligence
```

## Usage

Ask your agent for one of the converted workflows:

### Single-company research

```text
Use investment-research to analyze Costco as a long-term compounder.
```

```text
Use investment-team to run a Buffett, Munger, Duan Yongping, and Li Lu investment committee on ASML.
```

```text
Use investment-checklist to evaluate whether MercadoLibre passes a value-investing quality checklist.
```

```text
Use management-deep-dive to assess the quality, incentives, and capital allocation record of Apple's management team.
```

### Earnings and news

```text
Use earnings-review to analyze NVIDIA's latest quarterly results against guidance and the long-term thesis.
```

```text
Use earnings-team to run a multi-agent review of Tesla's most recent earnings release and conference call.
```

```text
Use news-pulse to summarize the last 30 days of thesis-relevant news for TSMC and separate signal from noise.
```

### Industry and screening

```text
Use industry-research to map the global obesity-drug value chain and identify the most advantaged public companies.
```

```text
Use industry-funnel to narrow the cybersecurity sector to the five highest-quality compounder candidates.
```

```text
Use quality-screen to screen Japanese listed companies for high returns on capital, net cash balance sheets, and reinvestment runway.
```

```text
Use bottleneck-hunter to find second-order public-company beneficiaries of AI data-center buildout.
```

### Portfolio and thesis work

```text
Use portfolio-review to review this portfolio for concentration risk, thesis drift, and opportunity cost: COST 25%, BRK.B 20%, MSFT 20%, TSM 15%, CASH 20%.
```

```text
Use thesis-tracker to create a monitoring checklist and kill criteria for my long-term Adobe thesis.
```

```text
Use financial-data to collect and reconcile the last 5 years of revenue, operating income, net income, free cash flow, and shares outstanding for LVMH.
```

### Publishing and private-company research

```text
Use private-company-research to research Stripe from public sources, focusing on business model, competitors, and IPO-readiness signals.
```

```text
Use deep-company-series to design a 5-part research series on BYD for long-form publication.
```

```text
Use wechat-article to turn this investment memo into a polished Chinese WeChat article while preserving the evidence and caveats.
```

## Repository Layout

```text
ai-stock-intelligence/
├── LICENSE
├── README.md
├── index.json
└── skills/
    ├── bottleneck-hunter/
    │   └── SKILL.md
    ├── investment-research/
    │   └── SKILL.md
    └── ...
```

## Bundled Tools

The upstream `tools/` directory is mirrored at the repository root for discovery. Skills that call a tool also include local copies under `skills/<name>/tools/`, so commands such as `python3 tools/financial_rigor.py ...` work after copying an individual skill into an agent skills directory.

## Conversion Notes

- Each upstream `.md` file is converted to `skills/<name>/SKILL.md`.
- Frontmatter includes `name`, `description`, `use_when`, source URL, source repository, and source license.
- Upstream command semantics such as `$ARGUMENTS` are preserved and normalized in the adapter instructions.
- Claude-specific tool references should be mapped by the active agent to equivalent local browsing, shell, search, or file tools.

## Attribution

The converted skill workflows are derived from [`xbtlin/ai-berkshire`](https://github.com/xbtlin/ai-berkshire), copyright xbtlin, licensed under MIT.

## Disclaimer

These skills are research aids, not financial advice. Outputs should cite sources, expose assumptions, and treat valuation as an input to judgment rather than a trading signal.
