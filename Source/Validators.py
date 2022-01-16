class Validator:
    def __init__(self, pedigree_family):
        self.__pedigree_family      =   pedigree_family


    def __del__(self):
        del self.__pedigree_family
