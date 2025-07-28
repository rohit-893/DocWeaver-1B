import os, json, time
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from outline_extractor import extract_sections

def rank_sections(pdfs, persona, job, top_k=5):
    model = SentenceTransformer("all-MiniLM-L6-v2")  # ~90MB fits <1GB
    query = f"{persona} ||| {job}"
    query_vec = model.encode([query])
    ranked = []
    for pdf_path in pdfs:
        docname = os.path.basename(pdf_path)
        outline = extract_sections(pdf_path)
        for section in outline:
            text = section["section_text"]
            sec_vec = model.encode([text])
            sim = cosine_similarity(query_vec, sec_vec)[0][0]
            ranked.append({
                "document": docname,
                "page": section["page"],
                "section_title": section["section_title"],
                "section_text": text,
                "score": sim
            })
    ranked_sections = sorted(ranked, key=lambda x: -x['score'])[:top_k * len(pdfs)]
    for i, sec in enumerate(ranked_sections):
        sec["importance_rank"] = i + 1
    return ranked_sections

def main():
    with open("/app/input/persona_task.json", "r") as f:
        meta = json.load(f)
    persona, job = meta["persona"], meta["job"]
    pdfs = [os.path.join("/app/input", f) for f in os.listdir("/app/input") if f.lower().endswith(".pdf")]
    ranked_sections = rank_sections(pdfs, persona, job)
    output = {
        "metadata": {
            "input_documents": [os.path.basename(x) for x in pdfs],
            "persona": persona,
            "job": job,
            "processing_timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        },
        "extracted_sections": []
    }
    for section in ranked_sections:
        output["extracted_sections"].append({
            "document": section["document"],
            "page": section["page"],
            "section_title": section["section_title"],
            "importance_rank": section["importance_rank"],
            "subsections": [
                {"text": section["section_text"], "page": section["page"]}
            ]
        })
    os.makedirs("/app/output", exist_ok=True)
    with open("/app/output/output.json", "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
