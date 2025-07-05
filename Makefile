SHELL := /bin/bash

######## WEB UI ########

# Build web UI
build-web-ui:
	docker build -t sermengi/web-ui:latest ./web_ui

# Run the Web UI locally
run-web-ui:
	cd web_ui && \
	source .venv/bin/activate && \
	streamlit run app.py

######## API Gateway ########

# Build API Gateway
build-api-gateway:
	docker build -t sermengi/api-gateway:latest ./api-gateway

# Run the API Gateway locally
run-api-gateway:
	cd api-gateway && \
	source .venv/bin/activate && \
	uvicorn main:app --reload --port 8000

######## Preprocessing Service ########

# Build Preprocessing Service
build-preprocessing:
	docker build -t sermengi/preprocessing:latest ./preprocessing-service

# Run the Preprocessing Service
run-preprocessing:
	cd preprocessing-service && \
	source .venv/bin/activate && \
	cd app && uvicorn main:app --reload --port 8001

######## TTS Service App ########

run-tts-microservice-app:
	docker-compose up --build
