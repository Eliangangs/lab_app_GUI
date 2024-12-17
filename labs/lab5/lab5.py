import streamlit as st

class MyString(str):
    def has_repeated_sequences(self):
        for i in range(len(self) - 2):
            substring = self[i:i + 3]
            if self.count(substring) > 1:
                return True
        return False

    def is_palindrome(self):
        normalized_str = self.lower()
        return normalized_str == normalized_str[::-1]

def run_lab5():
    st.markdown("Створення класу MyString з методами для перевірки повторюваних послідовностей та паліндромності.")

    input_string = st.text_input("Введіть рядок:", key="input_string5", value='AbaCba')

    s = MyString(input_string)

    if st.button("Перевірити паліндром", key="check_palindrome5"):
          st.write(f"Рядок '{input_string}' є паліндромом: {s.is_palindrome()}")

    if st.button("Перевірити повторення", key="check_repeats5"):
          st.write(f"Рядок '{input_string}' має повторювані послідовності: {s.has_repeated_sequences()}")


if __name__ == '__main__':
    run_lab5()