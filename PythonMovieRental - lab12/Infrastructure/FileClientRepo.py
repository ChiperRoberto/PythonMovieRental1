from DomainModel.Client import Client
from Infrastructure.ClientRepo import ClientRepo


class FileClientRepo(ClientRepo):
    def __init__(self, filePath):
        ClientRepo.__init__(self)
        self.__filePath = filePath
        self.__read_all_from_file()

    def __read_all_from_file(self):
        with open(self.__filePath, "r") as f:
            lines = f.readlines()
            self._clients.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    clientId = int(parts[0])
                    clientName = parts[1]
                    nrInchiriate = int(parts[2])
                    client = Client(clientId, clientName, nrInchiriate)
                    self._clients[clientId] = client

    def __write_all_to_file(self):
        with open(self.__filePath, "w") as f:
            for client in self._clients.values():
                f.write(str(client)+"\n")

    def add(self, film):
        self.__read_all_from_file()
        ClientRepo.add(self, film)
        self.__write_all_to_file()

    def delete(self, clientId):
        self.__read_all_from_file()
        ClientRepo.delete(self, clientId)
        self.__write_all_to_file()

    def update(self, client):
        self.__read_all_from_file()
        ClientRepo.update(self, client)
        self.__write_all_to_file()

    def searchById(self, clientId):
        self.__read_all_from_file()
        return ClientRepo.searchById(self, clientId)

    def getAll(self):
        self.__read_all_from_file()
        return ClientRepo.getAll(self)
