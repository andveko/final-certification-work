# Импортируем модуль tkinter и все его компоненты.
# Для создания графического пользовательского интерфейса.
from tkinter import *
# Импортируем модуль ttk.
# Расширяем стандартную библиотеку tkinter.
from tkinter import ttk
# Из tkinter импортируем messagebox.
# Модуль messagebox, для создания окон
# с сообщениями пользователю.
from tkinter import messagebox as mb
# Импортируем модуль requests. Для
# взаимодействия со страницами в интернете.
import requests


# Функция для загрузки
# данных с сервера.
def loading_data():
    # Получаем выбранную криптовалюту.
    currency_code = cryptocurrency_combobox.get()
    # Проверяем, чтобы была выбрана
    # одна из предложенных криптовалют.
    if currency_code:
        # Если id криптовалюты выбрано,
        # то отправляем запрос на сервер.
        # Включаем обработку возможных ошибок.
        try:
            # Запрос на сервер, с id
            # выбранной криптовалюты.
            response = requests.get(f'https://api.coingecko.com/api/v3/coins/{currency_code}')
            # Проверяем ответ сервера.
            response.raise_for_status()
            # Возвращаем ответ сервера.
            return response.json()
        # Если возникают ошибки, то выводим предупреждение.
        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка: {e}')
    else:
        # Сообщение пользователю, если id криптовалюты не выбрано.
        mb.showwarning("Внимание", "Выберите коды валют")


# Функция, которая создает дополнительное окно
# 'Text', с описанием выбранной криптовалюты.
def show_description():
    pass


# Список для выбора криптовалюты.
cryptocurrency = ['bitcoin', 'ethereum', 'ripple', 'litecoin', 'cardano', 'bitcoin-2']


# Словарь кодов валют и их полных названий
currencies = {
    "usd": "Американский доллар",
    "eur": "Евро",
    "jpy": "Японская йена",
    "gbp": "Британский фунт стерлингов",
    "aud": "Австралийский доллар",
    "cad": "Канадский доллар",
    "chf": "Швейцарский франк",
    "cny": "Китайский юань",
    "rub": "Российский рубль",
    "kzt": "Казахстанский тенге",
    "uzs": "Узбекский сум"
}


# Создаем графический интерфейс программы.
# Создаем окно программы.
window = Tk()
# Название программы.
window.title('Крипта - обменный курс криптовалюты.')
# Создаем информационные метки.
label_1 = Label(text='Для показа описания и обменного курса,')
label_2 = Label(text='выберете криптовалюту из списка.')
label_3 = Label(text='Криптовалюта:')
# Упаковываем информационные метки.
label_1.pack(padx=10, pady=(10, 0))
label_2.pack(padx=10, pady=(0, 10))
label_3.pack(padx=10, pady=10)
# Виджет комбобокс со списком криптовалюты.
cryptocurrency_combobox = ttk.Combobox(values=cryptocurrency)
# По умолчанию установлен Биткоин.
cryptocurrency_combobox.set(cryptocurrency[0])
# Упаковываем Комбобокс с криптовалютой.
cryptocurrency_combobox.pack(padx=10, pady=10)
# Запускаем главный цикл программы.
window.mainloop()