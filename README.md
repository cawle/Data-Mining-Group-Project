# 📊 iFood Marketing Intelligence Dashboard

A comprehensive Streamlit web application for data-driven marketing analytics, customer segmentation, and personalized product recommendations.

## 🎯 Overview

This dashboard transforms the iFood customer dataset into actionable marketing insights through:

- **📊 Customer Analytics** - Spending patterns by product category and customer demographics
- **🎯 Customer Segmentation** - K-Means clustering with PCA visualization
- **🛍️ Market Basket Analysis** - Association rules discovery using Apriori algorithm
- **🎁 Intelligent Recommendations** - Content-based, Collaborative, and Hybrid recommendation systems
- **📢 Campaign Analytics** - Campaign performance, channel analysis, and customer engagement metrics

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or conda package manager

### Installation

1. **Clone/Navigate to the project directory:**
```bash
cd "21. Digital Marketing Campaign Optimization"
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app:**
```bash
streamlit run app.py
```

4. **Access the app:**
   - Open your browser and navigate to `http://localhost:8501`

## 📁 Project Structure

```
21. Digital Marketing Campaign Optimization/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── ifood_df.csv                   # Customer dataset (~2000 records)
└── mba_rules.csv                  # Pre-computed market basket rules
```

## 🎨 Features & Sections

### 📊 Overview Page
- **Key Metrics Dashboard**: Total customers, average income, spending, campaign acceptance
- **Product Category Analysis**: Spending distribution by product type with visualizations
- **Customer Demographics**: Income, recency, and children distribution charts

### 🎯 Segmentation Page
- **Customer Clustering**: K-Means segmentation with adjustable cluster count (2-8)
- **PCA Visualization**: 2D scatter plot showing customer segments with cluster centers
- **Segment Characteristics**: Detailed metrics for each segment (Income, Spending, Purchase behavior)
- **Interactive Exploration**: Select and analyze individual segments with sample customers

### 🛍️ Market Basket Page
- **Association Rules**: Browse discovered rules with Support, Confidence, and Lift metrics
- **Filter by Metrics**: Dynamic filtering based on lift, confidence, or support thresholds
- **Visualizations**: 
  - Support vs Confidence scatter plot (colored by lift)
  - Top 10 association rules bar chart
- **Key Insights**: Strongest association patterns and average lift statistics

### 🎁 Recommendations Page
- **Three Recommendation Methods**:
  - 📖 **Content-Based**: Similar to customer's purchase history
  - 👥 **Collaborative Filtering**: Based on similar customers
  - 🔀 **Hybrid** (Recommended): 50/50 combination of both methods
- **Customer Selection**: Browse any customer by ID (0 to n-1)
- **Personalized Recommendations**: Top N product suggestions (3, 5, 7, or 10)
- **Confidence Scores**: Visualization of recommendation scores
- **Method Explanations**: Detailed breakdowns of each approach

### 📢 Campaign Insights Page
- **Campaign Performance Metrics**:
  - Total acceptance counts
  - Acceptance rates over time
  - Last campaign response rates
- **Channel Analysis**:
  - Pie chart: Purchase distribution across Web, Catalog, Store
  - Bar chart: Average purchases by channel
- **Segment Performance**: Campaign effectiveness by customer segment
- **Strategic Recommendations**: Best-performing channels and campaigns

## 🔧 Technical Stack

| Component | Purpose |
|-----------|---------|
| **Streamlit** | Web application framework |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computing |
| **Scikit-learn** | Machine learning (K-Means, PCA, similarity metrics) |
| **MLxtend** | Apriori algorithm for market basket analysis |
| **Matplotlib/Seaborn** | Data visualization |

## 📊 Recommendation System Details

### Content-Based Filtering
- Analyzes customer's existing purchase patterns
- Recommends products similar to what they've bought
- Score based on item-to-item similarity matrix
- Best for: Consistent customers with clear preferences

### Collaborative Filtering  
- Finds customers with similar purchase histories
- Recommends products those similar customers bought
- Score based on user-to-user similarity matrix
- Best for: Discovering new products across categories

### Hybrid Approach (Recommended)
- Combines both methods with equal weight (50/50)
- Balances familiar recommendations with discovery
- Masks already-purchased items to avoid redundancy
- Best for: Balanced, diverse recommendations

## 🎯 Market Basket Analysis

