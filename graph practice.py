class Account:
    def __init__(self,username):
        self.username=username
        self.friends=[]


class Facebook:
    def __init__(self):
        self.accounts={}

    def create_account(self,username):
        if username not in self.accounts:
            profile=Account(username)
            self.accounts[username]=profile
        else:
            print("account created")    

    def add_connection(self,user1,user2):
        if user1==user2:
            print("you can't add yourself as a friend")
        elif user1 in self.accounts and user2 in self.accounts:
            user1_profile=self.accounts[user1]
            user2_profile=self.accounts[user2]
            user1_profile.friends.append(user2_profile)
            user2_profile.friends.append(user1_profile)
            print("Yes,He/She is connected")
        else:
            print("user does not exist in friend list") 
    def friend_list(self,username):
        if username in self.accounts:
            user_profile=self.accounts[username]
            friends=user_profile.friends
            names=[user.username for user in friends]
            return names
        #for user in friends
        #names=
        else:
            print("username does not exist")

    def suggestion_list(self,username):
         if username in self.accounts:
             user_profile=self.accounts[username]
             friends=user_profile.friends
             suggestion_list=[]
             for user in friends:
                 if fr.username!=username and fr not in friends:
                     suggestion_list.append(fr.username)
             return suggestion_list
         else:
             print("user not exist")        


Facebook=Facebook()
Facebook.create_account("kanak")
Facebook.create_account("Arya") 
Facebook.create_account("Ankita")
Facebook.add_connection("kanak","Arya")
Facebook.friend_list("abhay")
Facebook.suggestion_list("Arya")

accounts=("kanak")
