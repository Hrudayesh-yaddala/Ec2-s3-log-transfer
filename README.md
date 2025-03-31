# Automating Log File Transfer from EC2 to S3 using AWS Lambda and SSM

## Overview

This guide explains how to **automate log file transfers** from an EC2 instance to an S3 bucket using:

- **AWS Lambda** to trigger the process.
- **AWS Systems Manager (SSM)** to execute commands on EC2.
- **Amazon S3** to store the logs.
- **Amazon EventBridge** to schedule execution at a fixed time.

---

## **Prerequisites**

Before proceeding, make sure you have:
✅ **An EC2 Instance** (Amazon Linux/Ubuntu)  
✅ **An S3 Bucket** (to store logs)  
✅ **AWS Lambda Function** (to trigger the process)  
✅ **IAM Roles with Proper Permissions**

---

## **Step 1: Create AWS Resources**

### **1.1 Create an S3 Bucket**

1. Open the **AWS S3 Console** → Click **Create Bucket**.
2. Enter a **unique bucket name** (e.g., `my-log-bucket`).
3. Choose a **region** and leave other settings as default.
4. Click **Create Bucket**.

### **1.2 Launch an EC2 Instance**

1. Open the **AWS EC2 Console** → Click **Launch Instance**.
2. Choose **Amazon Linux 2** or **Ubuntu** as the OS.
3. Select an instance type (e.g., `t2.micro` for free tier).
4. Configure networking and **attach the IAM role** (created in Step 2).
5. Click **Launch**.

---

## **Step 2: Create IAM Roles and Attach Policies**

### **2.1 IAM Role for EC2 (To run SSM commands and access S3)**

1. Open **AWS IAM Console** → **Roles** → Click **Create Role**.
2. Select **EC2** as the trusted entity.
3. Attach these policies:
   - `AmazonSSMManagedInstanceCore`
   - `AmazonS3FullAccess`
4. Name the role **EC2-SSM-S3-Role** and **attach it to your EC2 instance**.

### **2.2 IAM Role for Lambda (To send SSM commands and access S3)**

1. Open **AWS IAM Console** → **Roles** → Click **Create Role**.
2. Select **Lambda** as the trusted entity.
3. Attach these policies:
   - `AmazonSSMFullAccess`
   - `AmazonS3FullAccess`
4. Name the role **Lambda-SSM-S3-Role** and **attach it to the Lambda function**.

---

## **Step 3: Install and Verify Amazon SSM Agent on EC2**

For **Amazon Linux**:

```sh
sudo yum install -y amazon-ssm-agent
sudo systemctl enable amazon-ssm-agent
sudo systemctl start amazon-ssm-agent
```
