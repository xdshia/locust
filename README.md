# 🔥 Locust Performance Testing Script

This repository contains a sample **Locust** script that simulates user traffic for a fictional website. It's designed for performance testing with HTTP GET and POST requests.

## 🚀 Features

- Simulates multiple users
- GET requests for pages like `/` and `/about`
- POST request to `/submit` with JSON data
- Adjustable wait times between requests

---

## 📦 Requirements

- Python 3.7+
- Locust

Install Locust using pip:

```bash
pip install locust

```
🧪 Running the Test
Run Locust with your target host:

```bash
locust -f locustfile.py --host https://example.com
```
Then open http://localhost:8089 in your browser to start the test and monitor performance.
