# Contributing to Canvify

## Branching

We use `main` → `dev` → `feature/*`. **Read
[docs/branching-strategy.md](docs/branching-strategy.md) before your first
PR** — in particular, the shared state schema (`backend/graph/state.py`)
must be stable on `dev` before you branch off to build an individual agent.

## Commits

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(idea-validator): add Startup Genome matching
fix(report-generator): correct PDF page-break on long tables
docs(readme): update setup instructions
```

## Opening a PR

1. Use the PR template (auto-filled when you open a PR).
2. Target `dev`, unless you're doing an approved hotfix directly to `main`.
3. **CodeRabbit reviews automatically** — read its comments before
   requesting a human reviewer. See
   [docs/coderabbit-setup.md](docs/coderabbit-setup.md) if no review
   appears.
4. Tag the branch owner (see the table in `docs/branching-strategy.md`) as
   reviewer.

## Before you push

- [ ] `pytest tests/` passes locally
- [ ] No secrets/API keys in your diff
- [ ] New agent follows the existing `AgentState` pattern in `backend/agents/`
