
  #CLASS USER#
class User:
    '''
    Class that generates new instances of user
    '''
    user_list = []  # list of users to be stored here

    def __init__(self, username, password):
        '''
        saving user credentials into user_list for login
        '''
        self.username = username
        self.password = password

#########save multiple users#########

    def save_user(self):
        User.user_list.append(self)

        ###########Delete User######

    def delete_user(self):
        '''
        delete a user account
        '''
        User.user_list.remove(self)


        #Find User#

    @classmethod
    def find_user(cls, username):
        '''
        find username using search terms
        '''
        for user in cls.user_list:
            if user.username == username:
                return  user
