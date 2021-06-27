genders ={
        'FEMALE': 'F',
        'MALE': 'M',
    }




class Person:
    
    def __init__(self, name, gender, mother=None, father=None, partner=None):
        self.name = name
        self.gender = gender
        self.mother=mother
        self.father=father
        self.partner=partner
        self.children=[]

    def add_partner(self, member):
        self.partner=member 
    
    def add_children(self, child):
        self.children.append(child)
    
    def get_children(self):
        return [c.name for c in self.children]

    def get_child(self, gender):
        return [c.name for c in self.children if c.gender==gender]

    def get_partner(self):
        if self.partner:
            return self.partner.name
        return None
    
    def get_siblings(self):
        if self.mother:
            return [c for c in self.mother.children if c.name!=self.name]
        return None
    
    def get_partner_siblings(self, gender, name):
       return [c.name for c in self.children if c.gender==gender and c.name!=name]
    
    def get_parents_cousins(self, gender):
        if self.mother:
            return [c.name for c in self.mother.children if c.name!=self.name and c.gender==gender]
        return None
    
    def get_in_laws(self, gender):
        result=[]
        if self.partner and self.partner.mother:
            result=self.partner.mother.get_partner_siblings(gender, self.partner.name)
        self_siblings = self.get_siblings()
        if self_siblings:
            siblings_partners = [sibling.get_partner() for sibling in self_siblings if sibling.get_partner()]
            result.extend(siblings_partners)
        return result
    
    

