from dataclasses import dataclass, field
import string
import random
#to allow any tipe of dataclass:
from typing import Any

@dataclass
class User:
    username: str
    email: str
    password: str
    worker: bool
    father: bool
    student: bool
    salary: Any = '$13,000'
    def present_myself(self):
        print(f'Hello world, this is {self.username}, my email is: {self.email}')

#method to generate an id
def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass
class Worker:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    #if you add init=False, users can't modify this
    id: str = field(init = False, default_factory=generate_id)

class old_User:
    def __init__(self, username, email, password, worker, father, student):
        self.username = username
        self.email = email
        self.password = password
        self.worker = worker
        self.father = father
        self.student = student 

alejandro = User('alejandrodj.c', 'alejandrone@gmail.com', 'admin', True, False, False)
joel = old_User('joelovin', 'soancatl@gmail.com', 'admin2', False, False, True)
jesus = Worker('jesus', 'santa rosa 512', False, ['jesus@rosas.com','chuy@rosas.com','jechuy@chuyo.com'])

print(alejandro)
print(alejandro.username + "\n" + alejandro.email)
alejandro.present_myself()
print("\n\n")
print(jesus)