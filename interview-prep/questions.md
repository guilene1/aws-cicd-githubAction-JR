# Interview Preparation

Answer these from what you actually built.

1. Walk me through your CI/CD pipeline from `git push` to deployment.
2. Why did you use GitHub OIDC instead of AWS access keys stored as GitHub secrets?
3. Explain the IAM trust policy for GitHub Actions.
4. What is the difference between the IAM trust policy and the role permissions policy?
5. How do you ensure pull requests cannot deploy to production?
6. Why tag Docker images with a Git SHA instead of only `latest`?
7. How would you roll back a failed deployment?
8. Where should security scanning happen in a pipeline?
9. What should cause a pipeline to fail?
10. How do you prevent two deployments from racing each other?
11. How would you apply least privilege to ECR permissions?
12. Your workflow can assume the AWS role but gets AccessDenied pushing an image. How do you troubleshoot it?
13. A deployment says successful but users still see the old version. What do you check?
14. What belongs in Terraform versus GitHub Actions?
15. How would this pipeline change when deploying to ECS or Kubernetes?

## STAR story exercise
Prepare a 2-minute story covering a pipeline failure you diagnosed. Include the symptom, your investigation, evidence, root cause, fix, and one preventive improvement.
