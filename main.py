def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_number_of_letters(text))
    #print(type(text))
    print(get_total_number_of_words(text))

    # ...

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_total_number_of_words(words):
    counter = 0 
    total_words = words.split()
    #print(total_words)
    for word in total_words:
        counter += 1
    return counter

def get_number_of_letters(text):
    letters = {}

    for letter in text:
        lowered = letter.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters 


        
        
        #letters
        #if letter not in letters:

        

        
        #print(letter)
    

main()