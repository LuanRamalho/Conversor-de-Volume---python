import tkinter as tk

# Função para realizar a conversão
def converter():
    try:
        litros = float(entry_litros.get())
        metros_cubicos = litros / 1000
        mililitros = litros * 1000
        
        label_metros_cubicos_result.config(text=f"{metros_cubicos:.6f} m³", bg="lightcyan")
        label_mililitros_result.config(text=f"{mililitros:.0f} ml", bg="lightcyan")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Configuração da janela principal
root = tk.Tk()
root.title("Conversor de Volume")
root.geometry("400x300")
root.configure(bg="lightcyan")

# Título
title_label = tk.Label(root, text="Conversor de Volume", font=("Arial", 16, "bold"), bg="lightcyan", fg="indigo")
title_label.pack(pady=10)

# Entrada de litros
frame_input = tk.Frame(root, bg="lightcyan")
frame_input.pack(pady=10)
label_litros = tk.Label(frame_input, text="Digite o volume em litros:", bg="lightcyan")
label_litros.grid(row=0, column=0, padx=5, pady=5)
entry_litros = tk.Entry(frame_input, width=15, font=("Arial", 12))
entry_litros.grid(row=0, column=1, padx=5, pady=5)

# Botão de conversão
button_converter = tk.Button(root, text="Converter", command=converter, font=("Arial",14,"bold"), bg="olivedrab", fg="lavender")
button_converter.pack(pady=10)

# Resultados
result_frame = tk.Frame(root, bg="lightcyan")
result_frame.pack(pady=10)

label_metros_cubicos = tk.Label(result_frame, text="Em metros cúbicos:", bg="lightcyan")
label_metros_cubicos.grid(row=0, column=0, padx=5, pady=5, sticky="w")
label_metros_cubicos_result = tk.Label(result_frame, text="0 m³", font=("Arial", 12, "bold"), bg="lightcyan")
label_metros_cubicos_result.grid(row=0, column=1, padx=5, pady=5, sticky="w")

label_mililitros = tk.Label(result_frame, text="Em mililitros:", bg="lightcyan")
label_mililitros.grid(row=1, column=0, padx=5, pady=5, sticky="w")
label_mililitros_result = tk.Label(result_frame, text="0 ml", font=("Arial", 12, "bold"), bg="lightcyan")
label_mililitros_result.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Executa o aplicativo
root.mainloop()
