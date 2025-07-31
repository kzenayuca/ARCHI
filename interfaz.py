# Importación de contenidos
from INFORMACION import ENCYCLOPEDIA_DATA
import tkinter.font as tkFont

# Librerías para el manejo de separaciones de texto y manejo de URLs
import re
import webbrowser

# Librería para personalizar widgets 
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

# Librería para manejo de imágenes
from customtkinter import CTkImage
from PIL import Image, ImageTk


class EncartaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ARCHI: Asistente Virtual")
        self.geometry("900x720")

        self.set_styles()               # ====> Estilo general de la interfaz

        self.topic_map = {}             # ====> Mapeo de los temas
        self.bg_img = CTkImage(Image.open("Imagenes/main_bg.png").resize((900,720)))

        self.main_frame = None
        self.search_frame = None
        self.show_main_menu()           # ====> Muestra los widgets de la interfaz



    def set_styles(self):
        ctk.set_appearance_mode("light")            # Options: "light", "dark", "system"
        ctk.set_default_color_theme("blue")
        self.default_font = ctk.CTkFont(family="Arial", size=16, weight="bold") 


    def show_main_menu(self):
        if self.search_frame:
            self.search_frame.pack_forget()
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent", width=900, height=720)              # Frame principal
        self.main_frame.pack(fill="both", expand=True)

        bg_label = ctk.CTkLabel(self.main_frame, image=self.bg_img, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Establecer 3 columnas para organizar el contenido de la interfaz
        columns_frame = ctk. CTkFrame(self.main_frame, fg_color="transparent")
        columns_frame.pack(fill="both", expand=True)
        columns_frame.rowconfigure(0, weight=1)
        columns_frame.columnconfigure((0,1,2), weight=1)

        # Configuración inicial de las 3 columnas
        left_frame = ctk.CTkFrame(columns_frame, fg_color="transparent", corner_radius=0)
        center_frame = ctk.CTkFrame(columns_frame, fg_color="transparent", corner_radius=0)
        right_frame = ctk.CTkFrame(columns_frame, fg_color="transparent", corner_radius=0)

        # ==== Columna 1: botones izquierda ====
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 10))
        left_inner = ctk.CTkFrame(left_frame, fg_color="transparent")
        left_inner.pack(expand=True)

        botones_izquierda = [
            ("Arquitectura de Computadores", lambda: self.show_topic("  Arquitectura de computadores")),
            ("Sistemas Numéricos", lambda: self.show_topic("  Sistemas numéricos")),
            ("Electrónica Digital y Circuitos Lógicos", lambda: self.show_topic("  Electrónica digital y circuitos lógicos")),
        ]

        for text, command in botones_izquierda:
            btn = ctk.CTkButton(left_inner, text=self.wrap_text(text), command=command, width=200, corner_radius=10, font=self.default_font, height=50)
            btn.pack(pady=30, fill="x")

        # ==== Columna 2: imagen de portada y botones de búsqueda y salida ====
        center_frame.grid(row=0, column=1, sticky="nsew", padx=10)
        center_inner = ctk.CTkFrame(center_frame, fg_color="transparent")
        center_inner.grid(row=0, column=0, sticky="nsew")
        center_frame.columnconfigure(0, weight=1)
        center_frame.rowconfigure(0, weight=1)

        center_inner.rowconfigure(0, weight=1)      #filas invisibles
        center_inner.rowconfigure(4, weight=1)

        # Título: ARCHI
        title = ctk.CTkLabel(center_inner, text="ARCHI", font=('padmaa-Bold.1.1', 80, "bold"), text_color="#2c3e50")
        title.grid(row=0, column=0, pady=30, padx=30)

        # Imagen centrada
        try:
            self.image = Image.open("Imagenes/interfaz-imagen.png").resize((383, 256))
            self.photo = CTkImage(light_image=self.image, size=(383, 256))
            self.image_label = ctk.CTkLabel(center_inner, image=self.photo, text="")
            self.image_label.grid(row=2, column=0, pady=30)
        except:
            self.image_label = ctk.CTkLabel(center_inner, text="[Imagen no disponible]", font=self.default_font)
            self.image_label.grid(row=2, column=0, pady=10)

        botones_centro = [
            ("Buscar Temas", self.show_search_page),
            ("Salir", self.quit),
        ]

        for i, (text, command) in enumerate(botones_centro):
            btn = ctk.CTkButton(center_inner, text=self.wrap_text(text), command=command, width=200, corner_radius=10, font=self.default_font, height=50)
            btn.grid(row=3+i, column=0, pady=30)

        # ==== Columna 3: botones derecha ====
        right_frame.grid(row=0, column=2, sticky="nsew", padx=(10,20))
        right_frame.rowconfigure(0, weight=1)

        right_inner = ctk.CTkFrame(right_frame, fg_color="transparent")
        right_inner.pack(expand=True)

        botones_derecha = [
            ("Sistemas Digitales Analógicos", lambda: self.show_topic("  Sistemas digitales y sistemas analógicos")),
            ("Microoperaciones", self.show_microoperaciones),
            ("Assembler", lambda: self.show_topic("  Assembler")),
        ]

        for text, command in botones_derecha:
            btn = ctk.CTkButton(right_inner, text=self.wrap_text(text), command=command, width=200, corner_radius=10, font=self.default_font, height=50)
            btn.pack(pady=30, fill="x")


    def show_microoperaciones(self):
        self.show_search_page()
        self.search_var.set("")  # Limpia la entrada de búsqueda
        self.update_list()
        self.title_label.configure(text="Microoperaciones")

        # Mostrar descripción e imágenes con insert_content_with_images
        description = ENCYCLOPEDIA_DATA.get("  Microoperaciones y nivel RTL", {}).get("content", "")
        self.insert_content_with_images(description)

        # Slides: solo agrega después del texto
        self.micro_images = ["prueba1.jpeg", "prueba2.jpeg", "prueba3.jpeg"]
        self.micro_index = 0
        self.slide_frame = ctk.CTkFrame(self.content_text, fg_color="transparent")
        self.content_text.window_create(tk.END, window=self.slide_frame)
        self.update_slide_frame()

    def update_slide_frame(self):
        # Limpia el frame
        for widget in self.slide_frame.winfo_children():
            widget.destroy()
        # Muestra la imagen
        img_path = self.micro_images[self.micro_index]
        try:
            img = Image.open(img_path).resize((400, 250))
            self.micro_photo = CTkImage(light_image=img, size=(400, 250))
            img_label = ctk.CTkLabel(self.slide_frame, image=self.micro_photo, text="")
            img_label.pack()
        except Exception as e:
            err_label = ctk.CTkLabel(self.slide_frame, text=f"No se pudo cargar la imagen: {img_path}")
            err_label.pack()
        # Botones
        btn_frame = ctk.CTkFrame(self.slide_frame, fg_color="transparent")
        btn_frame.pack()
        prev_btn = ctk.CTkButton(btn_frame, text=self.wrap_text("Anterior"), command=self.show_prev_micro_image)
        prev_btn.pack(side="left", padx=5)
        next_btn = ctk.CTkButton(btn_frame, text=self.wrap_text("Siguiente"), command=self.show_next_micro_image)
        next_btn.pack(side="left", padx=5)

    def show_micro_image(self):
        self.update_slide_frame()

    def show_next_micro_image(self):
        if self.micro_index < len(self.micro_images) - 1:
            self.micro_index += 1
            self.show_micro_image()

    def show_prev_micro_image(self):
        if self.micro_index > 0:
            self.micro_index -= 1
            self.show_micro_image()


    def show_search_page(self):
        if self.main_frame:
            self.main_frame.pack_forget()
        if self.search_frame:
            self.search_frame.pack_forget()

        self.search_frame = ctk.CTkFrame(self, fg_color="transparent", width=900, height=720)          # Contenedor back_button
        self.search_frame.pack(fill="both", expand=True)

        bg_label = ctk.CTkLabel(self.search_frame, image=self.bg_img, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        back_button = ctk.CTkButton(self.search_frame, text=self.wrap_text("← Volver al inicio"), command=self.show_main_menu, height=30)
        back_button.pack(anchor="w", padx=5, pady=5)

        container = ctk.CTkFrame(self.search_frame, fg_color="transparent")     # Contenedor general para navegación y contenido
        container.pack(fill="both", expand=True)

        # ==== Marco de navegación: izquierda ====
        nav_frame = ctk.CTkFrame(container, width=220, fg_color="lightgreen")   # Lista de temas
        nav_frame.pack(fill="y", side="left", padx=5, pady=5)

        left_label = ctk.CTkLabel(nav_frame, text="Buscar:")
        left_label.pack(padx=5, anchor="w")

        self.search_var = ctk.StringVar()                                       # Barra de búsqueda
        search_entry = ctk.CTkEntry(nav_frame, textvariable=self.search_var)
        search_entry.pack(fill="x", padx=5, pady=5)
        search_entry.bind('<KeyRelease>', self.update_list)                     # Autocompletado

        self.topic_list = tk.Listbox(nav_frame, font=('Arial', 12), exportselection=False)
        self.topic_list.pack(fill="both", expand=True, padx=5, pady=5)
        self.topic_list.bind('<<ListboxSelect>>', self.display_topic)
        self.populate_list()                                                    

        # ==== Marco de contenidos: derecha ====
        content_frame = ctk.CTkFrame(container, fg_color="lightblue")
        content_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.title_label = ctk.CTkLabel(content_frame, text="Seleccione un tema", font=ctk.CTkFont(size=20, weight="bold"), fg_color="transparent")
        self.title_label.pack(pady=10)

        text_container = ctk.CTkFrame(content_frame)                            # Cotenido de los temas
        text_container.pack(fill="both", expand=True, padx=10, pady=5)

        self.content_text = tk.Text(text_container, wrap="word", font=('Arial', 14))
        self.content_text.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(text_container, orient="vertical", command=self.content_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.content_text.config(yscrollcommand=scrollbar.set)



    def populate_list(self):
        self.topic_list.delete(0, tk.END)
        self.topic_list.insert(tk.END, "          ")
        self.topic_map.clear()

        for topic in sorted(ENCYCLOPEDIA_DATA.keys()):
            topic_short = self.truncate_text(topic)
            self.topic_list.insert(tk.END, topic_short)
            self.topic_list.insert(tk.END, "          ")
            self.topic_map[topic_short] = topic


    
    def truncate_text(self, text, max_pixel_width=130):
        font = tkFont.Font(font=self.topic_list.cget("font"))
        ellipsis = "..."
        if font.measure(text) <= max_pixel_width:
            return text
        
        for i in range(len(text), 0, -1):
            if font.measure(text[:i] + ellipsis) <= max_pixel_width:
                return text[:i] + ellipsis
        return "..."



    def update_list(self, event=None):
        query = self.search_var.get().lower()
        filtered = [t for t in ENCYCLOPEDIA_DATA if query in t.lower()]
        self.topic_list.delete(0, tk.END)
        self.topic_list.insert(tk.END, "          ")
        self.topic_map.clear()

        for topic in sorted(filtered):
            topic_short = self.truncate_text(topic)
            self.topic_list.insert(tk.END, topic_short)
            self.topic_list.insert(tk.END, "          ")
            self.topic_map[topic_short] = topic



    def display_topic(self, event=None):
        selection = self.topic_list.curselection()
        if not selection:
            return

        topic_index = selection[0]
        if topic_index == 0:
            return

        topic_short = self.topic_list.get(topic_index)
        topic = self.topic_map.get(topic_short)
        if topic_short.strip() == "":
            return

        data = ENCYCLOPEDIA_DATA.get(topic)
        if data:
            self.title_label.configure(text=data['title'])
            self.insert_content_with_images(data['content'])
            url = data.get("url")
            if url:
                link_btn = ctk.CTkButton(self.content_text, text=self.wrap_text("Quizz time!"), command=lambda: webbrowser.open(url), corner_radius=10, fg_color="#4CAF50", hover_color="#45a049")
                self.content_text.window_create(tk.END, window=link_btn)
                self.content_text.insert(tk.END, "\n")
        else:
            messagebox.showerror("Error", f"No se encontró información para '{topic}'.")


    def insert_content_with_images(self, content):
        self.content_text.config(state="normal")
        self.content_text.delete(1.0, tk.END)
        self._text_images = []
        
        # Configurar tags
        self.content_text.tag_configure("padding", lmargin1=30, lmargin2=30, rmargin=30)
        self.content_text.tag_configure("subtitle", font=("Arial", 18, "bold"))
        self.content_text.tag_configure("bold", font=("Arial", 16, "bold"))
        self.content_text.tag_configure("center", justify="center")
        
        self.content_text.insert(tk.END, "\n\n", "padding")
        
        parts = re.split(r'(\[IMAGE:.*?\])|(\[SUBTITLE\].*?\[/SUBTITLE\])|(\[BOLD\].*?\[/BOLD\])', content)
        
        for part in parts:
            if part is None:
                continue
                
            match = re.match(r'\[IMAGE:(.*?)\]', part)
            if match:
                image_path = match.group(1).strip()
                self._insert_centered_image(image_path)
                
            elif re.match(r'\[SUBTITLE\](.*?)\[/SUBTITLE\]', part):
                self.content_text.insert(tk.END, "\n\n\n", "padding")
                subtitle = re.findall(r'\[SUBTITLE\](.*?)\[/SUBTITLE\]', part)[0]
                self.content_text.insert(tk.END, subtitle + "\n\n", ("subtitle", "padding", "center"))
                
            elif re.match(r'\[BOLD\](.*?)\[/BOLD\]', part):
                bold_text = re.findall(r'\[BOLD\](.*?)\[/BOLD\]', part)[0]
                self.content_text.insert(tk.END, bold_text, ("bold", "padding"))
                
            else:
                if part.strip():  # Solo insertar si no está vacío
                    self.content_text.insert(tk.END, part, "padding")
        
        self.content_text.insert(tk.END, "\n\n", "padding")
        self.content_text.config(state="disabled")

    def _insert_centered_image(self, image_path):
        """Inserta una imagen centrada con altura fija de 220px y ancho proporcional"""
        try:
            # Cargar la imagen original
            original_image = Image.open(image_path)
            
            # Calcular nuevas dimensiones manteniendo proporción con altura fija de 220
            target_height = 220
            original_width, original_height = original_image.size
            aspect_ratio = original_width / original_height
            new_width = int(target_height * aspect_ratio)
            
            # Redimensionar la imagen
            resized_image = original_image.resize((new_width, target_height), Image.LANCZOS)
            
            # Convertir a PhotoImage para tkinter
            photo = ImageTk.PhotoImage(resized_image)
            
            # Guardar referencia para evitar que se elimine por el garbage collector
            self._text_images.append(photo)
            
            # Insertar la imagen centrada en el texto
            self.content_text.insert(tk.END, "\n")
            
            # Crear un frame invisible para centrar la imagen
            image_index = self.content_text.index(tk.INSERT)
            
            # Insertar la imagen
            self.content_text.image_create(tk.INSERT, image=photo)
            
            # Aplicar tag de centrado a la línea de la imagen
            line_start = image_index.split('.')[0] + '.0'
            line_end = str(int(image_index.split('.')[0]) + 1) + '.0'
            self.content_text.tag_add("center", line_start, line_end)
            
            self.content_text.insert(tk.END, "\n\n")
            
        except Exception as e:
            print(f"Error cargando imagen {image_path}: {e}")
            # Insertar texto alternativo si la imagen no se puede cargar
            self.content_text.insert(tk.END, "\n[Imagen no disponible]\n\n", ("center", "padding"))
    

    def show_topic(self, *topics):
        self.show_search_page()
        combined_title = " + ".join([ENCYCLOPEDIA_DATA[t]['title'] for t in topics if t in ENCYCLOPEDIA_DATA])
        self.search_var.set("")  # Limpiar la entrada de búsqueda
        self.update_list()
        self.title_label.configure(text=combined_title)

        # Combinar el contenido del tema
        combined_content = "\n\n".join([ENCYCLOPEDIA_DATA[t]['content'] for t in topics if t in ENCYCLOPEDIA_DATA])
        self.insert_content_with_images(combined_content)

        # Si solo hay un topic y tiene URL
        if len(topics) == 1:
            topic = topics[0]
            url = ENCYCLOPEDIA_DATA.get(topic, {}).get("url")
            if url:
                link_btn = ctk.CTkButton(self.content_text, text=self.wrap_text("Quizz time!"), command=lambda: webbrowser.open(url))
                self.content_text.window_create(tk.END, window=link_btn)
                self.content_text.insert(tk.END, "\n")



    def wrap_text(self, text_string, max_chars=20):
        words = text_string.split()
        lines= []
        current_line = ""
        for word in words:
            if len(current_line + " " + word) <= max_chars:
                current_line += (" " if current_line else "") + word
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        return "\n".join(lines)



# Bucle principal
if __name__ == '__main__':
    app = EncartaApp()
    app.mainloop() # Funcion elemental para la ventana principal
