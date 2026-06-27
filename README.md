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

```text
Use investment-research to analyze Costco as a long-term compounder.
```

```text
Use bottleneck-hunter to find second-order public-company beneficiaries of AI data-center buildout.
```

```text
Use earnings-review to analyze NVIDIA's latest quarterly results against guidance and the long-term thesis.
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
