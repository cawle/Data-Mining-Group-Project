# 🚀 Quick Start Guide - iFood Marketing Dashboard

## ⚡ 5-Minute Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the App
```bash
streamlit run app.py
```

### Step 3: Open in Browser
```
http://localhost:8501
```

✅ **Done!** Your dashboard is now live.

---

## 📱 App Features at a Glance

| Page | What You Get | Key Insight |
|------|-------------|------------|
| **📊 Overview** | Spending patterns, customer stats, demographics | See which products customers buy most |
| **🎯 Segmentation** | Customer groups (K-Means), PCA visualization | Identify 4 distinct customer types |
| **🛍️ Market Basket** | "If-Then" purchase patterns, association rules | Wine → Meat (65% confidence, 1.42x lift) |
| **🎁 Recommendations** | Personalized product suggestions | Get top 5 products for any customer ID |
| **📢 Campaigns** | Campaign performance, channel analysis | Web beats Catalog for purchases |

---

## 🎮 Try These First

### 1️⃣ View Overview
- See total spending by product: **Wines leads with ~$680K**

### 2️⃣ Explore Segments  
- Click `🎯 Segmentation` → Adjust segments slider (2-8)
- See PCA scatter plot with 4 color-coded customer groups

### 3️⃣ Find Associations
- Go to `🛍️ Market Basket` 
- See "If customers buy WINE, they buy MEAT" patterns
- Adjust lift threshold to find strongest rules

### 4️⃣ Get Recommendations
- Select `🎁 Recommendations`
- Pick Customer ID (0-1999)
- Choose method: **Hybrid recommended** ⭐
- View top 5 products with scores

### 5️⃣ Campaign Insights
- Check `📢 Campaigns` 
- See which campaigns performed best
- Compare Web vs Catalog vs Store channels

---

## 🔧 System Requirements

| Requirement | Minimum | Recommended |
|------------|---------|-------------|
| Python | 3.8+ | 3.10+ |
| RAM | 2 GB | 4 GB |
| Disk | 100 MB | 500 MB |
| Time to Load | ~3 sec | <2 sec |

---

## 📊 Data Included

✅ **ifood_df.csv** - 2,000 customer records with:
- Demographics (Income, Age, Family status)
- Spending (6 product categories)
- Engagement (Campaign acceptance, Purchases)
- Channels (Web, Catalog, Store)

✅ **mba_rules.csv** - Pre-computed association rules (optional)

---

## 💡 Common Questions

**Q: What if I change the customer ID?**
- A: The recommendation engine analyzes that specific customer's profile and generates new suggestions instantly.

**Q: Can I see the code?**
- A: Yes! Open `app.py` - it's fully commented and documented (~1500 lines of clean Python).

**Q: How does Hybrid Recommendations work?**
- A: It combines:
  - **50%** Content-based (what similar customers bought)
  - **50%** Collaborative (what customers like them bought)
  - **Result**: Balanced, varied recommendations

**Q: Why some segments larger than others?**
- A: K-Means naturally groups customers by spending/income patterns. Larger segments = more typical customers.

**Q: Can I deploy this online?**
- A: Yes! See README.md for Streamlit Cloud, Hugging Face Spaces, or Docker options.

---

## 🎯 Real-World Use Cases

✅ **Marketing Team**: Target high-value segments with personalized campaigns  
✅ **Sales**: Cross-sell Wine customers with Meat products (1.42x boost)  
✅ **Product Manager**: Understand which categories bundle together  
✅ **Data Analyst**: Explore customer lifecycle and engagement patterns  
✅ **Executive**: Actionable KPIs on one dashboard  

---

## 🐛 If Something Goes Wrong

```bash
# Error: "No module named 'streamlit'"
pip install streamlit

# Error: "Data files not found"
# → Move app.py, ifood_df.csv, mba_rules.csv to same folder

# Error: "Port 8501 already in use"
streamlit run app.py --server.port 8502

# Slow performance
streamlit cache clear
```

---

## 📈 Next Steps

1. **Explore all 5 pages** - takes ~10 minutes
2. **Play with settings** - adjust clusters, customer IDs, recommendation types
3. **Read the charts** - understand spending patterns and associations
4. **Export insights** - use findings for marketing strategy
5. **Deploy online** - share with team via Streamlit Cloud (1 click)

---

## 🚀 Deploy to Cloud (Optional)

### Streamlit Cloud (Easiest)
```bash
# 1. Push to GitHub
git add .
git commit -m "add marketing dashboard"
git push

# 2. Visit https://streamlit.io/cloud
# 3. Connect GitHub repo
# 4. Select app.py
# 5. Deploy! ✨
```

Your app is now live and shareable!

---

## 📞 Tips & Tricks

💡 **Sidebar Navigation**: Use left sidebar to switch between pages instantly  
💡 **Caching**: First load takes 3-5 seconds, then instant on interactions  
💡 **Full Screen**: Press 'F' to maximize charts  
💡 **Download**: Hover over charts → click camera icon to save  
💡 **Responsive**: Works on desktop, tablet, mobile  

---

**Happy analyzing! 📊**

For detailed docs, see `README.md`
