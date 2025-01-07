
def main():
	with open("books/frankenstein.txt") as f:
		book = f.read()
		return book		
		
def word_count(book_content):
	words = book.split()
	print(len(words))

def count_characters(book_content):
	letter_count = {}
	lower_words = book.lower()
	for let in lower_words:
		letter_count[let] = letter_count.get(let, 0) + 1
	for key, value in letter_count.items():
		print(f"The {key} character was found {value} times")

book = main()
word_count(book)
count_characters(book)
