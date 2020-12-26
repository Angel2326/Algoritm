log_pas = {'admin': ['admin','activated'],
           'angel': ['12345','not activated'],
           'root': ['11111', 'activated']}


def check(login, password):
    if login in log_pas.keys() and log_pas[login][0] == password and log_pas[login][1] == 'activated': #O(N)
        print ('Welcome ', login) #O(1)
        return (False) #O(1)
    else:
        if login not in log_pas.keys(): #O(N)
            print(login +' is not exists') #O(1)
        else:
            if log_pas[login][1] != 'activated': #O(1)
                print ('is not activated') #O(1)
            else: print('Entered password ' + password + ' for '+ login + ' is not correct') #O(1)
#   #O(N)*(O(1)+ O(1))+O(N)*(O(1)+O(1))+O(1)*O(1)+O(1)) = O(N)
f = True #O(1)
while f == True: #O(N)
    login = input('Enter login:') #O(1)
    password = input('Enter password:') #O(1)
    f = check(login, password) #O(N)
#O(1)+O(N)*(O(1)+O(1)+O(N))=O(N^2)
# ===============









