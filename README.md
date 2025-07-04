# 🎬 Netflix Data Analysis Dashboard 📊

Welcome to the **Netflix Data Analysis Dashboard**—a Python project that helps you explore movie data interactively!  

This project includes:

✅ **User Registration & Login with OTP verification**  
✅ **Interactive Dashboard** to query movie details  
✅ **Beautiful Visualizations** to understand trends  

---

## ✨ Features

🎯 **User Authentication**
- 🔐 New users can **register** with name, email, and OTP verification via Gmail SMTP
- 🔑 Existing users can **log in** securely
- 🛑 Duplicate registrations are **blocked**

🎬 **Dashboard Functionalities**
Once logged in, you can:

1️⃣ **Find movie details:**
   - 📅 Release Date
   - 🌍 Country of Origin
   - ⭐ Ratings
   - ⏱️ Duration

2️⃣ **Explore visual trends:**
   - 📈 Movies released by Year (2015–2020)
   - 🎥 Movies by Top Directors
   - 🗺️ Movies by Country

📊 **Data Visualizations**
Graphs are generated with **matplotlib** to give clear insights.

---

## 🚀 How to Run
1️⃣ Set up MySQL and create the reg_users table:

CREATE TABLE reg_users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE
);

---

## 🛠️ Requirements

🐍 **Python 3.x**

💾 **MySQL Server** with a database named `netflix_data_analysis`

📧 A **Gmail account with an App Password**

📦 **Python Libraries:**
- `mysql-connector-python`
- `pandas`
- `matplotlib`
- `textblob`

💡 **Install dependencies:**

```bash
pip install mysql-connector-python pandas matplotlib textblob

