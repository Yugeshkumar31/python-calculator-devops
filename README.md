# Python Calculator – DevOps Project

## Project Overview

A Python-based calculator that performs addition, subtraction, and multiplication of two positive integers.

This project demonstrates a complete DevOps workflow using Python, Pytest, Docker, GitHub Actions, AWS Lambda, API Gateway, and AWS SAM.

## Features

- Addition, subtraction, and multiplication.
- Input validation for positive integers.
- Unit testing using Pytest.
- Docker containerization.
- Automated CI/CD using GitHub Actions.
- Serverless deployment on AWS using Lambda and API Gateway.
- Infrastructure as Code using AWS SAM and CloudFormation.

## Technologies Used

- **Programming Language:** Python 3.13
- **Testing:** Pytest
- **Containerization:** Docker
- **Version Control:** Git and GitHub
- **CI/CD:** GitHub Actions
- **Cloud Platform:** AWS
- **Serverless:** AWS Lambda
- **API Management:** Amazon API Gateway (HTTP API)
- **Infrastructure as Code:** AWS SAM and CloudFormation

## Project Structure

```text
python-calculator-devops/
│
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   └── lambda_handler.py
│
├── tests/
│   └── test_calculator.py
│
├── .github/
│   └── workflows/
│       └── pipeline.yml
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── template.yaml
├── samconfig.toml
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-calculator-devops.git
cd python-calculator-devops
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run unit tests

```bash
python -m pytest -v
```

## Run Using Docker

### 1. Build the Docker image

```bash
docker build -t python-calculator .
```

### 2. Run the container

```bash
docker run --rm python-calculator
```

The container automatically executes the unit tests.

## AWS Deployment

The application is deployed using AWS SAM.

### AWS Architecture

1. GitHub stores the application source code.
2. GitHub Actions automatically starts when code is pushed.
3. The CI job builds the Docker image and runs unit tests.
4. If the tests pass, the deployment job starts.
5. AWS SAM builds and deploys the application.
6. AWS Lambda executes the calculator logic.
7. Amazon API Gateway exposes the calculator through an HTTP endpoint.
8. AWS CloudFormation manages the AWS infrastructure.

### AWS Resources

- AWS Lambda – Executes the calculator application.
- Amazon API Gateway – Provides the HTTP API endpoint.
- AWS IAM Role – Allows Lambda to access required AWS services.
- AWS CloudFormation – Manages infrastructure.
- Amazon S3 – Stores deployment artifacts.

## API Usage

The application exposes the following endpoint:

```text
GET /calculate
```

### Supported Operations

**Addition**

```text
/calculate?operation=add&a=10&b=5
```

**Subtraction**

```text
/calculate?operation=subtract&a=10&b=5
```

**Multiplication**

```text
/calculate?operation=multiply&a=10&b=5
```

### Example Response

```json
{
  "operation": "add",
  "a": 10,
  "b": 5,
  "result": 15
}
```

Use the API Gateway URL shown in the AWS CloudFormation stack Outputs, followed by the appropriate path and query parameters.

## CI/CD Pipeline

The GitHub Actions workflow is defined in:

```text
.github/workflows/pipeline.yml
```

The pipeline contains two jobs:

**1. Continuous Integration (CI)**

- Checks out the source code.
- Builds the Docker image.
- Runs unit tests inside the Docker container.

**2. Continuous Deployment (CD)**

- Runs only after successful CI on pushes to the `main` branch.
- Configures AWS credentials using GitHub repository secrets.
- Sets up AWS SAM.
- Builds the SAM application.
- Deploys the application to AWS.

## GitHub Configuration

The following repository secrets are required:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

The following repository variable is required:

- `AWS_REGION`

The AWS credentials are stored securely in GitHub repository settings and are not included in the source code.

## Infrastructure as Code

The AWS infrastructure is defined in:

```text
template.yaml
```

AWS SAM uses this template to create and manage the Lambda function, API Gateway, IAM execution role, and related resources through CloudFormation.

## Author

**G Yugesh Kumar**
