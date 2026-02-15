# 📡 Telecom Support Triage Agent (AAI-39)

A production-style **AI-powered Telecom Support Triage Agent** built using Python, LangChain, and a Large Language Model (LLM) API.  
The system automates initial telecom customer support workflows by classifying incoming messages, extracting important entities, and generating contextual draft responses.

---

## 🚀 Project Overview

Telecommunication companies receive thousands of customer support messages daily.  
Manual triaging slows down response time and increases operational workload.

This project implements an **AI-driven reactive triage agent** that:

- Classifies customer messages by **urgency** and **intent**
- Extracts critical information using **Named Entity Recognition (NER)**
- Automatically generates professional **draft responses**
- Routes issues to appropriate internal support teams

The agent runs directly in the **terminal** and communicates with an LLM API without requiring a browser interface.

---

## 🎯 Problem Statement

**Division:** D8  
**Group:** 04D8  
**Project No:** AAI-39  

Create a production-grade reactive triage agent for telecom communications that:

- Performs real-time classification of incoming messages
- Extracts structured entities such as IDs and dates
- Generates context-aware draft replies
- Accelerates customer issue resolution workflows

---

## 🧠 Key Features

✅ Real-time message classification (Urgency + Intent)  
✅ Named Entity Recognition (Customer ID, Phone Number, Ticket ID, Date)  
✅ Automated draft response generation  
✅ Intelligent escalation routing  
✅ Structured JSON output parsing  
✅ Terminal-based interaction (no browser required)  
✅ Modular and production-like architecture  

---

## 🏗️ System Architecture

```
Customer Message
        │
        ▼
┌────────────────────┐
│  Classification LLM │
│ (Urgency + Intent)  │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│   NER Extraction    │
│  (Entity Parsing)   │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Response Generator  │
│   (Draft Reply)     │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Escalation Routing  │
└────────────────────┘
```

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **LangChain**
- **Groq LLM API (Llama 3.1 models)**
- dotenv (environment management)
- Regex-based structured parsing

---

## 📂 Project Structure

```
telecom-triage-agent/
│
├── agents/            # Main triage agent logic
├── chains/            # LangChain workflows
├── prompts/           # LLM prompt templates
├── utils/             # Parser, formatter, routing logic
│
├── app.py             # Terminal entry point
├── config.py          # LLM configuration
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

Make sure Python 3.11 or later is installed.

```bash
pip install -r requirements.txt
```

*(Optional: You may use a virtual environment if preferred, but it is not required.)*

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

⚠️ Never upload `.env` to GitHub.

---

### 4️⃣ Run the Agent

```bash
python app.py
```

---

## 💻 Example Usage

```
Customer Message > my internet is not working since morning
```

Output:

```
Urgency: high
Intent: network_issue

Routed To:
🌐 Network Support Team

Entities:
{
  'customer_id': 'Not Provided',
  'phone_number': 'Not Provided',
  'ticket_id': 'Not Provided',
  'date': 'Not Provided'
}
```

---

## 🤖 How It Works

1. User enters a telecom support message.
2. LLM classifies urgency and intent.
3. NER module extracts structured entities.
4. Output is cleaned using a JSON parser.
5. System generates a professional draft reply.
6. Ticket is routed to the appropriate department.

---

## 🔒 Security Considerations

- API keys stored using `.env`
- `.env` excluded via `.gitignore`
- Structured output validation prevents malformed responses

---

## 📈 Future Improvements (Optional)

- Multi-agent CrewAI workflow
- Conversation memory
- Ticket database integration
- Web dashboard interface
- Confidence scoring system

---

## 👨‍💻 Author

**Sanidhya Yadav and Team**

QA & Software Engineering Student

---

## 🤝 Acknowledgements

This project was developed with implementation guidance and technical assistance from AI tools (ChatGPT) for learning, architecture design, and debugging support.

---

## 📜 License

This project is developed for academic and educational purposes.