# 🚀 Azure CI/CD Pipeline using Azure DevOps

## 📌 Project Overview

This project demonstrates the implementation of a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline using Azure DevOps. The application is containerized using Docker, stored in Azure Container Registry (ACR), and automatically deployed to Azure App Service whenever changes are pushed to the GitHub repository.

The project showcases modern DevOps practices, automation, and cloud-native deployment workflows.

---

## 🎯 Objectives

- Implement Continuous Integration using Azure Pipelines
- Containerize the application using Docker
- Store Docker images in Azure Container Registry (ACR)
- Automate deployment to Azure App Service
- Demonstrate Continuous Deployment practices
- Monitor and manage the deployment pipeline

---

## 🛠️ Technologies Used

- Azure DevOps
- Azure Pipelines
- Azure Container Registry (ACR)
- Azure App Service
- Docker
- Python Flask
- Git & GitHub

---

## 📂 Project Structure

```text
CodeAlpha_CICD_Azure/
│
├── screenshots/
│   ├── deployment-success.png
│
├── Dockerfile
├── README.md
├── app.py
├── azure-pipelines.yml
└── requirements.txt
```

---

## ⚙️ CI/CD Workflow

```text
Developer Pushes Code
          │
          ▼
      GitHub
          │
          ▼
 Azure DevOps Pipeline
          │
          ▼
 Docker Image Build
          │
          ▼
 Azure Container Registry
          │
          ▼
 Azure App Service
          │
          ▼
 Live Web Application
```

---

## 🐳 Docker Containerization

The Flask application is packaged into a Docker container to ensure consistency across development, testing, and production environments.

### Build Docker Image

```bash
docker build -t flaskapp .
```

### Run Container

```bash
docker run -p 5000:5000 flaskapp
```

---

## ☁️ Azure Services Used

### Azure Container Registry (ACR)

Stores and manages Docker container images securely.

### Azure App Service

Hosts the containerized web application and enables automatic deployment from Azure Pipelines.

### Azure Pipelines

Automates build, test, and deployment processes.

---

## 🔄 Pipeline Features

- Automated Build Process
- Docker Image Creation
- Image Push to Azure Container Registry
- Automated Deployment
- Continuous Integration
- Continuous Delivery
- Version Control Integration

---

## 📸 Screenshots

Add the following screenshots inside the `screenshots` folder:

- Successful Deployment Logs

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/YourUsername/CodeAlpha_CICD_Azure.git
```

### Navigate to Project

```bash
cd CodeAlpha_CICD_Azure
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 📈 Benefits of CI/CD

- Faster Software Delivery
- Reduced Manual Errors
- Automated Deployments
- Improved Reliability
- Better Collaboration Between Development and Operations Teams
- Faster Feedback and Issue Resolution

---

## 🎓 Internship Task

This project was developed as part of the **CodeAlpha DevOps Internship Program**.

### Task 1: CI/CD Pipeline using Azure

Requirements Completed:

✔ Azure Pipeline Configuration  
✔ Docker Containerization  
✔ Azure Container Registry Integration  
✔ Azure App Service Deployment  
✔ Continuous Integration Setup  
✔ Continuous Deployment Setup

---

## 👨‍💻 Author

**Kartik Gupta**

DevOps Intern – CodeAlpha


---

## 📄 License

This project is developed for educational and internship purposes.
