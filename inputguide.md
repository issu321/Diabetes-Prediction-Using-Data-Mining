# 📋 Input Parameter Guide

**Project:** Diabetes Prediction Using Data Mining  
**Project ID:** EDUFYPML007  
**Developed By:** EduPhonix-Solution  
**GitHub:** [github.com/issu321](https://github.com/issu321)  
**Repository:** [github.com/issu321/Diabetes-Prediction-Using-Data-Mining](https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining)

---

## 🎯 Overview

This guide provides detailed information about each input parameter used in the Diabetes Prediction system. Understanding these parameters will help you enter accurate values and interpret the prediction results correctly.

---

## 📊 Input Parameters

### 1. 🤰 Pregnancies

| Attribute | Details |
|-----------|---------|
| **Description** | Number of times the patient has been pregnant |
| **Data Type** | Integer |
| **Valid Range** | 0 - 20 |
| **Unit** | Count |
| **Risk Indicator** | Higher pregnancy counts may increase diabetes risk, especially with gestational diabetes history |

**Reference Values:**
- 0-2: Low risk
- 3-5: Moderate risk
- 6+: Higher risk (especially if previous gestational diabetes)

---

### 2. 🍬 Glucose

| Attribute | Details |
|-----------|---------|
| **Description** | Plasma glucose concentration after 2 hours in an oral glucose tolerance test (OGTT) |
| **Data Type** | Float |
| **Valid Range** | 0 - 300 mg/dL |
| **Unit** | mg/dL (milligrams per deciliter) |
| **Risk Indicator** | **Primary diabetes indicator** - elevated glucose strongly suggests diabetes |

**Glucose Level Categories:**

| Level | Range (mg/dL) | Interpretation |
|-------|---------------|----------------|
| Normal | < 100 | Healthy fasting glucose |
| Prediabetes | 100 - 125 | Impaired fasting glucose |
| Diabetes | ≥ 126 | Diabetes threshold |
| Severe | > 200 | Requires immediate medical attention |

**Note:** This is a 2-hour post-load glucose test, not fasting glucose. Values above 200 mg/dL after 2 hours indicate diabetes.

---

### 3. 🩸 Blood Pressure

| Attribute | Details |
|-----------|---------|
| **Description** | Diastolic blood pressure (the lower number in BP reading) |
| **Data Type** | Float |
| **Valid Range** | 0 - 200 mm Hg |
| **Unit** | mm Hg (millimeters of mercury) |
| **Risk Indicator** | Hypertension is often associated with diabetes (comorbidity) |

**Blood Pressure Categories:**

| Category | Diastolic (mm Hg) | Status |
|----------|-------------------|--------|
| Normal | < 80 | Healthy |
| Elevated | 80 - 89 | Prehypertension |
| Stage 1 Hypertension | 90 - 99 | High blood pressure |
| Stage 2 Hypertension | ≥ 100 | Very high blood pressure |

---

### 4. 📏 Skin Thickness

| Attribute | Details |
|-----------|---------|
| **Description** | Triceps skin fold thickness (measure of body fat) |
| **Data Type** | Float |
| **Valid Range** | 0 - 100 mm |
| **Unit** | mm (millimeters) |
| **Risk Indicator** | Higher values indicate higher body fat, which correlates with insulin resistance |

**Reference Values:**
- < 15 mm: Very lean
- 15-25 mm: Normal
- 25-35 mm: Above average
- > 35 mm: High body fat (increased diabetes risk)

---

### 5. 💉 Insulin

| Attribute | Details |
|-----------|---------|
| **Description** | 2-Hour serum insulin level |
| **Data Type** | Float |
| **Valid Range** | 0 - 900 μU/mL |
| **Unit** | μU/mL (micro International Units per milliliter) |
| **Risk Indicator** | Abnormal levels indicate insulin resistance or insufficient insulin production |

**Insulin Level Interpretation:**

| Level | Range (μU/mL) | Interpretation |
|-------|---------------|----------------|
| Low | < 16 | Possible insulin deficiency |
| Normal | 16 - 166 | Typical range |
| High | > 166 | Insulin resistance (common in Type 2 diabetes) |

**Note:** Very high insulin with high glucose suggests insulin resistance (Type 2 diabetes). Low insulin with high glucose suggests insulin deficiency (Type 1 diabetes).

---

### 6. ⚖️ BMI (Body Mass Index)

| Attribute | Details |
|-----------|---------|
| **Description** | Body mass index calculated as weight(kg) / height(m)² |
| **Data Type** | Float |
| **Valid Range** | 0.0 - 70.0 kg/m² |
| **Unit** | kg/m² |
| **Risk Indicator** | **Major risk factor** - obesity significantly increases diabetes risk |

**BMI Categories:**

| Category | BMI Range | Diabetes Risk |
|----------|-----------|---------------|
| Underweight | < 18.5 | Low |
| Normal | 18.5 - 24.9 | Low |
| Overweight | 25.0 - 29.9 | Moderate |
| Obese Class I | 30.0 - 34.9 | High |
| Obese Class II | 35.0 - 39.9 | Very High |
| Obese Class III | ≥ 40.0 | Extremely High |

**How to Calculate BMI:**
```
BMI = weight (kg) / [height (m)]²

Example: If weight = 70 kg, height = 1.75 m
BMI = 70 / (1.75 × 1.75) = 70 / 3.0625 = 22.86 (Normal)
```

---

### 7. 🧬 Diabetes Pedigree Function

| Attribute | Details |
|-----------|---------|
| **Description** | A genetic score representing the diabetes influence from family history |
| **Data Type** | Float |
| **Valid Range** | 0.000 - 3.000 |
| **Unit** | Score (dimensionless) |
| **Risk Indicator** | Higher values indicate stronger genetic predisposition to diabetes |

**Interpretation:**

| Score | Risk Level | Family History |
|-------|------------|----------------|
| < 0.5 | Low | No immediate family history |
| 0.5 - 1.0 | Moderate | Some family history |
| 1.0 - 1.5 | High | Strong family history |
| > 1.5 | Very High | Multiple family members with diabetes |

**Note:** This function mathematically models the genetic influence based on:
- Number of relatives with diabetes
- Relationship closeness (parents, siblings, grandparents)
- Age at diagnosis of relatives

---

### 8. 🎂 Age

| Attribute | Details |
|-----------|---------|
| **Description** | Age of the patient in years |
| **Data Type** | Integer |
| **Valid Range** | 1 - 120 years |
| **Unit** | Years |
| **Risk Indicator** | Risk increases significantly after age 45 |

**Age Risk Categories:**

| Age Group | Risk Level | Notes |
|-----------|------------|-------|
| < 35 | Low | Generally low risk unless other factors present |
| 35 - 45 | Moderate | Risk begins to increase |
| 45 - 55 | High | Significant increase in risk |
| 55 - 65 | Very High | Peak risk period |
| > 65 | High | Risk remains high but may plateau |

---

## 🎯 Quick Reference Table

| Parameter | Normal Range | Warning Range | Danger Range |
|-----------|-------------|---------------|--------------|
| Pregnancies | 0-2 | 3-5 | 6+ |
| Glucose | < 100 mg/dL | 100-125 mg/dL | ≥ 126 mg/dL |
| Blood Pressure | < 80 mm Hg | 80-89 mm Hg | ≥ 90 mm Hg |
| Skin Thickness | 15-25 mm | 25-35 mm | > 35 mm |
| Insulin | 16-166 μU/mL | 166-300 μU/mL | > 300 μU/mL |
| BMI | 18.5-24.9 | 25.0-29.9 | ≥ 30.0 |
| Pedigree Function | < 0.5 | 0.5-1.0 | > 1.0 |
| Age | < 35 | 35-45 | > 45 |

---

## ⚡ Quick Profile Examples

### 👤 Healthy Profile (Low Risk)
```
Pregnancies: 1
Glucose: 85
Blood Pressure: 70
Skin Thickness: 20
Insulin: 80
BMI: 22.0
Diabetes Pedigree: 0.2
Age: 25
```

### ⚠️ At-Risk Profile (Moderate Risk)
```
Pregnancies: 3
Glucose: 140
Blood Pressure: 80
Skin Thickness: 30
Insulin: 150
BMI: 32.0
Diabetes Pedigree: 0.8
Age: 45
```

### 🔴 High-Risk Profile (High Risk)
```
Pregnancies: 5
Glucose: 180
Blood Pressure: 90
Skin Thickness: 40
Insulin: 300
BMI: 38.0
Diabetes Pedigree: 1.5
Age: 55
```

---

## 📝 How to Use the Application

1. **Enter Values:** Input the patient's medical data in the form fields
2. **Select Model:** Choose "All Models (Ensemble)" for combined prediction or a specific model
3. **Click Predict:** Press the "PREDICT DIABETES RISK" button
4. **Review Results:** Check the risk level, probability gauge, and individual model predictions
5. **Follow Recommendations:** Read the personalized health recommendations provided

---

## ⚠️ Important Notes

1. **Medical Disclaimer:** This tool is for educational purposes only. Always consult a healthcare professional for medical diagnosis.

2. **Data Accuracy:** Ensure input values are accurate. Small errors can significantly affect predictions.

3. **Glucose Test:** The Glucose value should be from a 2-hour oral glucose tolerance test (OGTT), not a random or fasting test.

4. **Blood Pressure:** Enter the diastolic (lower) value, not the systolic (upper) value.

5. **BMI Calculation:** If you only know weight and height, calculate BMI first using the formula provided above.

6. **Pedigree Function:** If exact value is unknown, estimate based on family history:
   - No family history: 0.1-0.3
   - One parent: 0.5-0.8
   - Both parents or siblings: 1.0-1.5
   - Multiple relatives: > 1.5

---

## 📚 Additional Resources

- [American Diabetes Association](https://www.diabetes.org/)
- [CDC Diabetes Information](https://www.cdc.gov/diabetes/)
- [WHO Diabetes Facts](https://www.who.int/news-room/fact-sheets/detail/diabetes)

---

<div align="center">

**🩺 Diabetes Prediction Using Data Mining | Project ID: EDUFYPML007**

👨‍💻 Developed By **EduPhonix-Solution**

🐙 [GitHub: @issu321](https://github.com/issu321) | 📁 [Repository](https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining)

</div>
