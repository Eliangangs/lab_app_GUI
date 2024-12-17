import streamlit as st
import random

# Завдання 1
def task_1():
    st.subheader("Завдання 1")
    n = st.number_input("Введіть значення n:", step=1.0)
    m = st.number_input("Введіть значення m (не повинно дорівнювати 0):", step=1.0)
    if st.button("Виконати Завдання 1"):
        if m == 0:
            st.error("m не може бути нулем")
        else:
            result = (2**0.5 - (3 * n)**0.5) / (2 * m)
            st.success(f"Результат: z = {result}")

# Завдання 2
def task_2():
    st.subheader("Завдання 2")
    if 'secret_number' not in st.session_state:
        st.session_state['secret_number'] = random.randint(1, 100)
    if 'attempts' not in st.session_state:
        st.session_state['attempts'] = 0
    guess = st.number_input("Введіть число від 1 до 100:", step=1, min_value=1, max_value=100)
    if st.button("Відповісти"):
        st.session_state['attempts'] += 1
        if guess < st.session_state['secret_number']:
            st.info("Моє число більше")
        elif guess > st.session_state['secret_number']:
            st.info("Моє число менше")
        else:
            st.success(f"Ви вгадали число {st.session_state['secret_number']} з {st.session_state['attempts']} спроб!")
            st.session_state['attempts'] = 0
            st.session_state['secret_number'] = random.randint(1, 100)

# Завдання 3
def task_3():
    st.subheader("Завдання 3")
    elements = st.text_area("Введіть цілі числа через пробіл:")
    if st.button("Виконати Завдання 3"):
        try:
            arr = list(map(int, elements.split()))
            if arr:
                min_element = min(arr)
                positive_odd_sum = sum(x for x in arr if x > 0 and x % 2 != 0)
                positive_elements = [x for x in arr if x > 0]

                st.write(f"Мінімальний елемент: {min_element}")
                st.write(f"Сума додатніх непарних елементів: {positive_odd_sum}")
                st.write(f"Додатні елементи: {positive_elements}")
            else:
                 st.error("Будь ласка, введіть числа.")
        except ValueError:
            st.error("Переконайтеся, що введені дані містять лише цілі числа.")

# Виконання завдань
def run_lab1():
    task_1()
    st.markdown("---")
    task_2()
    st.markdown("---")
    task_3()

if __name__ == '__main__':
    run_lab1()