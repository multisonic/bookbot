def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print(count_letters(text))


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_letters(text):
    lowercase_input = text.lower()
    freq = {}
    for c in set(lowercase_input):
       freq[c] = lowercase_input.count(c)
    return freq


main()
