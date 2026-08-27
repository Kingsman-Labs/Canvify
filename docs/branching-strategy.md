# Canvify — Git Branching Strategy & DevOps Workflow

**Project:** Canvify (Autonomous Multi-Agent AI Startup Co-Founder)
**Competition:** CodeSplash '26 — Agentic AI Phase
**Repository model:** Monorepo (frontend + backend in one repo)
**Team size assumption:** 4–5 developers, 10-day sprint

---

## 1. Why This Model (Not Full Git Flow)

Classic Git Flow (with `release/*`, `hotfix/*`, versioned tags, etc.) is built for
long-lived software products with scheduled releases. A 10-day hackathon sprint
with a small team doesn't need that overhead — it just adds ceremony that slows
a small team down.

Canvify uses a **simplified 3-tier model**: `main` → `dev` → `feature/*`.
It gives you the two things that actually matter under a deadline:

1. **`main` always stays demo-safe** — judges or mentors can check out `main`
   at any moment and see something that runs.
2. **Parallel work doesn't block each other** — 8 agents + frontend + infra
   can all be built at the same time without one broken agent stopping
   everyone else.

---

## 2. Branch Types

| Branch | Purpose | Lives forever? | Who can push directly? |
|---|---|---|---|
| `main` | Judge/demo-facing, always working | Yes | No one — PR only |
| `dev` | Integration branch, all features merge here first | Yes | No one — PR only |
| `feature/*` | One agent / one component, one branch | No — deleted after merge | Owner of that branch |
| `fix/*` | Non-urgent bug fix found during integration | No — deleted after merge | Anyone |
| `hotfix/*` | Urgent fix needed directly on `main` (e.g. demo-breaking bug found right before submission) | No — deleted after merge | Anyone, with immediate review |

---

## 3. Branch Naming Convention

Use lowercase, hyphen-separated names. Prefix tells you the *type*, the rest
tells you the *scope*.

```
feature/orchestrator
feature/idea-validator
feature/market-research
feature/business-model
feature/marketing-strategy
feature/financial-analysis
feature/validation-agent
feature/report-generator
feature/api-gateway
feature/frontend-idea-input
feature/frontend-progress-dashboard
feature/frontend-report-viewer
feature/ci-cd-pipeline
feature/genome-seed-data

fix/pdf-export-crash
fix/websocket-disconnect

hotfix/api-key-leak
hotfix/deploy-broken
```

**Rule of thumb:** if you can't name the branch after a single Section 4.1
agent, a single frontend component, or a single infra task, the branch is
probably trying to do too much — split it.

---

## 4. Team → Branch Assignment Map

Assign **one owner per branch** so there's never a question of who resolves
conflicts on it. Adjust names to your actual team.

| Component | Branch | Suggested Owner |
|---|---|---|
| Orchestrator + shared state schema | `feature/orchestrator` | Backend lead (build this **first**, see Section 5) |
| API Gateway (auth, rate limit, validation) | `feature/api-gateway` | Backend lead |
| Idea Validator Agent | `feature/idea-validator` | Dev A |
| Market Research Agent | `feature/market-research` | Dev A |
| Business Model Agent | `feature/business-model` | Dev B |
| Marketing Strategy Agent | `feature/marketing-strategy` | Dev B |
| Financial Analysis Agent | `feature/financial-analysis` | Dev B |
| Validation Agent | `feature/validation-agent` | Backend lead (build this **last**, see Section 5) |
| Report Generator Agent | `feature/report-generator` | Dev A |
| Frontend — idea input + dashboard | `feature/frontend-progress-dashboard` | Dev C |
| Frontend — report viewer + charts | `feature/frontend-report-viewer` | Dev C |
| CI/CD + deployment | `feature/ci-cd-pipeline` | DevOps/integration owner |

---

## 5. Critical Rule: Schema-First, Not Agent-First

**Do not let 8 people branch off `dev` on Day 1 and start editing
`backend/graph/state.py` independently.** That file is the shared contract
every agent reads and writes to — if everyone edits it in parallel, you get
merge-conflict hell on Day 3.

**Correct order:**

1. Backend lead builds `feature/orchestrator` first — this includes
   finalizing `graph/state.py` (the `AgentState` shape) and the empty
   `graph/workflow.py` skeleton with all 8 nodes registered as no-ops.
