# 🧠 Xcerpt
**Xcerpt** is an AI-powered social media assistant that analyzes trending topics and automatically generates high-quality tweet drafts using large language models (LLMs).  
It combines real-time data from **X (Twitter)** and **Google Trends** to help creators, marketers, and brands stay ahead of social conversations.
---
## 🚀 Features
- 🔥 **Trending Topic Discovery**  
  Fetches real-time trending topics from X and Google Trends.
- ✍️ **AI Tweet Generation**  
  Generates tweet drafts using OpenAI’s API based on current trending topics.
- 💬 **Sentiment Analysis**  
  Analyzes tweet replies to categorize audience sentiment (positive, negative, neutral).
- 🧩 **Simple, Clean UI**  
  Built with CustomTkinter for easy login, key management, and content preview.
- 📊 **Data Logging & Analytics (Planned)**  
  Stores performance data to measure engagement and optimize future posts.
---
## 🧱 Project Structure
```
xcerpt/
├── app.py                    # Main entry point
├── README.md
├── requirements.txt
├── .env.example              # Example environment file
│
├── config/                   # Configuration and settings
│   └── settings.py
│
├── data/                     # Cached and generated data
│   ├── logs/
│   └── tweets/
│
├── src/                      # Core application logic
│   ├── api/                  # External APIs (Twitter, Google Trends)
│   ├── ai/                   # LLM + Sentiment modules
│   ├── core/                 # Main orchestration logic
│   ├── ui/                   # Login & interface
│   └── utils/                # Helper utilities
│
└── tests/                    # Test files
```
---
## ⚙️ Installation
### 1. Clone the Repository
```bash
git clone https://github.com/johnh-harris/Xcerpt.git
cd Xcerpt
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables
Copy `.env.example` → `.env` and add your keys:
```
OPENAI_API_KEY=your_openai_api_key_here
```
---
## 🧠 Usage
```bash
python app.py
```
1. Sign in with your X account (OAuth redirect)  
2. Enter your OpenAI API key  
3. Generate trending tweet ideas instantly  
---
## 🧩 Tech Stack
| Component | Technology |
|------------|-------------|
| **Language** | Python 3.10+ |
| **Frameworks** | CustomTkinter, FastAPI (planned) |
| **AI/ML** | OpenAI API, VADER Sentiment |
| **Data Sources** | Twitter/X API, Google Trends |
| **Storage** | JSON-based cache (future DB support) |
---
## 🧾 License
This project is licensed under the [MIT License](LICENSE).  
© 2025 John Harris
---
## ✨ Inspiration
> “AI can’t replace creativity — but it can keep you one step ahead of what everyone’s talking about.”
