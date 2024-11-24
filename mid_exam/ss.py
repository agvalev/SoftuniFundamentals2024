shelf = input().split("&")

def add_book(book):
    if book not in shelf:
        shelf.insert(0, book)

def take_book(book):
    if book in shelf:
        shelf.remove(book)

def swap_books(book1, book2):
    if book1 in shelf and book2 in shelf:
        index1 = shelf.index(book1)
        index2 = shelf.index(book2)
        shelf[index1], shelf[index2] = shelf[index2], shelf[index1]

def insert_book(book):
    if book not in shelf:
        shelf.append(book)

def check_book(index):
    index = int(index)
    if 0 <= index < len(shelf):
        print(shelf[index])

commands = {
    "Add Book": add_book,
    "Take Book": take_book,
    "Swap Books": swap_books,
    "Insert Book": insert_book,
    "Check Book": check_book
}

while True:
    command = input().split(" | ")
    if command[0] == "Done":
        break
    command_name, *args = command
    commands[command_name](*args)

print(", ".join(shelf))
