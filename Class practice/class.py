



class User:
    def __init__(self, username, password):
        print('A NEW USER HAS BEEN MADE')
        self.username = username
        self.password = password

    def print_my_name(self):
        print(self.username)

    def login(self):
        if self.username == 'Mike':
            if self.password == 'password':
                print('you logged in!')
            else:
                print('Error')
        else:
            print('Error!')

user1 = User('Mike', 'password')
user2 = User('Greg', '123456')

user1.print_my_name()
user2.print_my_name()


#x = [1,2,3,4,5,6]
#y = [2,4,6,8,10,12]
#plt.bar(x,y)
