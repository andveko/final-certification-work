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




def update_b_label(event):
    # Получаем полное название базовой валюты из словаря и обновляем метку
    b_code = base_combobox.get()
    # name = code
    b_label.config(text=b_code)


def update_t_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()

    if target_code and base_code:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/coins/{base_code}')
            response.raise_for_status()

            data = response.json()

            if target_code in data['market_data']['current_price']:
                exchange_rate = data['market_data']['current_price'][target_code]
                base = base_code
                target = currencies[target_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate} {target} за 1 {base}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")
    return data


def show_history(data):
    # Создаем вторичное окно.
    history_window = Toplevel(window)
    # Заголовок вторичного окна
    history_window.title("Описание криптовалюты")

    # Виджет многострочного окна Text.
    # Цвет заднего фона окна белый, цвет текста черный.
    files_listbox = Text(history_window, bg='white', fg='black')
    # Упаковываем виджет с отступами со всех сторон.
    files_listbox.pack(padx=10, pady=10)
    if not data['description']['en']:
        description = data['description']['en']
        files_listbox.insert(END, description)
    # Делаем проверку существования истории загрузок.
    # if not os.path.exists(history_file):
    #     # Если история пустая, то выводим сообщение пользователю.
    #     messagebox.showinfo("История", "История загрузок пуста")
    #     # Выходим из функции.
    #     return

    # Создаем вторичное окно.
    history_window = Toplevel(window)
    # Заголовок вторичного окна
    history_window.title("Описание криптовалюты")

    # Виджет многострочного окна Text.
    # Цвет заднего фона окна белый, цвет текста черный.
    files_listbox = Text(history_window, bg='white', fg='black')
    # Упаковываем виджет с отступами со всех сторон.
    files_listbox.pack(padx=10, pady=10)
    # Открываем файл с историей загрузок.
    # Файл открываем для чтения.
    # with open(history_file, "r") as file:
    #     # В переменную history загружаем
    #     # содержимое файла истории, в формате json.
    #     history = json.load(file)
    #     # Цикл для перебора данных файла.
    #     for item in history:
    #         # Присваиваем переменной значение
    #         # содержащиеся в значении item['file_path'].
    #         file_path = item['file_path']
    #         # Присваиваем переменной значение
    #         # содержащиеся в значении item['download_link'].
    #         download_link = item['download_link']
    #         # Из полученных значений, с помощью f-строки создаем строку.
    #         # В конце строки вставляем управляющий символ переноса строки.
    #         create_string = f'Файл: {file_path},  Ссылка: {download_link}\n'
    #         # Вставляем полученную строку в виджет Text.
    #         files_listbox.insert(END, create_string)
    # С помощью виджета ttk создаем кнопку закрытия вторичного окна.
    close_button = ttk.Button(history_window, text='Закрыть', command=history_window.destroy)
    # Упаковываем кнопку закрытия вторичного окна, и размещаем её внизу окна.
    close_button.pack(side=BOTTOM, padx=10, pady=(0, 10))

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

cryptocurrency = ['bitcoin', 'ethereum', 'ripple', 'litecoin', 'cardano', 'bitcoin-2']

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x400")

Label(text="Базовая криптовалюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(textvariable=cryptocurrency[4], values=cryptocurrency)
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = Label()
b_label.pack(padx=10, pady=10)
data = exchange()
upload_button = ttk.Button(text="Загрузить описание криптовалюты", width=27, command=show_history)
# Упаковываем кнопку загрузки файлов.
upload_button.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = Label()
t_label.pack(padx=10, pady=10)

ttk.Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)
# Кнопка "Выход"
exit_button = ttk.Button(text='Выход', command=window.destroy)
# Упаковываем кнопку "Выход".
# Кнопку устанавливаем внизу окна программы.
# С отступами по горизонтали и вертикали.
exit_button.pack(side=BOTTOM, padx=10, pady=10)
# Запускаем главный цикл программы.

window.mainloop()
