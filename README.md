# Menstrual Cycle Length Prediction

This repository contains a Jupyter Notebook (`Menstrual_cycle_length_prediction.ipynb`) that explores and processes menstrual cycle data, aiming to prepare it for potential prediction tasks.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Data Cleaning and EDA Highlights](#data-cleaning-and-eda-highlights)

## Project Overview
This notebook focuses on the initial steps of a machine learning project: data acquisition, exploratory data analysis (EDA), and extensive data cleaning. The primary goal is to transform raw menstrual cycle data into a clean and suitable format for building predictive models for cycle length.

## Dataset
The dataset used in this project is sourced from Kaggle:
- **Name**: Menstrual Cycle Data
- **Source**: Kaggle ([nikitabisht/menstrual-cycle-data](https://www.kaggle.com/datasets/nikitabisht/menstrual-cycle-data))
- **File**: `FedCycleData071012 (2).csv`

The dataset contains various features related to menstrual cycles, including `LengthofCycle`, `EstimatedDayofOvulation`, `LengthofLutealPhase`, and many others (80 columns initially).

## Dependencies
The following libraries are required to run the notebook:
- `numpy`
- `pandas`
- `matplotlib.pyplot`
- `seaborn`
- `sklearn.preprocessing.LabelEncoder`
- `sklearn.preprocessing.StandardScaler`
- `sklearn.model_selection.train_test_split`
- `kagglehub` (for downloading the dataset)
- `os` (for file path operations)

## Usage

1.  **Clone the repository (or download the notebook):**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Install dependencies:**
    ```bash
    pip install numpy pandas matplotlib seaborn scikit-learn kagglehub
    ```
    *Note: If running in Google Colab, `kagglehub` might already be installed, or you can install it within a notebook cell.*

3.  **Download Kaggle API Key:**
    -   Go to your Kaggle account settings.
    -   Under the "API" section, click "Create New API Token" to download `kaggle.json`.
    -   Upload this `kaggle.json` file to your Colab environment (if using Colab) or place it in the `~/.kaggle/` directory on your local machine.

4.  **Run the Jupyter Notebook:**
    Open `Menstrual_cycle_length_prediction.ipynb` in a Jupyter environment (Jupyter Lab, Jupyter Notebook, or Google Colab) and run the cells sequentially.

    The notebook will automatically download the dataset using `kagglehub`.

## Data Cleaning and EDA Highlights

The notebook performs comprehensive data cleaning and exploratory data analysis (EDA) steps, including:
-   **Initial Data Loading**: Reads the `FedCycleData071012 (2).csv` file into a pandas DataFrame.
-   **Handling Missing Values**:
    -   Identifies whitespace characters (" ") as missing values and replaces them with `np.nan`.
    -   Visualizes the percentage of missing values in columns, categorizing them into columns with more than 50% missing values and less than 50% missing values.
    -   Removes columns that have more than 50% missing values.
-   **Feature Engineering/Removal**:
    -   Removes the "ClientID" column as it's deemed not contributory to cycle length prediction.
-   **Data Type Conversion**:
    -   Identifies columns with `object` (string) data types that should be numerical.
    -   Converts various columns like `EstimatedDayofOvulation`, `LengthofLutealPhase`, `FirstDayofHigh`, `TotalNumberofHighDays`, `TotalHighPostPeak`, `TotalNumberofPeakDays`, `TotalDaysofFertility`, `TotalFertilityFormula`, `LengthofMenses`, `MensesScoreDayOne` to `MensesScoreDayFive`, `TotalMensesScore`, `NumberofDaysofIntercourse`, `IntercourseInFertileWindow`, `UnusualBleeding` from `object` to numeric types, filling `NaN` with 0 where appropriate.
    -   The notebook also includes a comment about converting the 'MeanCycleLength' column to numeric, which would be a critical step for further analysis or prediction of cycle length.
-   **Distribution Analysis**:
    -   Visualizes the distribution of key numerical columns to understand their spread and detect outliers.
    -   The output shows distributions for `CycleNumber`, `Group`, `CycleWithPeakorNot`, `ReproductiveCategory`, and `LengthofCycle`.
-   **Outlier Treatment**:
    -   Identifies and addresses outliers in numerical columns like `LengthofCycle` (e.g., values less than 15 or greater than 45 are likely outliers). Outliers outside a reasonable menstrual cycle range are set to `NaN`.
-   **Imputation**:
    -   Numerical `NaN` values are imputed using the median.
    -   Categorical `NaN` values are imputed using the mode.
-   **Categorical Encoding**:
    -   Applies Label Encoding to all categorical (object) columns remaining in the dataset.
-   **Correlation Analysis**:
    -   Computes and visualizes the correlation matrix of the processed DataFrame using a heatmap to understand feature relationships.
    -   Identifies and removes highly correlated columns (e.g., `ReproductiveCategory` and `Reprocate` are highly correlated; `Spousesame` and `SpousesameM` are identical).
-   **Feature Scaling**:
    -   Applies StandardScaler to scale numerical features, preparing them for machine learning models.
-   **Data Splitting**:
    -   Splits the dataset into training and testing sets (`X_train`, `X_test`, `y_train`, `y_test`) for model development.

## Next Steps (Not Covered in this Notebook)
This notebook provides a cleaned and preprocessed dataset. The next logical steps would involve:
-   **Model Training**: Applying various machine learning models (e.g., regression models like Linear Regression, Random Forest Regressor, Gradient Boosting) to predict `LengthofCycle`.
-   **Model Evaluation**: Assessing model performance using appropriate metrics (e.g., MAE, MSE, R2-score).
-   **Hyperparameter Tuning**: Optimizing model parameters for better performance.
