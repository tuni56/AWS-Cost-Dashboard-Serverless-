# Step-by-Step Setup

## 1. Create S3 Bucket

1. Go to S3 console.
2. Create bucket (example: `my-cur-bucket`).
3. Enable **Cost & Usage Reports (CUR)**:
   - Name: aws-cost-report
   - Time unit: DAILY
   - Format: CSV
   - Compression: GZIP
   - Additional schema elements: RESOURCES
4. Ensure Lambda has `s3:GetObject` access.

---

## 2. Deploy Lambda

1. Create new Lambda (Python 3.11).
2. Assign IAM role with:
   - `AWSLambdaBasicExecutionRole`
   - `CloudWatchPutMetricData`
   - `S3Read`
3. Upload `lambda_function.py`.
4. Set S3 trigger on bucket for `PUT` events.

---

## 3. CloudWatch Dashboard

1. Go to CloudWatch > Dashboards > Create dashboard.
2. Import `cloudwatch_dashboard.json`.
3. Monitor `DailyTotalCost` and service-level costs.

---

## 4. Optional SNS Alerts

1. Create SNS topic.
2. Subscribe your email.
3. Update Lambda to push alerts if cost exceeds threshold.

---

## 5. Test

1. Upload sample CUR file to S3.
2. Check CloudWatch for new metrics.
3. Verify email alerts if configured.

---

## Notes & Tips

- Keep stack minimal for ~$12/month.
- Perfect hands-on practice for **SAA-C03** concepts:
  - Event-driven architecture
  - IAM best practices
  - Monitoring & alerting
