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
