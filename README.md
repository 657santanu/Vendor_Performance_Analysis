# Vendor Performance Analysis

An end-to-end Data Analytics project focused on evaluating vendor performance, procurement efficiency, profitability trends, and operational costs using Python, SQL, SQLite, and Power BI concepts.

## 📌 Table of Contents

- <a href="#project-overview">Project Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#technology-stack">Technology Stack</a>
- <a href="#dataset-summary">Dataset Summary</a>
- <a href="#data-preparation">Data Preparation & Cleaning</a>
- <a href="#eda">Exploratory Data Analysis (EDA)</a>
- <a href="#sql-analysis">SQL Business Analysis</a>
- <a href="#statistical-analysis">Statistical Analysis</a>
- <a href="#power-bi-recommendations">Power BI Dashboard Recommendations</a>
- <a href="#business-insights">Key Business Insights</a>
- <a href="#business-recommendations">Business Recommendations</a>
- <a href="#skills-demonstrated">Skills Demonstrated</a>
- <a href="#project-workflow">Project Workflow</a>
- <a href="#conclusion">Conclusion</a>

---

<h2><a class="anchor" id="project-overview"></a>📌 Project Overview</h2>

This project analyzes procurement, sales, inventory, and freight datasets to uncover business insights related to vendor contribution, profit generation, and operational efficiency.

**The objective of this analysis is to help businesses:**
- Optimize vendor relationships
- Improve procurement planning
- Identify profit-driving brands
- Reduce operational costs
- Enhance inventory efficiency
- Support data-driven business decisions

---

<h2><a class="anchor" id="business-problem"></a>🎯 Business Problem</h2>

Businesses managing large procurement and inventory operations often struggle with:
- Identifying high-performing vendors
- Understanding profitability drivers
- Managing freight and operational costs
- Optimizing inventory turnover
- Detecting underperforming products
- Improving procurement efficiency

This project provides analytical solutions to these challenges using real-world business intelligence workflows.

---

<h2><a class="anchor" id="technology-stack"></a>🛠️ Technology Stack</h2>

| Technology | Purpose |
| :--- | :--- |
| **Python** | Data Analysis & ETL |
| **SQL** | Business Querying & Analysis |
| **SQLite** | Database Management |
| **Pandas** | Data Manipulation |
| **NumPy** | Numerical Analysis |
| **Matplotlib** | Data Visualization |
| **Seaborn** | Statistical Visualization |
| **Jupyter Notebook** | Development Environment |
| **Power BI** | Dashboard Planning |

---

<h2><a class="anchor" id="dataset-summary"></a>📂 Dataset Summary</h2>

The project uses multiple transactional datasets including:
- Purchases
- Purchase Prices
- Vendor Invoices
- Sales
- Vendor Sales Summary

### Key Features Analyzed:
- Vendor Information
- Product & Brand Details
- Purchase Quantities
- Sales Revenue
- Gross Profit
- Freight Costs
- Inventory Metrics

---

<h2><a class="anchor" id="data-preparation"></a>⚙️ Data Preparation & Cleaning</h2>

Data preprocessing and ingestion were performed using Python.

### Steps Performed:
- Imported datasets using Pandas
- Connected Python with SQLite database
- Loaded CSV files into structured database tables
- Checked for missing values
- Standardized column names
- Verified data consistency
- Removed redundant records

### ETL Pipeline Features:
- Automated CSV-to-database ingestion
- Chunk-based processing for large datasets
- Logging mechanism for monitoring ingestion

### Feature Engineering:
Created important business KPIs such as:
- Gross Profit
- Profit Margin
- Purchase-to-Sales Ratio
- Vendor Efficiency Metrics

---

<h2><a class="anchor" id="eda"></a>📊 Exploratory Data Analysis (EDA)</h2>

EDA was performed to identify business trends, vendor behavior, and profitability patterns.

### Analysis Conducted:

#### 📈 Descriptive Statistics
- Analyzed Mean, Median, Standard Deviation, and Quartiles.
- Evaluated broad revenue distributions.

#### 📉 Distribution Analysis
Created histograms for:
- Sales Revenue
- Purchase Amount
- Gross Profit
- Freight Costs

#### 📦 Outlier Detection
Used boxplots to identify:
- High-volume vendors
- High-margin brands
- Unusual freight costs

#### 🔥 Correlation Analysis
Generated heatmaps to study relationships between **Purchase Dollars**, **Sales Revenue**, **Gross Profit**, and **Inventory Metrics**.

