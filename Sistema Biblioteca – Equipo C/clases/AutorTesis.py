class AutorTesis:
    def __init__(self, autor, tesis):
        self.Autor = autor
        self.Tesis = tesis

        autor.getTesis().append(self)
        tesis.getAutor().append(self)

    def __str__(self):
        return f"AutorLibro: ({self.Autor.getNombre()}, {self.Tesis.getID()})"
