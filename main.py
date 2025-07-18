import re
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Necesario para manejar imágenes


# Sample data: topics and their content
ENCYCLOPEDIA_DATA = {

    "Prueba": {
        "title": "Bienvenido a ARCHI: Prueba imagenes",
        "content": (
            "ARCHI es un asistente virtual diseñado para ayudarte a explorar temas relacionados con sistemas digitales y analógicos, micro-operaciones, circuitos lógicos y más. "
            "Utiliza el menú principal para navegar por los temas o utiliza la función de búsqueda para encontrar información específica."
            "\n[IMAGE:micro.png]"
            "[IMAGE:micro.png] Más texto."
        ),
    },

    "ANALOGICO": {
        "title": "Representaciones Analógicas",
        "content": (
            "En la representación analógica una cantidad se representa mediante un indicador proporcional que varía en forma continua. Un ejemplo es el velocímetro de los automóviles clásicos de las décadas de 1960 o 1970. La deﬂexión de la aguja es proporcional a la velocidad del automóvil y sigue cualquier cambio que se produzca a medida que el vehículo aumente o reduzca su velocidad. En los automóviles antiguos se utilizaba un eje mecánico ﬂexible para conectar la transmisión con el velocímetro en el tablero. Es interesante observar que en automóviles recientes, por lo general, se preﬁere la representación analógica, aun y cuando la velocidad ahora se mide en forma digital."
            "Por ejemplo: [IMAGE:computer.png]"
        ),
    },
    "DIGITAL": {
        "title": "Representaciones Digitales",
        "content": (
            "En la representación digital las cantidades se representan no mediante indicadores que varían en forma continua, sino mediante símbolos llamados dígitos."
            "Considere como ejempo el reloj digital, que indica la hora del día en forma de dígitos decimales que representan horas y minutos."
            "Como es sabido, la hora del día cambia en forma continua pero la lectura del reloj digital no cambia así, sino que cambia en intervalos de uno por minuto (o por segundo)."
            "En otras palabras, esta representación digital de la hora del día cambia en incrementos discretos en comparación con la repressentación de la hora que proporciona un reloj de pared operado mediante corriente alterna analógica, donde la lectura cambia en forma continua."

        ),
    },
    "SISTEMAS": {
        "title": "Sistemas Digitales y Analógicos",
        "content": (
               "Un sistema digital es la combinación de dispositivos diseñados para manipular información lógica o cantidades físicas que se representan en forma digital; es decir, las cantidades solo pueden tener valores discretos."
            "Estos dispositivos, por lo general, son electrónicos, pero también pueden ser mecánicos, magnétivos o neumáticos. Algunos de los sistemas digitales más comunes son las computadoras y las calculadoras digitales, los equipos de audio y video digital y el sistema telefónico."
            "Un sistema analógico contiene dispositivos que manipulan cantidades físicas que se representan en forma analógica."
            "En un sistema analógico, las cantidades pueden variar sobre un intervalo continuo de valores."
            "Por ejemplo, la amplitud de la señal de salida a la bocina en un receptor de radio puede tener cualquier valor entre cero y su límite máximo."
        ),
    },

    "DECIMAL": {
        "title": "Sistemas Numéricos Digitales",
        "content": (
            "Sistema decimal"
            "Está compuesto de 10 números o símbolos. Estos 10 símbolos son: 0,1,2,3,4,5,6,7,8,9; al utilziarlos como dígitos de un número, podemos expresar cualquier cantidad."
            "EL sistema decimal se conoce también como sistema de base 10 ya que tiene 10 dígitos y ha evolucionado en forma natural debido al hecho de que las personas tenemos 10 dedos."
            "EL decimal es un sistema de valor posicional, en el cual el valor de un dígito depende de su posición."
            "Dicho de forma rigurosa, las diversas posiciones relaticas al punto decimal llevan pesos que pueden expresarse como potencias de 10."
            ""
            "Conteo Decimal"
            "Al contar en el sistema decimal, empezamos con 0 en la posición de las unidades y tomamos cada símbolo (dígito) en forma progresiva hasta llegar al 9."
            "Luego agregamos un 1 a la siguiente posición más alta y empezamos de nuevo con 0 en la primera posición."
            "Este proceso continúa hasta llefar al conteo de 99."
            "EL mismo patrón se sigue hasta llegar al número que deseamos contar."
        ),
    },
    "BINARIO": {
        "title": "Sistema Binario",
        "content": (
            "Para los sistemas digitales, el sistema numérico decimal no se presta para una implementación conveniente."
            "Por ejemplo, es muy difícil diseñar equipo electŕonico de manera que pueda trabajar con 10 niveles de voltaje distintos."
            "Por otro lado, es muy sencillo diseñar circuitos electrónicos simples y rpecisos que operen solo con dos niveles de voltaje."
            "Por esta razón casi cualquier sistema digital utiliza el sistema numérico binario como el sistema básico de sus operaciones."
            "En el sistema binario solo hay dos posibles valores de dígitos: 0 y 1."
            ""
            "Conteo Binario"
            "Por lo general, al tratarse de números binarios, nos restringimos a un número específico de bits."
            "Comenzando con todos los bits en cero, conocido como cuenta cero."
            "Para cada cuenta sucesiva se alterna la posición de las unidades; es decir, cambia de un valor binario al otro."
        ),
    },
    "CIRCUITOS": {
        "title": "Circuitos Digitales / Circuitos Analógicos",
        "content": (
            "Los circuitos digitales están diseñados para producir voltajes de salida que se encuentren dentro de los intervalos de voltaje prescritos para 0 y 1."
            "Estos están diseñados para responder en forma predecible a los voltajes de entrada que se encuentran dentro de los intervalos definidos de 0 y 1."
            "Esto significa "
        ),
    },

    "MICRO_OPERACIONES": {
        "title": "Micro Operaciones",
        "content": (
           " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque mi eros, feugiat eget orci qis, sodales imperdiet mauris. Maecenas et arcu maximus, egestas odio a, aliquam augue. Donec magna lorem, finibus in euismod nec, rhoncus at ligula. Curabitur nec dui quis lectus tincidunt tristique eu id risus. Nam a dolor a lorem placerat laoreet. Proin ut lobortis purus. Pellentesque sed malesuada lorem, nec mollis magna. Morbi vel odio eu massa laoreet semper. Fusce vitae dapibus velit. Aliquam erat volutpat. Nullam et cursus nunc, accumsan feugiat ex. Suspendisse eget diam vitae lacus bibendum facilisis. Mauris dapibus ligula a odio sodales faucibus. Curabitur blandit dignissim sapien, vel rhoncus erat aliquet quis. Suspendisse varius velit luctus, lacinia erat in, faucibus ligula. Nam in eros a nisl tempus varius sagittis vel diam. Duis dignissim tristique mi, pulvinar malesuada odio. Donec eu tellus ac orci maximus pharetra vitae nec augue. In accumsan, dolor sit amet ornare consequat, massa odio bibendum eros, non imperdiet ante erat et velit. Quisque eu ipsum id neque laoreet placerat et varius tellus. Vivamus posuere sem dui, sit amet luctus augue finibus ac. Mauris ultricies, elit a dapibus efficitur, urna justo venenatis metus, at aliquet augue nibh eu magna. Sed id scelerisque lacus, ac finibus erat. Morbi blandit leo eget sapien pulvinar dapibus. Nam fringilla ac arcu sit amet vulputate. Nulla a enim in lectus gravida vehicula lacinia in diam. Praesent tellus purus, efficitur et urna quis, suscipit gravida dolor. In nec orci sit amet enim placerat lobortis. Maecenas malesuada libero ut purus feugiat, nec aliquet orci elementum. Ut posuere diam lobortis, pretium elit et, sodales ante. Morbi tempus risus vestibulum velit efficitur faucibus. Curabitur luctus congue pharetra. Quisque sagittis libero velit, vitae maximus lorem finibus nec. Morbi sed viverra augue. Fusce vestibulum ex eget egestas efficitur. Nam vulputate tempus nibh, id elementum ipsum commodo sed. Aliquam erat volutpat. Nunc non dignissim ante. Pellentesque consequat, nulla quis suscipit elementum, nunc purus dapibus magna, eu blandit eros orci sed mauris. Phasellus vulputate dolor eget tincidunt vehicula. Integer a faucibus felis. Phasellus tristique et dolor sed fermentum. Integer id tincidunt felis, et tincidunt ligula. Proin lacinia, orci id viverra feugiat, mauris elit efficitur justo, nec pellentesque risus ex eget massa. Integer eleifend accumsan urna sit amet pharetra. Donec auctor vitae risus non sollicitudin. Nunc eu ipsum nunc. Donec ornare felis a nulla semper elementum nec ut quam. Etiam est augue, commodo finibus ullamcorper eget, volutpat sagittis libero. Pellentesque ac pulvinar quam. Curabitur dictum congue lacinia. Donec imperdiet felis vel tortor consectetur, vel rutrum sem dignissim. In sollicitudin turpis non ligula porttitor rhoncus. Aenean ac condimentum mauris. Pellentesque et lobortis felis. Quisque id lorem a lorem suscipit sagittis nec id sapien. Integer eleifend porttitor mattis. Pellentesque nibh mi, finibus sed leo non, laoreet euismod sem. Phasellus nec nunc porta, vulputate arcu eu, vulputate purus. "
        ),
        "Label" : "micro.png"
    },
    "CL": {
        "title": "Circuitos Logicos",
        "content": (
            "Circuitos Logicos"
        ),
    },
    "ASSEMBLER": {
        "title": "Assembler",
        "content": (
            "Assemblr"
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
            ("PRUEBA", lambda: self.show_topic("Prueba")),
            ("REPRESENTACIONES", lambda: self.show_topic("ANALOGICO", "DIGITAL")),
            ("SISTEMAS", lambda: self.show_topic("SISTEMAS","DECIMAL", "BINARIO", "CIRCUITOS")),
            ("Micro-Operaciones", lambda: self.show_topic("MICRO_OPERACIONES")),
            ("Circuitos Lógicos", lambda: self.show_topic("CL")),
            ("Assembler", lambda: self.show_topic("ASSEMBLER")),
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

    def show_topic(self, *topics):  # <-- MOVE THIS INSIDE THE CLASS
        self.show_search_page()
        combined_title = " + ".join([ENCYCLOPEDIA_DATA[t]['title'] for t in topics if t in ENCYCLOPEDIA_DATA])
        self.search_var.set("")  # Clear search
        self.update_list()
        self.title_label.config(text=combined_title)
        self.content_text.delete(1.0, tk.END)

        # Remove any previous image label widget if present
        if hasattr(self, 'topic_image_label') and self.topic_image_label.winfo_exists():
            self.topic_image_label.destroy()

        # Store references to images to prevent garbage collection
        self._text_images = []

        # Combine all content
        combined_content = "\n\n".join([ENCYCLOPEDIA_DATA[t]['content'] for t in topics if t in ENCYCLOPEDIA_DATA])

        # Regex to find [IMAGE:filename]
        parts = re.split(r'(\[IMAGE:.*?\])', combined_content)
        for part in parts:
            match = re.match(r'\[IMAGE:(.*?)\]', part)
            if match:
                image_path = match.group(1).strip()
                try:
                    img = Image.open(image_path)
                    img = img.resize((400, 250))
                    photo = ImageTk.PhotoImage(img)
                    self.content_text.image_create(tk.END, image=photo)
                    self._text_images.append(photo)  # Prevent GC
                    self.content_text.insert(tk.END, '\n')
                except Exception as e:
                    self.content_text.insert(tk.END, f"[No se pudo cargar la imagen: {image_path}]\n")
            else:
                self.content_text.insert(tk.END, part)
    
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
