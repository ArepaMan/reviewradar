# Quiz seed: Phase 0 question bank

Source material for the owner's self-test artifact. Each item: topic, question, answer, and the mistake the owner actually made (if any), because real mistakes are the best questions. Add new items as later phases add concepts.

## Python environments and tooling
1. **sys.path.** What is `sys.path` and why does order matter? A list of folders Python searches when you `import`; first match wins.
2. **Virtual environment.** What does a venv change in `sys.path`? The global `site-packages` entry is replaced by the venv's own `.venv/lib/.../site-packages` (the owner first only noticed what disappeared). A fresh venv has only `pip`.
3. **Isolation vs pinning.** Isolation (venv) stops other projects/global installs from changing yours. Pinning (lockfile) records exact versions so others can rebuild. The owner first credited pinning with isolation's job.
4. **`pyproject.toml` vs `uv.lock`.** pyproject says what you will accept (ranges like `>=9.1.1`); the lock records exactly what was resolved, including transitive dependencies. Commit both.
5. **Why is `.venv/` not committed?** It is large, machine/OS-specific, and can be rebuilt from `uv.lock` with `uv sync`.
6. **`uv sync` vs `uv sync --locked`.** `--locked` errors if the lockfile is out of date instead of updating it; CI should test exactly what is committed.
7. **`requires-python` vs `.python-version`.** `.python-version` is the exact interpreter used; `requires-python` is the supported range. `>=3.12` has no upper bound, but TensorFlow supports only up to 3.12, so add `<3.13`.
8. **Why pin Python 3.12?** Newest version both PyTorch (3.10-3.14) and TensorFlow (3.9-3.12) support. Re-check supported ranges before adding libraries.
9. **Compilers and wheels.** Why does `build-essential` matter for a Python project? Libraries like NumPy have C/C++ cores; they usually ship precompiled wheels, but with no wheel for your Python/OS the installer compiles from source (new Python versions often lack wheels). The owner first guessed compilers check for crashes or memory leaks.
10. **Never `pip install` into the system Python** (Ubuntu's own Python at `/usr/bin/python3.x`).

## Shell, PATH and WSL
11. **PATH.** A list of folders the shell searches for commands, in order; first match wins. `~/.local/bin` must be on it to find `uv`.
12. **`~` means different things.** In PowerShell it is `C:\Users\manol`; in Ubuntu it is `/home/mjvargas99` (the owner's `cd ~/projects/...` failed in PowerShell).
13. **How do you know which terminal you are in?** Prompt: `PS C:\...>` is PowerShell; `user@host:~$` is Ubuntu. VS Code's terminal showing `PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\...` means VS Code is NOT connected to WSL.
14. **`where` in PowerShell** is an alias for another command; use `where.exe python`.
15. **`/mnt/c`.** The Windows C: drive seen from Linux. Do project work in the Linux home, not there.
16. **`sudo` vs user installs.** System-wide software (`apt`) needs admin rights because it writes to folders shared by every user; venvs and `uv` write to your own folders.
17. **Quoting/commands.** `python -c "import sys; print(sys.path)"`: without the `python -c "..."` wrapper PowerShell tries to run `import` itself (which program is complaining?). `curl -LsSf` vs `-LsFf`: one letter changes a flag's meaning.
18. **Hidden files** start with `.`; `ls -a` shows them. `.bashrc` runs every time a shell starts.

## Git and GitHub
19. **The four places.** working folder, staging area, local repo, remote. `add` stages, `commit` snapshots, `push` uploads, `fetch` downloads without touching files, `pull` = fetch + merge.
20. **Tracked, untracked, ignored.** `.gitignore` lists what to ignore; files not listed (like new `src/`) are untracked, not ignored (the owner predicted the opposite). `git check-ignore -v <path>` shows the matching rule.
21. **Staging snapshot.** After `git add`, editing the file again leaves a staged old version and an unstaged new version (seen when end-of-file-fixer modified an already-staged file).
22. **Branches are labels.** The owner committed on `main` by mistake; fix with `git switch -c <branch>` then `git branch -f main origin/main`. `git switch -c` carries uncommitted changes along.
23. **Fast-forward.** Your branch had no commits of its own, so Git only moves the pointer.
24. **Squash merge.** Squashes a branch into one commit on `main`; the old branch commits are not on `main`, so `git branch -d` refuses and `-D` is needed. `-D` is risky on branches never merged.
25. **Pull request.** A GitHub feature (not Git): review plus automated checks before merging. Why not push to `main`: keeps a stable version and runs CI first.
26. **SSH keys.** Private key stays secret; public key (`.pub`) goes to GitHub; passphrase protects the private key file.
27. **Error reading.** `pathspec ... did not match any files` = typo in a name; `commit: command not found` = forgot `git`; `src refspec ... does not match any` = no such local branch.

## Testing and code quality
28. **A pytest test.** Function named `test_*` in `test_*.py`; `assert` fails the test when false. A test with no assert is only a smoke test.
29. **`capsys`.** A pytest fixture, requested by naming it as a parameter, that captures printed output (`capsys.readouterr().out`); `print` adds `\n`.
30. **Reading an assertion failure.** In `assert left == right`, pytest shows the actual value on the left and the expected on the right.
31. **ruff check vs ruff format.** check lints (bugs like unused imports, F401); format fixes layout. `--check` reports without changing files; `--diff` shows what would change.
32. **End-of-file newline.** Text files should end with `\n`; the diff shows `\ No newline at end of file`. A formatter or hook can fix it.

## pre-commit and CI
33. **What is a git hook?** A script in `.git/hooks/` Git runs at certain moments; `.sample` files are inactive templates; pre-commit installs a real `pre-commit` hook.
34. **When a hook modifies files** the commit is blocked; re-`git add` the fixed files and commit again.
35. **pre-commit only checks tracked/staged files**; an untracked file shows `Skipped (no files to check)`.
36. **YAML.** Indentation matters (spaces, never tabs); a list item is `- ` (dash and space); keys of the same item line up with the first key. Booleans (`false`) are not lists (`[]`).
37. **Local hook.** `repo: local`, no `rev`; `entry: uv run pytest`, `language: system` (command already on PATH), `pass_filenames: false` (run all tests, not just changed files).
38. **Passing hooks hide their output** unless verbose.
39. **CI vs pre-commit.** pre-commit runs on your machine and can be skipped; CI runs on every pull request on a clean machine and cannot.
40. **CI steps from empty.** checkout, install uv, `uv sync --locked`, run checks. Python is downloaded/selected by uv from `.python-version`.
41. **Action versions.** `actions/checkout@v7` is a floating major tag; `astral-sh/setup-uv` only has exact tags (`@v10.2.0`); verify with `git ls-remote --tags <url>`. A commit hash is the strictest pin.
42. **Cache.** The first CI run saves a cache; later runs restore it and are faster.
