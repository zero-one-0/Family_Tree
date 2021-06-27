genders ={
        'FEMALE': 'F',
        'MALE': 'M',
    }




class Person:
    
    def __init__(self, name, gender, mother=None, father=None, partner=None):
        '''
        Initialize a Person with the given attributes


        params: name, gender, mother, father, partner


        '''
        self.name = name
        self.gender = gender
        self.mother=mother
        self.father=father
        self.partner=partner
        self.children=[]

    def add_partner(self, member):
        '''
        Add the partner to the person

        params: member ( a Person object )
        '''
        self.partner=member 
    
    def add_children(self, child):
        '''
        Add child to the person 

        params: child (a Person object)
        '''
        self.children.append(child)
    
    def get_children(self):
        '''
        Get the list of children of the Person

        '''
        return [c.name for c in self.children]

    def get_child(self, gender):
        '''
        Get the list of children of the Person of particular gender

        params: gender

        '''
        return [c.name for c in self.children if c.gender==gender]

    def get_partner(self):
        '''
        Retuns the name of the partner of the person if exists 

        '''
        if self.partner:
            return self.partner.name
        return None
    
    def get_siblings(self):
        '''
        Returns the list of the siblings if the mother for the person exists

        '''
        if self.mother:
            return [c for c in self.mother.children if c.name!=self.name]
        return None
    
    def get_partner_siblings(self, gender, name):
        '''
        Return the list of the Person's partner's siblings of particular gender

        params: name (partners' name), gender

        '''
        return [c.name for c in self.children if c.gender==gender and c.name!=name]
    
    def get_parents_cousins(self, gender):
        '''
        Retuns the list of Person's parent's cousins of particular gender

        params: gender

        '''
        if self.mother:
            return [c.name for c in self.mother.children if c.name!=self.name and c.gender==gender]
        return None
    
    def get_in_laws(self, gender):
        '''
        Returns the list of in-laws of a Person of particular gender

        params: gender
        
        '''
        result=[]
        if self.partner and self.partner.mother:
            result=self.partner.mother.get_partner_siblings(gender, self.partner.name)
        self_siblings = self.get_siblings()
        if self_siblings:
            siblings_partners = [sibling.get_partner() for sibling in self_siblings if sibling.get_partner()]
            result.extend(siblings_partners)
        return result
    
    

