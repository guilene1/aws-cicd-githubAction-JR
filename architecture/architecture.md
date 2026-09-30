# Target Architecture

```text
Developer
   |
   | git push / pull request
   v
GitHub Repository
   |
   v
GitHub Actions
   |-- unit tests
   |-- dependency / source checks
   |-- Docker build
   |-- image scan
   |
   | OIDC (no AWS access keys)
   v
AWS IAM Role
   |
   v
Amazon ECR
   |
   | immutable commit-SHA image
   v
Deployment Target
   |
   v
Health / deployment verification
```

## Required principles
- Short-lived AWS credentials via OIDC.
- Least privilege for the GitHub Actions IAM role.
- Never deploy an image that failed tests or required security checks.
- Every build must be traceable to a Git commit.
- Do not rely only on `latest`; publish a commit-SHA tag.
- Production deployment must not run from arbitrary pull-request code.
