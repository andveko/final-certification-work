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


# Функция для обновления метки
# выбора криптовалюты пользователем.
def update_cryptocurrency_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = cryptocurrency_combobox.get()
    name = cryptocurrency[code]
    cryptocurrency_label.config(text=name)


# Функция, которая создает дополнительное окно
# 'Text', с описанием выбранной криптовалюты.
def show_description():
    pass


# Словарь для выбора криптовалюты.
cryptocurrency = {
    'bitcoin': 'Биткоин',
    'ethereum': 'Эфириум',
    'ripple': 'XRP',
    'litecoin': 'Лайткоин',
    'cardano': 'Кардано',
    'bitcoin-2': 'Bitcoin 2'
}


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
# Создаем фреймы, чтобы упорядочить расположение меток и кнопок, в окне программы.
# Первый фрейм содержит две информационные метки.
frame_1 = Frame()
frame_1.pack(padx=10)
# Во втором фрейме располагается
# информационная метка и виджет комбобокса.
frame_2 = Frame()
frame_2.pack(padx=10)
frame_3 = Frame()
frame_3.pack(padx=10)
# Создаем информационные метки.
label_1 = Label(frame_1, text='Для показа описания и обменного курса,')
label_2 = Label(frame_1, text='выберете криптовалюту из списка.')
label_3 = Label(frame_2, text='Криптовалюта: ')
# Упаковываем информационные метки.
label_1.pack(padx=10, pady=(10, 0))
label_2.pack(padx=10, pady=(0, 10))
label_3.pack(side=LEFT, padx=(10, 0), pady=10)
# Виджет комбобокс со списком криптовалюты.
cryptocurrency_combobox = ttk.Combobox(frame_2, values=list(cryptocurrency.keys()))
# По умолчанию установлен Биткоин.
cryptocurrency_combobox.set('bitcoin')
# Упаковываем Комбобокс с криптовалютой.
cryptocurrency_combobox.pack(side=LEFT, padx=(0, 10), pady=10)
cryptocurrency_combobox.bind("<<ComboboxSelected>>", update_cryptocurrency_label)
# Метка с надписью "Ваш выбор".
your_choice = Label(frame_3, text='Ваш выбор: ')
your_choice.pack(side=LEFT, padx=(10, 0), pady=10)
cryptocurrency_label = Label(frame_3, text='Биткоин')
cryptocurrency_label.pack(side=LEFT, padx=(0, 10), pady=10)
# Запускаем главный цикл программы.
window.mainloop()