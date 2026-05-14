# ============================================================
# VULNERABLE APPLICATION - CodeAlpha Secure Code Review Task 3
# WARNING: This file is INTENTIONALLY vulnerable for education
# DO NOT use this code in any real project
# ============================================================

import sqlite3
import subprocess
import hashlib
import os

# -------------------------------------------------------
# VULNERABILITY 1: Hardcoded Credentials (HIGH severity)
# Passwords and API keys should NEVER be hardcoded
# -------------------------------------------------------
USERNAME = "admin"
PASSWORD = "admin123"
SECRET_KEY = "mysecretkey2024"
API_KEY = "sk-abc123hardcodedkey"

# -------------------------------------------------------
# VULNERABILITY 2: SQL Injection (HIGH severity)
# User input is directly placed into SQL query
# Attacker can input: ' OR '1'='1 to bypass login
# -------------------------------------------------------
def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # DANGEROUS: directly concatenating user input into SQL
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    print("[*] Running query:", query)
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    if result:
        return "Login successful!"
    else:
        return "Login failed."


# -------------------------------------------------------
# VULNERABILITY 3: Command Injection (HIGH severity)
# shell=True with user input allows attacker to run any command
# Attacker can input: "google.com; rm -rf /"
# -------------------------------------------------------
def ping_host(host):
    # DANGEROUS: shell=True with unsanitized input
    result = subprocess.call("ping " + host, shell=True)
    return result


# -------------------------------------------------------
# VULNERABILITY 4: Weak Hashing - MD5 (MEDIUM severity)
# MD5 is cryptographically broken and should not be used
# -------------------------------------------------------
def hash_password(password):
    # DANGEROUS: MD5 is easily cracked using rainbow tables
    return hashlib.md5(password.encode()).hexdigest()


# -------------------------------------------------------
# VULNERABILITY 5: No Input Validation (MEDIUM severity)
# No checks on input type or value before processing
# -------------------------------------------------------
def calculate_discount(price, discount):
    # DANGEROUS: No check if discount > 100 or negative
    # No check if inputs are valid numbers
    final_price = int(price) - (int(price) * int(discount) / 100)
    return final_price


# -------------------------------------------------------
# VULNERABILITY 6: Insecure File Read (MEDIUM severity)
# Reading files without validating the path
# Attacker can use: ../../etc/passwd to read system files
# -------------------------------------------------------
def read_file(filename):
    # DANGEROUS: No path validation - allows directory traversal
    with open(filename, "r") as f:
        return f.read()


# -------------------------------------------------------
# VULNERABILITY 7: Debug Mode / Information Disclosure (LOW)
# Printing sensitive error details to the user
# -------------------------------------------------------
def get_user_data(user_id):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = " + str(user_id))
        return cursor.fetchall()
    except Exception as e:
        # DANGEROUS: Exposing full error to user reveals system details
        print("ERROR DETAILS:", e)
        return None


# -------------------------------------------------------
# MAIN
# -------------------------------------------------------
if __name__ == "__main__":
    print("=== Vulnerable App Running ===")
    print("Password hash (MD5):", hash_password("admin123"))
    print("Discount result:", calculate_discount(1000, 10))
    print(login("admin", "admin123"))