
# 🔐 CyberCheck

CyberCheck is a **web-based vulnerability assessment platform** designed to identify security risks in web applications and provide **AI-powered remediation suggestions**. It helps developers and organizations proactively detect and fix vulnerabilities based on **OWASP Top 10 principles**.

----------

## 🚀 Features

### 🔹 Core Functionality

-   User Authentication & Role Management (Admin & Registered Users)
    
-   Comprehensive Vulnerability Scanning with 9 specialized modules:
    
    -   SQL Injection Detection
        
    -   Cross-Site Scripting (XSS)
        
    -   CSRF Token Validation
        
    -   Security Headers Analysis
        
    -   Insecure Deserialization Detection
        
    -   Sensitive Data Exposure Scanning
        
    -   Broken Authentication Testing
        
    -   Known Vulnerabilities Detection
        
    -   Insufficient Logging Identification
        
-   Multiple Scan Modes:
    
    -   Full Scan (All vulnerabilities)
        
    -   Targeted Scan (Single vulnerability)
        
-   Trial Scanning without authentication
    
-   Scan History & Report Generation
    

----------

### 🤖 AI-Powered Capabilities

-   AI-based vulnerability remediation suggestions using **Ollama (Llama 3.2)**
    
-   Natural language cybersecurity recommendations using **fine-tuned T5 model**
    

----------

### 🛠️ Admin Features

-   Flask-Admin dashboard for:
    
    -   User management
        
    -   Scan monitoring
        
    -   Vulnerability tracking
        
    -   Suggestion management
        
-   Full database control with CRUD operations
    

----------

### 🌐 Public Pages

-   Landing Page
    
-   Features Overview
    
-   How It Works Guide
    
-   About Section
    
-   FAQ
    
-   Contact Form
    
-   News Feed
    
-   Documentation Download
    
-   Trial Scanner Page
    

----------

### 📊 User Dashboard

-   Scan statistics visualization
    
-   Recent scan history tracking
    
-   Profile management with image upload support
    

----------

## 🧰 Tech Stack

### 🔹 Backend

-   Python
    
-   Flask
    
-   SQLAlchemy
    
-   SQLite
    
-   Flask-Migrate / Alembic
    

----------

### 🔐 Security & Authentication

-   Flask-Login
    
-   Flask-Bcrypt
    
-   Flask-WTF (CSRF Protection)
    

----------

### 🤖 AI / ML

-   Ollama (Local LLM Interface)
    
-   HuggingFace Transformers (T5 Model)
    
-   Pandas
    

----------

### 🌐 Web & Data Handling

-   Requests
    
-   BeautifulSoup4
    

----------

### 🎨 Frontend

-   Jinja2
    
-   WTForms
    
-   Bootstrap
    

----------

### ⚙️ Admin Panel

-   Flask-Admin
    

----------

### 🧩 Utilities

-   Markdown
    
-   python-dateutil / pytz
    
-   Jupyter Notebook / IPython
    

----------

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/cybercheck.git

# Navigate to project directory
cd cybercheck

# Create virtual environment
python -m venv env

# Activate virtual environment
# Windows
env\\Scripts\\activate
# Mac/Linux
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
flask run

```

----------

## 📌 Usage

1.  Register/Login as a user
    
2.  Enter a target website URL
    
3.  Choose scan type (Full / Specific)
    
4.  View detailed vulnerability reports
    
5.  Get AI-generated security recommendations
    

----------

## 📊 Key Highlights

-   Based on **OWASP Top 10 security standards**
    
-   Combines **security scanning + AI recommendations**
    
-   Supports both **authenticated and trial users**
    
-   Includes **admin-level monitoring system**
    
-   Designed for **scalability and real-world deployment**
    

----------

## 🔮 Future Enhancements

-   Integration with cloud deployment (AWS / Docker)
    
-   Real-time vulnerability alerts
    
-   CI/CD pipeline integration for automated scans
    
-   Advanced reporting with PDF export
    
-   Multi-language support
    

----------

## 👨‍💻 Author

**Seetansh Bhatnagar**  
Aspiring Software Developer | Cybersecurity Enthusiast

-   LinkedIn: https://www.linkedin.com/in/seetansh-m-bhatnagar/
    
-   GitHub: https://github.com/Seetansh
    

----------

## 📄 License

This project is licensed under the MIT License.

----------

## ⭐ Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

----------

## 📬 Contact

For any queries or collaboration opportunities, feel free to reach out via LinkedIn or GitHub.

----------
