import sys
from stats import get_num_words
from stats import count
from stats import sort_on
from stats import sort_it_out


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    no_of_words = get_num_words(text)
    count_em = count(text)
    final_sort = sort_it_out(count_em)
    print_report(book, no_of_words, final_sort)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def print_report(book, no_of_words, final_sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {no_of_words} total words")
    print("--------- Character Count -------")
    for item in final_sort:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


     
main()
