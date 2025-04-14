# 🚀 Optimized Log File Transfer from EC2 to S3 Using Cron Job (No Lambda!)

This guide helps you **automate the transfer of log files** from an EC2 instance to an S3 bucket using a simple and cost-effective method — **cron jobs and shell scripting**, instead of AWS Lambda and EventBridge.

---

## Problem Statement

Previously, we used **Lambda functions** and **EventBridge rules** to automate pushing logs from EC2 to S3. While this worked well, it introduced **extra service costs** and increased **infrastructure complexity**.

So we asked — *Can we do this better, cheaper, and simpler?*

Yes. Here’s how 👇

---

## Prerequisites

- EC2 instance with AWS CLI configured (IAM role attached or credentials available)
- S3 bucket created to receive the logs
- Your log file (e.g., `/var/log/app.log`) exists on the instance

---

## Step 1: Create a Shell Script

Open a terminal and run:

```bash
nano /home/ubuntu/upload_log.sh 

# Paste the following:
#!/bin/bash

# Date format
DATE=$(date +%Y-%m-%d)

# Upload log to S3 (use full path for AWS CLI)
# Replace 'your-log-file' and 'your-bucket-name' accordingly
/usr/bin/aws s3 cp /var/log/your-log-file.log s3://your-bucket-name/logs/your-log-file-$DATE.log
