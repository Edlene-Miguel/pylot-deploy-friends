""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Friend(Model):
    def __init__(self):
        super(Friend, self).__init__()

    def get_all_friends(self):
        query = "SELECT * FROM friends"
        return self.db.query_db(query)

    def create_friend(self, friend):
        query = "INSERT INTO friends(first_name, last_name, occupation, known_for) VALUES (:first_name, :last_name, :occupation, :known_for)"
        data = {
            'first_name' : friend['first_name'],
            'last_name' : friend['last_name'],
            'occupation' : friend['occupation'],
            'known_for' : friend['known_for']
        }
        self.db.query_db(query, data)

    def get_friend_by_id(self, id):
        query = "SELECT * FROM friends WHERE id = :id"
        data = {
            'id' : id
        }
        return self.db.query_db(query, data)[0]

    def update(self, id, friend):
        query = "UPDATE friends SET first_name= :first_name, last_name= :last_name, occupation= :occupation, known_for= :known_for WHERE id= :id"
        data = {
            'id' : id,
            'first_name' : friend['first_name'],
            'last_name' : friend['last_name'],
            'occupation' : friend['occupation'],
            'known_for' : friend['known_for']
        }
        self.db.query_db(query, data)

    def delete(self, id):
        query = "DELETE FROM friends WHERE id= :id"
        data = {
            'id': id
        }
        self.db.query_db(query, data)


    # """
    # Below is an example of a model method that queries the database for all users in a fictitious application
    
    # Every model has access to the "self.db.query_db" method which allows you to interact with the database

    # def get_users(self):
    #     query = "SELECT * from users"
    #     return self.db.query_db(query)

    # def get_user(self):
    #     query = "SELECT * from users where id = :id"
    #     data = {'id': 1}
    #     return self.db.get_one(query, data)

    # def add_message(self):
    #     sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
    #     data = {'message': 'awesome bro', 'users_id': 1}
    #     self.db.query_db(sql, data)
    #     return True
    
    # def grab_messages(self):
    #     query = "SELECT * from messages where users_id = :user_id"
    #     data = {'user_id':1}
    #     return self.db.query_db(query, data)

    # """