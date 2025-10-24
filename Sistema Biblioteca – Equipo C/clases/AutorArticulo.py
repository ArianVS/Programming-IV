class AutorArticulo:
    def __init__(self, autor, articulo):
        self.Autor = autor
        self.Articulo = articulo

        autor.getArticulos().append(self)
        articulo.getAutor().append(self)

    def __str__(self):
        return f"AutorLibro: ({self.Autor.getNombre()}, {self.Articulo.getDOI()})"
