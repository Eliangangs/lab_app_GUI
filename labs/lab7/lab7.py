import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import re
import streamlit as st

# Завдання 1
def task_1_ui():
    st.subheader("Завдання 1")
    st.markdown("Побудова графіку Y(x) = 2^x * sin(10x)")
    if st.button("Побудувати графік", key="plot1"):
        x = np.linspace(-3, 3, 400)
        y = 2**x * np.sin(10*x)
        
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title('Графік Y(x) = 2^x * sin(10x)')
        ax.set_xlabel('x')
        ax.set_ylabel('Y(x)')
        ax.grid()
        st.pyplot(fig)

# Завдання 2
def task_2_ui():
    st.subheader("Завдання 2")
    st.markdown("Побудова гістограми частоти літер у тексті")
    text = st.text_area("Введіть текст:", key="text2", value="Ваш текст тут. Букви а а а, б б, в")
    if st.button("Побудувати гістограму літер", key = "histo2"):
      letter_count = Counter(char.lower() for char in text if char.isalpha())
      letters = list(letter_count.keys())
      frequencies = list(letter_count.values())
      
      fig, ax = plt.subplots()
      ax.bar(letters, frequencies)
      ax.set_title('Гістограма частоти літер')
      ax.set_xlabel('Літери')
      ax.set_ylabel('Частота')
      ax.grid()
      st.pyplot(fig)

# Завдання 3
def task_3_ui():
    st.subheader("Завдання 3")
    st.markdown("Побудова гістограми частоти речень")
    text = st.text_area("Введіть текст:", key="text3", value="""Ваш текст тут. Яка погода? Це чудово! І ти...""")
    if st.button("Побудувати гістограму речень", key="histo3"):
        regular = re.findall(r'[^.!?]*[.!?]', text)
        counts = {
            'Звичайні': sum(1 for s in regular if not s.strip().endswith(('?', '!', '...'))),
            'Питальні': sum(1 for s in regular if s.strip().endswith('?')),
            'Окличні': sum(1 for s in regular if s.strip().endswith('!')),
        }

        fig, ax = plt.subplots()
        ax.bar(counts.keys(), counts.values())
        ax.set_title('Гістограма частоти речень')
        ax.set_xlabel('Типи речень')
        ax.set_ylabel('Кількість')
        ax.grid()
        st.pyplot(fig)

def run_lab7():
    task_1_ui()
    task_2_ui()
    task_3_ui()

if __name__ == '__main__':
    run_lab7()