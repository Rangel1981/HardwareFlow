import customtkinter as ctk
from views.app_interface import HardwareApp

if __name__ == "__main__":
    # Deixa o sistema com a cara do Windows/Mac (Dark Mode)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    app = HardwareApp()
    app.mainloop()