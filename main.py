import tkinter as tk
from tkinter import ttk, messagebox

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
}

class EncartaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Encarta-like Encyclopedia")
        self.geometry("800x600")

        # Configure PanedWindow for resizable panels
        paned = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)

        # Left frame: navigation
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

        # Populate topics
        self.populate_list()

        # Right frame: content display
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

    def populate_list(self):
        """Carga todos los temas en la lista de navegación."""
        self.topic_list.delete(0, tk.END)
        for topic in sorted(ENCYCLOPEDIA_DATA.keys()):
            self.topic_list.insert(tk.END, topic)

    def update_list(self, event=None):
        """Filtra los temas según lo escrito en la caja de búsqueda."""
        query = self.search_var.get().lower()
        filtered = [t for t in ENCYCLOPEDIA_DATA if query in t.lower()]
        self.topic_list.delete(0, tk.END)
        for topic in sorted(filtered):
            self.topic_list.insert(tk.END, topic)

    def display_topic(self, event=None):
        """Muestra el título y contenido del tema seleccionado."""
        selection = self.topic_list.curselection()
        if not selection:
            return
        topic = self.topic_list.get(selection[0])
        data = ENCYCLOPEDIA_DATA.get(topic)
        if data:
            self.title_label.config(text=data['title'])
            self.content_text.delete(1.0, tk.END)
            self.content_text.insert(tk.END, data['content'])
        else:
            messagebox.showerror("Error", f"No se encontró información para '{topic}'.")

if __name__ == '__main__':
    app = EncartaApp()
    app.mainloop()
