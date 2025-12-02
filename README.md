# Digital Marketing Campaign Optimization
### Data Mining & Analytics Project – Group 15

## Overview
This project applies a complete data mining framework to optimize digital marketing campaigns using the **Knowledge Discovery in Databases (KDD)** methodology. A real-world dataset containing **2,205 customer records with 39 attributes** was analyzed to uncover behavioral patterns, improve personalization, support strategic decision-making, and detect anomalies in marketing data.

The project integrates four major data mining components:
- **Market Basket Analysis (Apriori Algorithm)**
- **Customer Segmentation (K-Means Clustering)**
- **Recommender Systems (Hybrid Model)**
- **Anomaly Detection (Isolation Forest)**

All techniques were applied after thorough preprocessing, feature engineering, and model evaluation.

---

## Objectives
- Collect and prepare the digital marketing dataset, including cleaning, encoding, and normalizing features.
- Develop a complete analytical framework consisting of Market Basket Analysis, Clustering, Recommender Systems, and Anomaly Detection.
- Evaluate performance using metrics such as **support, confidence, lift**, **inertia**, **Precision@5**, **Recall@5**, and **anomaly scores**.

---

## Project Scope

### **Data Preparation**
The dataset was cleaned by handling missing values, removing duplicates, encoding categorical attributes, and normalizing numerical features. Feature engineering created meaningful variables such as:
- Total purchases  
- Total spending  
- Campaign response count  
- Family size  

---

### **Market Basket Analysis (Apriori)**
Apriori was applied to a basket binary matrix to identify frequent itemsets and generate association rules based on:
- **Support**
- **Confidence**
- **Lift**

Key insights:
- Strong co-purchasing relationships between **meats**, **wines**, and **fish**.
- Useful for **product bundling**, **cross-selling**, and **store layout** optimization.

---

### **Customer Segmentation (K-Means)**
K-Means clustering was applied to normalized behavioral and spending features. The elbow method determined the optimal number of clusters.

Identified segments:
1. **High-Value Customers**
2. **Active Shoppers**
3. **At-Risk Customers**
4. **Budget Families**

Each group displays unique purchasing traits enabling targeted marketing strategies.

---

### **Recommender System (Hybrid Approach)**
A combination of **content-based filtering** and **item–item collaborative filtering** was used.

Results:
- Hybrid approach improved **recall** while maintaining stable **precision**.
- Outperformed content-based filtering.
- Matched collaborative filtering accuracy with better balance.

---

### **Anomaly Detection (Isolation Forest)**
Isolation Forest was used to detect unusual behavioral patterns such as:
- Sudden spikes in spending  
- Irregular purchasing behavior  

PCA visualization showed clear separation between normal and anomalous customers.

Identified anomalies included:
- Possible fraud  
- Rare high-value customers needing retention strategies  

---

## Key Findings

### **Market Basket Analysis**
- Frequent itemsets had **support ≈ 0.64** and **confidence 0.80–0.89**.
- Strong associations among **meats**, **wines**, and premium items (e.g., *gold products*).
- Fruits and sweets often paired with high-value products.

### **Clustering**
- All clusters had near-even customer distribution.
- **High-Value Customers**: high spending & income.  
- **At-Risk Customers**: high recency, low spending.  
- **Budget Families**: larger households, low total spending.

### **Recommender System**
- Content-based performed poorly due to limited attribute availability.
- Collaborative filtering achieved high recall.
- Hybrid model balanced precision and recall effectively.

### **Anomaly Detection**
- Few customers showed extremely high income/spending levels.
- Helped identify:
  - Potential fraud signals  
  - VIP customers suitable for premium campaigns  

---

## Methodology
This study followed the full **KDD Process**:
1. **Data Selection**  
2. **Data Preprocessing**  
3. **Data Transformation**  
4. **Data Mining**  
5. **Knowledge Presentation**

---

## Technologies Used
- **Python**
- **Scikit-learn**
- **Pandas & NumPy**
- **MLxtend**
- **Matplotlib & Seaborn**
- **Jupyter Notebook**

---

## Conclusion
This project demonstrates how integrating multiple data mining techniques can significantly improve digital marketing strategies:

- **Apriori** reveals actionable product associations.  
- **K-Means** highlights meaningful customer segments.  
- **Hybrid recommender systems** enhance personalization.  
- **Isolation Forest** ensures data integrity and identifies unique customer behaviors.  

By combining classical algorithms with advanced modern techniques, this work contributes both academic and practical value, improving ROI and enabling data-driven marketing decisions.

---

## Future Work
- Add **real-time data processing** for live campaign monitoring.
- Implement deep learning models such as **Neural Collaborative Filtering (NCF)**, **Transformers**, or **LSTMs**.
- Apply **Explainable AI** to improve fairness and interpretability.
- Expand the framework to industries such as **healthcare**, **finance**, and **education**.

---

## Project Members

| Name | ID | Role |
|------|------|------|
| **Zayar Linn** | AIU23102140 | Market Basket Analysis |
| **Mohamed Abdullahi Ali** | AIU22102342 | Anomaly Detection |
| **Abdullahi Mohamed Ali** | AIU22102225 | Clustering |
| **Abdalle Ahmed Hassan** | AIU22102256 | Recommender Systems |

