#  Validation Checklist

- [ ] You can run the app and tests locally.
- [ ] Your own Dockerfile builds and the container health endpoint works.
- [ ] Terraform is formatted and validates.
- [ ] ECR was provisioned with Terraform.
- [ ] GitHub Actions authenticates to AWS through OIDC, not static access keys.
- [ ] Trust policy is restricted to the intended repository/context.
- [ ] IAM role is not AdministratorAccess.
- [ ] PR CI runs tests and does not deploy.
- [ ] Failed tests prevent delivery.
- [ ] Image is tagged with Git SHA and pushed to ECR.
- [ ] You can map the deployed image back to a commit.
- [ ] Deployment includes a health verification step.
- [ ] You can explain a rollback approach.
- [ ] You complete at least three break/fix scenarios without being given the answer.
- [ ] No secrets, `.tfstate`, AWS keys, or tokens are committed.
