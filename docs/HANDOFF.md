# Handoff

Overwrite this at the end of every session.

## Last updated
2026-10-02

## Owner's environment (set up and verified)
- Windows 11 + WSL2, Ubuntu 26.04.1 LTS. Open it from the Start menu ("Ubuntu") or `wsl ~` in PowerShell.
- Work only inside the Linux filesystem: `~/projects/reviewradar`. Never work under `/mnt/c`.
- VS Code connected to WSL (`code .` from the Ubuntu terminal; the terminal inside VS Code should show an Ubuntu prompt, not `PS ...`).
- `uv` 0.12.21, git 2.53, SSH key (with passphrase) added to GitHub. Git identity set; default branch `main`.
- The owner's Windows also has Python 3.12 and 3.14 installed globally (not used here).
- Owner is a beginner in the terminal and with Python tooling; explain every command. They answer prediction questions in chat and often reply "not sure": then escalate hints (hint, pseudocode, partial snippet, full answer with explanation).

## Done
- Environment, repo, continuity docs.
- Phase 0 so far (all merged to `main`, CI green):
  - `uv` project, Python 3.12 pinned, `.gitignore`
  - `ruff` + `pytest`, first smoke test (`tests/test_smoke.py`, written by owner with `capsys`)
  - `pre-commit` hooks: trailing whitespace, end-of-file, YAML, large files, `ruff-check`, `ruff-format`, local `uv run pytest`
  - GitHub Actions CI (`.github/workflows/ci.yml`): checkout, `setup-uv`, `uv sync --locked`, `uv run pre-commit run --all-files`
- Git workflow practiced: branch, add, commit, push, PR, squash merge, fetch/pull, branch cleanup; owner has made their own commits.
- Concepts covered with check questions: see `docs/LEARNING_LOG.md` and `docs/QUIZ_SEED.md`.

## In progress
- Nothing.

## Next step
1. Folder layout: ask the owner to propose the folder structure for the project (data, notebooks, src modules, configs, scripts) and defend each folder; then they create it. Do not hand it over.
2. `requires-python` upper bound: owner edits `pyproject.toml` to `>=3.12,<3.13`, runs `uv sync`, sees the lockfile update, commits.
3. Phase 0 wrap-up: owner rewrites `docs/LEARNING_LOG.md` in their own words. Then BUILD THE QUIZ ARTIFACT the owner asked for: an interactive artifact to test themselves on Phase 0 concepts and work, reusable after Phase 0 to retain knowledge. Use `docs/QUIZ_SEED.md` as the question bank. Load the `artifact-design` and `artifact-capabilities` skills first; progress and weak spots should persist (use a runtime capability, not browser storage alone).
4. Then Phase 1: walk the owner through choosing the dataset (Bitext customer-support vs Amazon Reviews).

## Blockers / open questions
- Owner's homework still open: difference between `apt upgrade` and `apt full-upgrade`.
- Optional: load the SSH key into `ssh-agent` so the passphrase isn't typed on every Git command.
- Owner should enable the VS Code setting "insert final newline" (the end-of-file hook keeps firing on new files).
