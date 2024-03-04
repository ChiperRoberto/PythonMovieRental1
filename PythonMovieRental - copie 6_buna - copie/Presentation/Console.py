from Infrastructure.Errors.RepoError import RepoError
from DomainModel.Errors.ValidError import ValidError

class UI():

    def __init__(self, moviesService, clientsService, rentalService):
        self.__moviesService = moviesService
        self.__clientsService = clientsService
        self.__rentalService = rentalService
        self.__commands = {
            "add_movie_for_rental":self.__ui_AddMovieForRental,
            "remove_movie_from_rental":self.__ui_RemoveMovieFromRental,
            "update_movie_name":self.__ui_UpdateMovieName,
            "generate_random_movies": self.__ui__generateMovies,
            "search_movie_by_id":self.__ui__searchMovieById,
            "print_movies":self.__ui_PrintMovies,
            "add_client":self.__ui_AddClient,
            "remove_client":self.__ui_RemoveClient,
            "update_client":self.__ui_UpdateClient,
            "generate_random_clients":self.__ui__GenerateClients,
            "search_client_by_id":self.__ui__searchClientById,
            "print_clients":self.__ui_PrintClients,
            "add_rental":self.__ui__RentMovie,
            "print_rentals":self.__ui__printRentals,
            "ordonare_dupa_nume":self.__ui__ordonare_dupa_nume,
            "ordonare_dupa_nr_inchirieri":self.__ui__orodnare_dupa_nr_inchirieri,
            "primi_30%":self.__ui__primi30,
            "cele_mai_inchiriate":self.__ui__cele_mai_inchiriate,
            "cel_mai_putin_inchiriat":self.__ui__cel_mai_putin_inchiriat
        }

    def     __ui__RentMovie(self):
        """
        Rent a movie
        :return:
        """
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        movieId = int(self.__params[0])
        clientId = int(self.__params[1])
        self.__rentalService.rentMovie(movieId, clientId)
        print("Film inchiriat cu succes!")

    def __ui__printRentals(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        rentals = self.__rentalService.getAll()
        if len(rentals) == 0:
            print("Nu exista inchirieri in aplicatie!")
            return
        for rental in rentals:
            print(rental)


    def __ui_UpdateMovieName(self):
        """
        Modifica numele unui film din dictionar.
        :return:
        """
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        movieId = int(self.__params[0])
        name = self.__params[1]
        self.__moviesService.updateMovieName(movieId, name)
        print("film modificat cu succes!")


    def __ui_RemoveMovieFromRental(self):
        """
        Sterge un film din dictionar.
        :return:
        """
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        movieId = int(self.__params[0])
        self.__moviesService.removeMovieFromRental(movieId)
        print(f"filmul cu idul {movieId} a fost scos de la inchiriere cu succes!")

    def __ui_AddMovieForRental(self):
        """
        Adauga un film in dictionarul de filme pentru inchiriat
        param1:Id
        param2:Nume
        param3:Gen
        param4:Descriere
        :return:
        """
        if len(self.__params) < 4:
            print("numar parametri invalid!")
            return
        movieId = int(self.__params[0])
        name = self.__params[1]
        category = self.__params[2]
        description = self.__params[3]
        self.__moviesService.addMovieForRental(movieId, name, category, description)
        print("film adaugat cu succes!")

    def __ui__generateMovies(self):
        """
        Genereaza un nr dat de la tastatura de filme.
        :return:
        """
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        nr_movies = int(self.__params[0])
        self.__moviesService.generateMoviesService(nr_movies)
        print("Generarea a avut succes!")

    def __ui__searchMovieById(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        movieId =int( self.__params[0])
        movie = self.__moviesService.searchById(movieId)
        print(movie)

    def __ui__searchClientById(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        clientId =int( self.__params[0])
        client = self.__clientsService.searchById(clientId)
        print(client)

    def __ui_PrintMovies(self):
        """
        Afiseaza toate filmele din dictionar.
        :return:
        """
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        movies = self.__moviesService.getAllMovies()
        if len(movies) == 0:
            print("nu exista filme in aplicatie!")
            return
        for movie in movies:
            print(movie)


    def __ui_AddClient(self):
        """
        Adauga client.
        param1:ID
        param2:Nume
        :return:
        """
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        clientId = int(self.__params[0])
        clientName = self.__params[1]
        self.__clientsService.addClient(clientId, clientName)
        print("Client adaugat cu succes!")

    def __ui_UpdateClient(self):
        """
        Modifica numele unui client din dictionar.
        :return:
        """
        if len(self.__params) !=2:
            print("Numar parametri invalid!")
            return
        clientId = int(self.__params[0])
        clientName = self.__params[1]
        self.__clientsService.updateClientName(clientId, clientName)
        print("client modificat cu succes!")

    def __ui__GenerateClients(self):
        """
        Genereaza un nr dat de la tastatura de clienti.
        :return:
        """
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        nrClients = int(self.__params[0])
        self.__clientsService.generateClientsService(nrClients)
        print("Generarea a avut loc cu succes!")

    def __ui_PrintClients(self):
        """
        Afiseaza toti clientii din dictionar.
        :return:
        """
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        clients = self.__clientsService.getAllClients()
        if len(clients) == 0:
            print("nu exista clienti in aplicatie!")
            return
        for client in clients:
            print(client)

    def __ui_RemoveClient(self):
        """
        Sterge un client din dictionar daca acesta exista.
        :return:
        """
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        clientId = int(self.__params[0])
        self.__clientsService.RemoveClient(clientId)
        print(f"clientul cu idul {clientId} a fost scos de la inchiriere cu succes!")

    def __ui__ordonare_dupa_nume(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return

        list = self.__clientsService.ordonare_dupa_nume()
        print(list)
        for client in list:
            print(client)

    def __ui__orodnare_dupa_nr_inchirieri(self):
        """

        :return:
        """
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return

        list = self.__clientsService.ordonare_dupa_nr()
        if len(list) == 0:
            print("Nu exista inchirieri!")
            return
        for client in list:
            print(client)

    def __ui__primi30(self):
        """
        Afiseaza primii 30% clienti care au inchiriat filme.
        :return:
        """
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return

        list = self.__clientsService.primi_30_la_suta()
        if len(list) == 0:
            print("Nu exista inchirieri!")
            return
        for client in list:
            print(client)

    def __ui__cele_mai_inchiriate(self):
        """
        Afiseaza cele mai inchiriate filme.
        :return:
        """
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return

        list = self.__moviesService.cele_mai_inchiriate()
        if len(list) == 0:
            print("Nu exista inchirieri!")
            return
        for movie in list:
            print(movie)


    def __ui__cel_mai_putin_inchiriat(self):
        """
        Afiseaza cele mai putin inciriate filme.
        :return:
        """
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return

        list = self.__moviesService.cel_mai_putin_inchiriat()
        if len(list) == 0:
            print("Nu exista inchirieri!")
            return
        movie = list[0]
        print(f"Cel mai putin inchiriat film este {movie}")
        #print(f"Cel mai putin inchiriat film este {self.__moviesService.cel_mai_putin_inchiriat().GetId}")

    def run(self):
        while True:
            command = input(">>>")
            command = command.strip()
            if command == "":
                continue
            if command == "exit":
                return
            parti = command.split()
            command_name = parti[0]
            self.__params = parti[1:]
            if command_name in self.__commands:
                try:
                    self.__commands[command_name]()
                except ValueError:
                    print("Eroare UI: tip numeric invalid")
                except ValidError as ve:
                    print(f"Valid Error:{ve}")
                except RepoError as re:
                    print(f"Repo Error:{re}")
            else:
                print("comanda invalida!")






















""" Add-urile mai au nevoie de ajustare in cazul in care vrem sa adaugam un client care a fost sters deja, nu cred ca voi face asta vreodata dar macar sa stiu ca am observat treaba asta la un moment dat. :)
"""