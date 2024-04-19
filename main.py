def main():
    path = "books/frankenstein.txt" 
    text = get_book_text(path)   
    print_report(path, text)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_total_number_of_words(text):
    counter = 0 
    total_words = text.split()
 
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

def get_list_of_words(text):
        count_of_letters = get_number_of_letters(text)
        x = []

        
        def create_list(text):
            for letter in count_of_letters:
                if letter.isalpha():
                    temp_dict = dict(char = letter, num = count_of_letters[letter])
                    x.append(temp_dict)
                    
        
            def sort_on(dict):
                return dict["num"]
            x.sort(reverse=True, key=sort_on)
        
        create_list(count_of_letters)
        return x        
        

def print_report(path, text):
    print(f"__..---- Beginning of report from {path} ----..__")  
    print(f"Total number of words: {get_total_number_of_words(text)}")
    get_list_of_words(text)
    for dict in get_list_of_words(text): 
        
        print(f"The '{dict["char"]}' character was found {dict["num"]} times.")
        

main()