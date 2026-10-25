# DevPortfolio — CCA 2

## Project Overview
DevPortfolio is a simple Flask-based portfolio website deployed using
an automated CI/CD pipeline with Jenkins, Docker, Docker Hub, and Kubernetes.

## Technologies Used
- Python and Flask
- Git and GitHub
- Jenkins
- Docker
- Docker Hub
- Kubernetes and Minikube
- AWS EC2

## Features
- Responsive portfolio landing page
- Introduction and skills sections
- Health-check endpoint at `/health`
- Docker-based application packaging
- Automated build and deployment pipeline

## CI/CD Pipeline
1. Pull the latest source code from GitHub.
2. Check Python syntax.
3. Build the Docker image.
4. Push the image to Docker Hub.
5. Deploy the application to Minikube.
6. Verify the Kubernetes deployment and service.
7. Repeat the pipeline after a source-code change.

## Run Locally

Install dependencies:

    python -m pip install -r requirements.txt

Start the application:

    python app.py

Open http://127.0.0.1:5000

Health check: http://127.0.0.1:5000/health

## Deployment
The application is containerized using the included Dockerfile
and deployed through Kubernetes Deployment and Service manifests
in the `k8s/` directory.

## Author
Kushagra Jha
