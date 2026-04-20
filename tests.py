from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Добавляем книгу с именем длиной 1 символ
    def test_add_new_book_name_length_one(self):
        collector = BooksCollector()
        collector.add_new_book('А')
        assert len(collector.get_books_genre()) == 1
        assert 'А' in collector.get_books_genre()

    # Книга с именем длиной 40 символов добавляется, а 41 – нет
    def test_add_new_book_name_length_boundaries(self):
        collector = BooksCollector()
        name_40 = 'а' * 40
        name_41 = 'а' * 41
        collector.add_new_book(name_40)
        collector.add_new_book(name_41)
        assert name_40 in collector.get_books_genre()
        assert name_41 not in collector.get_books_genre()

    # У добавленной книги нет жанра (пустая строка)
    def test_new_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Новая книга')
        assert collector.get_book_genre('Новая книга') == ''

    # Тест get_books_genre: возвращает полный словарь книг и их жанров
    def test_get_books_genre_returns_full_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Комедии')
        expected = {'Книга1': 'Комедии', 'Книга2': ''}
        assert collector.get_books_genre() == expected

    # Устанавливаем жанр существующей книге
    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    # Установка несуществующего жанра – жанр не меняется
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Роман')  # такого жанра нет в списке
        assert collector.get_book_genre('Книга') == ''

    # Тест get_books_with_specific_genre
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Детектив1')
        collector.add_new_book('Детектив2')
        collector.add_new_book('Фантастика1')
        collector.set_book_genre('Детектив1', 'Детективы')
        collector.set_book_genre('Детектив2', 'Детективы')
        collector.set_book_genre('Фантастика1', 'Фантастика')
        detectives = collector.get_books_with_specific_genre('Детективы')
        assert detectives == ['Детектив1', 'Детектив2']

    # Тест get_books_for_children: книги с возрастным рейтингом не попадают
    def test_get_books_for_children_excludes_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Детская')
        collector.add_new_book('Страшилка')
        collector.set_book_genre('Детская', 'Комедии')
        collector.set_book_genre('Страшилка', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Детская' in children_books
        assert 'Страшилка' not in children_books

    # Добавляем книгу в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    # Повторное добавление одной и той же книги в избранное
    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Дубль')
        collector.add_book_in_favorites('Дубль')
        collector.add_book_in_favorites('Дубль')
        assert collector.get_list_of_favorites_books().count('Дубль') == 1

    # Удаляем книгу из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Удаляемая')
        collector.add_book_in_favorites('Удаляемая')
        collector.delete_book_from_favorites('Удаляемая')
        assert 'Удаляемая' not in collector.get_list_of_favorites_books()

    # Получение пустого списка избранного, если ничего не добавляли
    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []