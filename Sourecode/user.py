import json

def readDatabase():
    f = open('./database/users.json')
    databaseUsers = json.load(f)
    f.close()
    return databaseUsers

def writeDatabase(data):
    with open('./database/users.json', 'w') as fp:
        json.dump(data, fp, indent=2)

def login(email, password):
    databaseUsers = readDatabase()
    for i in databaseUsers['users']:
        if i['email'] == email and i['password'] == password:
            return i
    return None

# Hàm băm mật khẩu (sử dụng đơn giản ở đây, nhưng nên dùng thư viện như bcrypt trong thực tế)
def hash_password(password):
    return password  # Chỉ là mã giả, bạn nên băm mật khẩu trong thực tế

def updateUserPassword(email, newPassword):
    return True

def insertUser(email, password, role, fullname):
    databaseUsers = readDatabase()
    databaseUsers["users"].append({
       "full_name": fullname,
       "email": email,
       "password": hash_password(password),
       "role": role
    })
    writeDatabase(databaseUsers)
 
def checkExistEmail(email):
    databaseUsers = readDatabase()
    for i in databaseUsers['users']:
        if i['email'] == email:
            return True
    return None

def getUserList():
    databaseUsers = readDatabase()
    return databaseUsers['users']

def findUser(email):
    databaseUsers = readDatabase()
    for i in databaseUsers['users']:
        if i['email'] == email:
            return i
        

    
