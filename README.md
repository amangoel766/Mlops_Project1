🚗 End-to-End MLOps Vehicle Price Prediction Pipeline
📌 Objective

Build and deploy a production-grade end-to-end MLOps pipeline covering:

Data ingestion from MongoDB

Validation, transformation, and model training

Model evaluation and versioning using AWS S3

CI/CD with Docker, GitHub Actions, ECR, and EC2

Real-time prediction via Flask web application

This project demonstrates industry-aligned MLOps practices with strong emphasis on reproducibility, scalability, and automation.

🧠 High-Level Architecture (Mental Model)
Data (MongoDB)
      ↓
Data Ingestion
      ↓
Data Validation → Schema Check
      ↓
Data Transformation
      ↓
Model Training (Random Forest)
      ↓
Model Evaluation
      ↓
Model Registry (AWS S3)
      ↓
Flask App (Prediction)
      ↓
Docker → ECR → EC2 (CI/CD)

🛠 Tools & Technologies
Category	Tools
Language	Python 3.10
ML	Scikit-learn, Pandas, NumPy
Database	MongoDB Atlas
Cloud	AWS S3, ECR, EC2
MLOps	Custom Pipeline, CI/CD
DevOps	Docker, GitHub Actions
Web	Flask (Async Ready)
Versioning	Git, GitHub
Environment	Conda, Virtual Envs
📂 Project Setup & Environment
1️⃣ Project Bootstrap

Created GitHub repository

Generated project template using template.py

Established modular folder structure with placeholders

2️⃣ Local Package Management

Implemented setup.py and pyproject.toml

Enabled editable installs (pip install -e .)

Ensured src/ recognized as a local package

3️⃣ Environment Setup
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list


Verified local packages successfully installed.

🗄 MongoDB Data Ingestion
MongoDB Setup

MongoDB Atlas (M0 cluster)

Network access: 0.0.0.0/0

Python connection via environment variable

export MONGODB_URL="mongodb+srv://<user>:<password>@cluster0..."

Data Flow

Data pushed via notebook → MongoDB

Fetched using custom data access layer

Converted from key-value format → Pandas DataFrame

Stored in artifact directory

📜 Logging & Exception Handling

Centralized logging using RotatingFileHandler

Custom exception class with traceback details

Configured at package import (__init__.py)

Validated via demo.py

🧪 ML Pipeline Components

Each component follows a consistent execution pattern:

constants → configuration

entity → config & artifact dataclasses

components → core logic

pipeline → orchestration

Components Implemented

Data Ingestion

Data Validation (schema-based)

Data Transformation

Model Training (Random Forest)

Model Evaluation

Model Pusher

Note:
GridSearchCV intentionally excluded to keep pipeline deterministic.

📦 Model Design (Key Insight)

A single deployable model object is created using:

MyModel(preprocessing_object, trained_model)


This ensures:

Identical preprocessing during training & inference

No feature mismatch in production

Clean model registry storage

☁️ AWS Integration
Services Used

S3 → Model registry

ECR → Docker image storage

EC2 → Application hosting

IAM → Secure access

Environment variables used for credentials to ensure:

Security

Environment decoupling

CI/CD compatibility

🌐 Web Application

Flask-based inference app

Async-ready routes

HTML/CSS frontend

/train route triggers training pipeline

/predict route serves predictions

🚀 CI/CD Pipeline
Continuous Integration

Docker build

Push image to AWS ECR

Continuous Deployment

Self-hosted GitHub Actions runner on EC2

Pull Docker image

Run container exposing port 5000

🔁 Deployment Flow
Git Push
   ↓
GitHub Actions
   ↓
Docker Build
   ↓
Push to ECR
   ↓
EC2 pulls image
   ↓
Flask App Live

🔐 Secrets Management

Configured via GitHub Secrets:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_DEFAULT_REGION

ECR_REPO

MONGODB_URL (optional)

🌍 Final Output

Application accessible via EC2 public IP

Model training & prediction available remotely

CI/CD fully automated

Scalable, reproducible ML system

