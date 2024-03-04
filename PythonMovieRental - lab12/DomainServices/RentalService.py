from DomainModel.Rental import Rental
from datetime import date, timedelta

from Infrastructure.Errors.RepoError import RepoError


class RentalService:

    def __init__(self, clientsRepo, moviesRepo, rentalRepo):
        self.__clientsRepo = clientsRepo
        self.__moviesRepo = moviesRepo
        self.__rentalRepo = rentalRepo

    def rentMovie(self, movieId, clientId):
        #returnDate = date.today() + timedelta(days=14)
        rental = Rental(
            movieId,
            clientId,
            self.__clientsRepo,
            self.__moviesRepo)

        self.__rentalRepo.add(rental)

        self.__clientsRepo._clients[clientId].inchiriaza()
        self.__moviesRepo._movies[movieId].inchiriaza()

        self.__clientsRepo.update(self.__clientsRepo._clients[clientId])
        self.__moviesRepo.update(self.__moviesRepo._movies[movieId])

    def returnMovie(self, clientId, movieId):
        rental = self.__rentalRepo(movieId, clientId)
        rental.returnMovie()
        self.__rentalRepo.update(rental)

    def getAll(self):
        rentals = []
        for rental in self.__rentalRepo._rentals.values():
            rentals.append(rental)
        return rentals[:]

    def add_recursive(self, lista, inchiriere, i):
        '''

        :param inchiriere:
        :return:
         '''
        if i >= len(lista):
            self.__rentalRepo.add(inchiriere)
            return
        elif lista[i].getId() == inchiriere.getMovieId():
            raise RepoError(" inchiriere deja existenta\n")
        else:
            self.add_recursive(lista, inchiriere, i + 1)