# 🎥 AI Video Assistant with RAG

An end-to-end Python tool that turns any YouTube video or audio/video file into a fully searchable, chat-ready meeting assistant — transcription, summarization, action-item extraction, and RAG-based Q&A, all in one Streamlit app.

## ✅ Features

- 📥 Accepts any **YouTube URL** or local **audio/video file** as input
- 🗣️ Transcribes **English** meetings using **local Whisper AI** (free, offline)
- 🇮🇳 Transcribes **Hindi & Hinglish** meetings using **Sarvam AI**
- 📝 Summarizes the full meeting into clear **bullet points**
- ✅ Extracts **action items** with owner and deadline
- 📌 Extracts **key decisions** made during the meeting
- ❓ Extracts **open questions** and follow-ups
- 💬 Lets you **chat with your meeting** using RAG + ChromaDB
- 📄 **Exports** the full report as **PDF** or **TXT**

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| Language | Python |
| Transcription (English) | OpenAI Whisper (local, free) |
| Transcription (Hindi/Hinglish) | Sarvam AI |
| Pipeline Orchestration | LangChain (LCEL) |
| LLM | Mistral AI (free API) |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace Embeddings (local, free) |
| UI | Streamlit |

## 📁 Project Structure

```
├── assets                        # Screenshots of the output
├── core/
│   └── extractor.py              # Extracts action items, decisions & questions
│   └── rag_engine.py             # Retrieval-Augmented Generation workflow
│   └── summarize.py              # Structured transcript summarization (LangChain + Mistral)
│   └── transcriber.py            # Speech-to-text transcript generation
│   └── vector_store.py           # Creates embeddings & stores vectors (ChromaDB)
├── utils/
│   └── audio_processor.py    # Extracts & optimizes audio from 
├── .env                      # API keys & config (Mistral, Sarvam, etc.)
├── .gitignore                # Files/folders excluded from Git (env, venv, media, cache, etc.)
├── app.py                    # Streamlit UI (chat with your meeting)
├── README.md
└── requirements.txt          # Project dependencies

```

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd AI-Video-Assistant-With-RAG
   ```

2. **Create and activate a virtual environment**
   ```bash
   uv venv
   On Windows: .venv\Scripts\activate 
   ```

3. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root with your API keys:
   ```env
   MISTRAL_API_KEY=your_mistral_api_key
   WHISPER_MODEL=""
   SARVAM_API_KEY=your_sarvam_api_key
   SARVAM_MODEL=""
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

## 🚀 Usage

1. Launch the Streamlit app.
2. Paste a YouTube URL or upload an audio/video file.
3. Choose the transcription mode (English via Whisper, or Hindi/Hinglish via Sarvam AI).
4. Let the pipeline transcribe, summarize, and extract action items, decisions, and open questions.
5. Chat with your meeting using the built-in RAG-powered assistant.
6. Export the final report as PDF or TXT.

## 🧩 How It Works (Pipeline)

```
YouTube URL / Audio-Video File
        ↓
  Audio Extraction & Optimization  (audio_processor.py)
        ↓
  Transcription (Whisper / Sarvam AI)  (transcriber.py)
        ↓
  Summarization (LangChain + Mistral)  (summarise.py)
        ↓
  Extraction: Action Items / Decisions / Questions  (extractor.py)
        ↓
  Embeddings + Vector Store  (vector_store.py)
        ↓
  RAG Engine (Chat with Meeting)  (rag_engine.py)
        ↓
  Streamlit UI + PDF/TXT Export
```
