from datetime import date

from DomainModel.Errors.ValidError import ValidError
from Infrastructure.MovieRepo import MovieRepo
from Infrastructure.ClientRepo import ClientRepo
from Infrastructure.Errors.RepoError import RepoError


class Rental:
    #def __init__(self, movieId, clientId, returnDate, clientsRepo:ClientRepo, moviesRepo:MovieRepo):
    def __init__(self, movieId, clientId, clientsRepo: ClientRepo, moviesRepo: MovieRepo):
        self.__movieId = movieId
        self.__clientId = clientId
        self.__rentalDate = date.today()
        #self.__returnDate = returnDate    #trebuie validat
        self.__isReturned = False
        self.__returnedAtDate = None

        self.__clientsRepo = clientsRepo
        self.__moviesRepo = moviesRepo

        self.validate()

    def getMovieId(self):
        return self.__movieId

    def getClientId(self):
        return self.__clientId

    def getIsReturned(self):
        return self.__isReturned

    def setIsReturned(self, TorF):
        self.__isReturned = TorF

    def validate(self):
        errors = ""
        if self.__movieId <= 0:
            errors += "id film incorect!\n"
        #if self.__movieId not in self.__moviesRepo.getAll():
           # errors +="Film inexistent"
        if self.__clientId <= 0:
            errors += "id client incorect!\n"
       # if self.__clientId not in self.__clientsRepo.getAll():
           # errors +="Client inexistent"
        """try:
            clientId = self.__clientId
            self.__clientsRepo.searchById(self.__clientId)
        except RepoError as re:
            errors += re.args
        try:
            movieId = self.__movieId
            self.__moviesRepo.searchById(self, self.__movieId)
        except RepoError as re:
            errors += re.args"""
        if len(errors) > 0:
            raise ValidError(errors)

    def returnMovie(self):
        self.__isReturned = True
        #self.__returnedAtDate = date.today()

    def getUniqueId(self):
        return self.__clientId + self.__movieId

    def __str__(self):
        return f"filmul cu id-ul {self.__movieId} este inchiriat de clientul cu id-ul {self.__clientId}"