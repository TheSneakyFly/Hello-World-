inp='none'
while inp.lower() not in ('yes','no','y','n'):
    inp=input('Are you Rachel? ')
    if inp.lower() in ["yes","y"]:
        print('\nCongratulations you are beautiful!')
    elif inp.lower() in ["no","n"]:
        print('\nYou are probably ugly.. sorry')
    else:
        print('\nPlease answer yes or no!')
