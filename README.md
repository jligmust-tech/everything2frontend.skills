# everything2frontend.skills

> Turn every question or problem into a **frontend** — something you can *see*, *touch*, and *handle*.

The core idea: any problem, no matter the domain, can be rewritten in the
**frontend language** — state, inputs, transforms, view, and verification. Once
it is in that language it can be rendered, manipulated, and checked.

```
Problem  ──▶  Frontend IR  ──▶  render target
                │                  ├── interactive app   (live, editable)
                │                  ├── visual explainer  (diagram / chart / steps)
                └──────────────────┴── frontend spec     (state + component design)
```

## Install

This repo ships the same skills in several agent dialects.

### Claude Code / Claude skills
Copy any skill folder into your skills directory and it is picked up by
frontmatter in `SKILL.md`:

```powershell
# per-project
New-Item -ItemType Directory -Force .claude\skills | Out-Null
Copy-Item -Recurse skills\* .claude\skills\
# or global
Copy-Item -Recurse skills\* "$env:USERPROFILE\.claude\skills\"
```

### Codex / OpenAI Codex CLI
Codex reads `AGENTS.md`. The root file explains how to use the collection, and
each skill ships its own `AGENTS.md` so it can be dropped anywhere:

```
AGENTS.md                      # repo guide for Codex + any general agent
skills/<skill>/AGENTS.md       # per-skill instructions (no frontmatter)
skills/<skill>/SKILL.md        # canonical, detailed skill body
```

### Other general agents
Any agent that can read files can use these skills: give it
`skills/everything2frontend/SKILL.md` (canonical spec) plus the `references/`
and `assets/` folders next to it. `AGENTS.md` is the portable entry point.

## Layout

```
everything2frontend.skills/
├── AGENTS.md                         # portable instructions for all agents
├── README.md
└── skills/
    ├── everything2frontend/          # CORE router skill (all 3 modes)
    │   ├── SKILL.md                  # canonical Claude-style skill
    │   ├── AGENTS.md                 # Codex / general-agent entry
    │   ├── references/
    │   │   ├── frontend-ir.md        # the Problem -> Frontend IR mapping
    │   │   ├── modes.md              # interactive / visual / spec
    │   │   └── quality-bar.md        # acceptance + verification rules
    │   ├── assets/
    │   │   ├── template-interactive.html
    │   │   ├── template-visual.html
    │   │   └── template-spec.md
    │   └── scripts/
    │       ├── scaffold.py           # start a deliverable from a template
    │       └── validate_output.py    # self-containment / sanity checker
    ├── problem2interactive/          # focused mode skill
    ├── problem2visual/               # focused mode skill
    └── problem2spec/                 # focused mode skill
```

## Quick start

```powershell
# turn any problem into a runnable interactive page
python skills\everything2frontend\scripts\scaffold.py `
  --mode interactive `
  --problem "Which mobile plan is cheapest for my usage?" `
  --slug mobile-plan-picker `
  --out .\out

python skills\everything2frontend\scripts\validate_output.py .\out\mobile-plan-picker.html
```

Then ask your agent: *"Use the everything2frontend skill to fill in out/mobile-plan-picker.html."*

## License

MIT — see `LICENSE`.
