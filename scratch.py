from main import getNameRandom,getTextRandom
import faker

lst1 = [1,2]
lst2 = [3,4]

# print(lst1 + lst2)
#
# f = lambda x: x==1
#
# print(getNameRandom())
# print(getTextRandom())
#
fake = faker.Faker().word()

print(fake)

table = 150
card = 3
line = 4
file = 2

print(table*card*line*file)