2. That branch merges to `dev` **before** anyone else branches off.
3. **Now** all 7 agent-owners branch off the updated `dev` — everyone builds
   against the same, already-agreed state schema.
4. `feature/validation-agent` is built **last** (or second-to-last), because
   it reads the output of every other agent — it can only be finished once
   the others' output shapes are stable.

This single rule prevents the majority of merge conflicts you'd otherwise hit.

---

## 6. One-Time Setup (Day 1, Repo Owner Only)

```bash
# 1. Push the scaffold to main
unzip Canvify_Project_Scaffold.zip
cd canvify
git init
git add .
git commit -m "chore: initial project scaffold"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main

# 2. Create dev from main
git checkout -b dev
git push -u origin dev
```

### Configure branch protection (GitHub → Settings → Branches)

**Rule for `main`:**
- ✅ Require a pull request before merging
- ✅ Require approvals — minimum 1 reviewer
- ✅ Require status checks to pass before merging (link the CI job from Section 11)
- ✅ Do not allow direct pushes (no exceptions, including admins)

**Rule for `dev`:**
- ✅ Require a pull request before merging
- ✅ Require status checks to pass before merging
- ⬜ Approvals optional if your team is small and trusts each other — but
  recommended at least for the `feature/orchestrator` merge (Section 5)

---

## 7. Daily Developer Workflow (Every Team Member, Every Day)

```bash
# Start of day — sync with dev
git checkout dev
git pull origin dev

# Create your feature branch (only once per component)
git checkout -b feature/idea-validator

# ... write code ...

# Commit in small, meaningful chunks (see Section 8 for message format)
git add backend/agents/idea_validator.py
git commit -m "feat(idea-validator): add viability scoring logic"

# Push regularly — don't wait until the component is 100% done
git push -u origin feature/idea-validator
```

### Before opening a PR — sync your branch with the latest `dev`

Do this daily if `dev` is moving fast, so conflicts are small and frequent
instead of one huge conflict at the end:

```bash
git checkout dev
git pull origin dev
git checkout feature/idea-validator
git merge dev
# resolve any conflicts locally, then:
git push
```

---

## 8. Commit Message Convention

