class Libro:
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self. anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas
    
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")
        print(f"Número de páginas: {self.numero_paginas}")
        
l1 = Libro("El Alquimista", "Paulo Coelho", 1994, 192)
l1.mostrar_informacion()