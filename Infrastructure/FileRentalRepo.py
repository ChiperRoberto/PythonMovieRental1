from DomainModel.Rental import Rental
from DomainServices.RentalService import RentalService
from Infrastructure.RentalRepo import RentalRepo


class FileRentalRepo(RentalRepo):
    def __init__(self, filePath):
        RentalRepo.__init__(self)
        self.__filePath = filePath
        self.__read_all_from_file()

    def __read_all_from_file(self):
        with open(self.__filePath, "r") as f:
            lines = f.readlines()
            self._rentals.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    movieId = parts[0]
                    clientId = parts[1]
                    rental = Rental(movieId, clientId)
                    self._rentals[movieId] = rental

    def __write_all_to_file(self):
        with open(self.__filePath, "w") as f:
            for rental in self._rentals.values():
                f.write(str(rental)+"\n")

    def rentMovie(self, movieId, clientId):
        self.__read_all_from_file()
        RentalService.rentMovie(self,movieId, clientId)
        self.__write_all_to_file()