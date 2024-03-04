from DomainModel.Movie import Movie
from Infrastructure.MovieRepo import MovieRepo


class FileMovieRepo(MovieRepo):
    def __init__(self, filePath):
        MovieRepo.__init__(self)
        self.__filePath = filePath
        self.__read_all_from_file()

    def __read_all_from_file(self):
        with open(self.__filePath, "r") as f:
            lines = f.readlines()
            self._movies.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    movieId = int(parts[0])
                    movieName = parts[1]
                    movieCategory = parts[2]
                    movieDescription = parts[3]
                    nrInchirieri = int(parts[4])
                    #myList = ' '
                    #for x in movieDescription:
                       # myList += ' '+ x
                    movie = Movie(movieId, movieName, movieCategory, movieDescription, nrInchirieri)
                    self._movies[movieId] = movie

    def __write_all_to_file(self):
        with open(self.__filePath, "w") as f:
            for movie in self._movies.values():
                f.write(str(movie)+"\n")

    def add(self, film):
        self.__read_all_from_file()
        MovieRepo.add(self, film)
        self.__write_all_to_file()

    def delete(self, movieId):
        self.__read_all_from_file()
        MovieRepo.delete(self, movieId)
        self.__write_all_to_file()

    def update(self, movie):
        self.__read_all_from_file()
        MovieRepo.update(self, movie)
        self.__write_all_to_file()

    def searchById(self, movieId):
        self.__read_all_from_file()
        return MovieRepo.searchById(self, movieId)

    def getAll(self):
        self.__read_all_from_file()
        return MovieRepo.getAll(self)

    def size(self):
        self.__read_all_from_file()
        return MovieRepo.size(self)