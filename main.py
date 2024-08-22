def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)
    word_count(book_text)
    print(char_count(book_text))

def word_count(book_text):
    words = book_text.split()
    count = len(words)
    print(f"Number of words in this book: {count}" )

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def char_count(book_text):
    lc_text = book_text.lower()
    char_counts = {}
    for char in lc_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

    
main()
    