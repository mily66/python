class User:
    # Define the fields and methods for your object here.
    def __int__(self, name):
        #attributes
        self.full_name = name
        self.username = []
        self.password = []
        self.DOB = [] #yyyymmdd
        self.email = []
        self.gender = []
        self.number = []
        self.age = []
        self.connections = connections

    def add_username(self, username):
        self.username = username
    def add_password(self, password):
        self.password = password
    def add_DOB(self, DOB):
        self.DOB = DOB
    def add_email(self, email):
        self.email = email
    def add_gender(self, gender):
        self.gender = gender
    def add_phonenumber(self, phonenumber):
        self.phonenumber = phonenumber
    def add_age(self, age):
        self.age = age
    def add_connections(self,connections):
        self.connections = connections

#objects
u1 = User("Mily")
print (u1.full_name)
u1.username = ""
