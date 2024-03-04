from DomainModel.Errors.ValidError import ValidError


class Client:
    def __init__(self, clientId, clientName, nrInchiriate=0):
        self.__clientId = clientId
        self.__clientName = clientName
        self.__isDeleted = False
        self.__nr_filme_inchiriate = nrInchiriate

        self.validate()

    def delete(self):
        self.__isDeleted = True

    def validate(self):
        """
        Valideaza clientul.
        :return:
        """
        erors = ""
        if self.getClientId() < 0:
            erors += "id invalid!\n"
        if self.getClientName() == "":
            erors += "nume invalid!\n"
        if self.getNrFilme() < 0:
            erors += "clientul nu mai are nimic de returnat!"
        if len(erors) > 0:
            raise ValueError(erors)

    def getClientId(self):
        return self.__clientId

    def getClientName(self):
        return self.__clientName

    def SetName(self, clientName):
        self.__clientName = clientName

    def getIsDeleted(self):
        return self.__isDeleted

    def setIsDeleted(self):
        self.__isDeleted = False

    def getNrFilme(self):
        return self.__nr_filme_inchiriate

    def inchiriaza(self):
        self.__nr_filme_inchiriate = self.__nr_filme_inchiriate + 1

    def returneaza(self):
        if self.__nr_filme_inchiriate == 0:
            raise ValidError("Clientul nu mai are nimic de returnat!")
            return
        self.__nr_filme_inchiriate = self.__nr_filme_inchiriate - 1

    def __str__(self):
        return f"{self.__clientId},{self.__clientName},{self.getNrFilme()}"

    def __repr__(self):
        return f"{self.__clientId},{self.__clientName},{self.getNrFilme()}"