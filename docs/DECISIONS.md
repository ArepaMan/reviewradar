# Decision log

Format: date — decision — why — alternatives considered.

- 2026-10-01 — Domain: support-ticket / review text classification + RAG — text roles dominate entry-level postings (NLP, LLMs, RAG) and one domain covers modeling, serving, MLOps — alternatives: vision, tabular, time series (more niche in postings).
- 2026-10-01 — Dual framework (PyTorch main, TensorFlow/Keras secondary) — postings list both — only PyTorch would leave a gap.
- 2026-10-01 — Skip Spark, Kafka, Hadoop, JAX, FHIR, OpenCV/signal processing — appear mainly in senior or domain-specific postings.
- 2026-10-01 — Separate public repo (not the GitHub profile repo) — keep the profile README clean; clean portfolio link.
- 2026-10-01 — Mentor mode: the owner writes the code, Claude guides — the purpose is learning the stack.
- 2026-10-01 — Pin Python 3.12 — owner checked official pages: PyTorch supports 3.10–3.14, TensorFlow 3.9–3.12, so 3.12 is the newest version both support; the system/Windows 3.14 is unsupported by TensorFlow — alternatives: 3.11 (one version of margin below TensorFlow's limit). Revisit when TensorFlow adds 3.13, and re-verify supported ranges before adding libraries.
- 2026-10-02 — `requires-python = ">=3.12,<3.13"` — TensorFlow (Phase 3) supports Python up to 3.12, and `uv.lock` resolves for every Python the range allows; owner first tried `==3.12` (means 3.12.0 only) and `==3.12.14` (too strict, patch-level) — alternatives: unbounded `>=3.12` (would break TensorFlow resolution).
- 2026-10-02 — pre-commit runs on every commit, including all tests (`uv run pytest`) — tests take milliseconds today — revisit and move pytest to push/CI if the suite becomes slow (slow hooks get bypassed).
- 2026-10-02 — CI runs `uv run pre-commit run --all-files` after `uv sync --locked` — one source of truth for checks locally and in CI, locked tool versions — alternative: separate explicit steps per check.
- 2026-10-02 — Folder layout: `src/reviewradar/` split by job (data, features, models, evaluation, serving, rag, monitoring), `data/{raw,interim,processed}` kept out of Git (DVC later), `models/` out of Git, `notebooks/` for exploration only, `configs/` for settings, `deploy/` for infrastructure — folders created only when first needed — alternative: create every folder upfront (clutter, empty folders).
