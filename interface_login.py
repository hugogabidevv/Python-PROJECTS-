import customtkinter as ctk

#appearance
ctk.set_appearance_mode ("dark")

#functionalities
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    #verification if the user is Hugo and the password is 123456
    if usuario == "hugo" and senha == "123456":
        resultado_login.configure(text="Login successful!", text_color="green")
    else:
        resultado_login.configure(text="Incorrect login", text_color="red")


# main window
app = ctk.CTk ()
app.title("Login System")
app.geometry("300x300")

#creation of fields

#label
label_usuario = ctk.CTkLabel (app, text="User:")
label_usuario.pack(pady=10)

#entry
campo_usuario = ctk.CTkEntry(app,placeholder_text="Enter your username")
campo_usuario.pack(pady=10)

#label
label_senha = ctk.CTkLabel (app, text="Password:")
label_senha.pack(pady=10)

#entry
campo_senha = ctk.CTkEntry(app,placeholder_text="Enter your password", show= "*")
campo_senha.pack(pady=10)

#button
botão_login = ctk.CTkButton(app, text="Login", command=validar_login)
botão_login.pack(pady=10)

#login feedback
resultado_login= ctk.CTkLabel(app,text= "")
resultado_login.pack(pady=10)

#start application
app.mainloop()