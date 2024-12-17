import streamlit as st
import os
import importlib.util
import subprocess

st.title("Лабораторні роботи")

labs_dir = "labs"
lab_dirs = [d for d in os.listdir(labs_dir) if os.path.isdir(os.path.join(labs_dir, d))]

selected_lab = st.selectbox("Оберіть лабораторну роботу:", lab_dirs)

if selected_lab:
    lab_path = os.path.join(labs_dir, selected_lab)
    readme_path = os.path.join(lab_path, "README.md")
    
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()
        st.markdown(readme_content)
    else:
        st.warning("Опис для цієї лабораторної роботи відсутній.")

    if st.button("Запустити"):
         lab_file = os.path.join(lab_path, f"{selected_lab}.py")

         if os.path.exists(lab_file):
            if selected_lab == "lab1":
              spec = importlib.util.spec_from_file_location("lab1", lab_file)
              lab_module = importlib.util.module_from_spec(spec)
              spec.loader.exec_module(lab_module)
              lab_module.run_lab1()
            elif selected_lab == "lab2":
               spec = importlib.util.spec_from_file_location("lab2", lab_file)
               lab_module = importlib.util.module_from_spec(spec)
               spec.loader.exec_module(lab_module)
               lab_module.run_lab2()
            elif selected_lab == "lab3":
              spec = importlib.util.spec_from_file_location("lab3", lab_file)
              lab_module = importlib.util.module_from_spec(spec)
              spec.loader.exec_module(lab_module)
              lab_module.run_lab3()
            elif selected_lab == "lab4":
              spec = importlib.util.spec_from_file_location("lab4", lab_file)
              lab_module = importlib.util.module_from_spec(spec)
              spec.loader.exec_module(lab_module)
              lab_module.run_lab4()
            elif selected_lab == "lab5":
              spec = importlib.util.spec_from_file_location("lab5", lab_file)
              lab_module = importlib.util.module_from_spec(spec)
              spec.loader.exec_module(lab_module)
              lab_module.run_lab5()
            elif selected_lab == "lab6":
              spec = importlib.util.spec_from_file_location("lab6", lab_file)
              lab_module = importlib.util.module_from_spec(spec)
              spec.loader.exec_module(lab_module)
              lab_module.run_lab6()
            elif selected_lab == "lab7":
              spec = importlib.util.spec_from_file_location("lab7", lab_file)
              lab_module = importlib.util.module_from_spec(spec)
              spec.loader.exec_module(lab_module)
              lab_module.run_lab7()
            else:
                st.error(f"Файл з кодом для {selected_lab} не знайдено.")
         else:
            st.error(f"Файл з кодом для {selected_lab} не знайдено.")