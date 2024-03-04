from Infrastructure.Errors.RepoError import RepoError

class ClientRepo:

    def __init__(self):
        self._clients = {}

    def getAll(self):
        clients = []
        for clientId in self._clients:
            if self._clients[clientId].getIsDeleted() == False:
                clients.append(self._clients[clientId])
        return clients

    def add(self, client):
        """
        Adaugare client in dictionarul de clienti.
        :param client: clientul care trebuie adaugat
        :return:
        """
        if client.getClientId() in self._clients and client.getIsDeleted() == False:
            raise RepoError("client existent!")
        if client.getIsDeleted():
            client.setIsDeleted()
        else:
            self._clients[client.getClientId()] = client

    def delete(self, clientId):
        if clientId not in self._clients or self._clients[clientId].delete() == True:
            raise RepoError("client inexistent!")
        self._clients[clientId].delete()

    def update(self, client):
        if client.getClientId() not in self._clients or client.getIsDeleted() == True:
            raise RepoError("client inexistent!")
        self._clients[client.getClientId()] = client

    def searchById(self, clientId):
        if clientId not in self._clients:
            raise RepoError("client inexistent!")
        elif self._clients[clientId].getIsDeleted() == True:
            raise RepoError("client inexistent!")
        return self._clients[clientId]









