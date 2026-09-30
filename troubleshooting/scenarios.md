# Break/Fix Scenarios

Do not read these as solution prompts. For each incident, capture: symptom, evidence, hypothesis, tests performed, root cause, fix, and prevention.

## Incident 1 — OIDC assumption failure
GitHub Actions repeatedly reports that it cannot assume the AWS role with web identity. Investigate the token trust relationship, repository/branch context and role configuration.

## Incident 2 — ECR push denied
AWS authentication succeeds, but the image cannot be pushed to ECR. Determine whether the problem is repository targeting, authentication, or authorization.

## Incident 3 — Pipeline is green but wrong version runs
The workflow reports success, but the application still returns an older version. Trace the artifact from Git commit through image tag/digest to deployment.

## Incident 4 — Security gate blocks release
A scan detects a high-severity issue. Decide what evidence you need before changing the gate, upgrading dependencies, accepting risk, or stopping deployment.

## Incident 5 — Pull request can deploy
A reviewer discovers that code from a pull request can reach the deployment job. Identify the trigger/condition/permissions problem and redesign the boundary.

## Incident 6 — Concurrent deployments
Two commits merge close together. The older workflow finishes after the newer one and overwrites the deployment. Add a safe mechanism to prevent stale deployment.

## Incident 7 — Docker build works locally, fails in CI
Compare build context, file paths, ignored files, architecture, environment and dependency behavior. Prove the cause rather than guessing.
