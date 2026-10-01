# Handoff

Overwrite this at the end of every session.

## Last updated
2026-10-01

## Owner's environment (set up and verified)
- Windows 11 + WSL2, Ubuntu 26.04.1 LTS. Open it from the Start menu ("Ubuntu") or `wsl ~` in PowerShell.
- Work only inside the Linux filesystem: `~/projects/reviewradar`. Never work under `/mnt/c`.
- Installed via apt: `git` 2.53, `curl`, `build-essential` (gcc 15.2).
- `uv` 0.12.21 in `~/.local/bin` (on PATH via `~/.bashrc` / `~/.profile`).
- Git identity set; default branch `main`. GitHub auth is SSH (ed25519 key with passphrase, added to GitHub).
- The owner's Windows also has Python 3.12 and 3.14 installed globally with many old packages (e.g. an editable `lante` install). These are NOT used for this project.
- Owner is a beginner in the terminal; explain every command. They have been answering prediction questions in chat.

## Done
- Repo created, continuity docs merged to `main`.
- Phase 0, environment: WSL2, Git, uv, SSH and clone all working.
- Concepts covered with check questions: sys.path, virtual environments, isolation vs pinning, PATH, sudo vs user-level installs, compilers and wheels, SSH keys, branches.

## In progress
- First Git workflow (branch, commit, push, PR, merge): the owner is doing it with the branch that carries this file.

## Next step
- Phase 0, project creation. Ask what the owner expects `uv init` to create, then have them run it themselves in `~/projects/reviewradar`.
- Python version decision (owner's task): look up which Python versions current PyTorch and TensorFlow support, choose one to pin, and record it in `docs/DECISIONS.md` with the reason.
- Then: add `ruff` and `pytest` as dev dependencies, create the folder layout, first CI workflow.

## Blockers / open questions
- Dataset not chosen yet (candidates: Bitext customer-support dataset, Amazon Reviews). Walk the owner through comparing them.
- Owner's homework still open: difference between `apt upgrade` and `apt full-upgrade`.
- Optional later: load the SSH key into `ssh-agent` so the passphrase isn't typed on every Git command.
