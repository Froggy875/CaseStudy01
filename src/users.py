import os
from tinydb import TinyDB, Query
from serializer import serializer


class User:

    # neue kategorie 'users' in datenbank
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('users')

    def __init__(self, id, name) -> None:
        """Create a new user based on the given name and id"""
        self.name = name
        self.id = id #email wird vorübergangsweise als id genutzt

    def store_data(self)-> None:
        """Save the user to the database"""
        
        # stark von device übernommen...
        print("Storing data...")
        # Check if the device already exists in the database

        UserQuery = Query()
        result = self.db_connector.search(UserQuery.id == self.id)
        
        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the device doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")

    def delete(self) -> None:
        """Delete the user from the database"""
        print("Deleting data...")
        # Check if the device exists in the database
        UserQuery = Query()
        result = self.db_connector.search(UserQuery.id == self.id)
        if result:
            # Delete the record from the database
            self.db_connector.remove(doc_ids=[result[0].doc_id])
            print("Data deleted.")
        else:
            print("Data not found.")
    
    def __str__(self):
        return f"User {self.id} - {self.name}"
    
    def __repr__(self):
        return self.__str__()
    
    # wie ganz normale fkt, die nur nur aus organisatorsischen gründen in klasse steht...
    # braucht keine instanz der klasse, dass man sie verwenden kann
    @staticmethod
    def find_all(cls) -> list:
        """Find all users in the database"""
    # Load all data from the database and create instances of the Device class
        users = []
        for user_data in users.db_connector.all():
            users.append(User(user_data['user_id'], user_data['user_name']))
        return users
    
    # zugehörig zur klasse, wegen parameter cls, aber auch unabhänig benutzbar
    # davon, ob schon instanz der klasse erstellt wurde.
    @classmethod
    def find_by_attribute(cls, by_attribute: str, attribute_value: str, num_to_return=1):
        # Load data from the database and create an instance of the Device class
        UserQuery = Query()
        result = cls.db_connector.search(UserQuery[by_attribute] == attribute_value)

        if result:
            data = result[:num_to_return]
            device_results = [cls(d['id'], d['name']) for d in data]            
            return device_results if num_to_return > 1 else device_results[0]      
        else:
            return None
        