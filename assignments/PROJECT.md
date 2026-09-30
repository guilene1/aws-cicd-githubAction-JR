# Project 2 Assignment

## Scenario
A development team currently builds and deploys its application manually. Releases are inconsistent, AWS credentials have previously been copied between laptops, and nobody can reliably identify which Git commit is running. Your job is to automate the release process.

## Task 1 — Application baseline
Run the supplied Flask app and test locally.

Acceptance criteria:
- `/health` returns HTTP 200.
- `pytest` passes.
- You can explain why a health endpoint matters to automated deployment systems.

Checkpoint: capture the local test result and health response.

## Task 2 — Containerize the application
Create your own `Dockerfile` and `.dockerignore` in `app/`.

Requirements:
- Use an appropriate Python base image.
- Install dependencies reproducibly.
- Copy only what the application needs.
- Expose/use port 5000.
- Start the application automatically.
- Avoid running as root if you can implement it safely.

Acceptance criteria:
- Image builds locally.
- Container starts successfully.
- `curl localhost:<mapped-port>/health` succeeds.
- You can explain Docker layers and build cache.

Write the Dockerfile yourself; do not copy one.

## Task 3 — ECR with Terraform
Inside `terraform/`, write Terraform that creates the ECR repository used by CI/CD.

Requirements:
- ECR repository for the application.
- Image scanning configuration.
- Encryption enabled.
- Lifecycle policy to prevent unlimited old images.
- Useful outputs, including repository URL.

Suggested files (create them yourself):
`versions.tf`, `providers.tf`, `variables.tf`, `ecr.tf`, `outputs.tf`.

Checkpoint: run `terraform fmt`, `terraform validate`, plan, apply, then demonstrate the ECR repository.

## Task 4 — GitHub OIDC and IAM with Terraform
Create the AWS identity configuration that allows GitHub Actions to assume an IAM role without stored AWS keys.

Requirements:
- GitHub Actions OIDC provider where appropriate for the account design.
- IAM role trusted through `sts:AssumeRoleWithWebIdentity`.
- Audience restricted to AWS STS.
- Subject condition restricted to **your repository** and intended branch/environment.
- Permissions limited to what the pipeline actually needs.
- Do not attach AdministratorAccess.

Checkpoint questions:
1. What are `aud` and `sub` in the GitHub OIDC token?
2. Why is `repo:ORG/REPO:*` broader than a branch-specific subject?
3. Why are GitHub AWS access-key secrets unnecessary here?

## Task 5 — Continuous Integration
Create the GitHub Actions CI workflow yourself.

It must run on pull requests and/or the branch strategy you choose and perform at least:
- checkout
- Python dependency installation
- automated tests
- Terraform formatting/validation when Terraform changes
- Docker build validation
- at least one security/static check you choose

The CI workflow must **not deploy pull requests**.

Checkpoint: intentionally break a unit test and prove that the workflow blocks progression.

## Task 6 — Continuous Delivery to ECR
Extend or create a workflow for trusted branch deployments.

Requirements:
- Request `id-token: write` only where OIDC is required.
- Assume your AWS IAM role using GitHub OIDC.
- Authenticate to ECR.
- Build the image.
- Tag it with the Git commit SHA.
- Push the SHA tag to ECR.
- Optionally maintain `latest`, but do not use it as the only deployment identity.

Checkpoint: select an ECR image and identify the exact Git commit that produced it.

## Task 7 — Deployment
Choose your deployment target. Recommended progression: reuse an existing EC2/ASG lab first; later repeat this pattern with ECS in Project 3 and EKS in Project 4.

Your deployment step must:
- use the immutable/SHA image identifier;
- fail if deployment fails;
- verify application health after deployment;
- avoid embedding credentials in scripts.

Document your deployment mechanism in the README you create for your implementation.

## Task 8 — Pipeline quality
Add at least three of these improvements and justify them:
- GitHub Environment approval for production
- concurrency protection
- dependency caching
- workflow timeouts
- artifact/SBOM generation
- image vulnerability gate
- rollback strategy
- separate CI and CD workflows
- reusable workflow

## Task 9 — Documentation
Write your own section explaining:
- pipeline stages;
- authentication flow;
- branching/deployment strategy;
- image-tagging strategy;
- security controls;
- rollback approach.

## Definition of done
You should be able to push a harmless application change and watch it pass tests, build a container, authenticate to AWS without long-lived keys, publish a traceable ECR image, deploy it, and verify health.
