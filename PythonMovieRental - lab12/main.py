from DomainModel import Client, Movie
from DomainServices.RentalService import RentalService
from Infrastructure.FileClientRepo import FileClientRepo
from Infrastructure.FileMovieRepo import FileMovieRepo
from Infrastructure.MovieRepo import MovieRepo
from Infrastructure.ClientRepo import ClientRepo
from Infrastructure.RentalRepo import RentalRepo
from DomainServices.MoviesService import MoviesService
from DomainServices.ClientsService import ClientsService
from Presentation.Console import UI


if __name__ == '__main__':
    moviesPath = "./Infrastructure/movies.txt"
    clientsPath = "./Infrastructure/clients.txt"
    movieRepo = FileMovieRepo(moviesPath)
    clientRepo = FileClientRepo(clientsPath)
    rentalRepo = RentalRepo()
    moviesService = MoviesService(movieRepo)
    clientsService = ClientsService(clientRepo)
    rentalsService = RentalService(clientRepo, movieRepo, rentalRepo)
    console = UI(moviesService, clientsService, rentalsService)
    console.run()
