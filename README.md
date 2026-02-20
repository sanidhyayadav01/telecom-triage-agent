# 📡 Telecom Support Triage Agent (AAI-39)

An **AI-powered End-to-End Telecom Support Triage System** that automatically analyzes customer complaints, extracts key information, and generates intelligent draft responses using Large Language Models (LLMs).

Built with **Python, LangChain, Groq LLM API, and a complete UI layer**, this project simulates a production-style telecom support automation workflow.

---

## 🚀 Project Overview

Telecommunication companies handle thousands of customer support requests daily. Manual triaging causes:

* Slow response times
* Increased operational workload
* Human routing errors
* Poor customer experience

This project introduces an **AI-driven reactive triage agent** that automates the first layer of telecom customer support.

The system now includes:

✅ Backend AI triage engine
✅ Entity extraction pipeline
✅ Automated response generation
✅ Intelligent routing logic
✅ End-to-End User Interface (UI)

---

## 🎯 Problem Statement

**Division:** D8
**Group:** 04D8
**Project No:** AAI-39

Design a production-grade telecom triage agent capable of:

* Real-time intent and urgency classification
* Structured entity extraction
* Context-aware response drafting
* Automated issue routing
* Interactive user interface for support workflows

---

## 🧠 Key Features

✅ Message Classification (Urgency + Intent)
✅ Named Entity Recognition (NER)

* Customer Name
* Phone Number
* Ticket ID
* Dates

✅ AI-generated professional telecom responses
✅ Smart escalation routing
✅ Structured JSON output validation
✅ Modular LangChain pipeline
✅ Environment-secured API usage
✅ End-to-End UI integration

---

## 🖥️ System Architecture

```
User Interface (UI)
        │
        ▼
Customer Message Input
        │
        ▼
┌────────────────────────┐
│  Classification Chain  │
│  (Urgency + Intent)    │
└────────────┬───────────┘
             ▼
┌────────────────────────┐
│  Entity Extraction     │
│  (NER Processing)      │
└────────────┬───────────┘
             ▼
┌────────────────────────┐
│ Response Generator LLM │
│ (Draft Reply Creation) │
└────────────┬───────────┘
             ▼
┌────────────────────────┐
│ Escalation Routing     │
└────────────────────────┘
             ▼
      UI Response Display
```

---

## 🛠️ Tech Stack

### Backend

* Python 3.11+
* LangChain
* Groq LLM API (Llama 3.1)
* dotenv
* Regex-based structured parsing

### Frontend / UI

* Interactive UI layer (chat-style telecom support interface)
* API-driven backend communication

### AI Components

* Prompt Engineering
* LLM Classification
* Named Entity Recognition
* Contextual Response Generation

---

## 📂 Project Structure

```
telecom-triage-agent/
│
├── agents/              # Core triage agent logic
├── chains/              # LangChain pipelines
├── prompts/             # Prompt templates
├── utils/               # Parsing & routing helpers
│
├── ui/                  # Frontend / UI components
│
├── app.py               # Backend entry point
├── config.py            # LLM configuration
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sanidhyayadav01/telecom-triage-agent.git
cd telecom-triage-agent
```

---

### 2️⃣ Install Dependencies

Ensure Python 3.11+ is installed.

```bash
pip install -r requirements.txt
```

(Optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Configure Environment Variables

Create `.env` in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

⚠️ Never commit `.env` to GitHub.

---

### 4️⃣ Run the Application

Start backend:

```bash
python app.py
```

Start UI:

```bash
streamlit run ui/app_ui.py
```

---

## 💻 Example Workflow

**User Input (UI):**

```
My internet has not been working since morning.
Ticket #1234
```

**System Processing:**

```
Urgency: High
Intent: Network Issue
```

**Extracted Entities:**

```json
{
  "ticket_id": "1234",
  "phone_number": "Not Provided",
  "date": "Not Provided"
}
```

**Generated Output:**

* Professional telecom draft response
* Issue routed to Network Support Team
* Displayed directly in UI

---

## 🤖 How It Works

1. User submits a support message via UI.
2. Classification chain determines urgency and intent.
3. NER pipeline extracts structured entities.
4. Output is validated via JSON parser.
5. Response generation chain drafts telecom reply.
6. Routing logic assigns correct support department.
7. Results are rendered back to the UI.

---

## 📸 Demo & Screenshots

(Add screenshots after UI completion)

```
/docs/screenshots/ui-home.png
/docs/screenshots/triage-result.png
```

---

## 🔒 Security Considerations

* API keys secured via `.env`
* `.gitignore` prevents credential exposure
* Structured parsing reduces hallucinated outputs
* Controlled prompt templates

---

## 📈 Future Improvements

* Multi-agent workflow (CrewAI)
* Conversation memory
* Ticket database integration
* Deployment (Docker + Cloud)
* Confidence scoring
* Analytics dashboard

---

## 👨‍💻 Author

**Sanidhya Yadav & Team**
QA / SDET Aspirant | Automation & AI Testing Enthusiast

---

## 🤝 Acknowledgements

Architecture design, debugging guidance, and implementation learning supported through AI-assisted development tools.

---

## 📜 License

Developed for academic and educational purposes.
