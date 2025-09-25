class User:
    #attributes => things the object has
    def __init__(self, user_id, username):
        """called everytime an instance of the class is created. the attributes should always be given when creating an object"""
        self.id = user_id
        self.username = username
        self.followers = 0 #default values. they change
        self.following = 0
        
    #methods => things the object does. They must always have a self parameter
    def follow(self, user):
        user.followers += 1
        self .following += 1
        
user_1 = User('001', 'wayne')
user_2 = User('002', 'joker')

user_1.follow(user_2)

print(user_2.followers)