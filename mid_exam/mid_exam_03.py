shelf_whit_books = input().split("&")
my_list_boshelf_whit_booksoks = shelf_whit_books
while True:
    command = input().split(" | ")
    if command[0] == "Done":
        print(', '.join(shelf_whit_books))
        break
    if command[0] == "Add Book":
        if command[1] in shelf_whit_books:
            continue
        else:
            shelf_whit_books.insert(0 , command[1])
    elif command[0] == "Take Book":
        if command[1] in shelf_whit_books:
            shelf_whit_books.remove(command[1])
        else:
            continue
    elif command[0] == "Swap Books":
        if command[1] in shelf_whit_books and command[2] in shelf_whit_books:

            index_first_book = shelf_whit_books.index(command[1])
            index_second_book = shelf_whit_books.index(command[2])
            shelf_whit_books[index_first_book], shelf_whit_books[index_second_book] = shelf_whit_books[index_second_book], shelf_whit_books[index_first_book]
        else:
            continue
    elif command[0] == "Insert Book":
        if command[1] not in shelf_whit_books:
            shelf_whit_books.append(command[1])
        else:
            continue
    elif command[0] == 'Check Book':
        index = command[1]
        index = int(index)
        if 0 <= index and index < len(my_list_boshelf_whit_booksoks):
            print(shelf_whit_books[index])







