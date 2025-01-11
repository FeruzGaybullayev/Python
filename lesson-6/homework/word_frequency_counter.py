import re
from collections import Counter

def create_sample_file():
    with open("lesson-6/homework/sample.txt", "w") as file:
        text = input("Enter text to create sample.txt: ")
        file.write(text)

def count_words():
    try:
        with open("lesson-6/homework/sample.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        create_sample_file()
        with open("lesson-6/homework/sample.txt", "r") as file:
            text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    
    total_words = sum(word_count.values())
    top_words = word_count.most_common(5)
    
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")
    
    with open("lesson-6/homework/word_count_report.txt", "w") as report:
        report.write("lesson-6/homework/word_count_report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top 5 Words:\n")
        for word, count in top_words:
            report.write(f"{word} - {count}\n")

if __name__ == "__main__":
    count_words()