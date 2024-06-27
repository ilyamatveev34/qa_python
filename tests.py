import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    @pytest.mark.parametrize('name_length', ['', 'Что делать, если ваш кот хочет вас убить?', 'Что делать, если ваш кот хочет вас убить??'])
    def test_add_new_book_name_add_negative_name_length_failed(self, collector, name_length):
        collector.add_new_book(name_length)
        assert len(collector.get_books_genre()) == 0


    def test_set_book_genre_added_book_success(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre.get('Гордость и предубеждение и зомби') == 'Ужасы'


    def test_get_book_genre_existing_name_success(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'


    def test_get_books_with_specific_genre_horror_3_books_success(self, collector):
        collector.books_genre = {'Гордость и предубеждение и зомби': 'Ужасы',
                                 'Крик': 'Ужасы', 'Зловещие мертвецы': 'Ужасы',
                                 'Король лев': 'Мультфильмы', 'Один дома': 'Комедии'}
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби', 'Крик', 'Зловещие мертвецы']


    def test_get_books_genre_existing_book_and_genre_success(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы'}


    def test_get_books_for_children_two_books_success(self, collector):
        collector.books_genre = {'Колобок': 'Мультфильмы', 'Гордость и предубеждение и зомби': 'Ужасы',
                               'Приключения Шерлока Холмса': 'Детективы', 'Король лев': 'Мультфильмы'}
        assert len(collector.get_books_for_children()) == 2


    def test_add_book_in_favorites_add_one_existing_book_success(self, collector):
        collector.books_genre = {'Колобок': 'Мультфильмы', 'Гордость и предубеждение и зомби': 'Ужасы',
                               'Приключения Шерлока Холмса': 'Детективы', 'Король лев': 'Мультфильмы'}
        collector.add_book_in_favorites('Король лев')
        assert len(collector.favorites) == 1


    def test_delete_book_from_favorites_delete_one_existing_book_success(self, collector):
        collector.books_genre = {'Колобок': 'Мультфильмы', 'Гордость и предубеждение и зомби': 'Ужасы',
                                 'Приключения Шерлока Холмса': 'Детективы', 'Король лев': 'Мультфильмы'}
        collector.add_book_in_favorites('Король лев')
        collector.delete_book_from_favorites('Король лев')
        assert len(collector.favorites) == 0


    def test_get_list_of_favorites_books_two_books_in_list(self, collector):
        collector.books_genre = {'Колобок': 'Мультфильмы', 'Гордость и предубеждение и зомби': 'Ужасы',
                                 'Приключения Шерлока Холмса': 'Детективы', 'Король лев': 'Мультфильмы'}
        collector.add_book_in_favorites('Король лев')
        collector.add_book_in_favorites('Колобок')
        collector.get_list_of_favorites_books()
        assert collector.get_list_of_favorites_books() == ['Король лев', 'Колобок']



