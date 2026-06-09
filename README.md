# 📊 Superstore Sales Dashboard

An interactive Sales Analytics Dashboard built using Python, Streamlit, Pandas, and Plotly to transform raw retail sales data into actionable business insights.

## 🚀 Live Link: https://sales-dashboard-lk6vrncgyweun6ywajx4yf.streamlit.app/

## 🚀 Project Overview

This project analyzes the Superstore dataset and provides insights into sales performance, profitability, customer segments, product categories, and regional trends through an interactive dashboard.

The project follows a complete data analytics workflow:

1. Data Exploration
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Interactive Dashboard Development
5. Deployment using Streamlit

---

## 🛠️ Technologies Used

* Python
* Pandas
* Streamlit
* Plotly

---

## 📂 Project Structure

```text
Sales-dashboard/
│
├── Data/
│   ├── Superstore.csv
│   └── Superstore_clean.csv
│
├── explore.py      # Initial dataset exploration
├── clean.py        # Data cleaning and preprocessing
├── eda.py          # Exploratory Data Analysis
├── app.py          # Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## 📈 Key Business Insights

### Regional Analysis

* West region generates the highest sales and profit.
* Central region records strong sales but comparatively lower profit, indicating possible discounting or operational inefficiencies.

### Category Analysis

* Technology is the most profitable category.
* Furniture generates substantial sales but contributes relatively low profit.

### Sub-Category Analysis

* Tables and Bookcases are loss-making products.
* These sub-categories significantly reduce overall Furniture profitability.

### Customer Segments

* Consumer segment contributes the highest sales and profit.
* All customer segments maintain healthy profit performance.

### Sales Trends

* Sales consistently grow from 2014 to 2017.
* Strong seasonal spikes occur during September, November, and December.

---

## 📊 Dashboard Features

* Region Filters
* Category Filters
* KPI Cards

  * Total Sales
  * Total Profit
  * Total Orders
  * Profit Margin
* Sales & Profit by Region
* Sales & Profit by Category
* Sales & Profit by Sub-Category
* Monthly Sales Trend Analysis
* Customer Segment Performance Analysis

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/GotheArpita/Sales-dashboard.git
```

Move into the project folder:

```bash
cd Sales-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 🎯 Skills Demonstrated

* Data Cleaning
* Data Transformation
* Exploratory Data Analysis
* Business Insight Generation
* Data Visualization
* Dashboard Development
* Streamlit Deployment

---

## 👩‍💻 Author

Arpita Gothe

Computer Engineering Student | Data Analytics Enthusiast