> **Key Insight:** Strong positive relationships were observed between purchase volume, sales revenue, and profitability.

---

<h2><a class="anchor" id="sql-analysis"></a>🗄️ SQL Business Analysis</h2>

SQL queries were used extensively to answer business questions and generate analytical insights.

### Business Analysis Performed:
1. **Vendor Revenue Analysis:** Identified top revenue-generating vendors.
2. **Profitability Analysis:** Calculated gross profit and profit margins vendor-wise.
3. **Freight Cost Analysis:** Evaluated vendors with high operational and freight costs.
4. **Brand Performance Analysis:** Identified high-margin brands and low-performing products.
5. **Procurement Efficiency:** Analyzed Purchase-to-Sales ratios.
6. **Vendor Segmentation:** Classified vendors based on profitability and contribution.
7. **Inventory Analysis:** Studied purchasing trends and inventory movement.
8. **Sales Contribution Analysis:** Evaluated vendor and brand contribution toward total sales.

---

<h2><a class="anchor" id="statistical-analysis"></a>📈 Statistical Analysis</h2>

The project used statistical techniques to improve business understanding.

### Techniques Used:
- Correlation Analysis
- Quantile Analysis
- Distribution Analysis
- Vendor Segmentation
- Outlier Detection

### Key Findings:
- A small number of vendors contributed disproportionately to revenue.
- Several low-volume brands generated high profit margins.
- Freight costs varied significantly across vendors.

---

<h2><a class="anchor" id="power-bi-recommendations"></a>📊 Power BI Dashboard Recommendations</h2>

The analytical dataset is suitable for creating an interactive Power BI dashboard.

### Recommended KPIs:
- Total Sales Revenue
- Gross Profit
- Profit Margin %
- Freight Cost
- Vendor Contribution
- Top Brands
- Purchase-to-Sales Ratio
- Inventory Efficiency

### Recommended Dashboard Pages:
- Executive Overview
- Vendor Performance
- Profitability Insights
- Brand Analysis
- Freight Cost Analysis
- Procurement Efficiency

---

<h2><a class="anchor" id="business-insights"></a>💡 Key Business Insights</h2>

- **Revenue Concentration:** A small percentage of vendors generated a major portion of overall revenue.
- **Hidden Profit Opportunities:** Several brands showed high profit margins despite low sales volume.
- **Procurement-Sales Relationship:** Purchase quantities strongly influenced sales performance.
- **Freight Optimization Opportunity:** Certain vendors had disproportionately high freight costs.
- **Inventory Efficiency Differences:** Vendor efficiency varied significantly based on Purchase-to-Sales ratios.

---

<h2><a class="anchor" id="business-recommendations"></a>✅ Business Recommendations</h2>

- **Optimize Vendor Management:** Focus more on high-performing and profitable vendors.
- **Improve Freight Efficiency:** Negotiate logistics and freight costs with expensive vendors.
- **Promote High-Margin Brands:** Increase visibility and inventory allocation for high-margin products.
- **Improve Procurement Planning:** Use sales trends to reduce over-purchasing and improve inventory turnover.
- **Implement Real-Time Monitoring:** Deploy Power BI dashboards for continuous performance tracking.

---

<h2><a class="anchor" id="skills-demonstrated"></a>🚀 Skills Demonstrated</h2>

### Technical Skills:
- Python, SQL, SQLite
- Pandas & NumPy
- Matplotlib & Seaborn
- Data Cleaning & ETL Pipeline Development
- Exploratory Data Analysis & Statistical Analysis

### Business Analytics Skills:
- Vendor & Profitability Analysis
- Procurement Analytics
- KPI Design
- Business Intelligence & Insight Generation

---

<h2><a class="anchor" id="project-workflow"></a>📌 Project Workflow</h2>

<pre><code>Raw Data → Data Cleaning → ETL Pipeline → SQL Analysis → EDA → Statistical Analysis → Insight Generation → Dashboard Planning → Business Recommendations</code></pre>

---

<h2><a class="anchor" id="conclusion"></a>🏆 Conclusion</h2>

This project successfully transformed raw transactional vendor data into actionable business insights using Python, SQL, and analytical techniques. 

**The analysis isolated:**
- High-performing vendors
- Procurement inefficiencies
- Freight optimization opportunities
- Profit-driving brands
- Vendor profitability trends
