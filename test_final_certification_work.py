# Этот файл предназначен для проведения
# автоматического тестирования программы
# final_certification_work.py
# Импортируем файл программы и
# присваиваем ему псевдоним fcw
import final_certification_work as fcw
# Импортируем библиотеку pytest,
# для проведения автоматических тестов.
import pytest


# Заготовка для тестирования
# функции test_loading_data
def test_loading_data():
    assert fcw.loading_data() == True

    with pytest.raises(BaseExceptionGroup):
        fcw.loading_data()


# Заготовка для тестирования
# функции update_cryptocurrency_label
def test_update_cryptocurrency_label(event):
    assert fcw.update_cryptocurrency_label() == True

    with pytest.raises(BaseExceptionGroup):
        fcw.update_cryptocurrency_label()


# Заготовка для тестирования
# функции update_currency_label
def test_update_currency_label(event):
    assert fcw.update_currency_label() == True

    with pytest.raises(BaseExceptionGroup):
        fcw.update_currency_label()


# Заготовка для тестирования
# функции show_exchange_rate
def test_show_exchange_rate():
    assert fcw.show_exchange_rate() == True

    with pytest.raises(BaseExceptionGroup):
        fcw.show_exchange_rate()


# Заготовка для тестирования
# функции show_description
def test_show_description():
    assert fcw.show_description() == True

    with pytest.raises(BaseExceptionGroup):
        fcw.show_description()


# Заготовка для тестирования
# функции show_about_program
def test_show_about_program():
    assert fcw.show_about_program() == True

    with pytest.raises(BaseExceptionGroup):
        fcw.show_about_program()

