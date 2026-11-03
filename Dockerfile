
# 1. Select the base Python image
FROM python:3.13-slim

# 2. Set the working directory inside container
WORKDIR /app

# 3. Copy dependency file
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application and test files
COPY app/ ./app/
COPY tests/ ./tests/

# 6. Run unit tests when container starts
CMD ["python", "-m", "pytest", "-v"]
