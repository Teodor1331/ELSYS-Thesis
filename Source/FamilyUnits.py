from Fields import Sex, Status, Role


class Individual:
    def __init__(self, individual_data) -> None:
        try:
            assert isinstance(individual_data, list)
        except AssertionError:
            raise AssertionError('The individual data is not valid!')

        self.__pedigree_identifier      =   individual_data[0]
        self.__individual_identifier    =   individual_data[1]
        self.__individual_father        =   individual_data[2]
        self.__individual_mother        =   individual_data[3]

        self.__individual_sex           =   self.decide_sex_individual(individual_data[4])
        self.__individual_status        =   self.decide_status_individual(individual_data[5])
        self.__individual_role          =   self.decide_role_individual(individual_data[6])


        self.__mating_unit_relation     =   None
        self.__sibship_unit_relation    =   None

        self.__generation_rank          =   None
        self.__number_matings           =   0


    @property
    def pedigree_identifier(self) -> str:
        return self.__pedigree_identifier


    @property
    def individual_identifier(self) -> str:
        return self.__individual_identifier


    @property
    def individual_father(self) -> str:
        return self.__individual_father


    @property
    def individual_mother(self) -> str:
        return self.__individual_mother


    @property
    def individual_sex(self) -> Sex:
        return self.__individual_sex


    @property
    def individual_status(self) -> Status:
        return self.__individual_status


    @property
    def individual_role(self) -> Role:
        return self.__individual_role


    @property
    def mating_unit_relation(self):
        return self.__mating_unit_relation


    @property
    def sibship_unit_relation(self):
        return self.__sibship_unit_relation


    @property
    def generation_rank(self):
        return self.__generation_rank


    @property
    def number_matings(self):
        return self.__number_matings


    @mating_unit_relation.setter
    def mating_unit_relation(self, mating_unit_relation):
        assert isinstance(mating_unit_relation, MatingUnit)
        self.__mating_unit_relation = mating_unit_relation


    @sibship_unit_relation.setter
    def sibship_unit_relation(self, sibship_unit_relation):
        assert isinstance(sibship_unit_relation, SibshipUnit)
        self.__sibship_unit_relation = sibship_unit_relation


    @generation_rank.setter
    def generation_rank(self, generation_rank):
        assert isinstance(generation_rank, int)
        self.__generation_rank = generation_rank


    @number_matings.setter
    def number_matings(self, number_matings):
        self.__number_matings = number_matings


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


    @individual_status.deleter
    def individual_status(self):
        del self.__individual_status


    @individual_role.deleter
    def individual_role(self):
        del self.__individual_role


    @mating_unit_relation.deleter
    def mating_unit_relation(self):
        del self.__mating_unit_relation


    @sibship_unit_relation.deleter
    def sibship_unit_relation(self):
        del self.__sibship_unit_relation


    @generation_rank.deleter
    def generation_rank(self):
        del self.__generation_rank


    @number_matings.deleter
    def number_matings(self):
        del self.__number_matings


    def __hash__(self):
        return  hash(self.pedigree_identifier) + \
                hash(self.individual_identifier)


    def __eq__(self, individual):
        if not isinstance(individual, (Individual, type(None))):
            return False
        return self.__hash__() == individual.__hash__()


    def __repr__(self):
        return self.individual_identifier


    def __del__(self):
        del self.__pedigree_identifier
        del self.__individual_identifier
        del self.__individual_father
        del self.__individual_mother

        del self.__individual_sex
        del self.__individual_status
        del self.__individual_role

        del self.__mating_unit_relation
        del self.__sibship_unit_relation

        del self.__generation_rank
        del self.__number_matings


    def decide_sex_individual(self, string):
        if string == '0':
            return Sex.UNKNOWN
        elif string == '1':
            return Sex.MALE
        elif string == '2':
            return Sex.FEMALE
        else:
            return None


    def decide_status_individual(self, string):
        if string == '0':
            return Status.UNKNOWN
        elif string == '1':
            return Status.UNAFFECTED
        elif string == '2':
            return Status.AFFECTED
        else:
            return None


    def decide_role_individual(self, string):
        if string == 'prb':
            return Role.PROBAND
        elif string == 'father':
            return Role.FATHER
        elif string == 'mother':
            return Role.MOTHER
        elif string == 'brother':
            return Role.BROTHER
        elif string == 'sister':
            return Role.SISTER
        elif string == 'grandfather':
            return Role.GRANDFATHER
        elif string == 'grandmother':
            return Role.GRANDMOTHER
        else:
            return None


