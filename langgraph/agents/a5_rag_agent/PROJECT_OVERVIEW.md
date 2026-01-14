# PROJECT_OVERVIEW.md

## RAG Agent with LangGraph and ChromaDB

### Overview
This project implements a **Retrieval-Augmented Generation (RAG)** agent that answers questions about Stock Market Performance in 2024 by querying a PDF document. It uses LangGraph for orchestration, ChromaDB for vector storage, and OpenAI for embeddings and LLM capabilities.

---

## Step-by-Step Implementation

### 1. **Setup & Dependencies**
- Loads environment variables (OpenAI API key)
- Initializes OpenAI LLM (`gpt-4o`) with zero temperature for deterministic responses
- Sets up embedding model (`text-embedding-3-small`)

### 2. **Document Loading**
- **File**: `Stock_Market_Performance_2024.pdf`
- Uses `PyPDFLoader` to load the PDF
- Validates file existence and handles errors
- Extracts all pages from the document

### 3. **Text Chunking**
- Uses `RecursiveCharacterTextSplitter` to break documents into manageable pieces
- **Chunk size**: 1000 characters
- **Chunk overlap**: 200 characters (maintains context between chunks)
- Creates smaller, searchable text segments from PDF pages

### 4. **Vector Store Creation**
- **Storage**: ChromaDB (local persistent storage)
- **Directory**: `~/Git/Personal/ai-agents-in-langgraph/langgraph/agents/a5_rag_agent/stock_market_data`
- **Collection name**: `stock_market`
- Converts text chunks into embeddings using OpenAI's embedding model
- Stores embeddings in ChromaDB for similarity search

### 5. **Retriever Setup**
- Creates a retriever from the vector store
- **Search type**: Similarity search
- **Top-K**: Returns 5 most relevant chunks per query

### 6. **Tool Definition**
- **`retriever_tool`**: A LangChain tool that:
  - Accepts a query string
  - Searches the vector store for relevant documents
  - Returns formatted results with document numbers
  - Handles cases where no relevant information is found

### 7. **Agent State Management**
- **`AgentState`**: TypedDict containing:
  - `messages`: Annotated sequence of BaseMessage objects
  - Uses `add_messages` operator for message accumulation

### 8. **Decision Logic**
- **`should_continue`**: Checks if the LLM response contains tool calls
  - Returns `True` → Execute retriever agent
  - Returns `False` → End conversation

### 9. **System Prompt**
Defines the agent's behavior:
- Acts as an AI assistant for stock market questions
- Uses the retriever tool to access knowledge base
- Can make multiple tool calls if needed
- Must cite specific document parts in answers

### 10. **Graph Nodes**

#### **LLM Node** (`call_llm`)
- Prepends system prompt to conversation
- Invokes the LLM with current messages
- Returns LLM response (may include tool calls)

#### **Retriever Agent Node** (`take_action`)
- Extracts tool calls from last message
- Validates tool names against `tools_dict`
- Executes retriever tool with provided query
- Returns ToolMessage results to continue conversation

### 11. **LangGraph Workflow**
```
User Input → LLM Node → Decision
                ↓           ↓
         Tool Calls?    No Tool Calls
                ↓           ↓
        Retriever    →   END
           Agent
             ↓
         Back to LLM (with results)
```

**Flow**:
1. Start at LLM node
2. LLM decides if it needs to retrieve information
3. If yes → Call retriever agent → Return results to LLM
4. If no → End and return final answer

### 12. **Interactive Loop** (`running_agent`)
- Continuously prompts user for questions
- Converts user input to `HumanMessage`
- Invokes the RAG agent graph
- Displays the final answer
- Exits on 'quit' or 'exit' commands

---

## Key Features

✅ **PDF Document Processing**: Loads and chunks PDF content  
✅ **Vector Storage**: Persistent ChromaDB for efficient retrieval  
✅ **Semantic Search**: Returns top 5 relevant chunks per query  
✅ **Tool-Based Architecture**: LLM decides when to use retriever  
✅ **Multi-Turn Conversations**: Supports follow-up questions  
✅ **Citation Support**: Encourages citing specific document parts  
✅ **Error Handling**: Validates tools and handles missing data  

---

## Usage Example

```
What is your question: What were the top performing stocks in Q1 2024?
```

**Agent Flow**:
1. User asks question
2. LLM calls `retriever_tool` with query
3. Retriever searches vector store
4. Returns 5 relevant document chunks
5. LLM synthesizes answer with citations
6. User receives final response

---

## File Structure

```
a5_rag_agent/
├── RAG_Agent.py                    # Main agent implementation
├── Stock_Market_Performance_2024.pdf  # Source document
├── PROJECT_OVERVIEW.md             # This file
└── stock_market_data/             # ChromaDB persistent storage
    └── [vector embeddings]
```

---

## Technologies Used

- **LangGraph**: Agent orchestration and workflow
- **LangChain**: Tools, message handling, document processing
- **ChromaDB**: Vector database for semantic search
- **OpenAI**: GPT-4o (LLM) and text-embedding-3-small (embeddings)
- **PyPDFLoader**: PDF document loading

---

## Key Concepts Explained

### What is RAG (Retrieval-Augmented Generation)?
RAG combines:
1. **Retrieval**: Finding relevant information from a knowledge base
2. **Generation**: Using an LLM to generate answers based on retrieved context

This approach grounds LLM responses in actual documents, reducing hallucinations.

### Why Vector Embeddings?
- Text is converted to numerical vectors (embeddings)
- Similar concepts have similar vector representations
- Enables semantic search (meaning-based) vs keyword search

### Why ChromaDB?
- Lightweight, persistent vector database
- Easy integration with LangChain
- Efficient similarity search for RAG applications

---

## How to Run

1. Ensure OpenAI API key is set in `.env` file
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python RAG_Agent.py`
4. Ask questions about stock market performance
5. Type 'quit' or 'exit' to stop

