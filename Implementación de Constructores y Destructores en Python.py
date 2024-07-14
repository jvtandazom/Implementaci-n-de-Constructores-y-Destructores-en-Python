class Persona:
    def __init__(self, clase, problema):
        """Constructor de la clase Persona.
        Inicializa los atributos nombre y edad.
        """
        self.nombre = clase
        self.edad = problema
        print(f"Persona {self.nombre}, de {self.edad} años, ha sido creada.")

    def __del__(self):
        """Destructor de la clase Persona.
        Realiza tareas de limpieza cuando el objeto es destruido.
        """
        print(f"Persona {self.nombre} ha sido destruida.")


class Archivo:
    def __init__(self, nombre_archivo, modo):
        """Constructor de la clase Archivo.
        Abre el archivo especificado en el modo indicado.
        """
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None
        self.abrir_archivo()

    def abrir_archivo(self):
        """Método para abrir el archivo."""
        self.archivo = open(self.nombre_archivo, self.modo)
        print(f"Archivo {self.nombre_archivo} abierto en modo {self.modo}.")

    def escribir(self, datos):
        """Método para escribir datos en el archivo."""
        if self.archivo and not self.archivo.closed:
            self.archivo.write(datos)
            print(f"Datos escritos en {self.nombre_archivo}.")
        else:
            print("El archivo no está abierto para escritura.")

    def leer(self):
        """Método para leer datos del archivo."""
        if self.archivo and not self.archivo.closed:
            return self.archivo.read()
        else:
            print("El archivo no está abierto para lectura.")
            return None

    def __del__(self):
        """Destructor de la clase Archivo.
        Cierra el archivo si está abierto.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo {self.nombre_archivo} ha sido cerrado.")


# Ejemplo de uso de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Ejemplo de uso de la clase Archivo
archivo1 = Archivo("ejemplo.txt", "w")
archivo1.escribir("Hola, aprendiendo a programar en la mejor univercidad UEA.")
del archivo1  # Cierra el archivo explícitamente

archivo2 = Archivo("ejemplo.txt", "r")
contenido = archivo2.leer()
print("Contenido del archivo:", contenido)
del archivo2  # Cierra el archivo explícitamente