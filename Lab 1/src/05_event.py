# Дополнительное задание. Событийный стиль (tkinter)
import tkinter as tk


def calculate():
    try:
        numbers = [int(x) for x in entry.get().split()]
    except ValueError:
        result_label.config(text="Ошибка: введите целые числа через пробел")
        return
    result = sum(n ** 2 for n in numbers if n % 2 == 0)
    result_label.config(text=f"Результат: {result}")


def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Нажмите кнопку")


root = tk.Tk()
root.title("Парадигмы программирования")

entry = tk.Entry(root, width=30)
entry.insert(0, "4 7 2 9 12 5 8 3")
entry.pack(padx=20, pady=10)

result_label = tk.Label(root, text="Нажмите кнопку")
result_label.pack(padx=20, pady=10)

tk.Button(root, text="Вычислить", command=calculate).pack(padx=20, pady=5)
tk.Button(root, text="Очистить", command=clear).pack(padx=20, pady=5)

root.mainloop()
