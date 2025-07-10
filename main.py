import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Necesario para manejar imágenes

# Sample data: topics and their content
ENCYCLOPEDIA_DATA = {
    "Python": {
        "title": "Python Programming Language",
        "content": (
            "Python es un lenguaje de programación interpretado, de alto nivel y propósito general. "
            "Creado por Guido van Rossum y lanzado por primera vez en 1991, Python cuenta con una sintaxis clara y legible."
        ),
    },
    "Tkinter": {
        "title": "Tkinter GUI Toolkit",
        "content": (
            "Tkinter es la biblioteca estándar de Python para la creación de interfaces gráficas de usuario (GUI). "
            "Proporciona un conjunto de widgets como botones, etiquetas, cuadros de texto, y permite construir ventanas y diálogos interactivos."
        ),
    },
    "Encarta": {
        "title": "Microsoft Encarta",
        "content": (
            "Microsoft Encarta fue una enciclopedia digital multimedia publicada por Microsoft entre 1993 y 2009. "
            "Ofrecía artículos, imágenes, videos y actividades interactivas para estudiantes y usuarios generales."
        ),
    },
    "MicroOperaciones": {
        "title": "Microsoft Encarta",
        "content": (
            "Microsoft Encarta fue una enciclopedia digital multimedia publicada por Microsoft entre 1993 y 2009. "
            "Ofrecía artículos, imágenes, videos y actividades interactivas para estudiantes y usuarios generales."
        ),
        "Label" : "micro.png"
    },
    "CL": {
        "title": "Microsoft Encarta",
        "content": (
            "Microsoft Encarta fue una enciclopedia digital multimedia publicada por Microsoft entre 1993 y 2009. "
            "Ofrecía artículos, imágenes, videos y actividades interactivas para estudiantes y usuarios generales."
        ),
    },
    "Assemblr": {
        "title": "Microsoft Encarta",
        "content": (
            "Microsoft Encarta fue una enciclopedia digital multimedia publicada por Microsoft entre 1993 y 2009. "
            "Ofrecía artículos, imágenes, videos y actividades interactivas para estudiantes y usuarios generales."
        ),
    },
}

class EncartaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ARCHI: Asistente Virtual")
        self.geometry("800x700")

        self.main_frame = None
        self.search_frame = None
        self.show_main_menu()

    def show_main_menu(self):
        if self.search_frame:
            self.search_frame.pack_forget()
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Imagen centrada
        self.image = Image.open("sample_image.png")
        #self.image = self.image.resize((200, 200), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = ttk.Label(self.main_frame, image=self.photo)
        self.image_label.pack(pady=10)

        # Título de la aplicación
        title = ttk.Label(self.main_frame, text="ARCHI", font=(None, 20, 'bold'))
        title.pack(pady=5)

        # Botones de navegación
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)

        buttons = [
            ("Buscar Temas", self.show_search_page),
            ("Concepto 1", lambda: self.show_topic("Python")),
            ("Concepto 2", lambda: self.show_topic("Encarta")),
            ("Concepto 3", lambda: self.show_topic("Tkinter")),
            ("Micro-Operaciones", lambda: self.show_topic("MicroOperaciones")),
            ("Circuitos Lógicos", lambda: self.show_topic("CL")),
            ("Assemblr", lambda: self.show_topic("Assemblr")),
            ("Salir", self.quit)
        ]

        for i, (text, command) in enumerate(buttons):
            btn = ttk.Button(button_frame, text=text, command=command)
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)

    def show_search_page(self):
        if self.main_frame:
            self.main_frame.pack_forget()
        if self.search_frame:
            self.search_frame.pack_forget()

        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(fill=tk.BOTH, expand=True)

        # Botón de regreso
        back_button = ttk.Button(self.search_frame, text="← Volver al inicio", command=self.show_main_menu)
        back_button.pack(anchor=tk.W, padx=10, pady=5)

        paned = ttk.Panedwindow(self.search_frame, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)

        nav_frame = ttk.Frame(paned, width=200)
        paned.add(nav_frame, weight=1)

        ttk.Label(nav_frame, text="Buscar:").pack(padx=5, pady=(5, 0), anchor=tk.W)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(nav_frame, textvariable=self.search_var)
        search_entry.pack(fill=tk.X, padx=5)
        search_entry.bind('<KeyRelease>', self.update_list)

        self.topic_list = tk.Listbox(nav_frame)
        self.topic_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.topic_list.bind('<<ListboxSelect>>', self.display_topic)

        self.populate_list()

        content_frame = ttk.Frame(paned)
        paned.add(content_frame, weight=4)

        self.title_label = ttk.Label(content_frame, text="Seleccione un tema", font=(None, 16, 'bold'))
        self.title_label.pack(pady=10)

        text_container = ttk.Frame(content_frame)
        text_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.content_text = tk.Text(text_container, wrap=tk.WORD)
        self.content_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(text_container, orient=tk.VERTICAL, command=self.content_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.content_text.config(yscrollcommand=scrollbar.set)

    def show_topic(self, topic):
        self.show_search_page()
        self.search_var.set(topic)
        self.update_list()
        self.topic_list.selection_set(0)
        self.display_topic()

    def populate_list(self):
        self.topic_list.delete(0, tk.END)
        for topic in sorted(ENCYCLOPEDIA_DATA.keys()):
            self.topic_list.insert(tk.END, topic)

    def update_list(self, event=None):
        query = self.search_var.get().lower()
        filtered = [t for t in ENCYCLOPEDIA_DATA if query in t.lower()]
        self.topic_list.delete(0, tk.END)
        for topic in sorted(filtered):
            self.topic_list.insert(tk.END, topic)

    def display_topic(self, event=None):
        selection = self.topic_list.curselection()
        if not selection:
            return
        topic = self.topic_list.get(selection[0])
        data = ENCYCLOPEDIA_DATA.get(topic)
        if data:
            self.title_label.config(text=data['title'])
            self.content_text.delete(1.0, tk.END)
            self.content_text.insert(tk.END, data['content'])

            # Si existe un Label (imagen) para el tema, mostrarla
            if 'Label' in data:
                try:
                    image_path = data['Label']
                    img = Image.open(image_path)
                    img = img.resize((500, 400))
                    self.topic_photo = ImageTk.PhotoImage(img)

                    # Si ya existe una imagen previa, eliminarla
                    if hasattr(self, 'topic_image_label') and self.topic_image_label.winfo_exists():
                        self.topic_image_label.destroy()

                    # Crear y mostrar imagen nueva
                    self.topic_image_label = ttk.Label(self.search_frame, image=self.topic_photo)
                    self.topic_image_label.pack(pady=10)

                except Exception as e:
                    messagebox.showwarning("Imagen no encontrada", f"No se pudo cargar la imagen: {e}")
            else:
                # Si no hay imagen para el tema, eliminar la previa si existe
                if hasattr(self, 'topic_image_label') and self.topic_image_label.winfo_exists():
                    self.topic_image_label.destroy()
        else:
            messagebox.showerror("Error", f"No se encontró información para '{topic}'.")

if __name__ == '__main__':
    app = EncartaApp()
    app.mainloop()
