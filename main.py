def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    # print(get_chars_dict(text))
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    print(characters_found(count_letters(text)))
    print(f"--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)
    
def count_letters(text):
    lowercase_input = text.lower()
    freq = {}
    for c in set(lowercase_input):
       freq[c] = lowercase_input.count(c)
    return freq

def characters_found(dict):
    list = []
    for letter in dict:
      if letter.isalpha():
        new_dict = {}
        count = dict[letter]
        new_dict["letter"] = letter
        new_dict["count"] = count
        list.append(new_dict)
    def sort_on(letter_dictionary):
      return letter_dictionary["count"]
    list.sort(reverse=True, key=sort_on)
    for letter in list:
        print(f"The '{letter["letter"]}' was found {letter["count"]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
