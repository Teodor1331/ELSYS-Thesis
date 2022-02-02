class Drawer:
    def __init__(self, intervals):
        self.__intervals   =   intervals


    @property
    def intervals(self):
        return self.__intervals


    @intervals.setter
    def intervals(self, intervals):
        self.__intervals = intervals


    @intervals.deleter
    def intervals(self):
        del self.__intervals


    def __del__(self):
        del self.__intervals
