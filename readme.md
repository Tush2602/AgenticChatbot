# 🤖 AgenticChatbot — Stateful Agentic AI System

A full end-to-end **Agentic AI application** built using **LangGraph + LangChain + Streamlit**.

This project demonstrates how to design **stateful AI agents** capable of reasoning, tool usage, and structured workflows instead of simple prompt-response chatbots.

---

## 🚀 Live Capabilities

- ✅ Basic Conversational Chatbot  
- ✅ Web-enabled AI Agent with Tool Usage  
- ✅ AI News Intelligence Digest (Daily / Weekly / Monthly)  
- ✅ Stateful Graph-based Agent Architecture  
- ✅ Reader-friendly News Summaries with Clickable Sources  

---

## 🧠 Project Overview

Traditional chatbots respond statically.

**AgenticChatbot** introduces:

- Stateful execution  
- Multi-node reasoning  
- Tool calling  
- Conditional routing  
- Real-world data integration  

Built using **LangGraph**, the system models AI workflows as execution graphs.

---

## 🏗️ Architecture Flow

```
User Input
   ↓
Streamlit UI
   ↓
Graph Builder (LangGraph)
   ↓
StateGraph Execution
   ├── Basic Chatbot Node
   ├── Chatbot + Tools Node
   └── AI News Agent
   ↓
LLM + Tools
   ↓
Formatted Output
```

---

## ✨ Features

### 💬 Basic Chatbot
- LLM-powered conversational assistant  
- Modular node architecture  
- Easily extensible  

---

### 🌐 Chatbot With Web Access
- Tavily Search integration  
- Dynamic tool invocation  
- Conditional graph routing  
- Real-time information retrieval  

---

### 📰 AI News Intelligence Agent

Generates professional AI news digests:

- Daily / Weekly / Monthly summaries  
- Chronological date-wise arrangement  
- Insight-based summaries (not headline dumping)  
- Duplicate news removal  
- Strategic trend analysis  
- Clickable article links  

### Example Output

```
🧠 Weekly AI News Summary

📅 27 Feb 2026
• India accelerates semiconductor investments strengthening AI ecosystem.  
  [Read more](URL)

📅 26 Feb 2026
• Companies shift toward AI-first workforce transformation.  
  [Read more](URL)

🔎 Overall Trend
India is transitioning from AI experimentation to large-scale deployment.
```

---

## 🧩 Tech Stack

| Technology | Purpose |
|------------|----------|
| LangGraph | Stateful agent orchestration |
| LangChain | Prompt & LLM integration |
| Streamlit | Interactive UI |
| Groq LLM | Fast inference |
| Tavily API | Web search & news retrieval |
| Python | Core implementation |

---

## 📁 Project Structure

```
AgenticChatbot/
│
├── AINews/
│   ├── monthly_summary.md
│   └── weekly_summary.md
│
├── src/
│   └── langgraphagenticai/
│       │
│       ├── graph/
│       │   ├── __init__.py
│       │   └── graph_builder.py
│       │
│       ├── LLMS/
│       │   ├── __init__.py
│       │   └── groqllm.py
│       │
│       ├── nodes/
│       │   ├── __init__.py
│       │   ├── ai_news_node.py
│       │   ├── basic_chatbot_node.py
│       │   └── chatbot_with_tool_node.py
│       │
│       ├── state/
│       │   ├── __init__.py
│       │   └── state.py
│       │
│       ├── tools/
│       │   ├── __init__.py
│       │   └── search_tool.py
│       │
│       ├── ui/
│       │   ├── streamlitui/
│       │   │   ├── __init__.py
│       │   │   ├── display_result.py
│       │   │   ├── loadui.py
│       │   ├── uiconfigfile.ini
│       │   ├── uiconfigfile.py
│       │   ├── main.py
│       │   ├── __init__.py
│
├── .env
├── .gitignore
├── app.py
├── readme.md
└── requirements.txt
└── venv
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Tush2602/AgenticChatbot.git
cd AgenticChatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

You will need:

- Groq API Key  
- Tavily API Key  

The application UI allows entering keys securely via the sidebar.

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🧠 Agent Workflows

### Basic Chatbot
```
START → Chatbot → END
```

### Chatbot With Tools
```
START → Chatbot
           ↓
      Tool Condition
        ↙         ↘
     Tools         END
        ↓
     Chatbot
```

### AI News Agent
```
Fetch News → Summarize → Save Result → END
```

---

## 🧪 Learning Outcomes

This project demonstrates:

- Agentic AI Design  
- Stateful Graph Execution  
- Tool-Calling Agents  
- Prompt Engineering  
- Production Debugging  
- Streamlit + LLM Integration  
- Real-world AI Application Development  

---

## 🎯 Use Cases

- AI Research Assistant  
- Automated News Digest  
- Intelligent Chat Systems  
- Multi-tool AI Agents  
- Portfolio Demonstration Project  

---

## 🔮 Future Improvements

- Memory persistence  
- Autonomous scheduled agents  
- Email / Telegram newsletter delivery  
- Article preview inside app  
- Cloud deployment  

---

## 👨‍💻 Author

**Tushar Joshi**  
B.Tech Electrical Engineering — PEC Chandigarh  
Aspiring Data Scientist & AI Engineer  

GitHub: https://github.com/Tush2602  

---

## ⭐ Support

If you found this project useful:

- ⭐ Star the repository  
- 🍴 Fork and build your own agents  

---

## 🧠 Built With Passion for Agentic AI