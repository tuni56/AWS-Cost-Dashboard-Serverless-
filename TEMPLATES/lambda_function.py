import boto3
import csv
import gzip
import os
from datetime import datetime

cloudwatch = boto3.client('cloudwatch')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    tmp_file = '/tmp/cost_report.csv.gz'
    s3.download_file(bucket, key, tmp_file)
    
    # Detect if file is gzipped
    if key.endswith('.gz'):
        with gzip.open(tmp_file, 'rt') as f:
            reader = csv.DictReader(f)
            process_csv(reader)
    else:
        with open(tmp_file, 'r') as f:
            reader = csv.DictReader(f)
            process_csv(reader)

def process_csv(reader):
    daily_cost = 0.0
    service_costs = {}
    
    for row in reader:
        amount = float(row.get('BlendedCost', 0))
        service = row.get('ServiceName', 'Unknown')
        daily_cost += amount
        service_costs[service] = service_costs.get(service, 0) + amount
    
    # Push metrics to CloudWatch
    cloudwatch.put_metric_data(
        Namespace='AWS/CostDashboard',
        MetricData=[
            {
                'MetricName': 'DailyTotalCost',
                'Timestamp': datetime.utcnow(),
                'Value': daily_cost,
                'Unit': 'None'
            }
        ]
    )
    
    for service, cost in service_costs.items():
        cloudwatch.put_metric_data(
            Namespace='AWS/CostDashboard',
            MetricName=f'{service}_Cost',
            Timestamp=datetime.utcnow(),
            Value=cost,
            Unit='None'
        )
