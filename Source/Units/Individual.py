class Individual:
    def __init__(self, individual_data):
        assert isinstance(individual_data, list)

        self.__pedigree_identifier      =   individual_data[0]
        self.__individual_identifier    =   individual_data[1]
        self.__individual_father        =   individual_data[2]
        self.__individual_mother        =   individual_data[3]
        self.__individual_sex           =   individual_data[4]
        self.__individual_role          =   individual_data[5]
        self.__individual_statuses      =   list()
        self.__mating_unit_relation     =   None
        self.__sibship_unit_relation    =   None
        self.__generation_rank          =   None


    @property
    def pedigree_identifier(self):
        return self.__pedigree_identifier


    @property
    def individual_identifier(self):
        return self.__individual_identifier


    @property
    def individual_father(self):
        return self.__individual_father


    @property
    def individual_mother(self):
        return self.__individual_mother


    @property
    def individual_sex(self):
        return self.__individual_sex


    @property
    def individual_role(self):
        return self.__individual_role


    @property
    def individual_statuses(self):
        return self.__individual_statuses


    @property
    def mating_unit_relation(self):
        return self.__mating_unit_relation


    @property
    def sibship_unit_relation(self):
        return self.__sibship_unit_relation


    @property
    def generation_rank(self):
        return self.__generation_rank


    @pedigree_identifier.setter
    def pedigree_identifier(self, pedigree_identifier):
        self.__pedigree_identifier = pedigree_identifier


    @individual_identifier.setter
    def individual_identifier(self, individual_identifier):
        self.__individual_identifier = individual_identifier


    @individual_father.setter
    def individual_father(self, individual_father):
        self.__individual_father = individual_father


    @individual_mother.setter
    def individual_mother(self, individual_mother):
        self.__individual_mother = individual_mother


    @individual_sex.setter
    def individual_sex(self, individual_sex):
        self.__individual_sex = individual_sex


    @individual_role.setter
    def individual_role(self, individual_role):
        self.__individual_role = individual_role


    @individual_statuses.setter
    def individual_statuses(self, individual_statuses):
        self.__individual_statuses = individual_statuses


    @mating_unit_relation.setter
    def mating_unit_relation(self, mating_unit_relation):
        self.__mating_unit_relation = mating_unit_relation


    @sibship_unit_relation.setter
    def sibship_unit_relation(self, sibship_unit_relation):
        self.__sibship_unit_relation = sibship_unit_relation


    @generation_rank.setter
    def generation_rank(self, generation_rank):
        self.__generation_rank = generation_rank


    @pedigree_identifier.deleter
    def pedigree_identifier(self):
        del self.__pedigree_identifier


    @individual_identifier.deleter
    def individual_identifier(self):
        del self.__individual_identifier


    @individual_father.deleter
    def individual_father(self):
        del self.__individual_father


    @individual_mother.deleter
    def individual_mother(self):
        del self.__individual_mother


    @individual_sex.deleter
    def individual_sex(self):
        del self.__individual_sex


    @individual_role.deleter
    def individual_role(self):
        del self.__individual_role


    @individual_statuses.deleter
    def individual_statuses(self):
        del self.__individual_statuses


    @mating_unit_relation.deleter
    def mating_unit_relation(self):
        del self.__mating_unit_relation


    @sibship_unit_relation.deleter
    def sibship_unit_relation(self):
        del self.__sibship_unit_relation


    @generation_rank.deleter
    def generation_rank(self):
        del self.__generation_rank


    def __hash__(self):
        return  hash(self.pedigree_identifier) + \
                hash(self.individual_identifier)


    def __eq__(self, individual):
        assert isinstance(individual, (Individual, type(None)))
        return self.__hash__() == individual.__hash__()


    def __repr__(self):
        return self.individual_identifier


    def __del__(self):
        del self.__pedigree_identifier
        del self.__individual_identifier
        del self.__individual_father
        del self.__individual_mother
        del self.__individual_sex
        del self.__individual_role
        del self.__individual_statuses
        del self.__mating_unit_relation
        del self.__sibship_unit_relation
        del self.__generation_rank


    def set_mating_unit_relation(self, mating_unit_relation):
        self.__mating_unit_relation = mating_unit_relation


    def set_sibship_unit_relation(self, sibship_unit_relation):
        self.__sibship_unit_relation = sibship_unit_relation


    def set_generation_rank(self, generation_rank):
        self.__generation_rank = generation_rank
