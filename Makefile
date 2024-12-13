# Read variables from .env
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Variables
#APP_NAME = $(APP_NAME)
REGION = $(AWS_REGION)
ACCOUNT_ID = $(AWS_ACCOUNT_ID)
IMAGE_NAME = $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com/$(APP_NAME)

# Environment Management
install:
	pip install -r requirements.txt

# Start the application locally
start:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Lint and format the code
lint:
	black --check .
	isort --check-only .

format:
	black .
	isort .

# Run tests
test:
	pytest

# Build and run the Docker container locally
build:
	docker build -t $(APP_NAME) .

run-docker:
	docker run -p 8000:8000 $(APP_NAME)

# Deploy the Docker image to AWS Lambda
deploy:
	aws ecr get-login-password --region $(REGION) | docker login --username AWS --password-stdin $(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com
	docker tag $(APP_NAME):latest $(IMAGE_NAME):latest
	docker push $(IMAGE_NAME):latest
	aws lambda update-function-code --function-name $(APP_NAME) --image-uri $(IMAGE_NAME):latest

# Clean up Docker images
clean:
	docker rmi $(APP_NAME)
