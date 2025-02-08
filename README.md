# EthioMed Data Warehouse Project

[![CI Status](https://github.com/beckhamberhanu/EthioMed-DataWarehouse/actions/workflows/ci.yml/badge.svg)](https://github.com/beckhamberhanu/EthioMed-DataWarehouse/actions)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A comprehensive data engineering pipeline for Ethiopian medical businesses, featuring Telegram data scraping, YOLO object detection, and FastAPI data exposure.

---

## 🚀 Features

- **Telegram Data Scraping**: Automated collection of text and images from medical channels.
- **Data Cleaning Pipeline**: ETL/ELT workflows with DBT.
- **YOLO Object Detection**: Medical product recognition in images.
- **FastAPI Interface**: RESTful API for data access.
- **Google Colab Integration**: Notebooks for cloud-based analysis.

---

## 📁 Project Structure

```bash
EthioMed-DataWarehouse/
├── .github/              # GitHub Actions workflows
│   └── workflows/
│       ├── ci.yml        # CI/CD pipeline
├── data/                 # Raw and processed data (ignored in Git)
│   ├── raw/              # Raw scraped data
│   ├── processed/        # Cleaned and transformed data
│   ├── yolo_dataset/Images
│   ├── yolo_detections/    
├── scripts/              # Core pipeline scripts
│   ├── data_ingestion.py          # Telegram scraping pipeline
│   ├── data_preprocessing.py      # Cleaning and formatting text
│   dbt/
│   ├── ethiomed_transformations    # data transformation
│   yolo/
│   ├── detect.py          
│   ├── prepare_images.py
│   api/
│   ├── crud.py          
│   ├── database.py
│   ├── main.py          
│   ├── models.py
│   ├── schemas.py          
├── models/               # Trained models and evaluation results
│   ├── trained_models/   # Fine-tuned models
│   ├── results/          # Model performance reports
├── tests/                # Unit tests
│   ├── test_data_preprocessing.py
│   ├── test_ner_training.py
├── .gitignore            # Ignore unnecessary files
├── requirements.txt      # Python dependencies
├── dvc.yaml              # Data version control (DVC)
├── .env                  # Environment variables (Telegram API, DB connection)
├── LICENSE               # License information
└── README.md             # Project documentation


```

## 🛠 Installation

### 1️⃣ Clone the Repository

```bash
git clone [https://github.com/beckhamberhanu/EthioMed-DataWarehouse.git](https://github.com/beckhamberhanu/EthioMed-DataWarehouse.git)
cd EthioMed-DataWarehouse

```
### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt

```
3️⃣ Set Up Environment Variables
Create a .env file and add the following:

```bash

TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
DATABASE_URL=postgresql://user:password@localhost:5432/ethiomed

```
## 🚀 Usage
Running the Data Pipeline

```bash
# Run Telegram scraping pipeline
python scripts/data_ingestion.py

# Start DBT transformations
cd scripts/dbt
dbt run

```
### Install dependencies:

```bash
pip install /EthioMed-DataWarehouse/requirements.txt

```
## 📌 CI/CD with GitHub Actions
This repository includes an automated CI/CD pipeline using GitHub Actions. The workflow:

1. Runs unit tests on every commit.
2. Lints and formats the code.
3. Deploys new changes when merged to the main branch.

## 👥 Contributing
1. Create an issue to discuss proposed changes.
2. Fork the repository.
3. Create a feature branch (git checkout -b feature-branch).
4. Commit changes (git commit -m "Add new feature").
5. Push to GitHub (git push origin feature-branch).
6. Open a Pull Request.

## 📬 Contact
For questions or collaborations, contact Beckham Berhanu at getbeckham@gmail.com.