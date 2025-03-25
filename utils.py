from langchain.llms import Ollama

def get_llm_response(extension, po_text, image_path, history=None):
    llm = Ollama(model="llava:7b")
    prompt = f"""
    You are an AI manufacturing advisor.
    A {extension.upper()} CAD file has been provided with the following PO details:
    {po_text}

    Recommend the most suitable manufacturing method (e.g., CNC, Laser Cutting, 3D Printing) with reasoning.
    """
    if history:
        for msg in history:
            prompt += f"\n\n{msg['role'].capitalize()}: {msg['content']}"

    return llm.invoke(prompt, image=image_path)
