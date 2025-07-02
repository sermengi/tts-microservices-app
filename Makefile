SHELL := /bin/bash

# Build Docker images
build-api-gateway:
	docker build -t sermengi/api-gateway:latest ./api-gateway

# Run the API Gateway locally
run-api-gateway:
	cd api-gateway && \
	source .venv/bin/activate && \
	uvicorn main:app --reload

build-web-ui:
	docker build -t sermengi/web-ui:latest ./web_ui

# Run the Web UI locally
run-web-ui:
	cd web_ui && \
	source .venv/bin/activate && \
	streamlit run app.py
