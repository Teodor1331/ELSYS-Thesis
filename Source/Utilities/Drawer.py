class Drawer:
    def __init__(self, graph_instance):
        self.__graph_instance   =   graph_instance


    @property
    def graph_instance(self):
        return self.__graph_instance


    @graph_instance.deleter
    def graph_instance(self):
        del self.__graph_instance


    def __del__(self):
        del self.__graph_instance
