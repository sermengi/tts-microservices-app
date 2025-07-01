SHELL := /bin/bash

# Run the API Gateway locally
run-api-gateway:
	cd api-gateway && \
	source .venv/bin/activate && \
	uvicorn main:app --reload


# Run the Web UI locally
run-web-ui:
	cd web_ui && \
	source .venv/bin/activate && \
	streamlit run app.py
