# 🔍 Python Job Scraper – Naukri.com Automation  

## 📌 Overview  
This project automates real-time job listing extraction from [Naukri.com](https://www.naukri.com) using **Selenium** and **BeautifulSoup**.  
It bypasses Naukri's ₹1800 premium service to fetch the latest Python job postings, including those marked as *"just now"*.  

## 🚀 Features  
✅ **Automated Job Scraping** – Extracts Python job listings dynamically.  
✅ **Bypass Premium Restriction** – Fetches latest job postings without paying ₹1800.  
✅ **Dynamic Pagination Handling** – Scrapes all available job pages efficiently.  
✅ **Optimized Data Extraction** – Uses **XPath selectors** for accuracy.  
✅ **Excel Export** – Saves structured job data for easy analysis.  

## 🛠️ Tech Stack  
- **Python**  
- **Selenium**  
- **BeautifulSoup**  
- **Pandas** (for Excel export)  

## 📌 How It Works  
1. Uses **Selenium WebDriver** to navigate Naukri.com.  
2. Extracts job details (title, company, location, experience, and posted time).  
3. Handles pagination dynamically to fetch all jobs.  
4. Saves data into an **Excel file** for easy access.  

## 📂 Installation & Setup  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/python-job-scraper.git
cd python-job-scraper


### 2️⃣ Install Dependencies  
Ensure you have Python installed, then install the required libraries:

```bash
pip install selenium beautifulsoup4 pandas openpyxl

