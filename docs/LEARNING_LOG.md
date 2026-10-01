# Learning log

Written by the owner, in their own words. One entry per session or concept: what I learned, what confused me, what I'd explain differently. Useful for interview prep.

Claude records phase check-question results here too (question, owner's answer, gaps to revisit).

---

## Template

### YYYY-MM-DD — topic
- What I learned:
- What confused me:
- How I'd explain it to someone else:
- Still to review:

---

## Entries

### 2026-10-01 — Python environments, PATH and setting up WSL
*Drafted by Claude from the owner's own answers during the session. Owner: edit this into your own words.*

- What I learned:
  - Pinning means recording the exact package versions a project needs so someone else can reproduce the results. Without it, a newer pandas could change syntax and break the code.
  - Reproducibility matters for peer review ("trust but verify"), for checking good practice, and so others can reuse the code.
  - A virtual environment has its own `site-packages` folder. Inside one, `sys.path` points to `.venv\Lib\site-packages` instead of the global one, and a fresh venv contains only `pip`, while my global Python had around 130 packages.
  - Isolation protects the project's packages from changes in the global ones. Pinning (a lockfile) records versions so others can recreate the environment. They are different jobs.
  - The shell finds programs by searching the folders in `PATH` in order, and the first match wins. WSL copies the Windows PATH, which is why Windows programs like `clip.exe` run from Ubuntu.
  - `apt` installs system-wide software, so it needs `sudo`. Project tools go in my own folders without it.
- What confused me:
  - I guessed a compiler is for checking that code runs or finding memory leaks. It actually translates C/C++ code into machine code; libraries like NumPy need it only when no prebuilt wheel exists.
  - I forgot `python -c "..."` when I ran my first one-liner, so PowerShell, not Python, tried to read it.
- Still to review:
  - Difference between `apt upgrade` and `apt full-upgrade`.
  - Why public SSH keys are safe to share and private keys are not.

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
