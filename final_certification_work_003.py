from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_b_label(event):
    # Получаем полное название базовой валюты из словаря и обновляем метку
    code = b_combobox.get()
    name = cryptocurrency[code]
    b_label.config(text=name)

def update_t_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = t_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

def exchange():
    target_code = t_combobox.get()
    base_code = b_combobox.get()

    if target_code and base_code:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency={target_code}')
            response.raise_for_status()
            # Флаг для оповещения нахождения криптовалюты.
            flag_code = False

            data = response.json()
            for i in data:
                if i['id'] != base_code:
                    continue
                else:
                    exchange_rate = i['current_price']
                    base = cryptocurrency[base_code]
                    target = currencies[target_code]
                    mb.showinfo("Курс обмена", f"Курс {exchange_rate:.1f} {target} за 1 {base}")
                    flag_code = True
                    break
            if not flag_code:
                mb.showerror("Ошибка", f"Криптовалюта {base_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")

cryptocurrency = {
    'bitcoin': 'Биткоин',
    'ethereum': 'Эфириум',
    'ripple': 'XRP',
    'litecoin': 'Лайткоин',
    'cardano': 'Кардано',
    'dogecoin': 'Dogecoin',
    'tether': 'Tether',
    'solana': 'Solana',
    'the-open-network': 'Toncoin',
    'chainlink': 'Chainlink',
    'wrapped-bitcoin': 'Wrapped Bitcoin',
    'cosmos': 'Cosmos Hub',
    'staked-ether': 'Lido Staked Ether'
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

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x300")

Label(text="Криптовалюта:").pack(padx=10, pady=5)
b_combobox = ttk.Combobox(values=list(cryptocurrency.keys()))
b_combobox.pack(padx=10, pady=5)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Валюта обмена:").pack(padx=10, pady=5)
t_combobox = ttk.Combobox(values=list(currencies.keys()))
t_combobox.pack(padx=10, pady=5)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
