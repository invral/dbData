import faker
import psycopg2
import random
import string
from faker import Faker

# con = psycopg2.connect(
#     database = "postgres",
#     user = "postgres",
#     password = "passwd",
#     host = "127.0.0.1",
#     port = "5432",
# )

def getPathRandom():
    path = "/usr/"
    dirNames = ["bin", "lib", "local", "home", "log", "etc"]
    rand = random.randint(0,len(dirNames)-1)
    return path+dirNames[rand]

def getDateRandom():
    year = 2021
    month = random.randint(1,12)
    if month == 2:
        day = random.randint(1,28)
    else: day = random.randint(1,30)

    return str(2021)+"-"+str(month)+"-"+str(day)

def getWordRandom():
    fake = Faker()
    word = fake.word()
    return word

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def getNameRandom():

    fake = Faker()
    name = fake.name()
    return name

def getTextRandom():

    fake = Faker()
    text = fake.text(100)
    return text


def createUserData(n):

    namesUser = []
    idUser = []
    passwordsUser = []
    emailUser = []

    for i in range(n):
        namesUser.append(getNameRandom())
        idUser.append(100+i)
        emailUser.append(namesUser[i]+str(i)+"@y.ru")
        passwordsUser.append(generate_random_string(12))

    return namesUser, idUser, passwordsUser, emailUser

def createGroupData(n):

    namesGroup = []
    idGroup = []
    amountOfUsers = []

    for i in range(n):
        rand = random.randint(1,1000)
        namesGroup.append("Group" + str(rand))
        idGroup.append(100+i)
        amountOfUsers.append(150)

    return namesGroup, idGroup, amountOfUsers


def createTableData(n):

    # айдишники для группы брать из пред метода

    namesTable = []
    starredFlags = []
    tablesId = []

    f = lambda x: x == 1

    for i in range(n):
        namesTable.append(getWordRandom())
        rand = random.randint(0, 1)
        starredFlags.append(f(rand))
        tablesId.append(100+i)

    return namesTable, starredFlags, tablesId

def createCardData(n):

    # tableid userid брать из предыдущих

    cardsID = []
    starredflags = []
    namesCard = []

    f = lambda x: x == 1

    for i in range(n):
        cardsID.append(100+i)
        rand = random.randint(0,1)
        starredflags.append(f(rand))
        namesCard.append("Card"+str(i))

    return cardsID, starredflags, namesCard

def createLineData(n):

    # cardID userID было раньше

    namesLine = []
    linesID = []
    descriptions = []

    idCounter = 0

    for i in range(n):
        namesLine.append("Line"+str(i))
        linesID.append(100+i)
        descriptions.append(getTextRandom())

    return namesLine, linesID, descriptions

def createFileData(n):

    # лайнID брать выше

    rdTypes = ["doc","pdf","cpp","py","exe","txt","jpeg","zip","rar","gif","jar","ftp"]

    paths = []
    filesID = []
    types = []

    for i in range(n):
        rand = random.randint(0,len(rdTypes)-1)
        filesID.append(100+i)
        types.append(rdTypes[rand])
        paths.append(getPathRandom())

    return paths, filesID, types

def createComData(n):

    # userID, lineID взять выше

    dates = []
    comID = []
    text = []

    for i in range(n):
        comID.append(100+i)
        dates.append(getDateRandom())
        text.append(getTextRandom())

    return dates, comID, text

def createUIGdata(n):
    ids = []
    # n = len(userID)*len(groupId)
    for i in range(n):
        ids.append(100+i)
    return ids
def createVersioningData(n):

    # n - кол-во всех файлов
    # usersID и filesID брать выше

    dates = []
    oldPaths = []
    versionsID = []

    for i in range(n):
        versionsID.append(100+i)
        dates.append(getDateRandom())
        oldPaths.append(getPathRandom())

    return dates, oldPaths, versionsID


























# curr = con.cursor()
# curr.execute(
#
# )

