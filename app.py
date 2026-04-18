import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(
    page_title="iFood Marketing Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess the iFood customer data"""
    try:
        df = pd.read_csv('ifood_df.csv')

        # Create Education column from one-hot encoded columns
        education_cols = ['education_2n Cycle', 'education_Basic', 'education_Graduation', 'education_Master', 'education_PhD']
        df['Education'] = df[education_cols].idxmax(axis=1).str.replace('education_', '')

        # Create Marital_Status column from one-hot encoded columns
        marital_cols = ['marital_Divorced', 'marital_Married', 'marital_Single', 'marital_Together', 'marital_Widow']
        df['Marital_Status'] = df[marital_cols].idxmax(axis=1).str.replace('marital_', '')

        return df
    except FileNotFoundError:
        st.error("ifood_df.csv not found. Please ensure the data file is in the same directory.")
        return None

@st.cache_data
def load_mba_rules():
    """Load pre-computed market basket analysis rules"""
    try:
        rules_df = pd.read_csv('mba_rules.csv')
        return rules_df
    except FileNotFoundError:
        st.warning("mba_rules.csv not found. Market Basket Analysis will use computed rules.")
        return None

def perform_clustering(df, n_clusters=4):
    """Perform customer segmentation using K-means clustering"""
    # Select relevant features for clustering
    features = ['Income', 'Age', 'Recency', 'MntTotal', 'NumWebPurchases',
                'NumCatalogPurchases', 'NumStorePurchases']

    # Handle missing values
    df_clust = df[features].fillna(df[features].mean())

    # Standardize the features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df_clust)

    # Apply PCA for dimensionality reduction
    pca = PCA(n_components=2)
    pca_features = pca.fit_transform(scaled_features)

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(scaled_features)

    # Add cluster labels to dataframe
    df_clust['Cluster'] = clusters
    df_clust['PCA1'] = pca_features[:, 0]
    df_clust['PCA2'] = pca_features[:, 1]

    return df_clust, kmeans, pca

def build_recommendation_system(df):
    """Build recommendation systems"""
    # Content-based filtering using customer features
    features = ['Income', 'Age', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts',
                'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[features].fillna(df[features].mean()))

    # Calculate similarity matrix
    content_similarity = cosine_similarity(scaled_features)

    # Collaborative filtering using purchase patterns
    purchase_features = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases',
                        'NumWebVisitsMonth', 'NumDealsPurchases']

    collab_features = scaler.fit_transform(df[purchase_features].fillna(df[purchase_features].mean()))
    collab_similarity = cosine_similarity(collab_features)

    return content_similarity, collab_similarity

def get_recommendations(customer_id, df, content_sim, collab_sim, n_recommendations=5):
    """Get hybrid recommendations for a customer"""
    if customer_id >= len(df):
        return []

    # Content-based recommendations
    content_scores = content_sim[customer_id]
    content_indices = np.argsort(content_scores)[::-1][1:n_recommendations+1]

    # Collaborative recommendations
    collab_scores = collab_sim[customer_id]
    collab_indices = np.argsort(collab_scores)[::-1][1:n_recommendations+1]

    # Hybrid approach (weighted combination)
    hybrid_scores = 0.6 * content_scores + 0.4 * collab_scores
    hybrid_indices = np.argsort(hybrid_scores)[::-1][1:n_recommendations+1]

    recommendations = {
        'content_based': df.iloc[content_indices][['Income', 'Age', 'MntTotal']].to_dict('records'),
        'collaborative': df.iloc[collab_indices][['Income', 'Age', 'MntTotal']].to_dict('records'),
        'hybrid': df.iloc[hybrid_indices][['Income', 'Age', 'MntTotal']].to_dict('records')
    }

    return recommendations

def page_overview(df):
    """Overview page with key metrics and visualizations"""
    st.header("Marketing Intelligence Dashboard")

    if df is None:
        st.error("No data available")
        return

    # Filters
    st.sidebar.subheader("Filters")
    education_filter = st.sidebar.multiselect(
        "Education Level",
        options=df['Education'].unique(),
        default=df['Education'].unique()
    )
    marital_filter = st.sidebar.multiselect(
        "Marital Status",
        options=df['Marital_Status'].unique(),
        default=df['Marital_Status'].unique()
    )

    # Apply filters
    filtered_df = df[
        (df['Education'].isin(education_filter)) &
        (df['Marital_Status'].isin(marital_filter))
    ]

    # Check if filtered data is empty
    if filtered_df.empty:
        st.warning("No data matches the selected filters. Please adjust your filter selections.")
        return

    # Key Performance Indicators
    st.subheader("Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_customers = len(filtered_df)
        st.metric("Total Customers", f"{total_customers:,}")

    with col2:
        avg_income = filtered_df['Income'].mean()
        st.metric("Average Income", f"${avg_income:,.0f}")

    with col3:
        avg_age = filtered_df['Age'].mean()
        st.metric("Average Age", f"{avg_age:.1f} years")

    with col4:
        total_spent = filtered_df['MntTotal'].sum()
        st.metric("Total Revenue", f"${total_spent:,.0f}")

    # Additional KPIs
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        response_rate = (filtered_df['Response'].sum() / len(filtered_df)) * 100
        st.metric("Campaign Response Rate", f"{response_rate:.1f}%")

    with col2:
        avg_recency = filtered_df['Recency'].mean()
        st.metric("Average Recency", f"{avg_recency:.1f} days")

    with col3:
        total_purchases = filtered_df[['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum().sum()
        st.metric("Total Purchases", f"{total_purchases:,.0f}")

    with col4:
        avg_spent_per_customer = filtered_df['MntTotal'].mean()
        st.metric("Avg Spent per Customer", f"${avg_spent_per_customer:,.0f}")

    # Quick Insights
    st.subheader("Quick Insights")
    insight_col1, insight_col2 = st.columns(2)

    with insight_col1:
        if not filtered_df['Education'].value_counts().empty:
            top_education = filtered_df['Education'].value_counts().index[0]
            st.info(f"Most common education level: {top_education}")
        else:
            st.info("Education data not available")

        if len(filtered_df) > 0:
            high_value_customers = (filtered_df['MntTotal'] > filtered_df['MntTotal'].quantile(0.75)).sum()
            st.info(f"High-value customers (>75th percentile): {high_value_customers}")
        else:
            st.info("No customer data available")

    with insight_col2:
        if not filtered_df['Marital_Status'].value_counts().empty:
            top_marital = filtered_df['Marital_Status'].value_counts().index[0]
            st.info(f"Most common marital status: {top_marital}")
        else:
            st.info("Marital status data not available")

        recent_customers = (filtered_df['Recency'] <= 30).sum()
        st.info(f"Customers who purchased in last 30 days: {recent_customers}")

    # Visualizations
    st.subheader("Customer Analytics")

    if len(filtered_df) < 2:
        st.warning("Not enough data to generate visualizations. Please adjust your filters.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Income Distribution")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.histplot(filtered_df['Income'], bins=30, ax=ax, kde=True)
            ax.set_xlabel('Income ($)')
            ax.set_ylabel('Number of Customers')
            ax.set_title('Income Distribution')
            st.pyplot(fig)

        with col2:
            st.subheader("Age Distribution")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.histplot(filtered_df['Age'], bins=30, ax=ax, kde=True)
            ax.set_xlabel('Age')
            ax.set_ylabel('Number of Customers')
            ax.set_title('Age Distribution')
            st.pyplot(fig)

        # Spending Analysis
        st.subheader("Spending Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Spending by Product Category")
            categories = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts',
                          'MntSweetProducts', 'MntGoldProds']
            category_spending = filtered_df[categories].sum()

            fig, ax = plt.subplots(figsize=(8, 6))
            category_spending.plot(kind='bar', ax=ax, color='skyblue')
            ax.set_xlabel('Product Category')
            ax.set_ylabel('Total Spending ($)')
            ax.set_title('Total Spending by Product Category')
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)

        with col2:
            st.subheader("Purchase Channel Distribution")
            channels = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
            channel_purchases = filtered_df[channels].sum()

            fig, ax = plt.subplots(figsize=(8, 6))
            channel_purchases.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90)
            ax.set_title('Purchase Distribution by Channel')
            ax.set_ylabel('')
            st.pyplot(fig)

        # Customer Segmentation Preview
        st.subheader("Customer Segmentation Preview")
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(filtered_df['Income'], filtered_df['MntTotal'],
                            c=filtered_df['Age'], cmap='viridis', alpha=0.6)
        ax.set_xlabel('Income ($)')
        ax.set_ylabel('Total Spending ($)')
        ax.set_title('Income vs Total Spending (colored by Age)')
        plt.colorbar(scatter, ax=ax, label='Age')
        st.pyplot(fig)

        # Campaign Performance Summary
        st.subheader("Campaign Performance Summary")
        campaign_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3',
                         'AcceptedCmp4', 'AcceptedCmp5', 'Response']
        campaign_acceptances = filtered_df[campaign_cols].sum()

        fig, ax = plt.subplots(figsize=(10, 6))
        campaign_acceptances.plot(kind='bar', ax=ax, color='lightgreen')
        ax.set_xlabel('Campaign')
        ax.set_ylabel('Number of Acceptances')
        ax.set_title('Campaign Acceptances')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

