# qa_python
1) test_add_new_book_name_add_negative_name_length_failed - проверка невозможности добавления в словарь книги с некорректной длиной названия. 
2) test_set_book_genre_added_book_success - проверка возможности установки жанра книги, если книга есть в books_genre и её жанр входит в список genre.
3) test_get_book_genre_existing_name_success - проверка возможности вывода жанра книги по её имени.
4) test_get_books_with_specific_genre_horror_3_books_success - проверка возможности вывода списка книг с определённым жанром.
5) test_get_books_genre_existing_book_and_genre_success - проверка возможности вывода текущего словаря books_genre.
6) test_get_books_for_children_two_books_success - проверка возможности возвращения книг, которые подходят детям(то есть, без возрастного рейтинга).
7) test_add_book_in_favorites_add_one_existing_book_success - проверка возможности добавления книги в избранное.
8) test_delete_book_from_favorites_delete_one_existing_book_success - проверка возможности удаления книги из избранного.
9) test_get_list_of_favorites_books_two_books_in_list - проверка возможности получения списка избранных книг.