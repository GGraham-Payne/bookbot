def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = count_characters(text)
    report = gen_report(characters)
    print(f"--- begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for letter in report:
        print(f"The '{letter["name"]}' character was found {letter["num"]} times")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def gen_report(characters):
    letter_count = []
    for c in characters:
        if c.isalpha():
            letter_count.append({"name": c, "num": characters[c]})
        letter_count.sort(reverse=True, key=sort_on)
    return letter_count


main()