def page_segmentation(df):
    """Customer segmentation page"""
    st.header("Customer Segmentation")

    if df is None:
        st.error("No data available")
        return

    # Clustering parameters
    n_clusters = st.slider("Number of Clusters", 2, 8, 4)

    with st.spinner("Performing clustering analysis..."):
        clustered_df, kmeans, pca = perform_clustering(df, n_clusters)

    # Cluster visualization
    st.subheader("Customer Clusters")
    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(clustered_df['PCA1'], clustered_df['PCA2'],
                        c=clustered_df['Cluster'], cmap='viridis', alpha=0.6)
    ax.set_xlabel('PCA Component 1')
    ax.set_ylabel('PCA Component 2')
    ax.set_title('Customer Segments (PCA Projection)')
    plt.colorbar(scatter, ax=ax, label='Cluster')
    st.pyplot(fig)

    # Cluster characteristics
    st.subheader("Cluster Characteristics")

    cluster_summary = clustered_df.groupby('Cluster').agg({
        'Income': 'mean',
        'Age': 'mean',
        'Recency': 'mean',
        'MntTotal': 'mean'
    }).round(2)

    st.dataframe(cluster_summary)

    # Cluster sizes
    cluster_sizes = clustered_df['Cluster'].value_counts().sort_index()
    st.subheader("Cluster Sizes")
    st.bar_chart(cluster_sizes)