class MatingUnit:
    def __init__(self, pedigree_identifier, male_mate_individual, female_mate_individual, sibship_unit_relation) -> None:
        assert isinstance(pedigree_identifier, str)
        assert isinstance(male_mate_individual, Individual)
        assert isinstance(female_mate_individual, Individual)
        assert isinstance(sibship_unit_relation, (SibshipUnit, type(None)))
        
        self.__pedigree_identifier      =   pedigree_identifier
        self.__male_mate_individual     =   male_mate_individual
        self.__female_mate_individual   =   female_mate_individual
        self.__sibship_unit_relation    =   sibship_unit_relation
        self.__generation_rank          =   None


    @property
    def pedigree_identifier(self):
        return self.__pedigree_identifier


    @property
    def male_mate_individual(self):
        return self.__male_mate_individual


    @property
    def female_mate_individual(self):
        return self.__female_mate_individual


    @property
    def sibship_unit_relation(self):
        return self.__sibship_unit_relation


    @property
    def generation_rank(self):
        return self.__generation_rank


    @pedigree_identifier.setter
    def pedigree_identifier(self, pedigree_identifier):
        self.__pedigree_identifier = pedigree_identifier


    @male_mate_individual.setter
    def male_mate_individual(self, male_mate_individual):
        self.__male_mate_individual = male_mate_individual


    @female_mate_individual.setter
    def female_mate_individual(self, female_mate_individual):
        self.__female_mate_individual = female_mate_individual


    @sibship_unit_relation.setter
    def sibship_unit_relation(self, sibship_unit_relation):
        assert isinstance(sibship_unit_relation, SibshipUnit)
        self.__sibship_unit_relation = sibship_unit_relation


    @generation_rank.setter
    def generation_rank(self, generation_rank):
        self.__generation_rank = generation_rank


    @pedigree_identifier.deleter
    def pedigree_identifier(self):
        del self.__pedigree_identifier


    @male_mate_individual.deleter
    def male_mate_individual(self):
        del self.__male_mate_individual


    @female_mate_individual.deleter
    def female_mate_individual(self):
        del self.__female_mate_individual


    @sibship_unit_relation.deleter
    def sibship_unit_relation(self):
        del self.__sibship_unit_relation


    @generation_rank.deleter
    def generation_rank(self):
        del self.__generation_rank


    def __hash__(self):
        return  hash(self.male_mate_individual) + \
                hash(self.female_mate_individual)


    def __eq__(self, mating_unit):
        if not isinstance(mating_unit, MatingUnit):
            return False
        return self.__hash__() == mating_unit.__hash__()


    def __repr__(self):
        return "MU" + self.mating_string()


    def __del__(self):
        del self.__pedigree_identifier
        del self.__male_mate_individual
        del self.__female_mate_individual
        del self.__sibship_unit_relation
        del self.__generation_rank


    def mating_string(self):
        return  '(' + str(self.male_mate_individual) + \
                ', ' + str(self.female_mate_individual) + ')'


class SibshipUnit:
    def __init__(self, pedigree_identifier, mating_unit_relation):
        assert isinstance(pedigree_identifier,  str)
        assert isinstance(mating_unit_relation, (MatingUnit, type(None)))

        self.__pedigree_identifier      =   pedigree_identifier
        self.__siblings_individuals     =   list()
        self.__siblings_extended        =   list()
        self.__mating_unit_relation     =   mating_unit_relation
        self.__generation_rank          =   None


    @property
    def pedigree_identifier(self):
        return self.__pedigree_identifier


    @property
    def siblings_individuals(self):
        return self.__siblings_individuals


    @property
    def siblings_extended(self):
        return self.__siblings_extended


    @property
    def mating_unit_relation(self):
        return self.__mating_unit_relation


    @property
    def generation_rank(self):
        return self.__generation_rank


    @pedigree_identifier.setter
    def pedigree_identifier(self, pedigree_identifier):
        self.__pedigree_identifier = pedigree_identifier


    @siblings_individuals.setter
    def siblings_individuals(self, siblings_individuals):
        self.__siblings_individuals = siblings_individuals


    @siblings_extended.setter
    def siblings_extended(self, siblings_extended):
        self.__siblings_extended = siblings_extended


    @mating_unit_relation.setter
    def mating_unit_relation(self, mating_unit_relation):
        self.__mating_unit_relation = mating_unit_relation


    @generation_rank.setter
    def generation_rank(self, generation_rank):
        assert isinstance(generation_rank, int)
        self.__generation_rank = generation_rank


    @pedigree_identifier.deleter
    def pedigree_identifier(self):
        del self.__pedigree_identifier


    @siblings_individuals.deleter
    def siblings_individuals(self):
        del self.__siblings_individuals


    @siblings_extended.deleter
    def siblings_extended(self):
        del self.__siblings_extended


    @mating_unit_relation.deleter
    def mating_unit_relation(self):
        del self.__mating_unit_relation


    @generation_rank.deleter
    def generation_rank(self):
        del self.__generation_rank


    def __hash__(self):
        return hash(self.mating_unit_relation)


    def __eq__(self, sibship_unit):
        if not isinstance(sibship_unit, (SibshipUnit, type(None))):
            return False
        return self.__hash__() == sibship_unit.__hash__()


    def __repr__(self):
        return "SU" + self.mating_unit_relation.mating_string()


    def __del__(self):
        del self.__pedigree_identifier
        del self.__siblings_individuals
        del self.__siblings_extended
        del self.__mating_unit_relation
        del self.__generation_rank


    def add_sibling_individual(self, sibling_individual):
        assert isinstance(sibling_individual, Individual)
        self.__siblings_individuals.append(sibling_individual)


    def add_sibling_individual_mate(self, sibling_individual_mate):
        assert isinstance(sibling_individual_mate, Individual)
        self.__siblings_extended.append(sibling_individual_mate)


    def change_sibling_individual(self, sibling_individual, index_child):
        assert isinstance(sibling_individual, Individual)
        assert isinstance(index_child, int)
        self.__siblings_individuals[index_child] = sibling_individual
