# Menstrual Cycle and Emotion Predictor

This project is a Django web application that predicts menstrual cycle length and emotions based on user input. It includes a machine learning model trained on menstrual cycle data from Kaggle.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Models](#models)
- [Dataset](#dataset)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project combines a machine learning model with a web interface to provide predictions related to the menstrual cycle. The backend is built with Django, and the machine learning models are built using scikit-learn.

## Features

-   **Cycle Length Prediction:** Predicts the length of the menstrual cycle.
-   **Emotion Prediction:** Predicts emotions based on cycle data.
-   **Web Interface:** A user-friendly web form to input data and see predictions.

## Project Structure

```
├───manage.py                           # Django's command-line utility
├───Menstrual_cycle_length_prediction.ipynb # Jupyter notebook for data exploration and model training
├───menstrual_cycle_predictor/          # Django project directory
│   ├───settings.py                     # Django settings
│   └───urls.py                         # Project-level URL routing
├───predictor/                          # Django app for predictions
│   ├───models.py                       # Database models (if any)
│   ├───views.py                        # Views for handling requests
│   ├───urls.py                         # App-level URL routing
│   ├───static/                         # Static files (CSS, JS, images)
│   └───models/                         # Saved machine learning models
│       ├───DecisonTreeModel.pickle
│       ├───emotion_model.pkl
│       └───saved_model.sav
└───templates/                          # HTML templates
    ├───predictor_form.html
    └───predictor_results.html
```

## Models

The project uses the following pre-trained machine learning models:

-   **`DecisonTreeModel.pickle`:** A decision tree model for cycle length prediction.
-   **`emotion_model.pkl`:** A model for emotion prediction.
-   **`saved_model.sav`:** Another model for cycle length prediction (likely a different algorithm).

These models are stored in the `predictor/models/` directory.

## Dataset

The dataset used for training the models is from Kaggle:

-   **Name**: Menstrual Cycle Data
-   **Source**: [Kaggle](https://www.kaggle.com/datasets/nikitabisht/menstrual-cycle-data)

The `Menstrual_cycle_length_prediction.ipynb` notebook contains the code for downloading, cleaning, and preparing the data.

## Getting Started

### Prerequisites

-   Python 3.10 or later
-   pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd Mentrual-Cycle-to-Emotion-Predictor
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download Kaggle API Key:**
    -   Go to your Kaggle account settings.
    -   Under the "API" section, click "Create New API Token" to download `kaggle.json`.
    -   Place this `kaggle.json` file in the `~/.kaggle/` directory on your local machine.

## Usage

1.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

2.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```

3.  Open your web browser and go to `http://127.0.0.1:8000/` to use the application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is unlicensed. You are free to use, modify, and distribute the code. However, it is provided "as is" without any warranty. Consider adding an open-source license like MIT if you want to encourage collaboration.