# Atlas Release Readiness Lab

Small containerised Flask service used for a DevOps Foundation Module 3 release-readiness exercise.

## ⚠️ This repository is intentionally broken

This repository contains **exactly three planted release-blocking issues** (one Docker
issue, one Kubernetes issue, one release-workflow secret-safety issue). Your task is to
find and fix them, then produce a release-readiness pack.

**Do not work in this source repository.** Fork it first, then clone your fork:

```bash
git clone https://github.com/<your-username>/atlas-release-readiness-lab.git
cd atlas-release-readiness-lab
git checkout -b fix/release-readiness
```

## Expected healthy behaviour (target state)

When the three issues are fixed, the following should be true:

- Docker image builds and is tagged `atlas-service:v1.4.0`.
- Container listens on `0.0.0.0:5000` inside the image.
- Running the container with `-p 8080:5000` exposes the health endpoint at
  `http://localhost:8080/health`, returning:

  ```json
  {"status": "ok", "version": "1.4.0"}
  ```

  with HTTP 200.

- Kubernetes Deployment `atlas-deployment` (namespace: default) runs one replica of
  container port `5000`, with Pod label `app: atlas`.
- Kubernetes Service `atlas-service`, type `ClusterIP`, exposes port `80` targeting
  container port `5000`, and its selector **must match** the Deployment Pod label
  `app: atlas` for traffic to route correctly.
- `.github/workflows/release.yml` triggers on tags matching `v*.*.*` and on
  `workflow_dispatch`. It has a `release-check` job and a `production-deploy` job
  that `needs: release-check` and runs under a GitHub `environment: production`
  gate (so a human approval is required before the deploy job can run).
- Any reference to the registry token must use `${{ secrets.REGISTRY_TOKEN }}` only
  where required, and the value must never be printed or logged.
- Release is tagged `v1.4.0`. If the release must be rolled back, the documented
  rollback action is to redeploy the previous known-good image, `atlas-service:v1.3.0`.

## Repository layout

```
app.py                        Flask app, GET /health
requirements.txt              pinned dependencies
Dockerfile                    container build
k8s/deployment.yaml           Deployment atlas-deployment
k8s/service.yaml              Service atlas-service
k8s/secret.yaml               placeholder Secret (stringData, fake value only)
.github/workflows/release.yml release workflow with production gate
release-readiness.md          template you must complete
```

## Safe commands you will need

Build and run:

```bash
docker build -t atlas-service:v1.4.0 .
docker run -d --name atlas-release -p 8080:5000 atlas-service:v1.4.0
curl http://localhost:8080/health
```

Validate Kubernetes manifests (no live cluster required):

```bash
kubectl apply --dry-run=client -f k8s/
kubectl diff -f k8s/
```

If Kind or Minikube is available:

```bash
kubectl apply -f k8s/
kubectl get deployment,pods,service
kubectl describe service atlas-service
```

Tag and inspect the release:

```bash
git status
git tag v1.4.0
git show v1.4.0 --stat
git log -1 --oneline
```

## Notes

- Never commit real secrets, tokens, private keys, or cloud credentials.
  `k8s/secret.yaml` must only ever contain a placeholder value.
- Do not delete checks, remove the `production` environment gate, or bypass
  failing steps to "fix" an issue — find the actual root cause instead.
- Complete `release-readiness.md` as part of your submission.
