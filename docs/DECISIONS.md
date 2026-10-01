# Decision log

Format: date — decision — why — alternatives considered.

- 2026-10-01 — Domain: support-ticket / review text classification + RAG — text roles dominate entry-level postings (NLP, LLMs, RAG) and one domain covers modeling, serving, MLOps — alternatives: vision, tabular, time series (more niche in postings).
- 2026-10-01 — Dual framework (PyTorch main, TensorFlow/Keras secondary) — postings list both — only PyTorch would leave a gap.
- 2026-10-01 — Skip Spark, Kafka, Hadoop, JAX, FHIR, OpenCV/signal processing — appear mainly in senior or domain-specific postings.
- 2026-10-01 — Separate public repo (not the GitHub profile repo) — keep the profile README clean; clean portfolio link.
- 2026-10-01 — Mentor mode: the owner writes the code, Claude guides — the purpose is learning the stack.
- 2026-10-01 — Pin Python 3.12 — owner checked official pages: PyTorch supports 3.10–3.14, TensorFlow 3.9–3.12, so 3.12 is the newest version both support; the system/Windows 3.14 is unsupported by TensorFlow — alternatives: 3.11 (one version of margin below TensorFlow's limit). Revisit when TensorFlow adds 3.13, and re-verify supported ranges before adding libraries.
