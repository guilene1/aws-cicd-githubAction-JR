# Project 2 — Production CI/CD Pipeline with GitHub Actions and AWS

## Job-readiness goal
You are the DevOps engineer responsible for taking a small application from source code to an automated AWS deployment. The application is provided. **The pipeline is not.**

You will design and implement a CI/CD pipeline using GitHub Actions, Docker, Amazon ECR and AWS IAM/OIDC. Terraform must be used for the AWS resources required by the pipeline.

## What is provided
- Small Flask application and one automated test
- Architecture target and requirements
- Progressive assignments
- Validation checklist
- Troubleshooting incidents
- Interview questions

## What you must write
- `Dockerfile` and `.dockerignore`
- Terraform for ECR and GitHub OIDC/IAM
- GitHub Actions CI/CD workflow(s)
- Repository variables/configuration required by your workflow
- Deployment strategy chosen for the lab target

No completed infrastructure or workflow solution is included.

## Target flow
`git push -> GitHub Actions -> test -> scan -> build -> ECR -> deploy -> verify`

Authentication to AWS must use **GitHub OIDC and an IAM role**. Do not store long-lived AWS access keys in GitHub.

## Your progression
1. Run and test the application locally.
2. Containerize it.
3. Provision ECR with Terraform.
4. Configure GitHub-to-AWS OIDC with least-privilege IAM.
5. Build CI checks.
6. Build CD: tag and push images to ECR.
7. Deploy the image to the target you selected.
8. Add verification and failure handling.
9. Troubleshoot broken pipeline scenarios.
10. Explain the design in an interview.

Start with `assignments/PROJECT.md`.
