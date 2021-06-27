from Person import Person, genders

CHILD_ADDITION_FAILED="CHILD_ADDITION_FAILED"
PERSON_NOT_FOUND="PERSON_NOT_FOUND"
CHILD_ADDITION_SUCCEEDED="CHILD_ADDITION_SUCCEEDED"
VALID_ADD_CHILD_ARGS=4


class FamilyTree:

    def __init__(self):
        self.members={}
        self.head=None

    def add_persons_to_family(self, member):
        self.members.update({member.name: member})
    
    def get_family_member(self, name):
        return self.members.get(name, None)
    
    def add_head(self, name, gender):
        if self.head is None:
            self.head=Person(name, genders[gender.upper()])
            self.add_persons_to_family(self.head)
        else:
            raise Exception('Failer to add Family Head as head already present.')
    
    def add_partner(self, name, partner_name, gender):
        member=self.members.get(name, None)
        if member is not None and member.partner is None:
            partner = Person(partner_name, genders[gender.upper()], partner=member)
            member.add_partner(partner)
            self.add_persons_to_family(partner)
        else:
            raise Exception('Failer to add Partner as already exists or Person not found')
    
    def add_child(self, mother_name, child_name, gender):
        member = self.members.get(mother_name, None)
        if member is None:
            result = PERSON_NOT_FOUND
        elif child_name is None or gender is None:
            result = CHILD_ADDITION_FAILED
        elif member.gender==genders['FEMALE']:
            child = Person(child_name, genders[gender.upper()], mother=member, father=member.partner)
            member.add_children(child)
            member.partner.add_children(child)
            self.add_persons_to_family(child)
            result = CHILD_ADDITION_SUCCEEDED
        else:
            result = CHILD_ADDITION_FAILED
        return result

