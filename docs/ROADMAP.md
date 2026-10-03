# Roadmap (~14–16 weeks part-time)

Each phase ends with something demonstrable. Stopping after any phase still leaves a coherent project.

- [ ] **Phase 0 — Setup (week 1):** `uv` project, folder layout, ruff, pytest, pre-commit, first CI workflow.
  - [x] `uv` project, Python 3.12 pinned, `.gitignore`
  - [x] ruff + pytest, first smoke test
  - [x] pre-commit hooks (hygiene, ruff, pytest)
  - [x] first CI workflow (GitHub Actions running pre-commit), green
  - [x] folder layout (`configs/`, `data/{raw,interim,processed}/`, `models/`, `notebooks/`, `reports/`, `scripts/`; `src/` subpackages and `deploy/` are added when first needed)
  - [x] `requires-python = ">=3.12,<3.13"` (TensorFlow supports up to 3.12)
  - [ ] Phase 0 wrap-up: owner edits `LEARNING_LOG.md` into their own words; Claude builds the quiz artifact from `docs/QUIZ_SEED.md`
- [ ] **Phase 1 — Data & baselines (weeks 1–3):** dataset choice, Postgres + SQL queries, DVC, EDA, TF-IDF + logistic regression / XGBoost / LightGBM, evaluation harness with bootstrap CIs, calibration, error analysis.
  *Done when:* one command reproduces the baseline table.
- [ ] **Phase 2 — Deep model (weeks 4–6):** PyTorch + Hugging Face fine-tuning, domain-adaptive pretraining, augmentation experiments, MLflow tracking, Optuna tuning.
  *Done when:* transformer vs baselines compared with confidence intervals.
- [ ] **Phase 3 — Second framework & optimization (weeks 7–8):** Keras/TensorFlow re-implementation, ONNX + TFLite export, quantization, latency/throughput/memory benchmarks.
  *Done when:* README benchmark table filled in.
- [ ] **Phase 4 — Serving & RAG (weeks 9–10):** FastAPI service, pydantic schemas, pytest suite, Dockerfile, embeddings + pgvector RAG assistant, retrieval eval (recall@k).
- [ ] **Phase 5 — Cloud & CD (weeks 11–13):** Kubernetes (kind first, then EKS), Helm, Terraform, ECR/S3, one SageMaker training job, GitHub Actions deploy, model-registry promotion gate.
- [ ] **Phase 6 — Monitoring & polish (weeks 14–16):** Prometheus/Grafana, Evidently drift report, retraining trigger, model card, architecture diagram, demo video, portfolio write-up.

Least valuable if scope must shrink: SageMaker run, domain-adaptive pretraining.
