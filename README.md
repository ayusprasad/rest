# 🍽️ Restaurant Health & Analytics Profiling

Exploratory data analysis, automated profiling reports, and interactive HTML dashboards examining restaurant inspection metrics, health compliance, and operational indicators.

---

## 🚀 Quickstart

### 1. View Report Locally
```bash
python serve_report.py
```
Open [http://localhost:8080](http://localhost:8080) to inspect the interactive dashboard.

---

### 2. Deploy with Docker
```bash
docker build -t restaurant-analytics .
docker run -p 8080:8080 restaurant-analytics
```
Open [http://localhost:8080](http://localhost:8080).

---

## 📁 Repository Structure
```text
rest/
├── serve_report.py                # Lightweight zero-dependency HTTP server
├── Dockerfile                     # Slim container deployment
├── notebook/
│   ├── insight_notebook.ipynb     # Feature extraction notebook
│   ├── notebook.ipynb             # Exploratory analysis notebook
│   ├── output.html                # Interactive automated EDA profiling report
│   └── output1.html               # Secondary inspection dataset profiling
└── README.md                      # Documentation
```