class AutorLibro:
    def __init__(self, autor, libro):
        self.Autor = autor
        self.Libro = libro

        autor.getLibros().append(self)
        libro.getAutor().append(self)

    def __str__(self):
        return f"AutorLibro: ({self.Autor.getNombre()}, {self.Libro.getTitulo()})"