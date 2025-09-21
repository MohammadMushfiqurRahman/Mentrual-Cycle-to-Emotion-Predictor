# Menstrual Cycle and Emotion Predictor

This project is a Django web application that predicts menstrual cycle length and emotions based on user input. It includes a machine learning model trained on menstrual cycle data from Kaggle.

## Table of Contents
- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Features](#features)
- [Project Structure](#project-structure)
- [Models](#models)
- [Dataset](#dataset)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project combines a machine learning model with a web interface to provide predictions related to the menstrual cycle. The backend is built with Django, and the machine learning models are built using scikit-learn.

## Motivation

*(Please add a brief description of the problem this project solves or the motivation behind creating it.)*

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

*(Please update this section with more details about the models, such as the features used, the target variables, and the model performance metrics like accuracy, F1-score, etc.)*

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
-   Kaggle API Key

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

## Testing

To run the tests, you need to have the Django development server running.

1.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Open a new terminal and run the test scripts:**
    ```bash
    python test_frontend.py
    python test_predictor.py
    ```

## Deployment

This is a standard Django application and can be deployed to any platform that supports Python and Django. Here are some general steps for deployment:

1.  **Choose a hosting provider:** Heroku, PythonAnywhere, AWS, Google Cloud, etc.
2.  **Configure your `settings.py` for production:**
    -   Set `DEBUG = False`.
    -   Configure `ALLOWED_HOSTS` with your domain name.
    -   Use a production-ready database like PostgreSQL.
3.  **Set up a production-ready web server:** Use a web server like Gunicorn or uWSGI to serve your application.
4.  **Serve static files:** Configure a service like Whitenoise or use a separate web server like Nginx to serve your static files.

For detailed instructions, please refer to the Django deployment documentation.

## Future Work

*(Please add any ideas for future improvements to the project, such as adding new features, improving the models, or supporting more languages.)*

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify,merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
