# AI Workflow Deployment Project

This repository contains the code for deploying an AI workflow to predict revenue based on transaction data.

## Project Structure

- `app/`: Contains the Flask application and related modules.
  - `app.py`: Main application script for Flask.
  - `model.py`: Contains the machine learning model.
  - `data_ingestion.py`: Script for data ingestion and preprocessing.
  - `logging_config.py`: Configuration for logging.
  - `tests/`: Contains unit tests for the application.
    - `test_api.py`: Unit tests for API endpoints.
    - `test_model.py`: Unit tests for the machine learning model.
    - `test_logging.py`: Unit tests for logging.
    - `run_tests.sh`: Script to run all unit tests.

- `prometheus_monitoring.py`: Script to monitor model performance using Prometheus.
- `visualizations/`: Contains scripts for data visualizations.
  - `eda_visualization.py`: Script for EDA visualizations.
  - `model_vs_baseline.py`: Script to visualize model vs. baseline performance.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ai-workflow-deployment.git
    cd ai-workflow-deployment
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app/app.py
    ```

4. Run unit tests:

    ```bash
    bash app/tests/run_tests.sh
    ```

5. Build and run the Docker container:

    ```bash
    docker build -t ai-workflow-deployment .
    docker run -p 5000:5000 ai-workflow-deployment
    ```

6. Monitor model performance:

    ```bash
    python prometheus_monitoring.py
    ```

## Usage

The API provides endpoints to get revenue predictions for specific countries and all countries combined.

- `/predict?country=<country>`: Get prediction for a specific country.
- `/predict_all`: Get predictions for all countries.

