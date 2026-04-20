# Enterprise AI Assistant – Agentic RAG-Based System

## Description
The Enterprise AI Assistant is an agentic, retrieval-augmented generation (RAG) system designed to handle enterprise-level queries and workflows. It integrates multiple specialized agents for classification, reasoning, validation, and action planning to provide accurate, context-aware responses and structured task execution.

The system supports both information retrieval from enterprise documents and automated action planning, making it suitable for internal enterprise use cases such as IT service management, HR operations, and developer support.

---

## Key Features

- Multi-agent architecture with dedicated modules for classification, reasoning, validation, and action planning  
- Retrieval-Augmented Generation (RAG) pipeline using FAISS for efficient semantic search  
- Context-grounded responses with source citations  
- Intelligent query classification into factual, analytical, and action-based categories  
- Automated action planning using structured JSON outputs  
- Support for enterprise workflows such as ticket creation, meeting scheduling, and leave requests (mock execution)  
- Interactive dashboard using Streamlit for real-time interaction and traceability  

---

## System Architecture

```
User Query
   ↓
Query Classifier (Intent Detection)
   ↓
 ┌───────────────┬────────────────┐
 │               │                │
Action Path   Retrieval Path   Analytical Path
 │               │                │
Action Planner   FAISS Retriever  Context Processing
 │               │                │
Mock Execution   Reasoning Agent  LLM Reasoning
 │               │                │
Structured Output  Validated Answer with Sources
```

---

## Technology Stack

### Backend and Core Logic
- Python  
- LangChain ecosystem  
- FAISS (Vector Database)  
- Sentence Transformers (Embeddings)  

### AI and LLM Integration
- Groq API (LLaMA models)  
- Retrieval-Augmented Generation (RAG)  
- Multi-agent orchestration  

### Data Processing
- PyPDF for document ingestion  
- Recursive text chunking  

### Frontend
- Streamlit  

---

## Project Structure

```
agents/
  ├── classifier.py
  ├── reasoner.py
  ├── action_planner.py
  ├── validator.py
  └── evidence.py

ingestion/
  ├── load_pdf.py
  ├── chunker.py
  ├── embed_store.py
  └── build_index.py

retrieval/
  └── retriever.py

tools/
  └── actions.py

ui/
  └── streamlit_app.py

app/
  ├── main.py
  └── config.py
```

---

## Workflow

1. User submits a query through the interface  
2. Query is classified into one of three categories:
   - Factual  
   - Analytical  
   - Action  

3. Based on classification:
   - Action queries → processed by action planner  
   - Information queries → processed through RAG pipeline  

4. Retrieval pipeline:
   - Relevant document chunks are retrieved using FAISS  
   - Context is validated and passed to reasoning agent  

5. Response generation:
   - LLM generates answer strictly from context  
   - Sources are appended for traceability  

6. Action execution:
   - Structured JSON output is generated  
   - Actions are simulated (mock execution)  

---

## Setup and Execution

### 1. Install Dependencies
```
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file and add:
```
GROQ_API_KEY=your_api_key
```

### 3. Build Vector Index
```
python ingestion/build_index.py
```

### 4. Run Application
```
streamlit run ui/streamlit_app.py
```

---

## Sample Outputs

### Query Classification
```
Input: "My VPN is not working"
Output: action
```

### Planned Action
```json
{
  "action": "create_it_ticket",
  "issue_type": "VPN Issue",
  "priority": "High",
  "description": "User unable to connect to VPN"
}
```

### RAG-Based Answer
```
Answer generated from document context.

Sources: Page 3, Page 7
```

---

## Known Issues

- Dependence on external LLM APIs introduces latency and availability concerns  
- Action execution is currently mocked and not integrated with real enterprise systems  
- Retrieval quality depends on document chunking and embedding performance  
- Limited support for complex multi-step reasoning workflows  
- No role-based access control or authentication mechanisms  

---

## Future Improvements

- Integration with real enterprise systems such as ServiceNow, Jira, or HRMS  
- Implementation of role-based access control and authentication  
- Enhancement of retrieval quality using hybrid search (keyword and semantic)  
- Support for multi-document and cross-domain reasoning  
- Fine-tuning of models for enterprise-specific datasets  
- Deployment as a scalable microservices architecture  
- Addition of conversational memory for multi-turn interactions  

---

## Use Cases

- IT service desk automation  
- HR workflow management  
- Enterprise document querying and analytics  
- Developer support and knowledge retrieval  
- Internal automation of routine business operations  

---

## Conclusion

The Enterprise AI Assistant demonstrates a structured implementation of agentic AI combined with retrieval-augmented generation to solve real-world enterprise problems. By integrating multiple intelligent components, the system enables both accurate information retrieval and automated decision-making, making it a strong foundation for scalable enterprise AI solutions.
