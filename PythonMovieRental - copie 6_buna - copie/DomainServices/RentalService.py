from DomainModel.Rental import Rental
from datetime import date, timedelta

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