Use [Conventional Commits](https://www.conventionalcommits.org/) — short,
consistent, and it makes the PR history genuinely readable during judging Q&A.

```
<type>(<scope>): <short description>

feat(idea-validator): add Startup Genome matching via ChromaDB
fix(report-generator): correct PDF page-break on long risk tables
test(validation-agent): add feedback-loop trigger test
docs(readme): add local setup instructions
chore(ci): add pytest step to workflow
refactor(orchestrator): simplify routing logic
```

| Type | When to use |
|---|---|
| `feat` | New functionality |
| `fix` | Bug fix |
| `test` | Adding/fixing tests |
| `docs` | Documentation only |
| `chore` | Tooling, config, dependencies |
| `refactor` | Code change with no behavior change |

---

## 9. Pull Request Process

**Every PR — whether into `dev` or `main` — must include:**

1. **Title** in the same `type(scope): description` format as commits.
2. **What changed** — 2-3 lines.
3. **How it was tested** — which sample startup idea(s) you ran it against,
   or which `tests/test_*.py` file covers it.
4. **Linked branch owner as reviewer** (see Section 4 table) if merging
   into `dev`; **any second team member** if merging into `main`.

**Reviewer checklist before approving:**
- [ ] Code runs locally (`uvicorn main:app --reload` doesn't crash)
- [ ] No API keys or secrets committed (check `git diff` for stray `.env` values)
- [ ] New agent follows the existing pattern in `backend/agents/` (same
      input/output shape via `AgentState`)
- [ ] Relevant test file in `tests/` updated or added

---

## 10. Merge Strategy

| Merging into | Strategy | Why |
|---|---|---|
| `dev` | **Squash and merge** | Keeps `dev` history clean — one commit per feature, not 15 "wip" commits |
| `main` | **Merge commit** (no squash) | Preserves the full `dev` history so you can see exactly what shipped at each milestone |

On GitHub: set this per-PR using the dropdown next to the merge button, or
set repo-wide defaults under **Settings → General → Pull Requests**.

---

## 11. CI/CD Pipeline Per Branch

Update `.github/workflows/ci-cd.yml` to behave differently depending on
which branch triggered it:

- **Any `feature/*` or `fix/*` push** → run tests + lint only. No deploy.
- **Merge into `dev`** → run tests + deploy to a **staging** environment
  (Vercel preview + a separate Railway service) so the team can click-test
  the integrated system before it reaches `main`.
- **Merge into `main`** → run tests + deploy to **production** (the real
  Vercel + Railway URLs you'll submit to judges).

```yaml
name: CI/CD

on:
  push:
    branches: [main, dev, "feature/**", "fix/**"]
  pull_request:
    branches: [main, dev]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install backend deps
        run: pip install -r backend/requirements.txt
      - name: Run backend tests
        run: pytest tests/
      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: "20"
      - name: Install frontend deps
        run: cd frontend && npm install
      - name: Lint frontend
        run: cd frontend && npm run lint --if-present

  deploy-staging:
    needs: test
    if: github.ref == 'refs/heads/dev'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploy backend to Railway staging service"
        # TODO: railway deploy --service canvify-backend-staging
      - run: echo "Vercel auto-deploys a preview URL for this branch already"

  deploy-production:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploy backend to Railway production service"
        # TODO: railway deploy --service canvify-backend-prod
      - run: echo "Vercel auto-deploys production from main already"
```

> Vercel and Railway both auto-detect branch pushes once connected to the
> repo — you mainly need the **staging vs production service split**
> configured once in their dashboards (two Railway services pointing at
> `backend/`, one tracking `dev`, one tracking `main`).

---

## 12. Environments & Secrets

| Environment | Tracks branch | Frontend URL | Backend URL | API keys |
|---|---|---|---|---|
| **Production** | `main` | Vercel production domain | Railway production service | Real keys, in Railway/Vercel dashboard secrets |
| **Staging** | `dev` | Vercel preview domain (auto) | Railway staging service | Same or separate keys — separate is safer so staging bugs can't burn production quota |
| **Local** | any local branch | `localhost:3000` | `localhost:8000` | `.env` / `.env.local`, never committed |

Never put real API keys in `.env.example` or `.env.local.example` — those
files stay as templates only (already set up this way in the scaffold).

---

## 13. Handling Merge Conflicts

Most conflicts in this project will happen in exactly two files:
`backend/graph/state.py` and `backend/graph/workflow.py` — because they're
the two files every agent touches.

**If you hit a conflict there:**
1. Don't just pick one side blindly — both changes are usually additive
   (someone added a new state field, someone else added a new node).
2. Keep both additions, re-run `pytest tests/` locally to confirm nothing
   broke.
3. If unsure, ping the branch owner from Section 4 rather than guessing.

---

## 14. Hotfix Process (Emergency Only)

Only use this if something is broken **on `main`** close to a deadline and
you can't wait for the normal `dev` → `main` cycle.

```bash
git checkout main
git pull origin main
git checkout -b hotfix/deploy-broken

# ... fix it ...

git commit -m "hotfix: fix broken Railway env variable"
git push -u origin hotfix/deploy-broken
```
Open a PR **directly into `main`**, get one quick review, merge, then
immediately back-merge the fix into `dev` too so they don't drift apart:

```bash
git checkout dev
git merge main
git push
```

---

## 15. Pre-Submission Freeze Checklist

Do this the evening before each deadline (proposal, semi-final, final):

- [ ] All planned `feature/*` branches merged into `dev`
- [ ] Full `dev` → `main` PR opened, tests green, merged
- [ ] Pull `main` fresh on a clean machine/folder and run it start-to-finish
      once, exactly like a judge would
- [ ] Confirm production URLs (Vercel + Railway) are live and match `main`
- [ ] Tag the commit for your own record:
  ```bash
  git checkout main
  git tag -a v1.0-semifinal -m "Semi-final submission"
  git push origin v1.0-semifinal
  ```
- [ ] After tagging, avoid pushing anything else to `main` until after judging

---

## 16. Quick Command Reference

```bash
# Daily sync
git checkout dev && git pull origin dev

# Start new work
git checkout -b feature/<name>

# Save progress
git add . && git commit -m "feat(<scope>): <description>"
git push -u origin feature/<name>

# Sync your branch with latest dev (do this often)
git checkout dev && git pull
git checkout feature/<name> && git merge dev

# See what branch you're on / all branches
git branch

# See what changed before committing
git status
git diff

# Delete a branch after it's merged (locally + remote)
git branch -d feature/<name>
git push origin --delete feature/<name>
```
