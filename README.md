# 🏘️ Real Estate Analysis in Casablanca

## 📊 Overview  
This project analyzes real estate listings in **Casablanca, Morocco**, exploring the relationships between **price**, **surface area**, and **number of bedrooms**. It involves **web scraping**, **data transformation**, and **interactive visualizations** using **Excel** and **Power BI**.

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `yakey1.py` | 🔍 Python script for web scraping real estate listings from Yakeey.com |
| `annonces_maisons.xlsx` | 📄 Cleaned dataset with 18 real estate listings |
| `dashboard_powerbi.png` | 📊 Power BI dashboard with advanced visualizations |

---

## 🧪 Features & Process

### 1. 🕷️ Web Scraping
- **Tool**: `Selenium` (with `webdriver-manager`)
- **Website**: [Yakeey.com](https://www.yakeey.com)
- **Extracted Fields**: Property type, price, neighborhood, surface area, bedrooms, bathrooms, furnished status
- **Output**: Structured DataFrame → Excel file

### 2. 🔧 Data Transformation
- **Library**: `pandas`
- Cleaned and formatted fields:
  - `prix`: `"22 000 DH"` → `22000`
  - `superficie`: `"110 m²"` → `110`
  - `chambres`: `"2 Chambre(s)"` → `2`, `"N/A"` → `0`
- Saved as `annonces_maisons.xlsx`

### 3. 📈 Data Visualization

#### 🧮 Excel Visualization
- **Scatter Plot**:  
  - **X-Axis**: Surface Area (m²)  
  - **Y-Axis**: Price (DH)  
  - **Series**: Colored by number of bedrooms

#### 📉 Power BI Dashboard
- Interactive charts:
  - 🟢 **Scatter Plot** – Price vs Surface Area, sized by bedrooms
  - 🔵 **Line Charts** – Trends across price ranges
  - 🟣 **Pie Chart** – Bedrooms by neighborhood
  - 🟠 **Bar Charts** – Bedrooms by property type & furnishing

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| `Python` | Core scripting and processing |
| `Selenium` | Browser automation for scraping |
| `pandas` | Data manipulation |
| `webdriver-manager` | Automatic ChromeDriver handling |

| `Power BI` | Dashboard and advanced visualizations |

---

