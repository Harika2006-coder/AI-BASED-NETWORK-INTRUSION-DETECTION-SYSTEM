# 🛡️ AI-Based Network Intrusion Detection System (NIDS)

This is a **Streamlit web application** that uses **Machine Learning** to detect network intrusions in real time. The system allows users to upload datasets, train a model, and test network traffic for malicious activity—all within a secure, user-friendly dashboard.

---

## 🔹 Features

- **Secure Login/Signup** with JSON-based user authentication.
- **AI Detection**: Train a Random Forest Classifier to detect attacks.
- **Dashboard**:
  - Upload training datasets (`CSV`) with a `label` column.
  - Train model and see **accuracy**.
  - Upload test files to detect attacks.
- **Stats Tracking**:
  - Datasets uploaded
  - Files checked
  - Last detection result
- **Interactive UI** with custom CSS and hover effects.
- **Session Management** using `st.session_state`.

---

## 🛠️ Languages & Tools Used

- **Python** – Backend logic & Machine Learning
- **Streamlit** – Web app framework
- **pandas** – Data manipulation
- **scikit-learn** – Machine Learning models
- **JSON** – User authentication storage
- **CSS** – Custom styling for UI

---

## 📦 Requirements

- Python 3.8+
- Streamlit
- pandas
- scikit-learn

Install dependencies via:

```bash
pip install streamlit pandas scikit-learn
