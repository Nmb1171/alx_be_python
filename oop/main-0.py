from library_system import Book, EBook, PrintBook

def main():
    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Print instances to demonstrate __str__ functionality
    print(classic_book)
    print(digital_novel)
    print(paper_novel)

if __name__ == "__main__":
    main()
