class Person:
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        super().__init__()
    
    def __repr__(self):
        return f'Person: {self.first_name} {self.last_name} hash = {hash(self)}'

    def __hash__(self):
        to_hash = (self.first_name, self.last_name)
        return hash(to_hash)
    
    def __eq__(self, value):
        return type(self) == type(value) and self.last_name == value.last_name \
            and self.first_name == value.first_name

# in a long running program we might not be able to keep all the person objects
# around
def is_person_in_dict(first_name: str, last_name: str, the_dictionary: dict):
    return Person(first_name, last_name) in the_dictionary