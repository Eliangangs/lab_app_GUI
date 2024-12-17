import os
import re

def create_group_files(base_dir):
    groups = ['group_1.txt', 'group_2.txt', 'group_3.txt']
    for group_file in groups:
        file_path = os.path.join(base_dir, group_file)
        with open(file_path, 'w') as f:
            f.write(f"Name,Grade\n")
    print(f"Файли груп створено у {base_dir}")

def write_student_data(base_dir, group_file, student_name, grade):
    file_path = os.path.join(base_dir, group_file)
    with open(file_path, 'a') as f:
        f.write(f"{student_name},{grade}\n")

def read_file_data(base_dir, group_file):
    file_path = os.path.join(base_dir, group_file)
    with open(file_path, 'r') as f:
        return f.readlines()

def search_files(base_dir, search_pattern):
     matched_files = []
     for filename in os.listdir(base_dir):
         if re.search(search_pattern, filename):
             matched_files.append(filename)
     return matched_files

def search_data(base_dir, group_file, search_term):
    file_path = os.path.join(base_dir, group_file)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line for line in lines if search_term in line]

def sort_by_grade(base_dir, group_file):
    file_path = os.path.join(base_dir, group_file)
    with open(file_path, 'r') as f:
        lines = f.readlines()[1:]
    students = []
    for line in lines:
         if "," in line:
            name, grade = line.strip().split(',')
            students.append((name, float(grade)))

    students.sort(key=lambda x: x[1], reverse=True)
    print("Сортовані дані:")
    for name, grade in students:
         print(f"{name}: {grade}")

def run_lab3():
    base_dir = 'student_groups'
    os.makedirs(base_dir, exist_ok=True)
    create_group_files(base_dir)

    write_student_data(base_dir, 'group_1.txt', 'Іван', 4.5)
    write_student_data(base_dir, 'group_1.txt', 'Марія', 4.8)
    write_student_data(base_dir, 'group_2.txt', 'Петро', 4.2)
    write_student_data(base_dir, 'group_2.txt', 'Ольга', 4.9)
    write_student_data(base_dir, 'group_3.txt', 'Микола', 4.6)
    
    print("Читання файлу group_1.txt:")
    print(read_file_data(base_dir, 'group_1.txt'))

    print(f"Пошук файлів, що містять 'group' у назві:{search_files(base_dir, 'group')}")

    print("Пошук студентів з ім'ям 'Іван' у group_1.txt:")
    print(search_data(base_dir, 'group_1.txt', 'Іван'))
    
    sort_by_grade(base_dir, 'group_1.txt')


if __name__ == '__main__':
    run_lab3()