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


# Функция для показа курса обмена криптовалюты.
def show_exchange_rate():
    # Получаем криптовалюту, выбранную пользователем.
    crypto = cryptocurrency_combobox.get()
    # Получаем валюту, для показа курса обмена.
    currency = currency_combobox.get()
    # Вызываем функцию отправляющую запрос на сервер.
    request_data = loading_data()
    # Проверяем, чтобы полученный
    # запрос не был пустым.
    if request_data:
        # Для обработки возможных ошибок.
        try:
            # Существует ли в полученных нами
            # данных, выбранная пользователем валюта.
            if currency in request_data['market_data']['current_price']:
                # Переменной присваиваем курс обмена из запроса.
                exchange_rate = request_data['market_data']['current_price'][currency]
                # Получаем из словаря название валюты обмена.
                name_currency = currencies[currency]
                # Получаем название криптовалюты.
                name_crypto = cryptocurrency[crypto]
                # Показываем пользователю сообщение с курсом обмена.
                mb.showinfo("Курс обмена", f"Курс {exchange_rate} {name_currency} за 1 {name_crypto}")
            else:
                # Если пользователь не ввел неправильную валюту обмена, показываем ему предупреждение.
                mb.showerror("Ошибка", f"Валюта {currency} не найдена")
        except Exception as e:
            # В случае возникновения ошибки, показываем её пользователю.
            mb.showerror("Произошла ошибка!", f"Произошла ошибка: {e}")
    else:
        # Сообщение торопливому пользователю.
        mb.showwarning("Внимание", "Выберите коды валют")



# Функция, которая создает дополнительное окно
# 'Text', с описанием выбранной криптовалюты.
def show_description():
    # Вызываем функцию отправляющую запрос на сервер.
    request_data = loading_data()
    # Проверяем, чтобы полученный
    # запрос не был пустым.
    if request_data['description']['en']:
        # Для обработки возможных ошибок.
        try:
            # Присваиваем переменной текст описания из запроса.
            text_description = request_data['description']['en']
            # Создаем вторичное окно.
            description_window = Toplevel(window)
            # Заголовок вторичного окна
            description_window.title("Описание криптовалюты")
            description_text = Text(description_window, bg='white', fg='black')
            description_text.insert(END, text_description)
            description_text.pack()
            # С помощью виджета ttk создаем кнопку закрытия вторичного окна.
            close_button = ttk.Button(description_window, text='Закрыть', command=description_window.destroy)
            # Упаковываем кнопку закрытия вторичного окна, и размещаем её внизу окна.
            close_button.pack(side=BOTTOM, padx=10, pady=(10, 10))
        except Exception as e:
            # В случае возникновения ошибки, показываем её пользователю.
            mb.showerror("Произошла ошибка!", f"Произошла ошибка: {e}")
    else:
        # Сообщение пользователю.
        mb.showwarning("Внимание!", "Описание криптовалюты отсутствует.")



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
# Размещаем во фрейме две информационные метки.
# "Ваш выбор" и метка с названием выбранной валюты
frame_6 = ttk.Frame()
# Упаковываем фрейм.
frame_6.pack(padx=10)
frame_7 = ttk.Frame()
# Упаковываем фрейм.
frame_7.pack(padx=10)
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
# Функция для обработки выбора элементов комбобокс.
cryptocurrency_combobox.bind("<<ComboboxSelected>>", update_cryptocurrency_label)
# Метка с надписью "Ваш выбор".
# Размещаем в третьем фрейме.
your_choice = ttk.Label(frame_3, text='Ваш выбор: ')
# Упаковываем метку.
your_choice.pack(side=LEFT, padx=(10, 0), pady=10)
# Метка для показа названия криптовалюты.
# Размещаем в третьем фрейме.
cryptocurrency_label = ttk.Label(frame_3, text='Биткоин')
# Упаковываем метку.
cryptocurrency_label.pack(side=LEFT, padx=(0, 10), pady=10)
# Информационная метка с надписью.
label_4 = ttk.Label(frame_4, text='Выберите валюту для показа курса обмена.')
# Упаковываем метку.
label_4.pack(padx=10, pady=10)
# Информационная метка с надписью.
label_4 = ttk.Label(frame_5, text='Валюта: ')
# Упаковываем метку
label_4.pack(side=LEFT, padx=(10, 0), pady=10)
# Комбобокс для выбора валюты
# обмена. Размещен в пятом фрейме.
currency_combobox = ttk.Combobox(frame_5, values=list(currencies.keys()))
# Упаковываем Комбобокс с валютой.
currency_combobox.pack(side=LEFT, padx=(0, 10), pady=10)
# Функция для обработки выбора элементов комбобокс.
currency_combobox.bind("<<ComboboxSelected>>", update_currency_label)
# Метка с надписью "Ваш выбор".
choice_currency = ttk.Label(frame_6, text='Ваш выбор: ')
# Упаковываем метку.
choice_currency.pack(side=LEFT, padx=(10, 0), pady=10)
# Информационная метка показывающая название валюты.
currency_label = ttk.Label(frame_6)
# Упаковываем метку.
currency_label.pack(side=LEFT, padx=(0, 10), pady=10)
# Выводим кнопку 'Показать курс обмена'.
# Кнопку размещаем в 7 фрейме. Ширина кнопки равна 30 символов,
# чтобы верхняя и нижняя кнопки были одинаковой ширины.
exchange_button = ttk.Button(frame_7,width=30, text='Показать курс обмена', command=show_exchange_rate)
# Упаковываем кнопку.
exchange_button.pack(padx=10, pady=10)
# Информационная метка с надписью.
label_5 = ttk.Label(frame_7, text='Описание доступно только')
# Упаковываем метку
label_5.pack(padx=10, pady=(10, 0))
# Информационная метка с надписью.
label_5 = ttk.Label(frame_7, text=' на английском языке!')
# Упаковываем метку
label_5.pack(padx=10)
# Выводим кнопку 'Показать описание криптовалюты'.
# Кнопку размещаем в 7 фрейме.
description_button = ttk.Button(frame_7, text='Показать описание криптовалюты', command=show_description)
# Упаковываем кнопку.
description_button.pack(padx=10, pady=10)

# Кнопка "Выход"
exit_button = ttk.Button(text='Выход', command=window.destroy)
# Упаковываем кнопку "Выход".
# Кнопку устанавливаем внизу окна программы.
# С отступами по горизонтали и вертикали.
exit_button.pack(side=BOTTOM, padx=10, pady=10)
# Запускаем главный цикл программы.
window.mainloop()
