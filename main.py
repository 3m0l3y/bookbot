import pprint

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    print("\r\n")
    #print(book_text)
    word_count(book_text)
    current_book_dict = char_count(book_text)
    text = convert_to_list(current_book_dict)
    display_text(text)
    print(f"--- End report ---")


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

def convert_to_list(my_dict):
    list_of_dicts = []
    for k,v in my_dict.items():
        if k.isalpha():
            #print(f"The '{k}' character was found {v} times")
            list_of_dicts.append({"char":k, "num":v})  #This line of code was grabbed from the solution. I couldn't figure out how to do this.
            list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
    print(list_of_dicts)

def sort_on(dict):
    return dict["num"]

def display_text(list_of_dicts):
    for i in list_of_dicts:
        letter = i.get("char")
        number = i.get("num")
        print(f"The '{letter}' was found {number} times ")
        #print(f"The '{k}' character was found {v} times") 
    
main()

