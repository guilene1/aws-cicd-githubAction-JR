# Terraform Workspace — Yours to Build

Create the Terraform implementation here. There is intentionally no solution code.

Minimum resources/configuration expected:
- Amazon ECR repository and lifecycle policy
- GitHub Actions OIDC trust configuration
- CI/CD IAM role
- least-privilege role policy
- variables and outputs

Run before submission:
```bash
terraform fmt -recursive
terraform init
terraform validate
terraform plan
```

Do not commit state files, credentials, or secret values.
