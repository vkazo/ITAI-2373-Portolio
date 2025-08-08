
# 🚀 Deployment Guide for NewsBot 2.0

This guide walks you through the steps to deploy the NewsBot Intelligence System 2.0 in a local or cloud-based environment.

---

## 🧰 Prerequisites

- Python 3.8 or above
- Git
- pip or conda
- API keys (saved in `config/api_keys_template.txt`)
- Jupyter Notebook or Colab
- (Optional) Docker for containerized deployment

---

## 📦 Installation Steps

1. **Clone the Repository**

```bash
git clone https://github.com/vkazo/ITAI2373-NewsBot-Final.git
cd ITAI2373-NewsBot-Final
```

2. **Create a Virtual Environment (optional but recommended)**

```bash
python -m venv newsbot_env
source newsbot_env/bin/activate  # On Windows: newsbot_env\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Set Up Configuration**

Rename `config/api_keys_template.txt` to `api_keys.txt` and insert your API keys as needed.

---

## 💻 Running the Application

To run the notebooks:

```bash
jupyter notebook
# Then open any notebook inside /notebooks
```

To run the modules from Python scripts:

```bash
python src/main.py
```

(Adjust as needed depending on your script structure)

---

## ☁️ Optional: Docker Deployment

1. **Build Docker Image**

```bash
docker build -t newsbot:latest .
```

2. **Run the Container**

```bash
docker run -p 8000:8000 newsbot:latest
```

3. **Access Application**

Go to `http://localhost:8000`

---

## 🔧 Configuration Options

Edit `config/settings.py` to change:
- Model paths
- Language preferences
- Logging/debug settings

---

## 🧪 Testing

```bash
pytest tests/
```

---

## ✅ Final Checklist

- [ ] All modules run without error
- [ ] Jupyter notebooks render visualizations
- [ ] API keys are securely stored
- [ ] Project structure matches README.md

---

For any issues, contact Professor McManus or post on the class discussion board.
