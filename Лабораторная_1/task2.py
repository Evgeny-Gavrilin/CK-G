# TODO Найдите количество книг, которое можно разместить на дискете
bytes_of_1_symbol = 4
quantity_of_1_string = 25
strings_of_page = 50
strings_in_book = 100
inf_disk_byte = round(1024 * 1024 * 1.44)
bytes_of_1_book = bytes_of_1_symbol * quantity_of_1_string * strings_of_page * strings_in_book
quantity_of_books = inf_disk_byte // bytes_of_1_book
print("Количество книг, помещающихся на дискету:", quantity_of_books)
