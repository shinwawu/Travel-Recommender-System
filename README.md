# ✈️ Brazil Travel Recommendation System

## 📌 Project Overview
An End-to-End Machine Learning project that recommends hotels in **São Paulo**, **Rio de Janeiro**, and **Curitiba**. It utilizes **Content-Based Filtering (TF-IDF)** and **Cosine Similarity** to match users with hotels based on amenities, location, and description.

The system is built with **FastAPI** for high-performance inference, utilizes **uv** for blazing fast dependency management, and features a responsive **HTML/JS** frontend.

## 🏗️ Architecture
- **ML Engine:** Scikit-Learn (TF-IDF Vectorization) maps hotel descriptions into high-dimensional vectors for similarity search.
- **Backend:** FastAPI service exposing REST endpoints for recommendations.
- **Tooling:** Managed with **uv** for reproducible environments and instant package resolution.

## 🔧 Tech Stack
- **Language:** Python 3.12
- **Package Manager:** [uv](https://github.com/astral-sh/uv) (Modern, high-performance replacement for pip)
- **Framework:** FastAPI & Uvicorn
- **ML/Libraries:** Scikit-Learn, Pandas, Numpy

## 🚀 How to Run

### 1. Prerequisites
Ensure you have `uv` installed.
```bash
# On macOS/Linux
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh

# On Windows (PowerShell)
powershell -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"

## 2. Run
uv uvicorn app.main:app --reload

## 3. Open the html page index.html