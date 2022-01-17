from Loader     import Loader
from Builder    import Builder
from Graph      import Graph

from FamilyUnits    import Individual
from PedigreeFamily import PedigreeFamily


def main():
    loader = Loader('../Examples/TXT Examples/Pedigree1.txt')
    builder = Builder(loader.file_data)
    
    for pedigree in builder.file_pedigrees:
        graph = Graph(pedigree)

    for pedigree in builder.file_pedigrees:
        assert isinstance(pedigree, PedigreeFamily)
        print(pedigree.pedigree_identifier)
        print(pedigree.pedigree_individuals)
        print(pedigree.pedigree_mating_units)
        print(pedigree.pedigree_sibship_units)
        print()

        pedigree.print_pedigree_family_data()
        print()

        for individual in pedigree.pedigree_individuals:
            individual = pedigree.pedigree_individuals[individual]
            assert isinstance(individual, Individual)
            print(individual, individual.mating_unit_relation, individual.sibship_unit_relation)


        for mating_unit in pedigree.pedigree_mating_units:
            mating_unit = pedigree.pedigree_mating_units[mating_unit]
            print(mating_unit, mating_unit.male_mate_individual, mating_unit.female_mate_individual)


        for sibship_unit in pedigree.pedigree_sibship_units:
            sibship_unit = pedigree.pedigree_sibship_units[sibship_unit]
            print(sibship_unit, sibship_unit.siblings_individuals, sibship_unit.siblings_extended)


if __name__ == '__main__':
    main()
