# AWS Cost Dashboard (Serverless)

Turn your fear of surprise AWS bills into a $12/month learning project.  

This repository provides everything you need to build a **serverless cost-tracking dashboard** using:

- **Amazon S3** (store Cost & Usage Reports)
- **AWS Lambda** (process & transform CUR)
- **Amazon CloudWatch** (visualize metrics in near real-time)

Perfect for **SAA-C03 students**, small projects, or anyone who wants cost visibility without expensive tools.

---

## TL;DR

1. Set up S3 bucket for Cost & Usage Reports.
2. Deploy Lambda to process CUR.
3. Create CloudWatch dashboard with the provided template.
4. Monitor costs in near real-time for ~$12/month.

---

## Architecture

![Architecture Diagram](docs/architecture_diagram.png)

1. **CUR → S3**: Automatically delivered daily.
2. **S3 Event → Lambda**: Processes new reports, extracts key metrics.
3. **Lambda → CloudWatch**: Pushes metrics to a dashboard.
4. Optional: **SNS Alerts** for thresholds.

---

## Setup

See [docs/step_by_step_setup.md](docs/step_by_step_setup.md) for full instructions, including:

- IAM roles & permissions
- S3 bucket configuration
- Lambda deployment
- CloudWatch dashboard import
- Optional alerting

---

## Cost

- ~$12/month total
- Compare to $200+ for commercial solutions

---

## Learning Outcomes

- Event-driven architectures
- IAM best practices
- Real-time monitoring
- Cost optimization & serverless design

---

## Try It Yourself

Follow the instructions and customize the dashboard to your account.

Templates & scripts included in `/templates` and `/scripts`.

---

## License

MIT License

---

## Give this repo an star if you find it useful and share with someone who struggles with AWS costs.
This is an open source repo, fork it if you want to add some contributions.
