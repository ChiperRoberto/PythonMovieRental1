from DomainModel.Movie import Movie
from Infrastructure.Errors.RepoError import RepoError
class MovieRepo:

    def __init__(self):
        self._movies = {}

    def getAll(self):
        filme = []
        # itereaza DOAR filmele ne-sterse
        for movieId in self._movies:
            if self._movies[movieId].GetIsDeleted() == False:
                filme.append(self._movies[movieId])
        return filme

    def add(self, film):
        """
        Adauga film in dictionarul de filme.
        :param film:
        :return:
        """
        # itereaza DOAR filmele ne-sterse
        if film.GetId() in self._movies and film.GetIsDeleted() == False:
            raise RepoError("film existent!")
        if film.GetIsDeleted() == True:
            film.SetIsDeleted()
        else:
            self._movies[film.GetId()] = film

    def delete(self, movieId):
        if movieId not in self._movies or self._movies[movieId].delete() == True:
            raise RepoError("film inexistent!")
        self._movies[movieId].delete()

    def update(self, film):
        # itereaza DOAR filmele ne-sterse
        if film.GetId() not in self._movies or film.GetIsDeleted() == True:
            raise RepoError("film inexistent!")
        self._movies[film.GetId()] = film

    def searchById(self, movieId):
        # itereaza DOAR filmele ne-sterse
        if movieId not in self._movies or self._movies[movieId].GetIsDeleted() == True:
            raise RepoError("film inexistent!")
        return self._movies[movieId]



    def size(self):
        return len(self._movies)