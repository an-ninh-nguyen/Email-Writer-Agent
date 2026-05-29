# GenAI Email Writer Chatbot

An AI-powered writing assistant for ESL college students, built with a fine-tuned GPT-4o-mini model and a RAG pipeline using ChromaDB. Helps users write polite, professional academic emails, essays, and personal statements through a Gradio chat interface.

---

## Features

- **Fine-tuned model** — GPT-4o-mini fine-tuned on curated academic writing examples for ESL learners
- **RAG pipeline** — 20 domain-specific writing rules embedded in a ChromaDB vector store for context-aware responses
- **Gradio interface** — simple, browser-based chat UI requiring no frontend setup
- **Prompt engineering** — dynamic system prompts combine fine-tuning, RAG retrieval, and role instructions for higher quality outputs

---

## Tech Stack

- Python
- OpenAI API (GPT-4o-mini fine-tuning)
- ChromaDB (vector store)
- Gradio (chat interface)
- python-dotenv

---

## Project Structure

```
genai-email-writer/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
│   ├── facts.txt                   # 20 writing rules embedded in ChromaDB
│   └── fine_tuning_facts.jsonl     # Training data for fine-tuning
│
└── src/
    ├── 1_upload_and_finetune.py    # Upload training data and start fine-tune job
    ├── 2_check_finetune_status.py  # Check fine-tune job status and retrieve model ID
    └── 3_chatbot.py                # Launch the Gradio chatbot with RAG
```

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/an-ninh-nguyen/Email-Writer-Agent.git
cd Email-Writer-Agent
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
```
Fill in your `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
FINETUNE_JOB_ID=your_finetune_job_id_here
FINETUNED_MODEL_ID=your_finetuned_model_id_here
```

---

## Usage

Run the scripts in order:

**Step 1 — Upload training data and start fine-tuning:**
```bash
python src/1_upload_and_finetune.py
```

**Step 2 — Check fine-tune job status:**
```bash
python src/2_check_finetune_status.py
```
Wait until status shows `succeeded` and copy the model ID into your `.env`.

**Step 3 — Launch the chatbot:**
```bash
python src/3_chatbot.py
```
Open the local Gradio URL in your browser and start chatting.

---

## Example Prompts

- *"How do I email my professor to ask for an extension?"*
- *"Can you help me write an opening sentence for my scholarship essay?"*
- *"What's a polite way to follow up on a recommendation letter?"*

---

## Author

**An Nguyen** — [LinkedIn](https://linkedin.com/in/an-ninh-nguyen) · [GitHub](https://github.com/an-ninh-nguyen)
