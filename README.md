# 🩺 Diabetes Prediction Using Data Mining

**Project ID:** `EDUFYPML007`

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-orange)
![License](https://img.shields.io/badge/License-Educational-green)

---

## 👨‍💻 Developer Information

- **Developed By:** EduPhonix-Solution
- **GitHub Profile:** [@issu321](https://github.com/issu321)
- **Repository:** [Diabetes-Prediction-Using-Data-Mining](https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining)

---

## 📋 Project Overview

This project implements a **comprehensive Data Mining approach** to predict diabetes risk using multiple machine learning algorithms. The system analyzes 8 key medical parameters and provides predictions using 7 different classification models, with an ensemble option for combined predictions.

### 🎯 Features

- ✅ **7 Machine Learning Algorithms** - Logistic Regression, Random Forest, SVM, KNN, Decision Tree, Gradient Boosting, Naive Bayes
- ✅ **Interactive Streamlit Web Interface** - Beautiful, responsive UI
- ✅ **Ensemble Prediction** - Combine all models for robust results
- ✅ **Real-time Risk Assessment** - Gauge charts and probability visualization
- ✅ **Model Comparison Dashboard** - Side-by-side performance metrics
- ✅ **Data Analysis Tools** - Correlation heatmaps, distributions, pair plots
- ✅ **Input Parameter Guide** - Detailed reference values and risk indicators
- ✅ **Health Recommendations** - Personalized advice based on prediction results
- ✅ **Quick Presets** - Healthy, At-Risk, and High-Risk profile templates

---

## 🛠️ Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python 3.8+ |
| ML Framework | Scikit-Learn |
| Web Framework | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly, Matplotlib, Seaborn |

---

## 📁 Project Structure

```
Diabetes-Prediction-Using-Data-Mining/
├── 📄 app.py                    # Main Streamlit application
├── 📄 train_model.py            # Model training script
├── 📄 requirements.txt          # Python dependencies
├── 📄 install.sh               # Linux/Mac installer
├── 📄 install.bat              # Windows installer
├── 📄 start.sh                 # Linux/Mac launcher
├── 📄 start.bat                # Windows launcher
├── 📄 README.md                # Project documentation (this file)
├── 📄 inputguide.md            # Input parameter guide
├── 📁 data/
│   └── diabetes.csv            # Dataset (768 samples, 8 features)
└── 📁 models/
    ├── Logistic_Regression.pkl
    ├── Random_Forest.pkl
    ├── Support_Vector_Machine.pkl
    ├── K_Nearest_Neighbors.pkl
    ├── Decision_Tree.pkl
    ├── Gradient_Boosting.pkl
    ├── Naive_Bayes.pkl
    ├── scaler.pkl                # Feature scaler
    ├── feature_names.json
    ├── model_results.json        # Performance metrics
    └── best_model.json          # Best model info
```

---

## 🚀 Quick Start

### Option 1: Automated Installation (Recommended)

#### Linux / macOS
```bash
./install.sh
```

#### Windows
```cmd
install.bat
```

### Option 2: Manual Installation

1. **Clone the repository**
```bash
git clone https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining.git
cd Diabetes-Prediction-Using-Data-Mining
```

2. **Create virtual environment**
```bash
python -m venv venv
```

3. **Activate virtual environment**

Linux/macOS:
```bash
source venv/bin/activate
```

Windows:
```cmd
venv\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Train models**
```bash
python train_model.py
```

6. **Run the application**
```bash
streamlit run app.py
```

---

## 🖥️ Running the Application

After installation, start the app with:

#### Linux / macOS
```bash
./start.sh
```

#### Windows
```cmd
start.bat
```

Or manually:
```bash
streamlit run app.py
```

The application will be available at: **http://localhost:8501**

---

## 📊 Dataset Information

The dataset contains **768 samples** with **8 medical features**:

| Feature | Description | Range |
|---------|-------------|-------|
| Pregnancies | Number of times pregnant | 0-17 |
| Glucose | Plasma glucose concentration (mg/dL) | 0-199 |
| Blood Pressure | Diastolic blood pressure (mm Hg) | 0-122 |
| Skin Thickness | Triceps skin fold thickness (mm) | 0-99 |
| Insulin | 2-Hour serum insulin (μU/mL) | 0-846 |
| BMI | Body mass index (kg/m²) | 0-67.1 |
| Diabetes Pedigree Function | Genetic influence score | 0.078-2.42 |
| Age | Age in years | 21-81 |
| **Outcome** | **Diabetes test result (0 or 1)** | **0=No, 1=Yes** |

---

## 🤖 Machine Learning Models

| Model | Type | Description |
|-------|------|-------------|
| Logistic Regression | Linear | Baseline classifier with probability outputs |
| Random Forest | Ensemble | Bagging ensemble of decision trees |
| Support Vector Machine | Kernel-based | Optimal hyperplane classification |
| K-Nearest Neighbors | Instance-based | Distance-based classification |
| Decision Tree | Tree-based | Hierarchical rule-based classifier |
| Gradient Boosting | Ensemble | Sequential boosting of weak learners |
| Naive Bayes | Probabilistic | Bayesian inference with independence assumption |

---

## 📈 Performance Metrics

Models are evaluated using:
- **Accuracy** - Overall correct predictions
- **Precision** - True positives / Predicted positives
- **Recall** - True positives / Actual positives
- **F1-Score** - Harmonic mean of precision and recall
- **AUC-ROC** - Area under the ROC curve
- **Cross-Validation** - 5-fold CV for robust evaluation

---

## 📝 Input Guide

For detailed information about each input parameter, normal ranges, and risk indicators, see **[inputguide.md](inputguide.md)**.

---

## ⚠️ Disclaimer

**This application is for educational and research purposes only.**

The predictions made by this system should **NOT** be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to the repository.

---

## 📧 Contact

- **Developer:** EduPhonix-Solution
- **GitHub:** [@issu321](https://github.com/issu321)
- **Repository:** [Diabetes-Prediction-Using-Data-Mining](https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining)

---

## 📄 License

This project is created for educational purposes as part of a Final Year Project (FYP).

**© 2024 EduPhonix-Solution. All Rights Reserved.**

---

<div align="center">

**🩺 Diabetes Prediction Using Data Mining | Project ID: EDUFYPML007**

👨‍💻 Developed By **EduPhonix-Solution**

🐙 [GitHub: @issu321](https://github.com/issu321) | 📁 [Repository](https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining)

</div>
