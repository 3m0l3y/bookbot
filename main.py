with open("books/frankenstein.txt") as f:

    def main():
        file_contents = f.read()
        print(file_contents)
        word_count(file_contents)
    
    def word_count(string):
        words = string.split()
        count = len(words)
        print(f"Number of words in this book: {count}" )
        
    main()
    