import csv
import boto3

# Replace these with your AWS credentials and region
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
aws_region = 'us-east-1'  # Change to your desired AWS region

# Create an AWS IAM client
client = boto3.client('iam', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

input_file = 'input.csv'  # Change to your input CSV file name

with open(input_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        user = row['user']
        group = row['group']
        password = row['password']

        if user != 'user':
            # Create IAM user
            client.create_user(UserName=user)

            # Create login profile for the user with password reset required
            client.create_login_profile(UserName=user, Password=password, PasswordResetRequired=True)

            # Add user to IAM group
            client.add_user_to_group(GroupName=group, UserName=user)

print("IAM user creation completed.")
