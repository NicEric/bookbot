def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(get_number_of_words(text))

    # ...

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_of_words(words):
    counter = 0 
    total_words = words.split()
    print(total_words)
    for word in total_words:
        counter += 1
    return counter


main()