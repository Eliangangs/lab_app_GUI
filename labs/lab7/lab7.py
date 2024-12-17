import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import re

# Завдання 1
def task_1():
    x = np.linspace(-3, 3, 400)
    y = 2**x * np.sin(10*x)

    plt.plot(x, y)
    plt.title('Графік Y(x) = 2^x * sin(10x)')
    plt.xlabel('x')
    plt.ylabel('Y(x)')
    plt.grid()
    plt.show()

# Завдання 2
def task_2():
    text = "Ваш текст тут. Букви а а а, б б, в"
    letter_count = Counter(char.lower() for char in text if char.isalpha())

    letters = list(letter_count.keys())
    frequencies = list(letter_count.values())

    plt.bar(letters, frequencies)
    plt.title('Гістограма частоти літер')
    plt.xlabel('Літери')
    plt.ylabel('Частота')
    plt.grid()
    plt.show()

# Завдання 3
def task_3():
    text = """Ваш текст тут. Яка погода? Це чудово! І ти..."""

    regular = re.findall(r'[^.!?]*[.!?]', text)
    counts = {
        'Звичайні': sum(1 for s in regular if not s.strip().endswith(('?', '!', '...'))),
        'Питальні': sum(1 for s in regular if s.strip().endswith('?')),
        'Окличні': sum(1 for s in regular if s.strip().endswith('!')),
        'Трикрапка': sum(1 for s in regular if s.strip().endswith('...')),
    }

    plt.bar(counts.keys(), counts.values())
    plt.title('Гістограма частоти речень')
    plt.xlabel('Типи речень')
    plt.ylabel('Кількість')
    plt.grid()
    plt.show()

def run_lab7():
    task_1()
    task_2()
    task_3()
    

if __name__ == '__main__':
    run_lab7()