import tkinter as tk
from tkinter import messagebox

def to_bin4(n):
    return format(n, '04b')

def calcular():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        if not (0 <= a <= 15 and 0 <= b <= 15):
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Digite valores inteiros entre 0 e 15.")
        return

    a_bin = to_bin4(a)
    b_bin = to_bin4(b)

    and_bin = to_bin4(a & b)
    or_bin = to_bin4(a | b)
    xor_bin = to_bin4(a ^ b)
    not_a_bin = to_bin4(~a & 0b1111)

    # Atualiza campos
    label_bin_a_valor.config(text=a_bin)
    label_bin_b_valor.config(text=b_bin)
    label_and_valor.config(text=f"{and_bin} ({a & b})")
    label_or_valor.config(text=f"{or_bin} ({a | b})")
    label_xor_valor.config(text=f"{xor_bin} ({a ^ b})")
    label_not_valor.config(text=f"{not_a_bin} ({~a & 0b1111})")

# Criar janela
root = tk.Tk()
root.title("Simulador Lógico Binário")
root.geometry("600x500")
root.resizable(False, False)

# Estilo de fonte
FONT = ("Arial", 12)

# Entradas
tk.Label(root, text="Valor A (0-15):", font=FONT).pack(pady=5)
entry_a = tk.Entry(root, font=FONT, justify="center")
entry_a.pack()

tk.Label(root, text="Valor B (0-15):", font=FONT).pack(pady=5)
entry_b = tk.Entry(root, font=FONT, justify="center")
entry_b.pack()

tk.Button(root, text="Calcular", command=calcular, font=FONT).pack(pady=10)

# Resultados
label_bin_a = tk.Label(root, text="Binário A:", font=FONT)
label_bin_a.pack()
label_bin_a_valor = tk.Label(root, text="----", font=FONT)
label_bin_a_valor.pack()

label_bin_b = tk.Label(root, text="Binário B:", font=FONT)
label_bin_b.pack()
label_bin_b_valor = tk.Label(root, text="----", font=FONT)
label_bin_b_valor.pack()

tk.Label(root, text="Resultados Lógicos:", font=("Arial", 13, "bold")).pack(pady=10)

label_and_valor = tk.Label(root, text="AND: ----", font=FONT)
label_and_valor.pack()
label_or_valor = tk.Label(root, text="OR: ----", font=FONT)
label_or_valor.pack()
label_xor_valor = tk.Label(root, text="XOR: ----", font=FONT)
label_xor_valor.pack()
label_not_valor = tk.Label(root, text="NOT A: ----", font=FONT)
label_not_valor.pack()

root.mainloop()
