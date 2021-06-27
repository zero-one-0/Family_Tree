from Person import Person, genders
from FamilyTree import FamilyTree, PERSON_NOT_FOUND


VALID=3

class GetRelationship:

    def form_function(self, family, elements):
        '''
        It forms the function to get a particular relationship.

        params: family (a FamilyTree object), elements

        '''
        if len(elements) is VALID:
            func_name = "_".join(elements[2].lower().split('-'))
            func_name="_".join(["get", func_name])
            try:
                func = getattr(GetRelationship, func_name)
                member = family.members.get(elements[1])
                result = func(self, member) if member else PERSON_NOT_FOUND
                print(result)
            except Exception:
                raise Exception(f'Module has no attribute names {func_name}')
        else:
            raise Exception(f'Invalid number of arguments for operation {elements[0]}')
    
    def get_son(self, member):
        '''
        Returns the list of sons of given member

        params: member (a Person object)

        '''
        sons=member.get_child(genders['MALE'])
        return " ".join(sons) if sons else None
    
    def get_daughter(self, member):
        '''
        Returns the list of daughters of given member

        params: member (a Person object)
        
        '''
        daughters = member.get_child(genders['FEMALE'])
        return " ".join(daughters) if daughters else None
    
    def get_siblings(self, member):
        '''
        Returns the list of siblings of given member

        params: member (a Person object)
        
        '''
        siblings = member.get_siblings()
        siblings = [s.name for s in siblings]
        return " ".join(siblings) if siblings else None
    
    def get_brother_in_law(self, member):
        '''
        Returns the list of brother-in-laws of given member

        params: member (a Person object)
        
        '''
        brother_in_laws = member.get_in_laws(genders['MALE'])
        return " ".join(brother_in_laws) if brother_in_laws else None
    
    def get_sister_in_law(self, member):
        '''
        Returns the list of sister-in-laws of given member

        params: member (a Person object)
        
        '''
        sister_in_laws = member.get_in_laws(genders['FEMALE'])
        return " ".join(sister_in_laws) if sister_in_laws else None
    
    def get_paternal_uncle(self, member):
        '''
        Returns the list of paternal uncles of given member

        params: member (a Person object)
        
        '''
        paternal_uncles=[]
        if member.father:
            paternal_uncles = member.father.get_parents_cousins(genders['MALE'])
        return " ".join(paternal_uncles) if paternal_uncles else None

    def get_maternal_uncle(self, member):
        '''
        Returns the list of maternal uncles of given member

        params: member (a Person object)
        
        '''
        maternal_uncles=[]
        if member.mother:
            maternal_uncles = member.mother.get_parents_cousins(genders['MALE'])
        return " ".join(maternal_uncles) if maternal_uncles else None
    
    def get_paternal_aunt(self, member):
        '''
        Returns the list of paternal aunts of given member

        params: member (a Person object)
        
        '''
        paternal_aunts=[]
        if member.father:
            paternal_aunts = member.father.get_parents_cousins(genders['FEMALE'])
        return " ".join(paternal_aunts) if paternal_aunts else None
    
    def get_maternal_aunt(self, member):
        '''
        Returns the list of maternal aunts of given member

        params: member (a Person object)
        
        '''
        maternal_aunts=[]
        if member.mother:
            maternal_aunts = member.mother.get_parents_cousins(genders['FEMALE'])
        return " ".join(maternal_aunts) if maternal_aunts else None