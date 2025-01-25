# Synthetic Dataset Generator

## Overview
Synthetic dataset generator using Apache Airflow and Groq open-source models for data generation.

## Prerequisites
- Python 3.8+
- Apache Airflow 2.x
- Groq API access
- Pandas
- NumPy

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/synthetic-dataset-generator.git

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

### Groq API Setup
1. Obtain Groq API credentials
2. Set environment variables:
   - `GROQ_API_KEY`
   - `GROQ_MODEL`

### DAG Configuration
Customize `dags/synthetic_data_generator.py`:
- Dataset generation parameters
- Groq model configurations
- Output settings

## Usage

### Running the Airflow DAG
```bash
astro dev start
```

## Main Project Structure
```
synthetic-dataset-generator/
│
├── dags/
│   └── synthetic_data_generator.py
├── utils/
│   └── data_extraction.py
│   └── data_loading.py
|   └── data_transformation.py
└── requirements.txt
```

## Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request

## License
MIT License
