# Task: Obtaining the Data
class quote:
    id: int
    movie: str
    lines: str
    year: str
 
    def __init__(self, id: int, movie: str, lines: str, year: str):
        self.id = id
        self.movie = movie
        self.lines = lines
        self.year = year