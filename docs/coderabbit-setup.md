# CodeRabbit Setup

Canvify uses [CodeRabbit](https://coderabbit.ai) as an AI reviewer on every
pull request, alongside human review.

## How it's installed

CodeRabbit is a **GitHub App**, not a GitHub Actions workflow. It was
installed once, at the organization level, scoped to this repository only
(Settings → Applications → coderabbitai → Configure to change repo access).
It requires no CI/CD job to function.

## How it's configured

Behavior is controlled by [`.coderabbit.yaml`](../.coderabbit.yaml) in the
repo root. Key settings for this project:

| Setting | Value | Why |
|---|---|---|
| `base_branches` | `dev`, `feature/.*`, `fix/.*`, `hotfix/.*` | By default CodeRabbit only reviews PRs into the *default* branch (`main`). Since our workflow merges into `dev` first (see [branching-strategy.md](branching-strategy.md)), this extends auto-review to those branches too. |
| `path_instructions` | custom rules for `backend/agents/**`, `backend/api/gateway.py`, `frontend/**/*.tsx` | Points CodeRabbit at the specific architectural rules of this project (e.g. agents must only communicate through shared state, never call each other directly). |
| `auto_pause_after_reviewed_commits` | `5` | Avoids burning review quota on branches with many small WIP commits. |

**Important:** CodeRabbit reads `.coderabbit.yaml` from the PR's *target*
branch. If you ever change this file, make sure the change is present on
**both** `main` and `dev`, or reviews on `dev` will silently stop respecting
it again.

## Triggering a review manually

If a review is skipped or you want a fresh pass:

```
@coderabbitai review          # incremental review of new changes
@coderabbitai full review     # re-review the entire PR from scratch
@coderabbitai configuration   # show the config CodeRabbit is actually using
```

Comment any of these directly on the PR.

## Troubleshooting

**"Review skipped — auto reviews are disabled on base/target branches
other than the default branch"** → the target branch isn't in
`base_branches` in `.coderabbit.yaml`, or that file isn't present on the
target branch yet. See the table above.

**Config changes don't seem to apply** → run `@coderabbitai configuration`
on an open PR and compare the output to `.coderabbit.yaml`. A YAML syntax
error causes the whole file to be silently ignored.
