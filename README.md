# DocWeaver-1B

**Persona-driven Document Intelligence.**

## 🚀 How to Run

1. **Put your PDFs and `persona_task.json` into `input/`**
2. **Build:**
3. **Run:**
4. **Results:** Output at `output/output.json`, matches required schema.

## 📝 Input Example

`input/persona_task.json`:

## 💡 Approach

- Extracts outline/sections (from Round 1A).
- Ranks sections by semantic match to persona+job using MiniLM (~90MB).
- Outputs JSON as per challenge requirements, all CPU/offline.
