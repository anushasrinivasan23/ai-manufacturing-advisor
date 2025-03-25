import streamlit as st
from llm_utils import get_llm_response
from cad_utils.plot_dxf import plot_dxf_2d
from cad_utils.plot_obj import plot_obj_3d
import tempfile
import os

st.cache_resource.clear()
st.title("AI Manufacturing Advisor")

file = st.file_uploader("Upload your CAD file (DXF or OBJ)", type=["dxf", "obj"])
uploaded_po = st.file_uploader("Upload your PO (Purchase Order) as a .txt file", type=["txt"])

po_text = uploaded_po.read().decode("utf-8") if uploaded_po else ""

if file:
    extension = file.name.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{extension}") as temp_file:
        temp_file.write(file.read())
        temp_path = temp_file.name

    preview_path = None
    if extension == 'dxf':
        preview_path = plot_dxf_2d(temp_path)
        st.image(preview_path, caption="2D Preview", use_container_width=True)
    elif extension == 'obj':
        fig = plot_obj_3d(temp_path)
        st.plotly_chart(fig, use_container_width=True)

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    if len(st.session_state.chat_history) == 0:
        result = get_llm_response(extension, po_text, preview_path or temp_path)
        st.session_state.chat_history.append({"role": "assistant", "content": result})

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_query = st.chat_input("Ask follow-up questions about this part")
    if user_query:
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        result = get_llm_response(extension, po_text, preview_path or temp_path, st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "assistant", "content": result})
        st.rerun()

    os.remove(temp_path)
    if preview_path and extension == 'dxf':
        os.remove(preview_path)
