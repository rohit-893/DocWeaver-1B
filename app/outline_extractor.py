import pdfplumber

def extract_sections(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        sections = []
        for page in pdf.pages:
            lines = page.extract_text_lines()
            for line in lines:
                text = line["text"].strip()
                # Simple rule: headings are ALL CAPS or start with digit(s)
                if text.isupper() or (text and text[0].isdigit()):
                    sections.append({
                        "section_title": text,
                        "page": page.page_number,
                        "section_text": text  # For demo, you may extract whole chunk or page
                    })
        return sections
