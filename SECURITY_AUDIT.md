# Security Audit Report

This report documents the security vulnerabilities identified in the codebase, mapped to their corresponding GitHub issues, affected files, and recommended fixes.

## Summary of Findings

| Issue # | Title | Affected File | Recommended Fix |
|---|---|---|---|
| #3, #7 | Hardcoded DB password in config.py | `src/config.py` | Load database credentials dynamically from environment variables (`os.getenv("DB_PASSWORD")`) rather than hardcoding plaintext passwords. |
| #8 | SQL injection in database.py queries | `src/database.py` | Replace raw string formatting in SQL queries with parameterized queries / prepared statements. |
| #9 | eval() on request input in gateway.py | `src/gateway.py` | Remove `eval()` usage on unsanitized user input; replace with `ast.literal_eval()` or standard JSON validation. |
| #10 | Plaintext password comparison in auth.py | `src/auth.py` | Implement secure password hashing (e.g., `bcrypt`, `argon2`, or `pbkdf2_hmac`) instead of raw string equality checks. |
| #11 | JWT secret is hardcoded | `src/auth.py` | Move JWT secret key out of source code and load it from environment variables (`os.getenv("JWT_SECRET")`). |
| #12 | Card numbers written to logs | `src/payments.py` | Mask or truncate credit card numbers (e.g., showing only last 4 digits) before logging payment data. |
| #13 | Passwords appear in log output | `src/logger.py` / `src/auth.py` | Filter out or mask sensitive authentication parameters (passwords) from log outputs. |
| #14 | ALLOWED_HOSTS is set to wildcard | `src/config.py` | Replace wildcard (`"*"`) in `ALLOWED_HOSTS` with explicit trusted domains or load allowed hosts from configuration environment variables. |
| #15 | DEBUG left on in production config | `src/config.py` | Disable `DEBUG` mode in production configurations (`DEBUG = False`) or load from environment settings to avoid stack trace/information disclosure. |

## Detailed Recommendations

### 1. Hardcoded DB Password (#3, #7)
- **File:** `src/config.py`
- **Vulnerability:** Storing database passwords in source code exposes sensitive credentials to anyone with repository access.
- **Fix:** Fetch `DB_PASSWORD` from `os.getenv("DB_PASSWORD")`.

### 2. SQL Injection Vulnerability (#8)
- **File:** `src/database.py`
- **Vulnerability:** Executing SQL queries built using raw string concatenation or format strings permits arbitrary SQL injection.
- **Fix:** Refactor query execution to use parameterized queries supported by the database adapter.

### 3. Remote Code Execution via eval() (#9)
- **File:** `src/gateway.py`
- **Vulnerability:** Calling `eval()` on user request parameters allows remote code execution (RCE).
- **Fix:** Replace `eval()` with `ast.literal_eval()` or structured JSON parsing/validation models.

### 4. Plaintext Password Verification (#10)
- **File:** `src/auth.py`
- **Vulnerability:** Direct string comparison for passwords exposes plaintext passwords and is vulnerable to timing attacks.
- **Fix:** Hash passwords with `bcrypt` or `argon2` and verify using standard, constant-time hashing helper functions.

### 5. Hardcoded JWT Secret Key (#11)
- **File:** `src/auth.py`
- **Vulnerability:** Hardcoded `SECRET_KEY` allows attackers to forge valid JWT tokens.
- **Fix:** Retrieve secret keys securely from environment variables.

### 6. Sensitive Financial Data in Logs (#12)
- **File:** `src/payments.py`
- **Vulnerability:** Printing raw payment card numbers violates PCI DSS compliance and leaks sensitive financial details.
- **Fix:** Sanitize log entries by masking card numbers (e.g., `****-****-****-1234`).

### 7. Passwords Printed in Logs (#13)
- **File:** `src/logger.py`, `src/auth.py`
- **Vulnerability:** Capturing plaintext passwords in log outputs exposes user credentials across logging infrastructure.
- **Fix:** Redact password fields in logger functions and middleware.

### 8. Host Header Injection / Wildcard ALLOWED_HOSTS (#14)
- **File:** `src/config.py`
- **Vulnerability:** Setting `ALLOWED_HOSTS = ["*"]` opens the app to host header injection attacks.
- **Fix:** Restrict allowed hostnames to specific domain names.

### 9. Production Debug Mode Enabled (#15)
- **File:** `src/config.py`
- **Vulnerability:** Enabled `DEBUG` mode exposes detailed error traces, internal system paths, and environment settings.
- **Fix:** Set `DEBUG = False` for production configurations.
