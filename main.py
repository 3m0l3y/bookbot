def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)
    word_count(book_text)

def word_count(string):
    words = string.split()
    count = len(words)
    print(f"Number of words in this book: {count}" )

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
main()
    