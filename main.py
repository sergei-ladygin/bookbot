def read_a_book(book_link):
    try:
        with open(book_link, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"The book was not found.")
        return []
    except PermissionError:
        print(f"Permission denied to read the book.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the book: {e}")
        return []
    
def count_words(contents):
    if not contents:
        return 0
    
    words = contents.split()
    return len(words)

def count_chars(contents):
    letters_in_text = {}

    for i in contents.lower():
        if i.isalpha():
            if i in letters_in_text: 
                letters_in_text[i] += 1
            else:
                letters_in_text[i] = 1

    #sorted_alphabetically = dict(sorted(letters_in_text.items()))
    sorted_by_occurrence = dict(sorted(letters_in_text.items(), key=lambda item: item[1], reverse=True))
    return '\n'.join(f"The {key} character was found {value} times" for key, value in sorted_by_occurrence.items())

    

def main():
    book_link = "github.com/sergei-ladygin/bookbot/books/frankenstein.txt"
    book_contents = read_a_book(book_link)
    word_count = count_words(book_contents)
    chars_count = count_chars(book_contents)

    if book_contents:
        print(book_contents)
        print(f"--- Begin report of books/frankenstein.txt --- \n{word_count} words found in the document \n")
        print(f"{chars_count} \n--- End report ---")
        
    
if __name__ == "__main__":
    main()