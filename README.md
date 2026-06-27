# AI Stock Intelligence Skills

Open Agent Skills for adversarial, value-investing equity research inspired by the ai-berkshire multi-agent dialectic.

This repository packages a portable skill bundle that can be installed into OpenAI Codex, Claude Code, GitHub Copilot, Cursor, and other tools that support the Agent Skills layout.

## Skills

| Skill | Use case |
| --- | --- |
| `corporate-deep-dive` | Full fundamental research on a public company or ticker using Buffett, Munger, Duan Yongping, and Li Lu lenses. |
| `earnings-reviewer` | Rapid review of quarterly or annual earnings releases, filings, and guidance updates. |

## Install

Clone the repository and copy the skills into your agent skills directory:

```bash
git clone https://github.com/your-username/ai-stock-intelligence.git
cp -r ai-stock-intelligence/skills/* ~/.codex/skills/
```

For project-local usage, add the repository as a submodule and point your agent runtime at the `skills/` folder:

```bash
git submodule add https://github.com/your-username/ai-stock-intelligence.git .agents/skills/ai-stock-intelligence
```

## Usage

Ask your agent for a concrete research task:

```text
Use corporate-deep-dive to evaluate Costco as a long-term compounder.
```

```text
Use earnings-reviewer to analyze NVIDIA's latest quarterly earnings release against prior guidance.
```

The skills require agents to separate verified data from judgment, run standard-library helper tools where useful, and return deterministic Markdown reports with explicit verdicts.

## Repository Layout

```text
ai-stock-intelligence/
├── LICENSE
├── README.md
├── index.json
└── skills/
    ├── corporate-deep-dive/
    │   ├── SKILL.md
    │   ├── references/
    │   │   ├── buffett.md
    │   │   ├── lilu.md
    │   │   ├── munger.md
    │   │   └── yongping.md
    │   └── tools/
    │       └── financial_rigor.py
    └── earnings-reviewer/
        ├── SKILL.md
        └── tools/
            └── delta_analyzer.py
```

## Distribution

The `index.json` file provides registry metadata for community installers. To publish broadly, submit the repository to skills.sh or an awesome-codex-skills index.

## Disclaimer

These skills are research aids, not financial advice. Outputs should cite sources, expose assumptions, and treat valuation as an input to judgment rather than a trading signal.
