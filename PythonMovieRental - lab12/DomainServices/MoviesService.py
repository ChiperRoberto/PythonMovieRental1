import random
import string

from DomainModel.Movie import Movie
from Infrastructure.Errors.RepoError import RepoError


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
        n = 0
        for n in range(nr_movies):
            movieId = random.randrange(0, 10000)
            length = 7
            letters = string.ascii_lowercase
            movieName = ''.join(random.choice(letters) for i in range(length))
            movieCategory = ''.join(random.choice(letters) for i in range(length))
            movieDescription = ''.join(random.choice(letters) for i in range(length))
            movie = Movie(movieId, movieName, movieCategory, movieDescription)
            while movie in self.getAllMovies():
                self.generateMoviesService(nr_movies)
                return
            self.__moviesRepo.add(movie)

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

    def ordonare_dupa_nr(self, list):
        """
        Ordoneaza clientii dupa numarul de inchirieri.
        :return: clients - lista
        """
        gap = len(list)
        swaps = True
        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))
            swaps = False
            for i in range(len(list) - gap):
                j = i + gap
                if int(list[i].GetInchirieri()) > int(list[j].GetInchirieri()):
                    list[i], list[j] = list[j], list[i]
                    swaps = True
        return list

    def ordonare_dupa_nr_gen(self, list):
        gap = len(list)
        swaps = True
        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))
            swaps = False
            for i in range(len(list) - gap):
                j = i + gap
                if int(list[i].GetInchirieri()) > int(list[j].GetInchirieri()):
                    list[i], list[j] = list[j], list[i]
                    swaps = True
                elif int(list[i].GetInchirieri()) == int(list[j].GetInchirieri()):
                    if list[i].GetCategory() > list[j].GetCategory():
                        list[i], list[j] = list[j], list[i]
                        swaps = True
        return list

    def primi_30_la_suta(self):
        """
        Returneaza primi 30% clienti dupa nr inchirieri
        :return: clients - lista
        """
        list = self.getAllMovies()
        clients = self.ordonare_dupa_nr(list)
        return clients[int(0.7 * len(clients)):]
