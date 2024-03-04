from Infrastructure.Errors.RepoError import RepoError

class RentalRepo:

    def __init__(self):
        self._rentals = {}

    def add(self, rental):
        self._rentals[rental.getUniqueId()]= rental
        rental.getMovieId()

    def getAll(self):
        rentals = []
        for rental in self._rentals.values():
            rentals.append(rental)
        return rentals