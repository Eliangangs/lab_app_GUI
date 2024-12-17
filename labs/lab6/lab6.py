import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import streamlit as st

def get_page_content(url):
    """Завантажує HTML-код сторінки за допомогою requests."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Не вдалося завантажити сторінку: {url}. Помилка: {e}")

def count_words(text):
    """Підраховує частоту появи слів у тексті."""
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts

def count_html_tags(soup):
    """Підраховує частоту появи HTML-тегів."""
    tags = [tag.name for tag in soup.find_all(True)]
    tag_counts = Counter(tags)
    return tag_counts

def count_links_and_images(soup):
    """Підраховує кількість посилань (тег <a>) і зображень (тег <img>)."""
    links = soup.find_all('a')
    images = soup.find_all('img')
    return len(links), len(images)

def analyze_news_page(url):
    """Аналізує новинну сторінку: підраховує слова, теги, посилання та зображення."""
    html_content = get_page_content(url)
   
    soup = BeautifulSoup(html_content, 'html.parser')
   
    text_content = soup.get_text()
    word_counts = count_words(text_content)
   
    tag_counts = count_html_tags(soup)
   
    link_count, image_count = count_links_and_images(soup)
    
    st.write(f"Частота появи слів на сторінці '{url}':")
    for word, count in word_counts.most_common(10):
       st.write(f"{word}: {count}")
   
    st.write("\nЧастота використання HTML-тегів:")
    for tag, count in tag_counts.most_common(10):
      st.write(f"{tag}: {count}")
   
    st.write(f"\nКількість посилань: {link_count}")
    st.write(f"Кількість зображень: {image_count}")


def run_lab6():
    st.markdown("Веб-скрейпінг: аналіз HTML-коду сторінки.")

    url = st.text_input("Введіть URL для аналізу:", key="url6", value="https://uk.wikipedia.org/wiki/Головна_сторінка")
    
    if st.button("Аналізувати сторінку", key="analyze6"):
          try:
               analyze_news_page(url)
          except Exception as e:
               st.error(f"Помилка аналізу сторінки: {e}")

if __name__ == '__main__':
   run_lab6()