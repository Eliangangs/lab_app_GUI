def find_subsequence(lst, subseq):

    n = len(lst)
    m = len(subseq)
    
    for i in range(n - m + 1):
        if lst[i:i+m] == subseq:
            return True
    
    return False

def run_lab2():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    subseq = [4, 5, 6]

    if find_subsequence(lst, subseq):
        print("Послідовність знайдена!")
    else:
        print("Послідовність не знайдена.")

if __name__ == '__main__':
    run_lab2()