def page_market_basket(df):
    """Market Basket Analysis page"""
    st.header("Market Basket Analysis")

    if df is None:
        st.error("No data available")
        return

    # Load pre-computed rules if available
    rules_df = load_mba_rules()

    if rules_df is not None:
        st.subheader("Association Rules")
        st.dataframe(rules_df.head(20))

        # Rule visualization
        st.subheader("Top Rules by Confidence")
        top_rules = rules_df.nlargest(10, 'confidence')

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(range(len(top_rules)), top_rules['confidence'])
        ax.set_yticks(range(len(top_rules)))
        ax.set_yticklabels([f"Rule {i+1}" for i in range(len(top_rules))])
        ax.set_xlabel('Confidence')
        ax.set_title('Top 10 Rules by Confidence')
        st.pyplot(fig)
    else:
        st.info("Computing association rules...")

        # Prepare transaction data (simplified example)
        # In a real scenario, you'd have transaction-level data
        st.warning("Market basket analysis requires transaction-level data. Using sample analysis.")

        # Sample analysis with available data
        purchase_cols = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
        purchase_data = (df[purchase_cols] > 0).astype(int)

        # Apply Apriori algorithm
        frequent_itemsets = apriori(purchase_data, min_support=0.1, use_colnames=True)
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

        if not rules.empty:
            st.subheader("Generated Association Rules")
            st.dataframe(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
        else:
            st.info("No strong association rules found with current parameters.")

def page_recommendations(df):
    """Recommendation Systems page"""
    st.header("Recommendation Systems")

    if df is None:
        st.error("No data available")
        return

    # Build recommendation systems
    with st.spinner("Building recommendation systems..."):
        content_sim, collab_sim = build_recommendation_system(df)

    # Customer selection
    customer_id = st.number_input("Select Customer ID", 0, len(df)-1, 0)

    if st.button("Get Recommendations"):
        recommendations = get_recommendations(customer_id, df, content_sim, collab_sim)

        # Display recommendations
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Content-Based")
            if recommendations['content_based']:
                for rec in recommendations['content_based'][:3]:
                    st.write(f"Income: ${rec['Income']}, Age: {rec['Age']}, Total Spent: ${rec['MntTotal']}")

        with col2:
            st.subheader("Collaborative")
            if recommendations['collaborative']:
                for rec in recommendations['collaborative'][:3]:
                    st.write(f"Income: ${rec['Income']}, Age: {rec['Age']}, Total Spent: ${rec['MntTotal']}")

        with col3:
            st.subheader("Hybrid")
            if recommendations['hybrid']:
                for rec in recommendations['hybrid'][:3]:
                    st.write(f"Income: ${rec['Income']}, Age: {rec['Age']}, Total Spent: ${rec['MntTotal']}")

def page_campaigns(df):
    """Campaign Analytics page"""
    st.header("Campaign Analytics")

    if df is None:
        st.error("No data available")
        return

    # Campaign response analysis
    campaign_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3',
                     'AcceptedCmp4', 'AcceptedCmp5', 'Response']

    campaign_responses = df[campaign_cols].sum()

    st.subheader("Campaign Response Rates")
    fig, ax = plt.subplots(figsize=(10, 6))
    campaign_responses.plot(kind='bar', ax=ax)
    ax.set_xlabel('Campaign')
    ax.set_ylabel('Number of Acceptances')
    ax.set_title('Campaign Acceptances')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Overall campaign performance
    total_customers = len(df)
    acceptance_rate = (df['Response'].sum() / total_customers) * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Customers", f"{total_customers:,}")

    with col2:
        st.metric("Overall Acceptance Rate", f"{acceptance_rate:.1f}%")

    with col3:
        successful_campaigns = (campaign_responses > 0).sum()
        st.metric("Successful Campaigns", successful_campaigns)

    # Customer segments and campaign response
    st.subheader("Campaign Response by Customer Segments")

    # Simple segmentation based on income
    df['IncomeSegment'] = pd.cut(df['Income'],
                                bins=[0, 30000, 60000, 90000, float('inf')],
                                labels=['Low', 'Medium', 'High', 'Very High'])

    segment_response = df.groupby('IncomeSegment')['Response'].mean() * 100

    fig, ax = plt.subplots(figsize=(8, 6))
    segment_response.plot(kind='bar', ax=ax)
    ax.set_xlabel('Income Segment')
    ax.set_ylabel('Acceptance Rate (%)')
    ax.set_title('Campaign Acceptance by Income Segment')
    plt.xticks(rotation=45)
    st.pyplot(fig)

def main():
    """Main application function"""
    st.markdown('<h1 class="main-header">iFood Marketing Intelligence Dashboard</h1>',
                unsafe_allow_html=True)

    # Load data
    df = load_data()

    # Sidebar navigation
    st.sidebar.title("Navigation")
    pages = {
        "Overview": page_overview,
        "Customer Segmentation": page_segmentation,
        "Market Basket Analysis": page_market_basket,
        "Recommendation Systems": page_recommendations,
        "Campaign Analytics": page_campaigns
    }

    selected_page = st.sidebar.selectbox("Select Page", list(pages.keys()))

    # Display selected page
    pages[selected_page](df)

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.info("Built with Streamlit for iFood Marketing Analytics")

if __name__ == "__main__":
    main()
