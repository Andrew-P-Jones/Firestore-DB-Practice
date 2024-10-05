# import customtkinter as ctk

# ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
# ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# window = ctk.CTk()  # create CTk window like you do with the Tk window
# window.geometry("800x480")
# window.title("Demo")

# def button_function():
#     ...

# # Use CTkButton instead of tkinter Button
# button = ctk.CTkButton(master=window, text="button", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# tabview = ctk.CTkTabview(master=window, width=250, height=300, anchor="n")
# tabview.place(relx=0.0, rely=0.0)

# tabview.add("tab 1")  # add tab at the end
# tabview.add("tab 2")  # add tab at the end
# tabview.set("tab 1")  # set currently visible tab

# button = ctk.CTkButton(master=tabview.tab("tab 1"), text="tab button")
# button.pack(padx=20, pady=20)

# slider = ctk.CTkSlider(master=tabview.tab("tab 1"), text="Theme", command=ctk.set_appearance_mode("light"))
# slider.pack(padx=20, pady=20)

# window.mainloop()