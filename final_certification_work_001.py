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
    # Присваиваем переменной значение
    # полученное из словаря.
    name = cryptocurrency[code]
    # Изменяем текст метки.
    cryptocurrency_label.config(text=name)


def update_currency_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = currency_combobox.get()
    # Присваиваем переменной значение
    # полученное из словаря.
    name = currencies[code]
    # Изменяем текст метки.
    currency_label.config(text=name)


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
frame_1 = ttk.Frame()
# Упаковываем фрейм.
frame_1.pack(padx=10)
# Во втором фрейме располагается
# информационная метка и виджет комбобокса.
frame_2 = ttk.Frame()
# Упаковываем фрейм.
frame_2.pack(padx=10)
# В третьем фрейме размещаем метку
# с надписью "Ваш выбор" и метку с
# названием криптовалюты из словаря.
frame_3 = ttk.Frame()
# Упаковываем фрейм.
frame_3.pack(padx=10)
# В четвертом фрейме размещаем
# информацию для пользователя.
frame_4 = ttk.Frame()
# Упаковываем фрейм.
frame_4.pack(padx=10)
# В этом фрейме размещаем надпись
# и комбобокс с выбором валюты.
frame_5 = ttk.Frame()
# Упаковываем фрейм.
frame_5.pack(padx=10)

frame_6 = ttk.Frame()
# Упаковываем фрейм.
frame_6.pack(padx=10)
# Создаем информационные метки.
label_1 = ttk.Label(frame_1, text='Для показа обменного курса и описания,')
label_2 = ttk.Label(frame_1, text='выберете криптовалюту из списка.')
label_3 = ttk.Label(frame_2, text='Криптовалюта: ')
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
your_choice = ttk.Label(frame_3, text='Ваш выбор: ')
your_choice.pack(side=LEFT, padx=(10, 0), pady=10)
cryptocurrency_label = ttk.Label(frame_3, text='Биткоин')
cryptocurrency_label.pack(side=LEFT, padx=(0, 10), pady=10)
# Информационная метка с надписью.
label_4 = ttk.Label(frame_4, text='Выберите валюту для показа курса обмена.')
label_4.pack(padx=10, pady=10)

label_4 = ttk.Label(frame_5, text='Валюта: ')
label_4.pack(side=LEFT, padx=(10, 0), pady=10)
currency_combobox = ttk.Combobox(frame_5, values=list(currencies.keys()))
currency_combobox.pack(side=LEFT, padx=(0, 10), pady=10)
currency_combobox.bind("<<ComboboxSelected>>", update_currency_label)
# Метка с надписью "Ваш выбор".
choice_currency = ttk.Label(frame_6, text='Ваш выбор: ')
choice_currency.pack(side=LEFT, padx=(10, 0), pady=10)
currency_label = ttk.Label(frame_6, text='')
currency_label.pack(side=LEFT, padx=(0, 10), pady=10)
# Кнопка "Выход"
exit_button = ttk.Button(text='Выход', command=window.destroy)
# Упаковываем кнопку "Выход".
# Кнопку устанавливаем внизу окна программы.
# С отступами по горизонтали и вертикали.
exit_button.pack(side=BOTTOM, padx=10, pady=10)
# Запускаем главный цикл программы.
window.mainloop()
