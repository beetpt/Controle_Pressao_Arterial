import customtkinter as ctk
import os
import tempfile
from datetime import datetime
import tkinter.messagebox as messagebox
import csv
from tkinter import Scrollbar, Text, Toplevel


def search_data():
    # Get user input
    name = utente_entry_principal.get()
    # Read data from CSV file
    data = []
    with open('pressao.csv', 'r',encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row[1] == name:
                data.append(row)
    # Create new window to display results
    result_window = Toplevel()
    result_window.title(f'Results for {name}')
    # Create scrollbar and text widget to display results
    scrollbar = Scrollbar(result_window)
    scrollbar.pack(side='right', fill='y')
    text = Text(result_window, wrap='none', yscrollcommand=scrollbar.set)
    text.pack(fill='both', expand=True)
    scrollbar.config(command=text.yview)

    # Insert data into text widget
    for row in data:
        text.insert('end', ';'.join(row) + '\n')

    # Create buttons to print data or exit window
    print_button = ctk.CTkButton(result_window, text="Print", command=lambda: print_data(name, data))
    print_button.pack(pady=5)
    exit_button = ctk.CTkButton(result_window, text="Exit", command=result_window.destroy)
    exit_button.pack(pady=5)


def print_data(user, data):
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as temp:
        temp.write("Utente: {}\n".format(user))
        for row in data:
            temp.write(
                "{},Max-{},Min-{},BC-{},O2-{},Obs-{}\n".format(
                    row[0], row[2], row[3], row[4], row[5], row[6]
                )
            )
        temp.flush()
        os.startfile(temp.name, 'print')



def save_file():
    # Set filename
    filename = 'pressao.csv'
    # Get current date and time
    current_datetime = datetime.now().strftime('%d-%m-%Y')
    # Validate user input
    if not all([user_entry.get(), max_entry.get(), min_entry.get(), bc_entry.get(), o2_entry.get(), obs_entry.get()]):
        messagebox.showerror("Erro", "Todos os campos são\nde Preenchimento\nObrigatorio!")
        return
    # Save data to CSV file
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{current_datetime};{user_entry.get()};{max_entry.get()};{min_entry.get()};{bc_entry.get()};{o2_entry.get()};{obs_entry.get()}\n')
    # Display success message
    messagebox.showinfo("Sucesso", "Dados Gravados!")
    # Close window automatically
    menu_dados.destroy()



def abrir_menu_dados():
    global menu_dados, user_entry, max_entry, min_entry, bc_entry, o2_entry, obs_entry
    menu_dados = ctk.CTkToplevel()
    menu_dados.geometry("250x430")
    menu_dados.title("Inserir Dados Utente")
    user_label = ctk.CTkLabel(menu_dados, text="Nome:")
    user_entry = ctk.CTkEntry(menu_dados)
    max_label = ctk.CTkLabel(menu_dados, text="Maxima:")
    max_entry = ctk.CTkEntry(menu_dados)
    min_label = ctk.CTkLabel(menu_dados, text="Minima:")
    min_entry = ctk.CTkEntry(menu_dados)
    bc_label = ctk.CTkLabel(menu_dados, text="Batimentos:")
    bc_entry = ctk.CTkEntry(menu_dados)
    o2_label = ctk.CTkLabel(menu_dados, text="Oxigenio:")
    o2_entry = ctk.CTkEntry(menu_dados)
    obs_label = ctk.CTkLabel(menu_dados, text="Observações:")
    obs_entry = ctk.CTkEntry(menu_dados)
    save_button = ctk.CTkButton(menu_dados, text="Gravar dados", command=save_file)
    exit_button = ctk.CTkButton(menu_dados, text="Sair", text_color="red", command=menu_dados.destroy)
    user_label.pack()
    user_entry.pack()
    max_label.pack()
    max_entry.pack()
    min_label.pack()
    min_entry.pack()
    bc_label.pack()
    bc_entry.pack()
    o2_label.pack()
    o2_entry.pack()
    obs_label.pack()
    obs_entry.pack()
    save_button.pack(padx=0, pady=15)
    exit_button.pack(pady=0)
    menu_dados.focus_force()
    menu_dados.attributes("-topmost", True)



#Menu Principal
menu_principal = ctk.CTk()
menu_principal.title("Registo Pressão Arterial")
menu_principal.geometry("500x400")
menu_principal.resizable(width=False, height=False)
menu_principal.iconbitmap("Create.ico")



titlo_label_principal = ctk.CTkLabel(menu_principal, text="Controle Pressão Arterial", text_color="yellow", font=("arial bold", 35))
titlo_label_principal.pack(pady=5)

risco_topo_label_principal = ctk.CTkLabel(menu_principal, text="@☺♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫☺@", text_color="green", font=("arial bold", 15))
risco_topo_label_principal.pack(pady=10)

botao_inserir_Valores = ctk.CTkButton(menu_principal, text="Inserir Valores", text_color="white", font=("arial bold", 15), command=abrir_menu_dados)
botao_inserir_Valores.pack(pady=10)

risco_meio_label_principal = ctk.CTkLabel(menu_principal, text="@☺♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫☺@", text_color="green", font=("arial bold", 15))
risco_meio_label_principal.pack(pady=10)

utente_label_principal = ctk.CTkLabel(menu_principal, text="Identifique Utente para\nImprimir Relatorio", text_color="yellow", font=("arial bold", 15))
utente_label_principal.pack(padx=5, pady=0)

utente_entry_principal = ctk.CTkEntry(menu_principal, width=200, height=40)
utente_entry_principal.pack(pady=5)

botao_procurar_principal = ctk.CTkButton(menu_principal, text="Procurar Utente", text_color="white", font=("arial bold", 15), command=search_data)
botao_procurar_principal.pack(pady=5)

botao_sair_principal = ctk.CTkButton(menu_principal, text="Sair", text_color="red", font=("arial bold", 15),command=menu_principal.destroy)
botao_sair_principal.pack(pady=5)

author_label = ctk.CTkLabel(menu_principal, text="© Autor: Carlos Mação\n Version: 1.0.1")
author_label.pack(pady=5, side="bottom")


menu_principal.mainloop()
