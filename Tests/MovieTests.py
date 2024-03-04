from DomainModel.Client import Client
from DomainModel.Errors import ValidError
from DomainModel.Movie import Movie
from DomainModel.Rental import Rental
from DomainServices.ClientsService import ClientsService
from DomainServices.MoviesService import MoviesService
from DomainServices.RentalService import RentalService
from Infrastructure.MovieRepo import MovieRepo
from Infrastructure.ClientRepo import ClientRepo
from Infrastructure.RentalRepo import RentalRepo
import unittest


class MovieTests(unittest.TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()
        self.movieService = MoviesService(self.movieRepo)

    def test_add_movie_for_rental(self):
        self.movieService.addMovieForRental(1, "Film", "comedy", "interesting")
        self.assertEqual(len(self.movieRepo.getAll()), 1)

    def test_remove_movie_from_rental(self):
        self.movieService.addMovieForRental(1, "Film", "comedy", "interesting")
        self.movieService.removeMovieFromRental(1)
        self.assertEqual(len(self.movieRepo.getAll()), 0)

    def test_update_movie_name(self):
        self.movieService.addMovieForRental(1, "Film", "comedy", "interesting")
        self.movieService.updateMovieName(1, "Spiderman")
        self.assertEqual(self.movieRepo.getAll()[0].GetName(), "Spiderman")

    def test_generate_random_movies(self):
        self.movieService.generateMoviesService(10)
        self.assertEqual(len(self.movieRepo.getAll()), 10)

    def test_search_movie_by_id(self):
        self.movieService.addMovieForRental(1, "Film", "comedy", "interesting")
        self.movieService.addMovieForRental(2, "Poezie", "drama", "good")
        self.assertEqual(self.movieRepo.searchById(2).GetName(), "Poezie")

    def test_search_movie_by_id_fail(self):
        with self.assertRaises(Exception):
            self.assertEqual(self.movieRepo.searchById(999).GetName(), "Ion")

    def test_get_movies(self):
        self.assertEqual(self.movieService.getAllMovies(), self.movieRepo.getAll())

    def test_cele_mai_inchiriate(self):
        self.movieService.addMovieForRental(1, "Film", "comedy", "interesting", 5)
        self.movieService.addMovieForRental(2, "Poezie", "drama", "good", 5)
        self.movieService.addMovieForRental(3, "Roman", "comedy", "very interesting", 4)
        self.movieService.addMovieForRental(4, "Carte", "drama", "good", 3)

        movies = self.movieService.cele_mai_inchiriate()
        self.assertEqual(len(movies), 2)
        self.assertEqual(movies[0].GetInchirieri(), 5)
        self.assertEqual(movies[1].GetInchirieri(), 5)

    def test_cele_mai_putin_inchiriate(self):
        self.movieService.addMovieForRental(1, "Film", "comedy", "interesting", 5)
        self.movieService.addMovieForRental(2, "Poezie", "drama", "good", 5)
        self.movieService.addMovieForRental(3, "Roman", "comedy", "very interesting", 4)
        self.movieService.addMovieForRental(4, "Carte", "drama", "good", 3)

        movies = self.movieService.cel_mai_putin_inchiriat()
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].GetInchirieri(), 3)


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.clientRepo = ClientRepo()
        self.clientService = ClientsService(self.clientRepo)

    def test_add_client(self):
        self.clientService.addClient(1, "Ion")
        self.assertEqual(len(self.clientRepo.getAll()), 1)

    def test_remove_client(self):
        self.clientService.addClient(1, "Ion")
        self.clientService.addClient(2, "Alex")
        self.clientService.RemoveClient(1)
        self.assertEqual(len(self.clientRepo.getAll()), 1)
        self.assertEqual(self.clientRepo.getAll()[0].getClientName(), "Alex")

    def test_update_client(self):
        self.clientService.addClient(1, "Ion")
        self.clientService.addClient(2, "Alex")
        self.clientService.updateClientName(2, "George")
        self.assertEqual(self.clientRepo.getAll()[1].getClientName(), "George")

    def test_generate_random_clients(self):
        self.clientService.generateClientsService(10)
        self.assertEqual(len(self.clientRepo.getAll()), 10)

    def test_search_client_by_id(self):
        self.clientService.addClient(1, "Ion")
        self.clientService.addClient(2, "Alex")
        self.assertEqual(self.clientService.searchById(2).getClientName(), "Alex")

    def test_get_clients(self):
        self.assertEqual(self.clientService.getAllClients(), self.clientRepo.getAll())

    def test_ordonare_dupa_nume(self):
        self.clientService.addClient(1, "Ion", 4)
        self.clientService.addClient(2, "Alex", 2)
        self.clientService.addClient(3, "Mircea", 5)
        self.clientService.addClient(4, "Andrei", 1)
        clients = self.clientService.ordonare_dupa_nume()
        names = ["Alex", "Andrei", "Ion", "Mircea"]
        for i in range(len(names)):
            self.assertEqual(clients[i].getClientName(), names[i])

    def test_ordonare_dupa_nr_inchirieri(self):
        self.clientService.addClient(1, "Ion", 4)
        self.clientService.addClient(2, "Alex", 2)
        self.clientService.addClient(3, "Mircea", 5)
        self.clientService.addClient(4, "Andrei", 1)
        clients = self.clientService.ordonare_dupa_nr()
        rentals = [1, 2, 4, 5]
        for i in range(len(rentals)):
            self.assertEqual(clients[i].getNrFilme(), rentals[i])

    def test_primi_30_la_suta(self):
        self.clientService.addClient(1, "Ion", 4)
        self.clientService.addClient(2, "Alex", 2)
        self.clientService.addClient(3, "Mircea", 5)
        self.clientService.addClient(4, "Andrei", 1)
        self.clientService.addClient(5, "Marin", 8)
        self.clientService.addClient(6, "Valentin", 0)
        clients = self.clientService.primi_30_la_suta()
        self.assertEqual(clients[0].getClientName(), "Mircea")
        self.assertEqual(clients[1].getClientName(), "Marin")


class RentalTests(unittest.TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()
        self.movieService = MoviesService(self.movieRepo)
        self.clientRepo = ClientRepo()
        self.clientService = ClientsService(self.clientRepo)
        self.rentalRepo = RentalRepo()
        self.rentalService = RentalService(self.clientRepo, self.movieRepo, self.rentalRepo)

    def test_add_rental(self):
        self.movieService.addMovieForRental(1, "Film", "comedy", "interesting")
        self.movieService.addMovieForRental(2, "Poezie", "drama", "good")
        self.clientService.addClient(1, "Ion")
        self.clientService.addClient(2, "Alex")
        self.rentalService.rentMovie(2, 1)
        rentals = self.rentalRepo.getAll()
        self.assertEqual(len(rentals), 1)
        self.assertEqual(rentals[0].getMovieId(), 2)
        self.assertEqual(rentals[0].getClientId(), 1)
        self.assertEqual(self.clientRepo.getAll()[0].getNrFilme(), 1)
        self.assertEqual(self.movieRepo.getAll()[1].GetInchirieri(), 1)

    def test_get_rentals(self):
        self.assertEqual(self.rentalService.getAll(), self.rentalRepo.getAll())

if __name__ == "__main__":
    unittest.main()
