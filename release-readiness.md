# Release Readiness Pack — Atlas Service

Fill in every section below as you work through the three tasks. Keep entries short
and factual. Do not paste secret values anywhere in this file.

## 1. Release metadata

- Release version:
- Git commit hash:
- Git tag:
- Docker image name and version:
- Date/time:
- Prepared by:

## 2. Risk assessment (Task 1 — Docker)

- Issue found (what failed and how you noticed):
- Impact if shipped as-is:
- Evidence (build error summary):
- Fix applied:
- Residual risk after fix:

## 3. Pipeline stages (Task 2 — Kubernetes)

Describe what happens at each stage and where it was validated:

- Validate:
- Build:
- Deploy:
- Smoke test:

## 4. Environment gate

- Where does human approval occur in the pipeline?
- Which GitHub environment enforces it?
- Why is this gate placed before production and not before `release-check`?

## 5. Secret handling (Task 3 — Workflow)

- Issue found in `.github/workflows/release.yml`:
- Why was it unsafe?
- Fix applied (describe the safe pattern used, do not paste secret values):
- Confirm no password, token, or private key is committed anywhere in the repo:

## 6. Validation evidence

List commands run and a one-line result for each (attach screenshots separately
in your PDF submission):

- `docker build ...`:
- `curl http://localhost:8080/health`:
- `kubectl apply --dry-run=client -f k8s/`:
- `kubectl diff -f k8s/` (or note if a cluster was unavailable):
- `kubectl get deployment,pods,service` (or note if a cluster was unavailable):
- `git tag` / `git show v1.4.0 --stat`:

## 7. Rollback plan

- Rollback trigger (what condition would cause a rollback):
- Rollback action (previous known-good image tag and how it is redeployed):

## 8. Kubernetes vs Terraform

- One sentence: why would Terraform manage infrastructure provisioning while
  Kubernetes manages the application workload here?

## 9. Final decision

- Decision: **Ready** / **Not ready**
- Reason:
