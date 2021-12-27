class Builder:
    def __init__(self, file_data):
        self.__file_data        =   file_data
        self.__file_pedigrees   =   None
        self.__file_individuals =   None


    @property
    def file_data(self):
        return self.__file_data


    @property
    def file_pedigrees(self):
        return self.__file_pedigrees


    @property
    def file_individuals(self):
        return self.__file_individuals


    @file_data.deleter
    def file_data(self):
        del self.__file_data


    @file_pedigrees.deleter
    def file_pedigrees(self):
        del self.__file_pedigrees


    @file_individuals.deleter
    def file_individuals(self):
        del self.__file_individuals


    def __del__(self):
        del self.__file_data
        del self.__file_pedigrees
        del self.__file_individuals
