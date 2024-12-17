# GUI для лабораторних робіт

Цей проект надає графічний інтерфейс для запуску та перегляду лабораторних робіт.

## Структура
*   `labs/`: Містить папки з кодом для кожної лабораторної роботи.
*   `gui.py`: Основний файл для запуску GUI.
*   `README.md`: Цей файл з описом проекту.

## Запуск

1.  Встановіть Streamlit:
    ```
    pip install streamlit
    pip install requests
    pip install beautifulsoup4
    pip install matplotlib
    ```
2.  Запустіть `gui.py`:
    ```
    streamlit run gui.py
    ```

## Використання
У головному вікні виберіть лабораторну роботу зі списку, перегляньте її опис та запустіть.