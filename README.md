# AI Manufacturing Advisor

An interactive, multimodal Streamlit app that uses CAD files and purchase orders to recommend the most suitable manufacturing method using vision-language AI.

This tool allows users to upload **CAD drawings (DXF/OBJ)** and **purchase order (PO) text**, visualize part geometry, and receive contextual manufacturing process suggestions powered by **LLaVA** via **Ollama**. A built-in chatbot enables follow-up Q&A for exploring design-for-manufacturability (DFM) decisions.

---

## Features

- Upload CAD files (`.dxf`, `.obj`) and auto-generate visual previews
- Upload purchase orders (`.txt`) to provide context
- AI-powered process recommendation (e.g., CNC, 3D printing, laser cutting)
- Streamlit chat interface for interactive follow-up questions
- Powered by [LLaVA-7B](https://llava-vl.github.io/) (multimodal LLM) via [Ollama](https://ollama.com)

---

## Project Structure

```
ai-manufacturing-advisor/
│
├── app.py                      # Main Streamlit interface
├── utils.py                    # LLM prompt + Ollama invocation logic
├── cad_utils/
│   ├── plot_dxf.py             # 2D plotting for DXF files
│   └── plot_obj.py             # 3D plotting for OBJ files
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## Getting Started

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Start Ollama with LLaVA

Make sure you have [Ollama installed](https://ollama.com/download) and the LLaVA model pulled:

```bash
ollama pull llava:7b
ollama run llava:7b
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

---

## Dependencies

- `streamlit`
- `langchain`
- `ollama`
- `ezdxf`
- `matplotlib`
- `plotly`
- `trimesh`

---

## How It Works

1. Upload your CAD file (DXF or OBJ).
2. Upload a purchase order or job spec (TXT).
3. The app previews the CAD file:
   - 2D plot for DXF
   - 3D interactive mesh for OBJ
4. The AI model analyzes both inputs and suggests a manufacturing method.
5. Ask follow-up questions via chat (e.g., “Can I reduce cost by changing the radius?”)

---

## Roadmap

- [ ] Fine-tuning on manufacturing-specific DFM datasets
- [ ] Cost and lead time estimation
- [ ] Support for STEP/STL files
- [ ] API integration with PLM/MRP systems
- [ ] Real-time supplier manufacturability feedback

---

## License

This project is open-source under the [MIT License](LICENSE).

---

## Contributing

Contributions and ideas are welcome! Feel free to fork, suggest new features, or open issues.

---

## Contact

Built with ❤️ by [Anusha Srinivasan](https://github.com/anusha-srinivasan)