print('-------------------- AND -----------------------')
userAge = 19
userGender = "male"

if userAge >= 18 and userGender == "male":
    print("you have to go to soldiery")
else:
    print("you can stay at home")


print(f'True and True : {True and True}')
print(f'False and True : {False and True}')
print(f'True and False : {True and False}')
print(f'False and False : {False and False}')



print('-------------------- OR -----------------------')
weather = "sunny"
if weather == "sunny" or weather == "cloudy":
    print("we can travel")
else:
    print("we can't travel")



print('-------------------- NOT -----------------------')
isBrotherComming = False

if not isBrotherComming:
    print('my sister said: i want come')

print(f'not True : {not True}')
print(f'not False : {not False}')