The Apriori algorithm discovers patterns like:
- **Association**: If customers buy Product A, they often buy Product B
- **Support**: Percentage of transactions containing the itemset
- **Confidence**: Probability of buying B given they bought A
- **Lift**: How much more likely B is bought with A vs. without

Example Association:
```
Antecedent: Wine → Consequent: Meat
Confidence: 65% | Lift: 1.42x | Support: 8%
```

## 🌐 Deployment Options

### **Option 1: Streamlit Cloud** (Recommended)
1. Push your code to GitHub
2. Go to https://streamlit.io/cloud
3. Create new app → Select your GitHub repo
4. Streamlit handles hosting automatically

### **Option 2: Hugging Face Spaces**
1. Create a Space on https://huggingface.co/spaces
2. Upload files and requirements.txt
3. Select "Streamlit" as the SDK
4. Automatic deployment and public sharing

### **Option 3: Self-Hosted (Local/Server)**
```bash
# Install Streamlit
pip install streamlit

# Run app
streamlit run app.py

# For production, use gunicorn or Docker
```

### **Option 4: Docker**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 📈 Performance Considerations

- **Caching**: All expensive computations use `@st.cache_data` for instant page load
- **Lazy Loading**: Complex analyses only compute when sections are viewed
- **Data Preprocessing**: Done once at load time, results cached
- **Memory Efficient**: Supports datasets up to several MB

## 🔍 Customization

### Change Number of Clusters
Edit the default value in the Segmentation page:
```python
n_clusters = st.sidebar.slider('Number of Segments', 2, 8, 4)  # Change 4 to your default
```

### Adjust Market Basket Thresholds
Modify Apriori parameters in `page_market_basket()`:
```python
frequent_itemsets = apriori(basket_bool, min_support=0.05, use_colnames=True)  # Adjust 0.05
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)  # Adjust 0.3
```

### Modify Recommendation Weights
In `build_recommendation_system()`, change hybrid formula:
```python
hyb_scores = 0.5 * cb_n + 0.5 * cf_n  # Change weights here
```

## 🐛 Troubleshooting

### "Data files not found"
- Ensure `ifood_df.csv` and `mba_rules.csv` are in the same directory as `app.py`

### "Module not found" errors
```bash
pip install -r requirements.txt --upgrade
```

### Slow performance
- Check available RAM (app requires ~500MB for full dataset)
- Reduce data size by filtering to specific time periods
- Use cloud deployment for better resources

### Recommendation scores are all zeros
- This is normal if a customer has no purchase history
- The system masks known purchases to avoid redundancy

## 📚 API Reference

### Key Functions

#### `load_data()`
Loads and preprocesses the iFood CSV file
- Returns: DataFrame, spending_cols, campaign_cols, purchase_cols

#### `perform_clustering(df, n_clusters=4)`
Performs K-Means clustering with PCA projection
- Returns: clusters, X_pca, scaler, kmeans, pca

#### `build_recommendation_system(df, spend_cols)`
Builds three recommendation engines
- Returns: Dictionary with 'content', 'collaborative', 'hybrid' matrices

#### `get_recommendations(user_id, rec_system, method='hybrid', top_n=5)`
Gets top-N product recommendations for a user
- Returns: List of recommendation dictionaries with product names and scores

## 📊 Sample Data Statistics

| Metric | Value |
|--------|-------|
| Total Customers | ~2,000 |
| Products | 6 categories |
| Avg Annual Income | $52,000 |
| Avg Total Spending | $603 |
| Campaign Acceptance Rate | ~7% |
| Purchase Channels | 3 (Web, Catalog, Store) |

## 👥 Author Notes

This dashboard was created as part of a data science group project on digital marketing campaign optimization. The system uses unsupervised learning (clustering, association rules) and collaborative filtering to provide actionable insights for marketing teams.

**Key Insights Generated:**
- Customer lifetime value segmentation
- Product affinity patterns
- High-value customer identification
- Channel preference analysis
- Personalized product recommendations

## 📄 License

This project is provided as-is for educational and business intelligence purposes.

## 🙋 Support

For issues or feature requests:
1. Check the requirements.txt versions
2. Ensure data files are properly formatted
3. Try clearing Streamlit cache: `streamlit cache clear`
4. Review the troubleshooting section above

---

**Built with ❤️ using Streamlit, Scikit-learn, and Python**
