# Handoff

Overwrite this at the end of every session.

## Last updated
2026-10-03

## Owner's environment (set up and verified)
- Windows 11 + WSL2, Ubuntu 26.04.1 LTS. Open it from the Start menu ("Ubuntu") or `wsl ~` in PowerShell.
- Work only inside the Linux filesystem: `~/projects/reviewradar`. Never work under `/mnt/c`.
- VS Code connected to WSL (`code .` from the Ubuntu terminal; the terminal inside VS Code should show an Ubuntu prompt, not `PS ...`).
- `uv` 0.12.21, git 2.53, SSH key (with passphrase) added to GitHub. Git identity set; default branch `main`.
- The owner's Windows also has Python 3.12 and 3.14 installed globally (not used here).
- Owner is a beginner in the terminal and with Python tooling; explain every command. They answer prediction questions in chat and often reply "not sure": then escalate hints (hint, pseudocode, partial snippet, full answer with explanation). They sometimes ask for the answer directly; give it with a line-by-line explanation. They do their own commits; Claude opens and merges PRs on request.

## Done
- Environment, repo, continuity docs.
- Phase 0 is complete except the wrap-up (all merged to `main`, CI green):
  - `uv` project, Python pinned (`requires-python = ">=3.12,<3.13"`), `.gitignore` (including `data/*/*` and `models/*` with `.gitkeep` exceptions)
  - `ruff` + `pytest`, first smoke test (written by owner with `capsys`)
  - `pre-commit` hooks: trailing whitespace, end-of-file, YAML, large files, `ruff-check`, `ruff-format`, local `uv run pytest`
  - GitHub Actions CI: checkout, `setup-uv` (pinned `0.12.21`), `uv sync --locked`, `uv run pre-commit run --all-files`
  - Folder layout: `configs/`, `data/{raw,interim,processed}/`, `models/`, `notebooks/`, `reports/`, `scripts/` (each with `.gitkeep`); `src/reviewradar/` subpackages and `deploy/` are created when first needed
- Git workflow practiced end to end (branch, add, commit, push, PR, squash merge, fetch/pull, branch cleanup).
- `docs/LEARNING_LOG.md` was drafted by Claude from the owner's own answers; the owner should edit it into their own words.

## In progress
- Nothing.

## Next step
1. BUILD THE QUIZ ARTIFACT the owner asked for: an interactive artifact to test themselves on Phase 0 concepts and work, reusable after Phase 0 to retain knowledge. Use `docs/QUIZ_SEED.md` (42 questions with answers and the owner's real mistakes) as the question bank. Load the `artifact-design` and `artifact-capabilities` skills first; progress and weak spots should persist (use a runtime capability, not browser storage alone). Suggested features: mixed question types (multiple choice, "what does this command do", fix-the-bug, short answer with reveal), spaced repetition on missed items, topic filters, a score history, and a way to add questions later from `QUIZ_SEED.md`.
2. Then Phase 1: walk the owner through choosing the dataset (Bitext customer-support vs Amazon Reviews), then Postgres + SQL, DVC, EDA and baselines. Let the owner propose approaches first.

## Blockers / open questions
- Owner's homework still open: difference between `apt upgrade` and `apt full-upgrade`; explain in their own words what `check-added-large-files` does and how the `data/*/*` rule helps.
- Optional: load the SSH key into `ssh-agent` so the passphrase isn't typed on every Git command.
- Owner should enable the VS Code setting "insert final newline" (the end-of-file hook keeps firing on new files).
