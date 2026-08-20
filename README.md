# MIC-AI-Recruiter

**MIC-AI-Recruiter** is a command-line AI-powered resume analysis system that uses a local LLM, structured skill extraction, embeddings, and vector search to evaluate candidates.
> **Note:** This project is currently **CLI-based** and does **not** include a graphical user interface (GUI) or UI/UX layer.


## Overview
The system takes a candidate's resume as text and:
- Extracts skills, technologies, and programming languages.
- Retrieves semantically similar resume examples from a vector database.
- Uses **Llama 3.2** to analyse the candidate.
- Generates strengths, weaknesses, missing skills, suitability score, and recommendations.


## Architecture

```text
Candidate Resume
       │
       ▼
Skill Extraction
       │
       ▼
Resume Embeddings
       │
       ▼
ChromaDB Vector Search
       │
       ▼
Relevant Resume Context
       │
       ▼
Llama 3.2
       │
       ▼
Candidate Evaluation
```


## Tech Stack
- **Python** — Core application
- **Llama 3.2** — Local language model
- **Ollama** — Local LLM inference
- **LangChain** — LLM orchestration
- **Pydantic** — Structured skill extraction
- **Nomic Embed Text** — Embeddings
- **ChromaDB** — Vector database
- **Pandas** — Dataset processing


## Features
- Structured resume skill extraction
- Technology and programming-language identification
- Semantic resume retrieval
- Local LLM inference
- Retrieval-Augmented Generation (RAG)
- Candidate strengths and weaknesses analysis
- Missing-skill identification
- Suitability scoring
- Recruitment recommendations


## Installation


### Prerequisites
- Python 3.x
- [Ollama](https://ollama.com/)
- Llama 3.2
- Nomic Embed Text


### Setup
```bash
git clone https://github.com/nakshatra-s08/MIC-AI-Recruiter.git
cd MIC-AI-Recruiter

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

ollama pull llama3.2
ollama pull nomic-embed-text
```


## Usage
Run the application from the terminal:

```bash
python main.py
```

Enter a candidate's resume when prompted:

```text
Enter the candidate's resume (or type 'exit' to quit):
```

The system returns the extracted skills followed by an AI-generated candidate evaluation.

Type `exit` to terminate the application.


## Project Structure

```text
MIC-AI-Recruiter/
├── main.py
├── skill_extractor.py
├── vector.py
├── extracted_data.csv
├── chroma_langchain_db/
├── requirements.txt
└── README.md
```


## Project Status

**Active Development**
The current version focuses on the core AI pipeline and is intentionally implemented as a **command-line application**. A dedicated UI/UX interface is not currently part of the project.
Future development may include resume file parsing, job-description matching, candidate ranking, skill-gap analysis, and a user interface.


## Author
**Nakshatra Sharma**

[GitHub](https://github.com/nakshatra-s08)
