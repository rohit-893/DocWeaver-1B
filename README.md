# DocWeaver-1B

**Persona-Driven Document Intelligence**  
_A modular, offline, and Dockerized solution for Adobe Hackathon Round 1B_

## 🚀 Overview

This project **automatically extracts and ranks the most relevant sections from a collection of PDFs**, tailored to a specific persona and job-to-be-done statement.

- **Input:** Multiple PDFs and a persona/job definition (`persona_task.json`)
- **Output:** Ranked, contextual document sections in structured JSON
- **Features:**
    - Fast, fully offline (no runtime internet)
    - CPU-only, under 1GB model size, Dockerized
    - Modular (outline extraction + persona-aware ranking)
    - Output matches competition schema

## 📦 Project Structure

```
docweaver-1b/
├── app/
│   ├── outline_extractor.py    # Section extraction logic
│   ├── persona_ranker.py       # Main persona-driven ranking script
├── Dockerfile
├── requirements.txt
├── README.md                  # (You are here)
├── approach_explanation.md    # Details methodology (for submission)
├── input/                     # Place PDFs + persona_task.json here
└── output/                    # output.json will be created here
```

## 🛠️ How to Run

### 1. Prepare Inputs
- Put all target PDFs and a `persona_task.json` file inside the `input/` directory.  
  Example `persona_task.json`:
  ```json
  {
    "persona": "Investment Analyst",
    "job": "Analyze revenue trends and R&D investments"
  }
  ```

### 2. Build the Docker Image

```sh
docker build --platform=linux/amd64 -t docweaver-1b:latest .
```

### 3. Run the Container

```sh
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  docweaver-1b:latest
```

### 4. Check the Results

- Output will be available at: `output/output.json`  
  This JSON matches the required competition schema.

## 🧠 Approach Summary

- **Section Extraction**: Each PDF is chunked into heading-based candidate sections (see `outline_extractor.py`), using simple heuristics.
- **Semantic Ranking**: Both sections and the persona/task description are embedded using a light language model (MiniLM). Relevance to the user profile is measured by cosine similarity.
- **Output Construction**: The top-ranked sections with metadata are written to output JSON as required.

> All processing is **fully offline/CPU-only** and efficient (≤1GB model, ≤60s on 3–10 PDFs).

## 📑 Dependencies

Installed automatically by Docker:
- Python 3.10+
- pdfplumber
- sentence-transformers (MiniLM)
- numpy
- scikit-learn

## 👥 Authors

- Rohit Kumar & Shivam Kumar Singh
- Submission for **Adobe India Hackathon 2025**

## 📝 Notes

- For submission, keep your repo private until instructed.
- Improve heading detection, chunking, or add multilingual support for bonus points.
- For questions, contact the team or raise an issue.
