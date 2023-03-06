import random as rn

print('Random Password Generator by JuniorJacki')
print('-----------------------------------------------------------------')
print('-------- Settings --------')
print('How Long Should the Password be: ')
isOK = False

while not isOK:
    passwordLength = input('Enter [1 ... ∞]: ')
    if passwordLength.isdigit():
        if int(passwordLength) > 0:
            isOK = True
passwordLength = int(passwordLength)
print('--------------------------')
print('Alphabetic Characters:')
print('Both Lower and Uppercase = 0, Only Lower Case = 1, Only Upper Case = 2, Without Alphabetic Characters = 3')
isOK = False
while not isOK:
    passwordAlphabeticLowHeight = input('Enter [0,1,2 or 3]: ')
    if passwordAlphabeticLowHeight.isdigit():
        if int(passwordAlphabeticLowHeight) in range(-1,5):
            isOK = True
passwordAlphabeticLowHeight = int(passwordAlphabeticLowHeight)
print('--------------------------')

print('Numbers:')
print('With Numbers = y, Without Numbers = n')
passwordNumbers = input('Enter [y or n]: ')
while passwordNumbers != 'y' and passwordNumbers != 'n':
    passwordNumbers = input('Enter [y or n]: ')
print('--------------------------')

print('Special Characters:')
print('With Special Characters = y, Without Special Characters = n')
passwordSpecialCharacters = input('Enter [y or n]: ')
while passwordSpecialCharacters != 'y' and passwordSpecialCharacters != 'n':
    passwordSpecialCharacters = input('Enter [y or n]: ')


if passwordAlphabeticLowHeight == 3 and passwordNumbers == "n" and passwordSpecialCharacters == "n":
    print('Your Password would be empty. Script will Stop!')
    quit()

print('--------------------------')
print('Creating Password ...')
print(' ')

def getRandomNumber():
    return chr(rn.randint(48,57))

def getRandomSpecialCharacter():
    # List: https://www.petefreitag.com/cheatsheets/ascii-codes/
    #               !,  #,  $,  &,  @
    element_list = [33, 35, 36, 38, 64]
    return chr(rn.choice(element_list))

def getRandomAlphabetCharacter():
    if passwordAlphabeticLowHeight == 0:
        return chr(rn.randint(65,122)) # Random Lower or Upper Case
    if passwordAlphabeticLowHeight == 1:
        return chr(rn.randint(97, 122)) # Random Lower Case
    if passwordAlphabeticLowHeight == 2:
        return chr(rn.randint(65, 90)) # Random Upper Case


passwordOF = [] # List of Elements that should be in Password
if passwordNumbers == 'y':
    passwordOF.append(0) # Adds Numbers to List of Elements that should be in Password
if passwordSpecialCharacters == 'y':
    passwordOF.append(1) # Adds Special Characters to List of Elements that should be in Password
if passwordAlphabeticLowHeight == 0 or passwordAlphabeticLowHeight == 1 or passwordAlphabeticLowHeight == 2:
    passwordOF.append(2) # Adds Alphabetic Characters to List of Elements that should be in Password

password = ''
for i in range(passwordLength):
    randomId = rn.choice(passwordOF)
    match randomId:
        case 0:
            password += str(getRandomNumber())
        case 1:
            password += str(getRandomSpecialCharacter())
        case 2:
            password += str(getRandomAlphabetCharacter())



print('Random Password: ' + password)