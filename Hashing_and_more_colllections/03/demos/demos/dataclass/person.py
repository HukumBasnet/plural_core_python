from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    first_name: str
    last_name: str
    
    def __repr__(self):
        return f'Person: {self.first_name} {self.last_name} hash = {hash(self)}'

# in a long running program we might not be able to keep all the person objects
# around
def is_person_in_dict(first_name: str, last_name: str, the_dictionary: dict):
    return Person(first_name, last_name) in the_dictionary