# Learning log

One entry per phase or concept: what I learned, what confused me, what I'd explain differently. Useful for interview prep.

> **Note:** the entries below were drafted by Claude from the owner's own answers and explanations during the sessions (many sentences are close to the owner's wording). The owner should edit anything that doesn't sound like them. The "Check results" table is Claude's record.

---

## Template

### YYYY-MM-DD — topic
- What I learned:
- What confused me:
- How I'd explain it to someone else:
- Still to review:

---

## Phase 0 — Setup (2026-10-01 to 2026-10-02)

### Python environments, pinning and reproducibility
- Pinning means writing down the exact package versions a project needs, so someone else can run the code and get the same findings. If I only say "uses pandas", a newer version may change syntax or behavior and break things.
- Reproducibility matters for peer review ("trust but verify"), for checking that good practices were followed, and so others can reuse the code. It also protects me: in six months I'm the "friend" who has to rerun my own results.
- A virtual environment has its own `site-packages` folder. Inside one, `sys.path` points to `.venv/.../site-packages` instead of the global folder. A fresh venv holds only `pip`, while my global Python had about 130 packages.
- Isolation protects a project from changes to global packages (and other projects). Pinning (a lockfile) records the exact versions so others can rebuild. They're two different jobs.
- `pyproject.toml` says what I'll accept (ranges like `pytest>=9.1.1`); `uv.lock` records exactly what was installed. I commit both, but not `.venv/`: the folder is large, specific to my machine, and can be rebuilt from the lockfile.
- `uv sync --locked` fails if the lockfile is out of date, so CI tests exactly what's committed.

### Python version choice
- I checked the official pages: PyTorch supports Python 3.10 to 3.14 and TensorFlow 3.9 to 3.12, so I pinned 3.12 (the newest both support).
- `requires-python = "==3.12"` means exactly 3.12.0, so `uv sync` rejected my 3.12.14. Writing "any 3.12" takes `==3.12.*` or `>=3.12,<3.13`. An exact `==3.12.14` works but is too strict (every patch release would need a manual edit).
- Open decision: which range to keep.

### Shell, PATH and WSL
- The shell finds programs by searching the folders in `PATH` in order; the first match wins. WSL copies the Windows PATH, which is why Windows programs like `clip.exe` run from Ubuntu.
- `apt` installs system-wide software, so it needs `sudo`; project tools (venvs, `uv`) go in my own folders without it.
- `~` means a different folder in PowerShell (`C:\Users\manol`) and Ubuntu (`/home/mjvargas99`). The prompt tells me which shell I'm in: `PS C:\...>` is PowerShell, `user@host:~$` is Ubuntu.
- Project work lives in the Linux home (`~/projects/reviewradar`), not under `/mnt/c`.

### Git and GitHub
- Four places: working folder, staging area, local repo, remote. `add` stages, `commit` takes the snapshot, `push` uploads. `fetch` downloads without changing my files, and `pull` is fetch plus merge. I'd use `fetch` first when teammates have changed things and I want to see what before merging.
- A branch is a label pointing at a commit. I work on a branch, open a pull request and let checks run, so `main` always stays stable, and a branch with an unfixable bug can just be deleted.
- Squash merges leave the original branch commits off `main`, so `git branch -d` refuses and `-D` forces. `-D` is risky on a branch I never merged anywhere: the work can be lost.
- `.gitignore` lists what Git should skip. A new file that isn't listed is "untracked", not "ignored" (I predicted the opposite once).
- An SSH key is a pair: the private key never leaves my machine, and the public key (`.pub`) goes to GitHub.

### Testing and code quality
- A pytest test is a function named `test_*` in a `test_*.py` file; `assert` fails the test if the condition is false. A test with no assert is only a smoke test.
- `capsys` is a pytest fixture (requested by naming it as a parameter) that captures printed output; `print` adds a `\n`. In a failure message, the left side is the actual value and the right side is the expected one.
- `ruff check` finds likely bugs (like an unused import); `ruff format` fixes layout; `--check` reports without changing files.
- Text files should end with a newline; a diff shows `\ No newline at end of file` when they don't.

### pre-commit and CI
- A pre-commit hook runs checks automatically before each commit. If a hook modifies a file, the commit is blocked: I `git add` the fixed file and commit again. It only checks tracked or staged files.
- Passing hooks hide their output. A local hook uses `repo: local`, `entry: uv run pytest`, `language: system` and `pass_filenames: false` (run all tests, not only changed files).
- YAML: spaces only, a list item is `- ` (dash and space), and keys of one item line up. `false` is a boolean; `[]` is a list.
- CI runs the same checks on a clean GitHub machine for every pull request, and nobody can skip it. Steps from empty: checkout, install `uv`, `uv sync --locked`, run the checks. The second run is faster because the cache is restored.
- Actions have different tag conventions (`checkout@v7` floats, `setup-uv` needs `v10.2.0`); I verify tags with `git ls-remote --tags <url>`.

### What confused me (and what I learned from it)
- I ran `cd ~/projects/reviewradar` in the VS Code PowerShell terminal: VS Code wasn't connected to WSL. Fix: the WSL extension and `code .` from Ubuntu.
- I committed on `main` because I skipped `git switch -c`. Fix: create the branch label at my commit, then move `main` back with `git branch -f main origin/main`.
- I typed `commit` without `git`, `pyprojects.toml` for `pyproject.toml`, and `-LsFf` for `-LsSf`: each error message named what was wrong.
- I wrote `pass_filenames: []` (a list) instead of `false`, and the pytest hook pointed at a script that didn't exist.
- I guessed a compiler checks for crashes or memory leaks. It actually translates C/C++ code, which libraries like NumPy need when no prebuilt wheel exists.

### Still to review
- Difference between `apt upgrade` and `apt full-upgrade`.
- Why public SSH keys are safe to share and private keys are not.
- Why `import reviewradar` works from `tests/` (editable install of my own project).

### Check results (recorded by Claude)
| Question | Owner's answer | Gap to revisit |
|---|---|---|
| Pinning: what goes wrong without it? | Correct: new versions can break syntax and results | none |
| What changes in `sys.path` inside a venv? | Said the win32 and editable entries disappeared | Missed that the `site-packages` entry is replaced by the venv's own folder |
| Isolation vs pinning | Correct by the end | Initially credited pinning with isolation's job |
| Why a compiler for a Python project? | Guessed testing / memory leaks | Compilers translate C/C++; wheels vs building from source |
| Why apt needs sudo but a venv doesn't | Not sure | System folders vs own folders |
| Why order matters in PATH | Not sure | First match wins |
| `git switch -c` and why not edit `main` | Correct: create; keep a stable version | none |
| `-D` vs `-d` | Correct: deletes, risk of losing unmerged work | none |
| fetch vs pull | Correct, with a good use case | none |
| Why `git status` listed `src/` etc. after pull | Predicted they were in `.gitignore` | Untracked vs ignored |
| Which checks on every commit | Described Git steps first | Distinguish workflow commands from code checks (lint, format, tests) |
| Pytest on every commit vs CI | Good reasoning about pinpointing failures | Trade-off: slow hooks get bypassed |
| Second CI run speed | Correct: faster, cached | none |
| `requires-python` for 3.12 | Used `==3.12` then `==3.12.14` | `==3.12` means 3.12.0; ranges vs exact pins |
