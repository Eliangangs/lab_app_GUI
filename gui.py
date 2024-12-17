import streamlit as st
import os
import importlib.util
import subprocess

st.title("Лабораторні роботи")

labs_dir = "labs"
lab_dirs = [d for d in os.listdir(labs_dir) if os.path.isdir(os.path.join(labs_dir, d))]

selected_lab = st.selectbox("Оберіть лабораторну роботу:", lab_dirs, key="lab_selector")

if selected_lab:
    lab_path = os.path.join(labs_dir, selected_lab)
    readme_path = os.path.join(lab_path, "README.md")

    lab_file = os.path.join(lab_path, f"{selected_lab}.py")

    if os.path.exists(lab_file):
         spec = importlib.util.spec_from_file_location(selected_lab, lab_file)
         lab_module = importlib.util.module_from_spec(spec)
         spec.loader.exec_module(lab_module)

         if hasattr(lab_module, "run_" + selected_lab):
              if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8") as f:
                    readme_content = f.read()
                st.markdown(readme_content)

              getattr(lab_module, "run_" + selected_lab)()
         else:
             st.error(f"Функція запуску для {selected_lab} не знайдена.")
    else:
        st.error(f"Файл з кодом для {selected_lab} не знайдено.")