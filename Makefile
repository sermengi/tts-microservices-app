SHELL := /bin/bash

# Build web UI
build-web-ui:
	docker build -t sermengi/web-ui:latest ./web_ui

# Run the Web UI locally
run-web-ui:
	cd web_ui && \
	source .venv/bin/activate && \
	streamlit run app.py

# Build API Gateway
build-api-gateway:
	docker build -t sermengi/api-gateway:latest ./api-gateway

# Run the API Gateway locally
run-api-gateway:
	cd api-gateway && \
	source .venv/bin/activate && \
	uvicorn main:app --reload --port 8000

# Build Preprocessing Service
build-preprocessing:
	docker build -t sermengi/preprocessing:latest ./preprocessing-service

# Run the API Gateway locally
run-preprocessing:
	cd preprocessing-service && \
	source .venv/bin/activate && \
	cd app && uvicorn main:app --reload --port 8001

run-tts-microservice-app:
	docker-compose up --build
