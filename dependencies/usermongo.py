from pymongo import MongoClient

client = MongoClient("mongodb+srv://swoyamsiddharthnayak:swoyamsiddharthnayak@cluster1.jar6lr0.mongodb.net/")
db = client.test

class User:
    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def signup(self):
        db.users.insert_one({
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "password": self.password
        })

    def changepassword(self, newpassword):
        db.users.update_one({"email": self.email}, {"$set": {"password": newpassword}})

