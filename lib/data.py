from lib.parser.base import BaseType
import lib.usernames as Usernames

class Name(BaseType):
    data_type="paragraph"
    spellchecker=Usernames.get()
    
    def afterRead(self):
        self.val = self.val.split("\n")[0]

class Assists(BaseType):
    data_type="integer"

class Goals(BaseType):
    data_type="integer"

class Saves(BaseType):
    data_type="integer"

class Score(BaseType):
    data_type="integer"

class Shots(BaseType):
    data_type="integer"