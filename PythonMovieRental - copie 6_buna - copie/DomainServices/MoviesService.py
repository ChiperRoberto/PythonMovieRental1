import random
import string

from DomainModel.Movie import Movie

class MoviesService:

    def __init__(self, moviesRepo):
        self.__moviesRepo = moviesRepo

    def addMovieForRental(self, movieId, movieName, movieCategory, movieDescription, nrInchirieri=0):
        """
        Adaugare film in dictionarul de filme.
        :param movieId: Id-ul filmului - int
        :param movieName: Numele filmului - string
        :param movieCategory: Categoria filmului - string
        :param movieDescription: Descrierea filmului - string
        :return:
        """
        film = Movie(movieId, movieName, movieCategory, movieDescription, nrInchirieri)
        self.__moviesRepo.add(film)

    def removeMovieFromRental(self, movieId):
        """
        Sterge un film din dictionarul de filme.
        :param movieId: id-ul filmului - int
        :return:
        """
        self.__moviesRepo.delete(movieId)

    def updateMovieName(self, movieId, movieName):
        """
        Modifica un film daca acesta exista
        :param movieId: Id-ul filmului pe care dorim sa-l modificam - int
        :param movieName: Numele modificat - string
        :return: 
        """
        movie = self.__moviesRepo.searchById(movieId)
        movie.SetName(movieName)
        self.__moviesRepo.update(movie)

    def getAllMovies(self):
        return self.__moviesRepo.getAll()

    def generateMoviesService(self, nr_movies):
        """
        Genereaza nr_movies de filme.
        :param nr_movies:
        :return:
        """
        if nr_movies == 0:
            return

        movieId = random.randrange(0, 10000)
        length = 7
        letters = string.ascii_lowercase
        movieName = ''.join(random.choice(letters) for i in range(length))
        movieCategory = ''.join(random.choice(letters) for i in range(length))
        movieDescription = ''.join(random.choice(letters) for i in range(length))
        movie = Movie(movieId, movieName, movieCategory, movieDescription)
        self.__moviesRepo.add(movie)

        self.generateMoviesService(nr_movies - 1)

    def cele_mai_inchiriate(self):
        """
        Returneaza o lista cu cele mai inchiriate filme.
        :return:
        """
        movies = self.getAllMovies()
        most_rented = 0
        for movie in movies:
            most_rented = max(most_rented, movie.GetInchirieri())
        return [movie for movie in movies if movie.GetInchirieri() == most_rented]

    def cel_mai_putin_inchiriat(self):
        """
        Returneaza o lista cu cel mai putin inchiriate filme.
        :return:
        """
        movies = self.getAllMovies()
        least_rented = 1000000
        for movie in movies:
            if movie.GetInchirieri() != 0:
                least_rented = min(least_rented, movie.GetInchirieri())

        return [movie for movie in movies if movie.GetInchirieri() == least_rented]

        #return [movie for movie in movies if movie.GetInchirieri() == least_rented]

    def searchById(self, movieId):
        """
        Cauta un film dupa id.
        :param movieId:
        :return:
        """
        return self.__moviesRepo.searchById(movieId)
