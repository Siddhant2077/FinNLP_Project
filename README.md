  
**📊 FinNLP: AI-Powered Financial Sentiment Analysis**  
**FinNLP** is a full-stack microservice application designed to bridge the gap between financial news and actionable market insights. By leveraging **FinBERT** (a specialized NLP model), the system scrapes real-time headlines and provides a sentiment-driven outlook for publicly traded companies.

---

## **🚀 Key Features**

* **Targeted Web Scraping:** Automatically fetches news from official announcement pages and leading financial portals using BeautifulSoup4.  
* **Domain-Specific AI:** Uses **FinBERT**, a Transformer model fine-tuned specifically for financial vocabulary (e.g., understanding that "bullish" is positive).  
* **Microservice Architecture:** Seamless integration between a **Spring Boot** (Java) orchestrator and a **Flask** (Python) AI engine.  
* **Glassmorphism Dashboard:** A modern, interactive frontend featuring animated charts and sentiment cards.  
* **Trend Detection:** Logic-based categorization into *Positive*, *Stable*, or *Negative* outlooks.

---

## **🏗️ System Architecture**

The system operates as a distributed pipeline:

1. **Frontend:** User selects a company (HTML5/JS).  
2. **Orchestrator:** Spring Boot receives the request and triggers the Python AI service via REST.  
3. **Engine:** Python Flask scrapes data, runs inference via HuggingFace, and processes the math.  
4. **Result:** JSON data is sent back for visualization.

Plaintext  
Frontend (JS/Fetch) ↔ Spring Boot (REST) ↔ Python Flask (NLP/Scraper) ↔ FinBERT (Inference)

---

## **🧩 Technology Stack**

| Layer | Technologies |
| :---- | :---- |
| **Frontend** | HTML5, CSS3 (Glassmorphism), JavaScript (ES6+) |
| **Backend** | Java 17+, Spring Boot, Maven |
| **AI/NLP** | Python 3.10, PyTorch, HuggingFace Transformers (FinBERT) |
| **Data** | Pandas, BeautifulSoup4, Requests |

---

## **⚙️ Installation & Setup**

### **1\. Clone the Repository**

Bash  
git clone https://github.com/\<your-username\>/FinNLP.git  
cd FinNLP

### **2\. Python AI Service Setup**

Bash  
cd nlp\_python  
python \-m venv venv  
\# Activate: venv\\Scripts\\activate (Windows) or source venv/bin/activate (Mac/Linux)  
pip install \-r requirements.txt  
python \-m api.app

*Service runs on: http://localhost:5000*

### **3\. Spring Boot Backend Setup**

Bash  
cd ../fintech-backend  
mvn spring-boot:run

*Service runs on: http://localhost:8080*

### **4\. Launch Frontend**

Open frontend/index.html in your preferred browser.

---

## **📊 Sentiment Logic**

The system calculates an **Overall Trend Score** using the following formula:

$$Score \= \\frac{Positive \- Negative}{Total}$$

| Score Range | Market Trend |
| :---- | :---- |
| $Score \> 0.3$ | 📈 **Positive Outlook** |
| $Score \< \-0.3$ | 📉 **Negative Outlook** |
| Otherwise | ⚖️ **Stable Outlook** |

---

## **🧪 Sample API Response**

JSON  
{  
  "company": "Reliance Industries",  
  "positive": 18,  
  "neutral": 22,  
  "negative": 5,  
  "overall\_trend": "Positive Outlook",  
  "headlines\_analyzed": 45  
}

---

## **🔮 Future Scope**

* **Time-Series Analysis:** Tracking sentiment changes over weeks/months.  
* **Stock Correlation:** Overlaying sentiment charts with real-time stock price graphs.  
* **Dockerization:** Deploying the entire stack using Docker Compose.

---

## **👨‍💻 Author**

**Manoj Godh**

*AI / ML & Software Development Enthusiast*

---

## **📜 License**

This project is intended for educational and research purposes under the MIT License.

