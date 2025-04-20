import os,sys

os.system('cls')

# print(sys.argv)

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>\n')
    sys.exit(1)

def get_book_text(path):
    with open(path, encoding='utf8') as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    count_dict = {}
    split_chars = [char.lower() for char in text]
    for i in range(0, len(split_chars)):
        if split_chars[i].isalpha():
            count_dict[split_chars[i]] = count_dict.get(split_chars[i], 0) + 1
    return count_dict

def report(book_path, num_words, sorted_dict):
    print(f'---- Begin report of {book_path} ----')
    print(f'There are {num_words} words found in the book/document.\n')
    for k,v in sorted_dict.items():
        print(f"The '{k}' character was found {v} times.")
    print('---- End report ----')

def main():
    book_path = sys.argv[1]  # 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_dict = count_chars(text)
    sorted_dict = (dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True)))  # sorting on dict.values() (aka index=1)
    report(book_path, num_words, sorted_dict)
    
main()