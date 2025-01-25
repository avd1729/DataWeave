# DataWeave

## Overview
Synthetic dataset generator using Apache Airflow and Groq open-source models, designed to generate and load data into MongoDB collections.


## Project Core Values
- **Intelligent Data Generation**: Leveraging AI for synthetic dataset creation
- **Workflow Automation**: Streamlined data pipeline using Apache Airflow
- **Scalable Architecture**: Flexible data generation and loading mechanisms
- **Open-Source Transparency**: Modular design for easy customization

## Apache Airflow: Quick Introduction
Apache Airflow is an open-source platform for orchestrating complex computational workflows and data processing pipelines. Key benefits:
- Programmatic workflow definition
- Dependency management
- Monitoring and retry mechanisms
- Scalable task execution


### Airflow Installation
```bash
# Using pip
pip install apache-airflow

# Using Astro CLI (recommended)
brew install astro  # macOS
# Windows/Linux: Download from Astronomer website
```

## Prerequisites
- Python 3.8+
- Apache Airflow 2.x
- Groq API access
- MongoDB
- Astro CLI (optional)

## Installation
```bash
# Clone repository
git clone https://github.com/avd1729/DataWeave.git

# Create virtual environment
virtualenv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\Activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

## Configuration
1. Set Groq API credentials
2. Configure MongoDB connection
3. Define Airflow DAG parameters

## Project Structure
```
dataweave/
│
├── dags/                # Airflow workflow definitions
├── utils/               # Data processing utilities
│   ├── data_extraction.py
│   ├── data_loading.py
│   └── data_transformation.py
└── requirements.txt
```

## Data Extraction Strategy
- Use Groq AI models for intelligent data generation
- Parameterized generation based on predefined schemas
- Support for multiple data domain generations

## Running the Project
```bash
# Start Airflow development environment
astro dev start
```

![image](https://github.com/user-attachments/assets/67f0853d-20c2-405e-8590-c2c0125e9f7d)

