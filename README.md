# 🔐 Secure Code Review — CodeAlpha Internship Task 3

A complete security audit of a vulnerable Python application, identifying 7 security vulnerabilities using **Bandit (static analysis)** and **manual code review** — including a fully remediated secure version and a professional security findings report.

---

# 📋 Table of Contents

* About the Project
* Files in this Repository
* Vulnerabilities Found
* Tools Used
* How to Run (Windows)
* What I Learned
* Author

---

# 📖 About the Project

This project was developed as part of **Task 3 — Secure Code Review** for the CodeAlpha Cybersecurity Internship.

The objectives of this task were to:

* Select a Python application to audit
* Perform a security code review using static analysis tools and manual inspection
* Identify vulnerabilities with severity ratings
* Create a secure remediated version of the application
* Document findings and remediation techniques

---

# 📁 Files in this Repository

| File                 | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| `vulnerable_app.py`  | Original Python application containing intentional security vulnerabilities |
| `secure_app.py`      | Fixed version with vulnerabilities remediated                               |
| `bandit_report.txt`  | Security scan output generated using Bandit                                 |
| `findings_report.md` | Detailed findings report with remediation steps                             |
| `README.md`          | Project documentation                                                       |

---

# 🔴 Vulnerabilities Found

| # | Vulnerability                    | Severity  | Status |
| - | -------------------------------- | --------- | ------ |
| 1 | Hardcoded Credentials            | 🔴 HIGH   | Fixed  |
| 2 | SQL Injection                    | 🔴 HIGH   | Fixed  |
| 3 | Command Injection (`shell=True`) | 🔴 HIGH   | Fixed  |
| 4 | Weak Hashing (MD5)               | 🟡 MEDIUM | Fixed  |
| 5 | Missing Input Validation         | 🟡 MEDIUM | Fixed  |
| 6 | Path Traversal                   | 🟡 MEDIUM | Fixed  |
| 7 | Information Disclosure           | 🟢 LOW    | Fixed  |

---

# 🛠 Tools Used

| Tool               | Purpose                                |
| ------------------ | -------------------------------------- |
| Python 3           | Application Language                   |
| Bandit             | Python Static Security Analysis Tool   |
| Manual Code Review | Line-by-line security inspection       |
| OWASP Top 10       | Vulnerability classification reference |
| bcrypt             | Secure password hashing                |

---

# ▶️ How to Run (Windows)

## Step 1 — Clone the Repository

```powershell
git clone https://github.com/Balamurugan200526/CodeAlpha_SecureCodeReview.git

cd CodeAlpha_SecureCodeReview
```

---

## Step 2 — Install Dependencies

```powershell
python -m pip install bandit bcrypt
```

---

## Step 3 — Run Bandit Security Scan

```powershell
python -m bandit -r vulnerable_app.py -o bandit_report.txt -f txt
```

---

## Step 4 — View the Bandit Report

```powershell
type bandit_report.txt
```

---

## Step 5 — Run the Vulnerable Application

```powershell
python vulnerable_app.py
```

---

## Step 6 — Run the Secure Application

```powershell
python secure_app.py
```

---

# 📚 What I Learned

* How to identify OWASP Top 10 vulnerabilities in Python applications
* How SQL Injection attacks work and how parameterized queries prevent them
* Why using `shell=True` in subprocess calls is dangerous
* The difference between weak hashing (MD5) and secure hashing (bcrypt)
* How to use Bandit for automated static security analysis
* How to perform manual security code review
* The importance of secure input validation and error handling
* How environment variables help protect sensitive credentials

---

# 👤 Author

* **Name:** Balamurugan S
* **Internship:** CodeAlpha Cybersecurity Internship

## LinkedIn

https://www.linkedin.com/in/balamurugan-s-468387337

## GitHub

https://github.com/Balamurugan200526/CodeAlpha-Task-3.git

---

# ⭐ Project Status

✅ Task Completed Successfully
✅ Vulnerabilities Identified
✅ Secure Version Implemented
✅ Report Documented
✅ Static Analysis Performed

---

> ⭐ If you found this project useful, consider giving the repository a star.
