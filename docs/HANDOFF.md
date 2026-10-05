# Handoff

Overwrite this at the end of every session.

## Last updated
2026-10-05

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
1. The Phase 0 quiz artifact is BUILT and published (version 2): https://claude.ai/artifact/WAVGDedpkvkvMEHHgSuaqb (private to the owner). Source: `docs/quiz/index.html`. It holds 194 questions in 6 topics (env, shell, git, test, ci, proj) and 36 subtopics (at least 3 questions each), in four types: multiple choice, type-the-command, put-steps-in-order and self-graded recall. About 9% of questions are tied to mistakes the owner actually made (flagged "You hit this in Phase 0"); the rest cover the concepts broadly. The dashboard offers a daily session (10, 20 or 40 questions), a coverage sweep (one question per subtopic, preferring the least known), weak spots, and per-topic practice.
   - The question bank is the `QUESTIONS` array near the top of the script, built with helpers `mc`, `rec`, `cmd`, `ord`; every question has a topic key and a subtopic label. Ids are stable because progress is stored by id: never change or reuse an existing id.
   - Progress is saved per person in the artifact's `db` capability under `data/users/<id>/quiz` (fallback: browser storage). Scheduling is a 5-box Leitner system (intervals 1, 3, 7, 14, 30 days; a miss resets to box 1, due today; a missed question gets one second try at the end of the session).
   - To add questions after a later phase: add entries to `QUESTIONS` (new ids, existing topic keys or a new entry in `TOPICS`, at least 3 questions per new subtopic), keep `docs/QUIZ_SEED.md` as the original seed, then republish the same artifact: read it with the Artifact tool, edit `docs/quiz/index.html`, and publish with `url` set to the link above (capabilities `{db: {}, user: {}}` carry forward). A Playwright run (Chromium is at `/opt/pw-browsers`) that solves every question type through the UI is the way this was verified.
2. Phase 1 (current): data and baselines, about 20-25% done. **Dataset: Banking77** (decided 2026-10-03; CFPB rejected, no text narrative; see `docs/DECISIONS.md`, `docs/DATASET_EVALUATION.md`).
   - Done and merged: `scripts/download_data.py` (downloads train/test CSVs from the authors' GitHub repo `PolyAI-LDN/task-specific-datasets` into `data/raw/banking77/`; Hugging Face `datasets` failed because `PolyAI/banking77` still uses a loader script, so it was removed).
   - Merged since: `clean_text` (strip), `make_key` and `drop_duplicates_texts` (`duplicates.py`), `remove_overlap` (`overlap.py`), `clean_splits` (`pipeline.py`), each with tests, all written by the owner (PRs 24-26). Notebook `notebooks/01_first_look.ipynb` is still uncommitted by design (open decision: how to handle saved notebook output, for example `nbstripout`). Owner's environment: VS Code must be opened from the Ubuntu terminal (`code .`, badge says WSL: Ubuntu) and the Python and Jupyter extensions must be installed in WSL. Pre-commit ruff includes import sorting (I001): run `uv run ruff check --fix src tests` and `uv run ruff format src tests` before committing.
   - First-look findings (train 10,003 rows, test 3,080, 77 labels): train class counts range 35 to 187 (imbalanced, about 5:1; owner had guessed balanced), so report macro-F1 as well as accuracy and use stratified splits; text length mean 59.5, median 47, p75 64, max 433 characters (right-skewed; sequences are short, roughly up to about 100 tokens, measure with the tokenizer in Phase 2); exact duplicates 0 and exact train/test overlap 0, but after strip and lowercase there are 4 duplicate pairs inside train (same labels, differ only by stray `\n`) and 6 train texts that match test texts; 9 train texts have leading or trailing whitespace. Raw data is noisy.
   - Cleaning rule agreed in chat (owner proposed, Claude refined): strip the text but keep original case; use lowercase-and-strip only as a comparison key; drop duplicate train rows (keep first, assert labels agree); drop train rows whose key appears in test; strip test text but do not remove test rows (keeps scores comparable with published results); never edit `data/raw/`; write cleaned files to `data/interim/banking77/`, final splits to `data/processed/`. A validation split (stratified, from train) is still needed.
   - Pending for the owner: (1) write `scripts/clean_data.py` (read `data/raw/banking77/*.csv`, call `clean_splits`, write to `data/interim/banking77/` with `index=False`, print row counts; owner predicted train about 9,993 and test 3,080; Claude's own check of the raw files gives the same); (2) write 3-4 bullets of EDA findings in a notebook Markdown cell; (3) answer: why `index=False`; why macro-F1 matters (accuracy counts rows, macro-F1 counts classes equally; worked examples done in chat).
   - Then: stratified validation split, proper EDA with plots, Postgres + SQL (own tables: intents, runs, predictions), DVC, TF-IDF + logistic regression (owner guessed 85% on Bitext and has not yet guessed for Banking77; Claude expects high 80s for TF-IDF and low 90s for a fine-tuned transformer, unverified), XGBoost, LightGBM, evaluation harness with bootstrap CIs, calibration, error analysis. Let the owner propose approaches first. Estimates and hours tracking live in `docs/TIMELINE.md`; owner estimated about 10 hours spent on Phase 1 as of 2026-10-05 (recorded in `docs/TIMELINE.md`).

## Blockers / open questions
- Owner's homework still open: difference between `apt upgrade` and `apt full-upgrade`; explain in their own words what `check-added-large-files` does and how the `data/*/*` rule helps.
- Optional: load the SSH key into `ssh-agent` so the passphrase isn't typed on every Git command.
- Owner should enable the VS Code setting "insert final newline" (the end-of-file hook keeps firing on new files).
