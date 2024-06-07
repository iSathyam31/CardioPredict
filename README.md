# Heart Disease Prediction

This project aims to predict the presence of heart disease in a patient using various machine learning models. The best model, logistic regression without hyperparameter tuning, has been deployed using a Streamlit web app.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Modeling](#modeling)
  - [Logistic Regression](#logistic-regression)
  - [Support Vector Machine (SVM)](#support-vector-machine-svm)
  - [Decision Trees](#decision-trees)
  - [Random Forest](#random-forest)
- [Hyperparameter Tuning](#hyperparameter-tuning)
- [Best Model](#best-model)
- [Streamlit Web App](#streamlit-web-app)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
Heart disease is one of the leading causes of death worldwide. Early detection can save lives, and this project leverages machine learning techniques to predict the presence of heart disease based on various medical parameters.

## Dataset
The dataset used for this project includes several medical attributes and a target variable indicating the presence of heart disease. The dataset is sourced from the UCI Machine Learning Repository.

## Exploratory Data Analysis (EDA)
EDA was performed to understand the distribution and relationships of the features in the dataset. Key insights include:
- Distribution of numerical features
- Correlation between features
- Identification of missing values and outliers

## Modeling
Various machine learning models were trained and evaluated, including:

### Logistic Regression
- Implemented a logistic regression model which provided the best performance among all models.

### Support Vector Machine (SVM)
- Evaluated with different kernels (linear, polynomial, RBF).

### Decision Trees
- Implemented and evaluated using different depths and criteria.

### Random Forest
- Evaluated with different numbers of trees and depths.


## Hyperparameter Tuning
Hyperparameter tuning was performed using GridSearchCV and RandomizedSearchCV. Despite this, the logistic regression model without hyperparameter tuning yielded the best performance.

## Best Model
The logistic regression model without hyperparameter tuning was selected as the best model for this project. It provided the highest accuracy and generalization to the test data.

## Streamlit Web App
A Streamlit web app was developed to deploy the logistic regression model. This app allows users to input medical parameters and get a prediction on the likelihood of having heart disease.

## Installation

Follow these steps:
1. Clone the repository
```
git clone https://github.com/iSathyam31/CardioPredict.git
cd heart-disease-prediction
```   

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Run the Streamlit app:
```
streamlit run app.py

## Usage
Open your browser and go to http://localhost:8501.
Input the required medical parameters.
Click on the 'Predict' button to get the prediction result
```

## Results
The logistic regression model achieved the highest accuracy among all models. The results from the web app can provide a quick assessment of heart disease risk based on user inputs.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any features, bug fixes, or enhancements.

## License
This project is licensed under the MIT License.