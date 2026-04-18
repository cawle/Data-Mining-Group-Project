# 🌐 Deployment Guide

This guide covers deploying the iFood Marketing Dashboard to various platforms.

## 🚀 Option 1: Streamlit Cloud (Recommended - Easiest)

### Prerequisites
- GitHub account
- Streamlit account (free)
- Your code pushed to GitHub

### Steps

1. **Prepare your repository on GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Add iFood marketing dashboard"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ifood-dashboard.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to https://streamlit.io/cloud
   - Click "New app"
   - Select your GitHub repo
   - Choose branch: `main`
   - Enter path: `app.py`
   - Click "Deploy"

3. **Your app is live!** 🎉
   - Share URL: `https://YOUR_USERNAME-ifood-dashboard.streamlit.app`
   - Analytics included free

### Cost
✅ **Free** (up to 1 GB RAM)

### Advanced Settings
In Streamlit Cloud dashboard:
- Set environment variables
- Configure Python version
- Set memory limits

---

## 🤗 Option 2: Hugging Face Spaces

### Steps

1. **Create a Space:**
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Name: `ifood-marketing-dashboard`
   - Select "Streamlit" SDK
   - Create Space

2. **Upload Files:**
   - Add `app.py`
   - Add `requirements.txt`
   - Upload `ifood_df.csv`
   - Upload `mba_rules.csv`

3. **Wait for deployment**
   - ~2-3 minutes
   - URL: `https://huggingface.co/spaces/YOUR_USERNAME/ifood-marketing-dashboard`

### Benefits
✅ Easy GitHub sync  
✅ Persistent storage  
✅ Public/private options  
✅ GPU available (paid)  

---

## 🐳 Option 3: Docker (Self-Hosted)

### Build Docker Image

Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app.py .
COPY ifood_df.csv .
COPY mba_rules.csv .
COPY .streamlit .streamlit

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build & Run

```bash
# Build image
docker build -t ifood-dashboard .

# Run locally
docker run -p 8501:8501 ifood-dashboard

# Your app at http://localhost:8501
```

### Push to Container Registry

```bash
# Docker Hub
docker tag ifood-dashboard YOUR_USERNAME/ifood-dashboard
docker push YOUR_USERNAME/ifood-dashboard

# GitHub Container Registry
docker tag ifood-dashboard ghcr.io/YOUR_USERNAME/ifood-dashboard
docker push ghcr.io/YOUR_USERNAME/ifood-dashboard
```

### Deploy on Cloud Platforms
- **AWS ECS**: Use Docker image
- **Google Cloud Run**: `gcloud run deploy`
- **Azure Container Instances**: Azure Portal
- **DigitalOcean**: App Platform (Docker support)

---

## ☁️ Option 4: AWS (Advanced)

### Using AWS Elastic Beanstalk

1. **Create requirements.txt** ✅ (already done)

2. **Create `.ebextensions/01_streamlit.config`:**
```yaml
option_settings:
  aws:autoscaling:launchconfiguration:
    InstanceType: t3.small
  aws:elasticbeanstalk:application:environment:
    PYTHONUNBUFFERED: true

commands:
  01_install_streamlit:
    command: "pip install -r requirements.txt"
  02_install_graphviz:
    command: "yum install -y graphviz"
```

3. **Deploy:**
```bash
pip install awsebcli
eb init -p python-3.10 ifood-dashboard
eb create ifood-env
eb deploy
```

---

## 🔒 Security Best Practices

### For Production Deployment

1. **Environment Variables**
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   API_KEY = os.getenv("API_KEY")
   ```

2. **Hide Secrets**
   - Never commit `.env` files
   - Use platform secrets (Streamlit Cloud, Hugging Face, etc.)

3. **Use HTTPS**
   - All platforms provide SSL/TLS
   - Redirect HTTP to HTTPS

4. **Rate Limiting**
   ```python
   # Add to app.py if needed
   import time
   session_state = st.session_state
   ```

5. **Data Privacy**
   - Export only aggregated data
   - Don't expose customer IDs in public dashboards
   - Consider GDPR compliance

---

## 📊 Performance Optimization

### For Large Datasets

1. **Enable Caching** ✅ (already implemented)
   ```python
   @st.cache_data
   def load_data():
       return pd.read_csv("data.csv")
   ```

2. **Lazy Loading**
   - Load data only when page is viewed
   - Pre-process at startup

3. **Database Connection**
   ```python
   @st.cache_resource
   def init_connection():
       return psycopg2.connect(**st.secrets["postgres"])
   ```

4. **Reduce Chart Quality**
   ```python
   plt.savefig('chart.png', dpi=100)  # Lower DPI for faster rendering
   ```

---

## 🔄 CI/CD Pipeline

### GitHub Actions Example

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to Streamlit Cloud

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: |
          pip install -r requirements.txt
          pytest tests/
      - name: Deploy
        run: echo "Streamlit Cloud auto-deploys on push"
```

---

## 📈 Monitoring & Logging

### Streamlit Cloud
- Built-in logs: https://docs.streamlit.io/deploy/troubleshooting
- Real-time monitoring: Dashboard

### Self-Hosted
```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
logging.info("App started")
```

---

## 🆚 Platform Comparison

| Platform | Cost | Setup Time | Best For | Limits |
|----------|------|-----------|----------|--------|
| **Streamlit Cloud** | Free | 5 min | Quick demos, sharing | 1 GB RAM |
| **Hugging Face** | Free | 5 min | ML projects, community | Limited GPU |
| **Docker + AWS** | ~$10/mo | 30 min | Production apps | Scalable |
| **Heroku** | ❌ Discontinued | N/A | N/A | N/A |
| **Render** | ~$7/mo | 15 min | Small projects | 0.5 GB RAM |
| **Railway** | ~$5/mo | 10 min | Startups | Scalable |

---

## ✅ Deployment Checklist

- [ ] All requirements in `requirements.txt`
- [ ] All data files included (CSV, JSON, etc.)
- [ ] `.gitignore` configured
- [ ] `README.md` updated
- [ ] No hardcoded paths - use relative paths
- [ ] No sensitive data in code
- [ ] `requirements.txt` tested locally
- [ ] `app.py` runs without errors
- [ ] `.streamlit/config.toml` optimized
- [ ] Environment variables documented

---

## 🆘 Troubleshooting Deployment

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
streamlit run app.py
```

### "Port already in use"
```bash
streamlit run app.py --server.port 8502
```

### "Data files not found"
- Ensure files in same directory as app.py
- Use relative paths: `"./ifood_df.csv"`
- Not: `"C:/Users/.../ifood_df.csv"`

### "Out of memory"
- Upgrade tier on cloud platform
- Optimize data loading
- Reduce dataset size for free tier

### Slow performance
- Check network latency
- Enable caching: `@st.cache_data`
- Reduce chart resolution

---

## 🎯 Recommended Setup

**For Teams/Production:**
1. Deploy on **Streamlit Cloud** (easiest, free)
2. Use **GitHub** for version control
3. Add **environment variables** in Streamlit dashboard
4. Monitor with cloud logs
5. Scale to Docker if needed

**For Learning:**
1. Run locally: `streamlit run app.py`
2. Test changes instantly
3. Deploy when ready

---

**Questions?** Check README.md or QUICKSTART.md

