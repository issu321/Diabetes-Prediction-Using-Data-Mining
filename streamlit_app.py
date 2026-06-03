#!/usr/bin/env python3
"""
Diabetes Prediction Using Data Mining - Streamlit Web Application
Project ID: EDUFYPML007
Developed By: EduPhonix-Solution
GitHub: https://github.com/ussu321
Repository: https://github.com/ussu321/Diabetes-Prediction-Using-Data-Mining
"""

import os
import json
import pickle
import warnings
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Diabetes Prediction | EDUFYPML007",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .github-badge {
        text-align: center;
        padding: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .result-positive {
        background-color: #ffcccc;
        border-left: 6px solid #ff4444;
        padding: 20px;
        border-radius: 5px;
    }
    .result-negative {
        background-color: #ccffcc;
        border-left: 6px solid #44ff44;
        padding: 20px;
        border-radius: 5px;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 12px;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    .footer {
        text-align: center;
        padding: 20px;
        color: #666;
        font-size: 0.9rem;
        margin-top: 3rem;
        border-top: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'diabetes.csv')
MODELS_DIR = os.path.join(BASE_DIR, 'models')


def load_models():
    """Load all trained models and metadata."""
    models = {}
    model_files = {
        'Logistic Regression': 'Logistic_Regression.pkl',
        'Random Forest': 'Random_Forest.pkl',
        'Support Vector Machine': 'Support_Vector_Machine.pkl',
        'K-Nearest Neighbors': 'K_Nearest_Neighbors.pkl',
        'Decision Tree': 'Decision_Tree.pkl',
        'Gradient Boosting': 'Gradient_Boosting.pkl',
        'Naive Bayes': 'Naive_Bayes.pkl'
    }

    for name, filename in model_files.items():
        filepath = os.path.join(MODELS_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                models[name] = pickle.load(f)

    scaler_path = os.path.join(MODELS_DIR, 'scaler.pkl')
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)

    feature_path = os.path.join(MODELS_DIR, 'feature_names.json')
    with open(feature_path, 'r') as f:
        feature_names = json.load(f)

    results_path = os.path.join(MODELS_DIR, 'model_results.json')
    with open(results_path, 'r') as f:
        results = json.load(f)

    best_path = os.path.join(MODELS_DIR, 'best_model.json')
    with open(best_path, 'r') as f:
        best_info = json.load(f)

    return models, scaler, feature_names, results, best_info


def predict_diabetes(input_data, models, scaler, feature_names):
    """Make predictions using all models."""
    df_input = pd.DataFrame([input_data], columns=feature_names)
    scaled_input = scaler.transform(df_input)

    predictions = {}
    probabilities = {}

    for name, model in models.items():
        pred = model.predict(scaled_input)[0]
        prob = model.predict_proba(scaled_input)[0]
        predictions[name] = int(pred)
        probabilities[name] = float(prob[1])

    return predictions, probabilities


def get_risk_level(probability):
    """Determine risk level based on probability."""
    if probability < 0.3:
        return "Low Risk", "🟢", "#28a745"
    elif probability < 0.6:
        return "Moderate Risk", "🟡", "#ffc107"
    elif probability < 0.8:
        return "High Risk", "🟠", "#fd7e14"
    else:
        return "Very High Risk", "🔴", "#dc3545"


def main():
    # Header
    st.markdown('<div class="main-header">🩺 Diabetes Prediction Using Data Mining</div>', 
                unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Project ID: EDUFYPML007 | ML-Based Diabetes Risk Assessment</div>', 
                unsafe_allow_html=True)

    # GitHub Branding
    st.markdown("""
    <div class="github-badge">
        <h4>👨‍💻 Developed By EduPhonix-Solution</h4>
        <p>
            <a href="https://github.com/ussu321" target="_blank" style="color: white; text-decoration: none;">
                🐙 GitHub Profile: @ussu321
            </a> | 
            <a href="https://github.com/ussu321/Diabetes-Prediction-Using-Data-Mining" target="_blank" style="color: white; text-decoration: none;">
                📁 Repository: Diabetes-Prediction-Using-Data-Mining
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Load models
    try:
        models, scaler, feature_names, results, best_info = load_models()
    except Exception as e:
        st.error(f"❌ Error loading models: {e}")
        st.info("Please run `python3 train_model.py` first to train the models.")
        return

    # Sidebar
    st.sidebar.markdown("## 🧭 Navigation")
    page = st.sidebar.radio("", [
        "🏠 Home / Prediction",
        "📊 Model Comparison",
        "📈 Data Analysis",
        "📋 Input Guide",
        "ℹ️ About Project"
    ])

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🏆 Best Model")
    st.sidebar.success(f"**{best_info['best_model']}**")
    st.sidebar.markdown(f"- Accuracy: `{best_info['metrics']['Accuracy']:.4f}`")
    st.sidebar.markdown(f"- F1-Score: `{best_info['metrics']['F1-Score']:.4f}`")
    st.sidebar.markdown(f"- AUC-ROC: `{best_info['metrics']['AUC-ROC']:.4f}`")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔧 Models Loaded")
    for name in models.keys():
        st.sidebar.markdown(f"- ✅ {name}")

    # ==================== HOME / PREDICTION PAGE ====================
    if page == "🏠 Home / Prediction":
        st.markdown("### 🔮 Diabetes Risk Prediction")
        st.info("Enter the patient's medical details below to predict diabetes risk using multiple Data Mining algorithms.")

        # Preset handling - must be before widgets so inputs update on rerun
        preset_values = {
            'healthy': {
                'Pregnancies': 1, 'Glucose': 85, 'BloodPressure': 72,
                'SkinThickness': 18, 'Insulin': 60, 'BMI': 22.0,
                'DiabetesPedigreeFunction': 0.2, 'Age': 28
            },
            'atrisk': {
                'Pregnancies': 3, 'Glucose': 115, 'BloodPressure': 78,
                'SkinThickness': 25, 'Insulin': 110, 'BMI': 28.0,
                'DiabetesPedigreeFunction': 0.6, 'Age': 42
            },
            'highrisk': {
                'Pregnancies': 5, 'Glucose': 155, 'BloodPressure': 88,
                'SkinThickness': 35, 'Insulin': 180, 'BMI': 34.0,
                'DiabetesPedigreeFunction': 1.2, 'Age': 55
            }
        }

        if 'preset' in st.session_state:
            preset_name = st.session_state.pop('preset')
            if preset_name in preset_values:
                for k, v in preset_values[preset_name].items():
                    st.session_state[k] = v

        col1, col2, col3 = st.columns(3)

        with col1:
            pregnancies = st.number_input("🤰 Pregnancies", min_value=0, max_value=20, value=1, 
                                         help="Number of times pregnant", key='Pregnancies')
            glucose = st.number_input("🍬 Glucose (mg/dL)", min_value=0, max_value=300, value=120,
                                     help="Plasma glucose concentration after 2 hours in OGTT", key='Glucose')
            skin_thickness = st.number_input("📏 Skin Thickness (mm)", min_value=0, max_value=100, value=20,
                                            help="Triceps skin fold thickness", key='SkinThickness')

        with col2:
            blood_pressure = st.number_input("🩸 Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70,
                                            help="Diastolic blood pressure", key='BloodPressure')
            insulin = st.number_input("💉 Insulin (μU/mL)", min_value=0, max_value=900, value=80,
                                     help="2-Hour serum insulin", key='Insulin')
            bmi = st.number_input("⚖️ BMI (kg/m²)", min_value=0.0, max_value=70.0, value=25.0, step=0.1,
                                 help="Body mass index", key='BMI')

        with col3:
            diabetes_pedigree = st.number_input("🧬 Diabetes Pedigree Function", min_value=0.0, max_value=3.0, 
                                               value=0.5, step=0.001, format="%.3f",
                                               help="Genetic influence score", key='DiabetesPedigreeFunction')
            age = st.number_input("🎂 Age (years)", min_value=1, max_value=120, value=30,
                                 help="Age in years", key='Age')

            selected_model = st.selectbox("🤖 Select Model", 
                                         ["All Models (Ensemble)"] + list(models.keys()),
                                         help="Choose a specific model or use all models")

        # Quick presets
        st.markdown("#### ⚡ Quick Presets")
        preset_col1, preset_col2, preset_col3 = st.columns(3)

        with preset_col1:
            if st.button("👤 Healthy Profile"):
                st.session_state['preset'] = 'healthy'
                st.rerun()

        with preset_col2:
            if st.button("⚠️ At-Risk Profile"):
                st.session_state['preset'] = 'atrisk'
                st.rerun()

        with preset_col3:
            if st.button("🔴 High-Risk Profile"):
                st.session_state['preset'] = 'highrisk'
                st.rerun()

        # Predict button
        st.markdown("---")
        if st.button("🔍 PREDICT DIABETES RISK", type="primary"):
            input_data = {
                'Pregnancies': pregnancies,
                'Glucose': glucose,
                'BloodPressure': blood_pressure,
                'SkinThickness': skin_thickness,
                'Insulin': insulin,
                'BMI': bmi,
                'DiabetesPedigreeFunction': diabetes_pedigree,
                'Age': age
            }

            predictions, probabilities = predict_diabetes(input_data, models, scaler, feature_names)

            st.markdown("### 📋 Prediction Results")

            if selected_model == "All Models (Ensemble)":
                avg_prob = np.mean(list(probabilities.values()))
                ensemble_pred = 1 if avg_prob > 0.5 else 0
                risk_level, emoji, color = get_risk_level(avg_prob)

                result_col1, result_col2 = st.columns([1, 2])

                with result_col1:
                    if ensemble_pred == 1:
                        st.markdown(f'<div class="result-positive"><h2>{emoji} {risk_level}</h2><h3>Diabetes Detected</h3><p>Confidence: <b>{avg_prob*100:.2f}%</b></p></div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="result-negative"><h2>{emoji} {risk_level}</h2><h3>No Diabetes Detected</h3><p>Confidence: <b>{(1-avg_prob)*100:.2f}%</b></p></div>', unsafe_allow_html=True)

                with result_col2:
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number+delta",
                        value=avg_prob * 100,
                        domain={'x': [0, 1], 'y': [0, 1]},
                        title={'text': "Diabetes Risk Probability (%)", 'font': {'size': 24}},
                        gauge={
                            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                            'bar': {'color': color},
                            'bgcolor': "white",
                            'borderwidth': 2,
                            'bordercolor': "gray",
                            'steps': [
                                {'range': [0, 30], 'color': '#d4edda'},
                                {'range': [30, 60], 'color': '#fff3cd'},
                                {'range': [60, 80], 'color': '#ffe5b4'},
                                {'range': [80, 100], 'color': '#f8d7da'}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': 50
                            }
                        }
                    ))
                    fig.update_layout(height=300)
                    st.plotly_chart(fig, use_container_width=True)

                # Individual model results
                st.markdown("#### 🤖 Individual Model Predictions")
                model_cols = st.columns(len(models))
                for idx, (name, prob) in enumerate(probabilities.items()):
                    with model_cols[idx]:
                        pred_text = "🔴 Positive" if predictions[name] == 1 else "🟢 Negative"
                        st.metric(label=name, value=f"{prob*100:.1f}%", delta=pred_text)

                # Model agreement chart
                st.markdown("#### 📊 Model Agreement Analysis")
                fig_agree = go.Figure()
                model_names = list(probabilities.keys())
                model_probs = [probabilities[m] * 100 for m in model_names]
                model_colors = ['#ff4444' if p > 50 else '#44ff44' for p in model_probs]

                fig_agree.add_trace(go.Bar(
                    x=model_names, y=model_probs, marker_color=model_colors,
                    text=[f"{p:.1f}%" for p in model_probs], textposition='auto',
                ))
                fig_agree.add_hline(y=50, line_dash="dash", line_color="red", 
                                   annotation_text="Threshold (50%)")
                fig_agree.update_layout(title="Prediction Probability by Model", 
                                       yaxis_title="Probability (%)", xaxis_title="Model", height=400)
                st.plotly_chart(fig_agree, use_container_width=True)

            else:
                prob = probabilities[selected_model]
                pred = predictions[selected_model]
                risk_level, emoji, color = get_risk_level(prob)

                if pred == 1:
                    st.markdown(f'<div class="result-positive"><h2>{emoji} {risk_level}</h2><h3>Model: {selected_model}</h3><p>Diabetes Probability: <b>{prob*100:.2f}%</b></p></div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="result-negative"><h2>{emoji} {risk_level}</h2><h3>Model: {selected_model}</h3><p>Diabetes Probability: <b>{prob*100:.2f}%</b></p></div>', unsafe_allow_html=True)

                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=prob * 100,
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': f"{selected_model} - Risk Probability", 'font': {'size': 20}},
                    gauge={
                        'axis': {'range': [None, 100]},
                        'bar': {'color': color},
                        'steps': [
                            {'range': [0, 30], 'color': '#d4edda'},
                            {'range': [30, 60], 'color': '#fff3cd'},
                            {'range': [60, 80], 'color': '#ffe5b4'},
                            {'range': [80, 100], 'color': '#f8d7da'}
                        ],
                        'threshold': {'line': {'color': "red", 'width': 4}, 'value': 50}
                    }
                ))
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True)

            # Recommendations
            st.markdown("---")
            st.markdown("### 💡 Health Recommendations")

            check_prob = avg_prob if selected_model == "All Models (Ensemble)" else prob
            if check_prob > 0.5:
                st.warning("""
                **Based on the prediction results, the following actions are recommended:**

                1. 🏥 **Consult a Doctor**: Schedule an appointment with an endocrinologist for proper diagnosis.
                2. 🩸 **HbA1c Test**: Get a glycated hemoglobin test for accurate diabetes assessment.
                3. 🥗 **Dietary Changes**: Reduce sugar and carbohydrate intake; follow a diabetic-friendly diet.
                4. 🏃 **Exercise**: Aim for at least 150 minutes of moderate physical activity per week.
                5. ⚖️ **Weight Management**: Maintain a healthy BMI through diet and exercise.
                6. 💊 **Medication**: Follow doctor's advice regarding any prescribed medications.
                7. 📅 **Regular Monitoring**: Check blood glucose levels regularly.
                """)
            else:
                st.success("""
                **Great! Your risk appears low. Keep up the healthy lifestyle:**

                1. 🥗 **Balanced Diet**: Continue eating a balanced diet rich in vegetables and whole grains.
                2. 🏃 **Stay Active**: Maintain regular physical activity.
                3. ⚖️ **Healthy Weight**: Keep your BMI in the healthy range (18.5-24.9).
                4. 🩺 **Annual Checkups**: Continue regular health screenings.
                5. 🚭 **Avoid Smoking**: Smoking increases diabetes risk significantly.
                6. 😴 **Sleep Well**: Aim for 7-9 hours of quality sleep per night.
                """)

    # ==================== MODEL COMPARISON PAGE ====================
    elif page == "📊 Model Comparison":
        st.markdown("### 📊 Model Performance Comparison")
        st.info("Comparison of all Data Mining algorithms used in this project.")

        results_df = pd.DataFrame(results).T
        results_df = results_df.sort_values('F1-Score', ascending=False)
        st.dataframe(results_df.style.highlight_max(axis=0, color='lightgreen')
                     .highlight_min(axis=0, color='lightcoral'), use_container_width=True)

        st.markdown("#### 📈 Performance Metrics Visualization")
        metrics_to_plot = st.multiselect("Select Metrics to Compare", 
                                         ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'AUC-ROC'],
                                         default=['Accuracy', 'F1-Score', 'AUC-ROC'])

        fig = go.Figure()
        for metric in metrics_to_plot:
            fig.add_trace(go.Bar(
                name=metric, x=results_df.index, y=results_df[metric],
                text=[f"{v:.3f}" for v in results_df[metric]], textposition='auto'
            ))

        fig.update_layout(barmode='group', title="Model Performance Comparison",
                         xaxis_title="Model", yaxis_title="Score", height=500, yaxis=dict(range=[0, 1]))
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("#### 🕸️ Radar Chart - Multi-Metric View")
        selected_models_radar = st.multiselect("Select Models for Radar Chart", 
                                               list(results.keys()),
                                               default=[best_info['best_model']])

        if selected_models_radar:
            categories = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'AUC-ROC']
            fig_radar = go.Figure()

            for model_name in selected_models_radar:
                values = [results[model_name][cat] for cat in categories]
                values += values[:1]

                fig_radar.add_trace(go.Scatterpolar(
                    r=values, theta=categories + [categories[0]],
                    fill='toself', name=model_name
                ))

            fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                                   showlegend=True, height=500)
            st.plotly_chart(fig_radar, use_container_width=True)

    # ==================== DATA ANALYSIS PAGE ====================
    elif page == "📈 Data Analysis":
        st.markdown("### 📈 Dataset Analysis & Visualization")

        df = pd.read_csv(DATA_PATH)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Samples", len(df))
        with col2:
            st.metric("Features", len(df.columns) - 1)
        with col3:
            st.metric("Diabetic Cases", df['Outcome'].sum())
        with col4:
            st.metric("Non-Diabetic Cases", len(df) - df['Outcome'].sum())

        st.markdown("#### 📊 Feature Distributions")
        feature_to_plot = st.selectbox("Select Feature", df.columns[:-1])

        fig_dist = make_subplots(rows=1, cols=2, 
                                 subplot_titles=(f'{feature_to_plot} Distribution', 
                                                f'{feature_to_plot} by Outcome'))

        fig_dist.add_trace(
            go.Histogram(x=df[feature_to_plot], nbinsx=30, name="All Data", marker_color='#1f77b4'),
            row=1, col=1
        )

        fig_dist.add_trace(
            go.Box(x=df['Outcome'].astype(str), y=df[feature_to_plot], 
                  name="By Outcome", marker_color='#ff7f0e'),
            row=1, col=2
        )

        fig_dist.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_dist, use_container_width=True)

        st.markdown("#### 🔥 Correlation Heatmap")
        corr = df.corr()
        fig_corr = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r')
        fig_corr.update_layout(height=600)
        st.plotly_chart(fig_corr, use_container_width=True)

        st.markdown("#### 🔍 Pair Plot (Sample)")
        selected_features = st.multiselect("Select 3-4 features for pair plot", 
                                          df.columns[:-1].tolist(),
                                          default=['Glucose', 'BMI', 'Age', 'Insulin'])

        if len(selected_features) >= 2:
            fig_pair = px.scatter_matrix(df, dimensions=selected_features, color='Outcome',
                                        color_discrete_map={0: '#1f77b4', 1: '#ff4444'}, opacity=0.7)
            fig_pair.update_layout(height=700)
            st.plotly_chart(fig_pair, use_container_width=True)

    # ==================== INPUT GUIDE PAGE ====================
    elif page == "📋 Input Guide":
        st.markdown("### 📋 Input Parameter Guide")
        st.info("Understanding each input parameter for accurate predictions.")

        guide_data = {
            'Parameter': [
                'Pregnancies', 'Glucose', 'Blood Pressure', 'Skin Thickness',
                'Insulin', 'BMI', 'Diabetes Pedigree Function', 'Age'
            ],
            'Description': [
                'Number of times the patient has been pregnant',
                'Plasma glucose concentration after 2 hours in OGTT (mg/dL)',
                'Diastolic blood pressure (mm Hg)',
                'Triceps skin fold thickness (mm)',
                '2-Hour serum insulin (μU/mL)',
                'Body mass index (weight in kg / (height in m)²)',
                'Diabetes pedigree function - genetic score of diabetes influence',
                'Age in years'
            ],
            'Normal Range': [
                '0-10 (varies)',
                '70-100 mg/dL (fasting)',
                '60-80 mm Hg',
                '10-50 mm',
                '16-166 μU/mL',
                '18.5-24.9 kg/m²',
                '0.0-2.5',
                'Any age'
            ],
            'Risk Indicator': [
                'Higher counts may increase risk',
                '>126 mg/dL indicates diabetes',
                '>90 mm Hg indicates hypertension',
                'Higher values may indicate obesity',
                'Abnormal levels indicate insulin resistance',
                '>30 indicates obesity (high risk)',
                '>1.0 indicates strong genetic predisposition',
                'Risk increases after age 45'
            ]
        }

        guide_df = pd.DataFrame(guide_data)
        st.table(guide_df)

        st.markdown("---")
        st.markdown("#### 🎯 Reference Values")

        ref_col1, ref_col2 = st.columns(2)

        with ref_col1:
            st.markdown("""
            **Glucose Levels:**
            - Normal: < 100 mg/dL
            - Prediabetes: 100-125 mg/dL
            - Diabetes: ≥ 126 mg/dL

            **Blood Pressure:**
            - Normal: < 120/80 mm Hg
            - Elevated: 120-129/80 mm Hg
            - High: ≥ 130/80 mm Hg
            """)

        with ref_col2:
            st.markdown("""
            **BMI Categories:**
            - Underweight: < 18.5
            - Normal: 18.5 - 24.9
            - Overweight: 25.0 - 29.9
            - Obese: ≥ 30.0

            **Age Risk Factors:**
            - Low: < 35 years
            - Moderate: 35-50 years
            - High: > 50 years
            """)

    # ==================== ABOUT PAGE ====================
    elif page == "ℹ️ About Project":
        st.markdown("### ℹ️ About This Project")

        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            <h4>🎓 Project Details</h4>
            <ul>
                <li><b>Project Title:</b> Diabetes Prediction Using Data Mining</li>
                <li><b>Project ID:</b> EDUFYPML007</li>
                <li><b>Technology:</b> Python, Scikit-Learn, Streamlit</li>
                <li><b>Algorithms:</b> Logistic Regression, Random Forest, SVM, KNN, Decision Tree, Gradient Boosting, Naive Bayes</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        ### 🧠 Methodology

        This project implements a comprehensive **Data Mining** approach to predict diabetes risk:

        1. **Data Collection**: Medical dataset with 8 features and 1 target variable
        2. **Data Preprocessing**: Standardization using StandardScaler
        3. **Feature Engineering**: All 8 medical parameters used as features
        4. **Model Training**: 7 different machine learning algorithms trained and evaluated
        5. **Model Selection**: Best model selected based on F1-Score
        6. **Deployment**: Interactive Streamlit web application

        ### 🛠️ Technologies Used

        - **Python 3.8+**
        - **Scikit-Learn** - Machine Learning algorithms
        - **Pandas & NumPy** - Data manipulation
        - **Streamlit** - Web application framework
        - **Plotly** - Interactive visualizations
        - **Matplotlib & Seaborn** - Statistical plots

        ### 📁 Project Structure
        ```
        Diabetes-Prediction-Using-Data-Mining/
        ├── app.py                 # Main Streamlit application
        ├── train_model.py         # Model training script
        ├── requirements.txt       # Python dependencies
        ├── install.sh            # Linux/Mac installer
        ├── start.sh              # Launch script
        ├── README.md             # Project documentation
        ├── data/
        │   └── diabetes.csv      # Dataset
        └── models/
            ├── *.pkl             # Trained models
            ├── scaler.pkl        # Feature scaler
            ├── feature_names.json
            ├── model_results.json
            └── best_model.json
        ```
        """)

        st.markdown("---")
        st.markdown("### 👨‍💻 Developer Information")

        dev_col1, dev_col2 = st.columns(2)

        with dev_col1:
            st.markdown("""
            **Developed By:** EduPhonix-Solution

            **GitHub Profile:**
            - Username: @ussu321
            - URL: https://github.com/ussu321
            """)

        with dev_col2:
            st.markdown("""
            **Repository:**
            - Name: Diabetes-Prediction-Using-Data-Mining
            - URL: https://github.com/ussu321/Diabetes-Prediction-Using-Data-Mining

            **Project ID:** EDUFYPML007
            """)

        st.markdown("---")
        st.markdown("""
        ### ⚠️ Disclaimer

        **This application is for educational and research purposes only.** 

        The predictions made by this system should **NOT** be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
        """)

    # Footer
    st.markdown("""
    <div class="footer">
        <p>🩺 <b>Diabetes Prediction Using Data Mining</b> | Project ID: EDUFYPML007</p>
        <p>👨‍💻 Developed By <b>EduPhonix-Solution</b> | 
        <a href="https://github.com/ussu321" target="_blank">GitHub: @ussu321</a> | 
        <a href="https://github.com/ussu321/Diabetes-Prediction-Using-Data-Mining" target="_blank">Repository</a></p>
        <p style="font-size: 0.8rem; color: #999;">© 2024 All Rights Reserved. For educational purposes only.</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
