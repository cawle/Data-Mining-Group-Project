Digital Marketing Campaign Optimization

Data Mining & Analytics Project – Group 15

Overview

This project applies a complete data mining framework to optimize digital marketing campaigns using the Knowledge Discovery in Databases (KDD) methodology. A real-world dataset containing 2,205 customer records with 39 attributes was analyzed to uncover behavioral patterns, improve personalization, support strategic decision-making, and detect anomalies in marketing data.

The project integrates four major data mining components:

Market Basket Analysis (Apriori Algorithm)

Customer Segmentation (K-Means Clustering)

Recommender Systems (Hybrid Model)

Anomaly Detection (Isolation Forest)

All techniques were applied after thorough preprocessing, feature engineering, and model evaluation.

Objectives

Collect and prepare the digital marketing dataset, including cleaning, encoding, and normalizing features.

Develop a full analytical framework consisting of Market Basket Analysis, Clustering, Recommender Systems, and Anomaly Detection.

Evaluate the performance of each method using relevant metrics such as support, confidence, lift, inertia, Precision@5, Recall@5, and anomaly scores.

Project Scope
Data Preparation

The dataset was cleaned by handling missing values, removing duplicates, encoding categorical attributes, and normalizing numerical features. Feature engineering was also performed to create meaningful variables such as total purchases, total spending, campaign response count, and family size.

Market Basket Analysis (Apriori)

Apriori was applied to a basket binary matrix to identify frequent itemsets and generate association rules based on support, confidence, and lift. The analysis revealed strong co-purchasing relationships, with products such as meats, wines, and fish acting as central items. These insights support effective product bundling, cross-selling, and store layout planning.

Customer Segmentation (K-Means)

K-Means clustering was performed on normalized behavioral and spending features. The elbow method was used to determine the optimal number of clusters. Four key customer groups were identified:

High-Value Customers

Active Shoppers

At-Risk Customers

Budget Families

Each segment displays unique purchasing characteristics, enabling targeted and strategic marketing interventions.

Recommender System (Hybrid Approach)

A hybrid recommender system combining content-based and item–item collaborative filtering was developed. The hybrid model provided a balanced performance with improved recall and stable precision, outperforming content-based methods and matching collaborative filtering in accuracy.

Anomaly Detection (Isolation Forest)

Isolation Forest was used to identify unusual patterns such as sudden spikes in spending or irregular purchasing behavior. PCA visualization showed clear separation between normal and anomalous data points. Some anomalies represent potential fraudulent behavior, while others indicate rare high-value customers.

Key Findings
Market Basket Analysis

Frequent itemsets showed support values near 0.64 and confidence values between 0.80 and 0.89.

High-lift rules revealed strong associations among meats, wines, and premium products such as gold items.

Fruits and sweets were often found in combinations with higher-value products.

Clustering

Customer distribution across four clusters was nearly even.

High-Value customers showed high spending, high income, and high purchase counts.

At-Risk customers exhibited high recency but low spending and low purchase frequency.

Budget Families had larger household sizes but low spending.

Recommender System

Content-based filtering performed poorly due to limited item attributes.

Collaborative filtering achieved high recall.

The hybrid model successfully balanced both precision and recall, improving recommendation quality.

Anomaly Detection

A small portion of customers exhibited significantly higher income, spending, and purchase levels compared to the general population.

Anomaly detection helped reveal both potential fraudulent interactions and customers who may benefit from premium retention strategies.

Methodology

The entire analysis followed the KDD process:

Data Selection

Data Preprocessing

Data Transformation

Data Mining

Knowledge Presentation

This structured approach ensured consistency, interpretability, and accuracy in all modeling stages.

Technologies Used

Python

Scikit-learn

Pandas and NumPy

MLxtend

Matplotlib and Seaborn

Jupyter Notebook

Conclusion

This project demonstrates how multiple data mining techniques can be integrated to optimize digital marketing strategies. Market Basket Analysis identifies meaningful product associations. Clustering highlights distinct customer groups. A hybrid recommender system enhances personalization, while anomaly detection protects campaign integrity and identifies unique customer behaviors.

By combining traditional algorithms such as Apriori and K-Means with advanced methods like hybrid recommendation and Isolation Forest, this project offers both academic and practical value for improving return on investment (ROI) and supporting data-driven marketing decisions.

Future Work

Implement real-time data processing for live campaign monitoring.

Integrate deep learning models such as Neural Collaborative Filtering, Transformers, or LSTMs.

Improve transparency and fairness in recommendations using explainable AI.

Extend the framework to other industries such as healthcare, finance, or education.

Project Members
Name	ID	Role
Zayar Linn	AIU23102140	Market Basket Analysis
Mohamed Abdullahi Ali	AIU22102342	Anomaly Detection
Abdullahi Mohamed Ali	AIU22102225	Clustering
Abdalle Ahmed Hassan	AIU22102256	Recommender Systems
