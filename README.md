# 🚀 SpaceX First Stage Landing Prediction

### 🎓 Capstone Project | Machine Learning | Data Science  

This repository contains a complete end-to-end Machine Learning workflow designed to predict the successful landing of **SpaceX Falcon 9 first stage boosters**.  
The project demonstrates the complete **data science pipeline**, from data acquisition to model evaluation, focusing on building robust, reproducible, and interpretable predictive models.

Capstone project focused on predicting the successful landing of SpaceX Falcon 9 first stages using Machine Learning. The project covers data collection from APIs, preprocessing, exploratory data analysis, feature engineering, visualization, and model training with Scikit-learn to enhance landing success prediction accuracy.

---

##  Project Overview

The notebook implements a full ML workflow covering all essential stages:

- Data acquisition and integration from APIs and local datasets  
- Cleaning, wrangling, and preprocessing structured SpaceX data  
- Exploratory Data Analysis (EDA) and visualization  
- Feature engineering and model building  
- Hyperparameter tuning and performance evaluation  

The objective is to predict **landing success** while extracting key insights from operational and mission-level features.

---

## Objectives

- Prepare and preprocess structured datasets for modeling  
- Apply multiple machine learning algorithms: **Logistic Regression**, **Decision Trees**, **Random Forests**, and **SVMs**  
- Evaluate models using metrics such as **Accuracy, Precision, Recall, F1, ROC-AUC**, and **Confusion Matrix**  
- Compare model performance and identify the most effective approach  
- Extract insights into which features influence launch outcomes  

---

##  Methodology

### Environment & Libraries
**Core:** `numpy`, `pandas`, `os`, `json`, `re`  
**Visualization:** `matplotlib`, `seaborn`, `plotly`, `folium`  
**Machine Learning:** `scikit-learn` (Logistic Regression, Decision Tree, Random Forest, SVM, GridSearchCV)  
**Evaluation:** `accuracy_score`, `precision_score`, `recall_score`, `f1_score`, `roc_auc_score`, `confusion_matrix`  
**Utilities:** `joblib`, `JupyterDash`

###  Data Collection
- **Local Datasets:** Loaded using `pandas.read_csv()`  
- **External Sources:** Retrieved via REST API calls using `requests`  
- **Visualization:** Launch site data displayed using **Folium** maps and **Plotly** dashboards  

###  Data Wrangling & Preparation
- Missing values handled using **SimpleImputer**  
- Categorical encoding with **One-Hot Encoding**  
- Feature scaling using **StandardScaler**  
- Derived temporal and mission-related features  
- Dataset split with **train_test_split** and stratified sampling  

###  Exploratory Data Analysis (EDA)
- Class distribution visualization (count plots, pie charts)  
- Correlation analysis using heatmaps  
- Geographic visualization of launch sites  
- Interactive dashboards via **Plotly** and **JupyterDash**  

###  Modeling Approach
Tested classifiers include:
- Logistic Regression (baseline, interpretable)  
- Decision Tree Classifier (non-linear relationships)  
- Random Forest Classifier (ensemble accuracy)  
- Support Vector Machine (kernel-based separation)  

Hyperparameter tuning performed via **GridSearchCV**.

###  Evaluation Metrics
- **Accuracy** – Overall model performance  
- **Precision & Recall** – Balance of FP and FN  
- **F1-score** – Combined measure of precision and recall  
- **ROC-AUC** – Model ranking ability  
- **Confusion Matrix** – Prediction vs. actual analysis  
Cross-validation ensures robust and unbiased evaluation.

---

## 💡 Insights

- Launch site characteristics strongly impact landing success  
- Logistic Regression offers interpretability but lower accuracy  
- Random Forest emerged as the most robust and balanced model  
- Visualizations highlight geographic and operational trends  

---

##  Results

- **Accuracy:** ~80–85%  
- **Balanced Precision, Recall, and F1-scores**  
- **Confusion Matrix:** Shows good separability between classes  
- **Model Ranking:** Random Forest > SVM > Logistic Regression > Decision Tree  

---

##  Challenges & Mitigations

| Challenge | Solution |
|------------|-----------|
| Missing Values | Handled via imputation and data cleaning |
| Imbalanced Targets | Managed with stratified sampling and balanced metrics |
| Data Leakage | Prevented using pipelines and transformers |
| High Computation (GridSearchCV) | Mitigated with randomized search |
| Reproducibility | Controlled with random seeds and model persistence |

---

## Conclusion

This project demonstrates a **complete, reproducible machine learning pipeline** for SpaceX launch data.  
Ensemble models such as Random Forests outperform baselines, while Logistic Regression provides interpretability.  
The workflow is designed for **scalability**, **robustness**, and **further extension** to more complex data sources.

---

##  Future Recommendations

- Integrate **SHAP** or **LIME** for model interpretability  
- Deploy pipeline as a **reusable ML module**  
- Explore **deep learning** for unstructured data (images, telemetry)  
- Implement **data drift monitoring** and automated model retraining  

---

##  Author

**👨‍💻 [Muhammad Sikander Bakht]**  
*BS DATA Science, UET Peshawar*  
Capstone Project – SpaceX First Stage Landing Prediction  

---

## 🧰 Tech Stack

`Python` | `Pandas` | `NumPy` | `Scikit-learn` | `Matplotlib` | `Seaborn` | `Plotly` | `Folium` | `JupyterDash`

---

⭐ **If you like this project, please give it a star!**
