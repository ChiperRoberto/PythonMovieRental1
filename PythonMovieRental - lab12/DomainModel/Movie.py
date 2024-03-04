from DomainModel.Errors.ValidError import ValidError


class Movie:

    def __init__(self, movieId, name, category, description, nrInchirieri=0):
        self.__movieId = movieId
        self.__name = name
        self.__category = category
        self.__description = description
        self.__isDeleted = False
        self.__isRent = False
        self.__nrInchirieri = nrInchirieri
        
        self.validate()

    def validate(self):
        """
        Valideaza filmul.
        :return:
        """
        erors = ""
        if self.GetId() < 0:
            erors += "id invalid!\n"
        if self.GetName() == "":
            erors += "nume invalid!\n"
        if self.GetCategory() == "":
            erors += "gen invalid!\n"
        if self.GetDescription() == "":
            erors += "descriere invalida!\n"
        if len(erors) > 0:
            raise ValueError(erors)

    def inchiriaza(self):
        self.__nrInchirieri = self.__nrInchirieri + 1

    def delete(self):
        self.__isDeleted = True

    def GetId(self):
        return self.__movieId

    def GetName(self):
        return self.__name

    def SetName(self, name):
        self.__name = name

    def GetCategory(self):
        return self.__category

    def GetDescription(self):
        return self.__description

    def GetIsDeleted(self):
        return self.__isDeleted

    def GetInchirieri(self):
        return self.__nrInchirieri

    def SetIsDeleted(self):
        """
        Pentru readaugarea filmelor care au fost sterse anterior
        :return:
        """
        self.__isDeleted = False

    def __str__(self):
        return f"{self.__movieId},{self.__name},{self.__category},{self.__description},{self.__nrInchirieri}"

    def __repr__(self):
        return f"{self.__movieId},{self.__name},{self.__category},{self.__description},{self.__nrInchirieri}"
