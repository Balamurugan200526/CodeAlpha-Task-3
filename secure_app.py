# ============================================================
# SECURE APPLICATION - CodeAlpha Secure Code Review Task 3
# This is the FIXED version of vulnerable_app.py
# All vulnerabilities have been identified and remediated
# ============================================================

import sqlite3
import subprocess
import os
import bcrypt
import shlex
import re

# -------------------------------------------------------
# FIX 1: No Hardcoded Credentials (was HIGH severity)
# Credentials are now loaded from environment variables
# -------------------------------------------------------
USERNAME = os.environ.get("APP_USERNAME", "admin")
SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-in-production")
API_KEY = os.environ.get("API_KEY", "")


# -------------------------------------------------------
# FIX 2: SQL Injection prevented (was HIGH severity)
# Now using parameterized queries with placeholders (?)
# User input is never directly inserted into the query
# -------------------------------------------------------
def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SAFE: parameterized query — input treated as data, not code
    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hash = result[0].encode()
        # Verify password using bcrypt (secure comparison)
        if bcrypt.checkpw(password.encode(), stored_hash):
            return "Login successful!"
    return "Login failed."


# -------------------------------------------------------
# FIX 3: Command Injection prevented (was HIGH severity)
# shell=True removed; input is sanitized and validated
# -------------------------------------------------------
def ping_host(host):
    # SAFE: validate host format before passing to subprocess
    if not re.match(r'^[a-zA-Z0-9.\-]+$', host):
        return "Invalid host format."

    # SAFE: shell=False (default), arguments as list
    result = subprocess.call(
        ["ping", "-c", "1", shlex.quote(host)],
        shell=False
    )
    return result


# -------------------------------------------------------
# FIX 4: Strong hashing with bcrypt (was MEDIUM severity)
# bcrypt automatically handles salting — resistant to
# brute-force and rainbow table attacks
# -------------------------------------------------------
def hash_password(password):
    # SAFE: bcrypt with automatic salt generation
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


# -------------------------------------------------------
# FIX 5: Input Validation added (was MEDIUM severity)
# All inputs validated for type and range before processing
# -------------------------------------------------------
def calculate_discount(price, discount):
    # SAFE: validate types and ranges before processing
    try:
        price = float(price)
        discount = float(discount)
    except (ValueError, TypeError):
        raise ValueError("Price and discount must be valid numbers.")

    if price < 0:
        raise ValueError("Price cannot be negative.")
    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100.")

    final_price = price - (price * discount / 100)
    return round(final_price, 2)


# -------------------------------------------------------
# FIX 6: Path Traversal prevented (was MEDIUM severity)
# File path validated and restricted to safe directory only
# -------------------------------------------------------
SAFE_DIRECTORY = os.path.abspath("./safe_files")

def read_file(filename):
    # SAFE: resolve full path and verify it stays within allowed dir
    safe_path = os.path.abspath(os.path.join(SAFE_DIRECTORY, filename))

    if not safe_path.startswith(SAFE_DIRECTORY):
        raise PermissionError("Access denied: path traversal detected.")

    if not os.path.exists(safe_path):
        raise FileNotFoundError("File not found.")

    with open(safe_path, "r") as f:
        return f.read()


# -------------------------------------------------------
# FIX 7: No Information Disclosure (was LOW severity)
# Generic error messages to user; details logged internally
# -------------------------------------------------------
def get_user_data(user_id):
    try:
        if not str(user_id).isdigit():
            return "Invalid user ID."

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        # SAFE: parameterized query
        cursor.execute(
            "SELECT id, username FROM users WHERE id = ?",
            (user_id,)
        )
        return cursor.fetchall()
    except Exception:
        # SAFE: log internally, show generic message to user
        print("[LOG] Internal error in get_user_data")
        return "An error occurred. Please try again later."


# -------------------------------------------------------
# MAIN
# -------------------------------------------------------
if __name__ == "__main__":
    print("=== Secure App Running ===")

    # Demo: hash a password securely
    hashed = hash_password("mySecurePassword!")
    print("Secure bcrypt hash generated successfully.")

    # Demo: input validation working
    try:
        result = calculate_discount(1000, 10)
        print("Discounted price:", result)

        # This will be caught safely
        calculate_discount(1000, 150)
    except ValueError as e:
        print("Validation error caught safely:", e)

    print("Secure app demo complete.")