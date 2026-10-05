# Timeline and time tracking

Estimates are focused working hours for a beginner doing the work themselves with a mentor (reading, trying, debugging, writing up). They exclude the daily 10-15 minute quiz. Update the "Actual" column when a phase ends and re-estimate the later phases from your real pace.

Last revised: 2026-10-03 (after Phase 0).

| Phase | What | Estimate (hours) | Actual (hours) | Status |
|---|---|---|---|---|
| 0 | Setup: environment, Git, uv, tests, pre-commit, CI, layout, quiz | already done | ~3 calendar days, hours not tracked | Done (log edit pending) |
| 1 | Data and baselines: dataset choice, Postgres and SQL, DVC, EDA, TF-IDF + logistic regression, XGBoost, LightGBM, evaluation harness with confidence intervals, calibration, error analysis | 35 - 50 | ~10 so far (owner's estimate, 2026-10-05) | In progress |
| 2 | Deep model: PyTorch and Hugging Face fine-tuning, domain-adaptive pretraining, augmentation, MLflow, Optuna | 45 - 65 | | |
| 3 | Second framework and optimization: Keras/TensorFlow, ONNX and TFLite export, quantization, benchmarks | 30 - 45 | | |
| 4 | Serving and RAG: FastAPI, tests, Docker, embeddings and pgvector, retrieval evaluation | 40 - 55 | | |
| 5 | Cloud and delivery: Kubernetes, Helm, Terraform, AWS, one SageMaker run, deploy pipeline, model-registry gate | 45 - 65 | | |
| 6 | Monitoring and polish: Prometheus, Grafana, drift reports, retraining trigger, model card, diagram, demo, portfolio write-up | 25 - 35 | | |
| | **Remaining total** | **220 - 315** | | |

## Calendar view

| Hours per week | Weeks to finish | About |
|---|---|---|
| 8 | 28 - 39 | 7 - 9 months |
| 12 | 18 - 26 | 4.5 - 6 months |
| 15 | 15 - 21 | 3.5 - 5 months |

The first plan said 14 - 16 weeks. That assumed a faster pace than Phase 0 showed. Treat the table above as the plan.

## Cutting scope if time runs short (saves about 20 - 35 hours)
- Skip the SageMaker training run (Phase 5): about 8 - 12 hours.
- Skip domain-adaptive pretraining (Phase 2): about 8 - 12 hours.
- Do Kubernetes only locally with kind, no EKS (Phase 5): about 10 - 15 hours, and a smaller AWS bill.
- Stop after any phase and the project is still coherent and showable.

## Where the time goes
- Each phase includes learning the tool, not only using it. Phases 2, 3 and 5 introduce the most new technology (PyTorch/Hugging Face, TensorFlow/ONNX, Kubernetes/Terraform), so they carry the widest ranges.
- GPU training runs on Colab or Kaggle and should not count as your working time while they run.
- Budget a few hours at the end of each phase for the learning log, the quiz additions and the decision log. That is where the interview material comes from.
