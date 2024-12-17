import streamlit as st

def find_subsequence(lst, subseq):

    n = len(lst)
    m = len(subseq)
    
    for i in range(n - m + 1):
        if lst[i:i+m] == subseq:
            return True
    
    return False

def run_lab2():
    st.markdown("Пошук підпослідовності у списку.")
    
    list_input = st.text_input("Введіть список чисел через пробіл, наприклад: 1 2 3 4 5", key="list_input2", value='1 2 3 4 5 6 7 8 9')
    subseq_input = st.text_input("Введіть підпослідовність через пробіл, наприклад: 4 5 6", key="subseq_input2", value='4 5 6')
    
    if st.button("Перевірити", key="check_subseq2"):
      try:
          lst = list(map(int, list_input.split()))
          subseq = list(map(int, subseq_input.split()))

          if find_subsequence(lst, subseq):
             st.success("Послідовність знайдена!")
          else:
              st.error("Послідовність не знайдена.")
      except ValueError:
           st.error("Введені дані повинні бути числами")

if __name__ == '__main__':
    run_lab2()