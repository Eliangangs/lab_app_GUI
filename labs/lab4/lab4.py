from collections import Counter

def find_repeated_sequences(text, min_words=3, min_repeats=5):
    words = text.split()
    n = len(words)
    
    sequences = []
    
    for i in range(n - min_words + 1):
      for length in range(min_words, n - i + 1):
          sequence = ' '.join(words[i:i+length])
          sequences.append(sequence)
    
    sequence_counts = Counter(sequences)

    repeated_sequences = {seq: count for seq, count in sequence_counts.items() if count >= min_repeats}
    
    return repeated_sequences

def run_lab4():
    text = """Тестовий текст для перевірки повторюваних послідовностей. 
    Цей текст містить багато слів, серед яких є повторювані послідовності. 
    Повторювані послідовності повинні бути знайдені в тексті, якщо вони повторюються не менше 5 раз.
    Повторювані послідовності у тексті повинні бути знайдені, і цей текст містить їх декілька."""
    
    result = find_repeated_sequences(text)

    if result:
        print("Найдені послідовності:")
        for seq, count in result.items():
            print(f"\"{seq}\" повторюється {count} разів")
    else:
        print("Повторюваних послідовностей не знайдено.")

if __name__ == '__main__':
    run_lab4()