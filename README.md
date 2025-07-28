# 📚 DocWeaver 1B — Persona-Driven Document Intelligence

## ✅ Overview

DocWeaver 1B extracts and ranks the most **relevant sections** and **subsections** from a collection of documents based on a specific **persona** and their **job-to-be-done**. It’s built for the “Connecting the Dots” Challenge and designed to work efficiently within resource and runtime constraints.

---

## 🔧 Directory Structure

```
.
├── app/
│   ├── outline_extractor/
│   └── persona_ranker/
├── input/
│   ├── persona_task.json         ← Your persona & task description
│   └── (Your PDF files go here)
├── output/
│   └── output.json               ← Will be generated here
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🛠️ What It Does

- 📂 Accepts **3–10 related PDFs** placed in the `/input` folder.
- 📄 Requires `persona_task.json` inside `/input` with persona and job details.
- 👤 Takes a defined **persona** and **job description**.
- 🧠 Understands semantic intent using a lightweight sentence embedding model.
- 📈 Ranks and extracts sections/subsections by relevance.
- 📤 Outputs a structured `output.json` in `/output`, ready for Round 2 integration.

---

## 📄 Input & Output Format

### ➤ Input

- Place 3–10 PDFs in the `/input` directory.
- Also include `persona_task.json` with the following format:

```json
{
  "persona": "Undergraduate Computer Science Student",
  "job": "Identify important concepts, definitions, and exam-relevant sections from cloud computing textbooks"
}
```

### ➤ Output (`/output/output.json`)
Sample output:

```json
{
  "metadata": {
    "input_documents": [
      "module-1.pdf",
      "module-2.pdf"
    ],
    "persona": "Undergraduate Computer Science Student",
    "job": "Identify important concepts, definitions, and exam-relevant sections from cloud computing textbooks",
    "processing_timestamp": "2025-07-28T13:29:51Z"
  },
  "extracted_sections": [
    {
      "document": "module-1.pdf",
      "page": 33,
      "section_title": "5. Cloud computing programming and application development",
      "importance_rank": 1,
      "subsections": [
        {
          "text": "5. Cloud computing programming and application development",
          "page": 33
        }
      ]
    }
  ]
}
```

---

## 🧰 Requirements

Your system should have:

- Docker with support for AMD64 architecture  
- No GPU required  
- Memory: ≤ 16GB RAM  
- CPU-only execution  

---

## 📦 Dependencies (from `requirements.txt`)

| Library                   | Purpose                              |
|---------------------------|--------------------------------------|
| `pdfplumber==0.11.0`      | Extracts text from PDFs              |
| `sentence-transformers==2.2.2` | Computes semantic embeddings  |
| `transformers==4.30.2`    | Model backend support                |
| `huggingface-hub==0.14.1` | Handles model caching                |
| `scikit-learn==1.4.0`     | Vector scoring and ranking           |
| `numpy==1.26.0`           | Numerical operations                 |

---

## 🚀 How to Build and Run

> 📍 Ensure Docker is running. First build the image, then run it.

### 🔨 Step 1: Build the Docker Image (Only Once)

```bash
docker build --platform linux/amd64 -t docweaver-1b:latest .
```

### 🔵 Step 2: Run with Internet (First Time Only)

```bash
docker run --rm -v="D:\Adobe India Hackathon\DocWeaver-1B\input:/app/input" -v="D:\Adobe India Hackathon\DocWeaver-1B\output:/app/output" docweaver-1b:latest
```

✅ This allows the model to download once (cached inside Docker image under `/root/.cache`).

### 🔒 Step 3: Run Offline (After First Download)

```bash
docker run --rm -v="D:\Adobe India Hackathon\DocWeaver-1B\input:/app/input" -v="D:\Adobe India Hackathon\DocWeaver-1B\output:/app/output" --network none docweaver-1b:latest
```

---

## 🧠 Approach

### Text Extraction  
Using `pdfplumber`, all text is extracted page-wise from the PDF files.

### Semantic Embedding  
The combined persona and job prompt is converted into a vector using `sentence-transformers`.  
Each heading/subsection from the documents is also embedded.

### Relevance Scoring  
Cosine similarity is used to compute relevance between document sections and the persona-job vector.

### Ranking & Selection  
Top-k sections and their key subsections are selected and assigned an `importance_rank`.

### Output Generation  
A structured JSON containing document names, page numbers, sections, and subsections is generated in `/output/output.json`.

---

## 📌 Important Notes

- 🟢 Internet is needed only once (to download the embedding model inside the container).
- ❌ No hardcoding, no file-specific logic used.
- 🔁 Generalizes across domains like education, research, finance, etc.
- 📦 Model size is under **200MB** and meets all CPU and memory constraints.

---

## 👤 Author / Team

**Team Name**: DocWeaver  
**Hackathon**: Adobe India - Connecting the Dots Challenge  
**Team Members**: Shivam Kumar Singh & Rohit Kumar
