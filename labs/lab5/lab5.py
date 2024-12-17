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
    s = MyString("AbaCba")
    
    print(s.is_palindrome())  # Output: True
    print(s.has_repeated_sequences())  # Output: False

if __name__ == '__main__':
    run_lab5()