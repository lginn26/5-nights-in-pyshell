import random

# Me/Attributes
You = {
     "action": input('''type "pg" then a number 1-4 to pump gas into a certain part of the room and control how much
                     gas you pump by leaving a space then a number 1-3, type.
                     You can also type "mask" to clear out your gas levels,
                     or type anything else to sit and wait.'''),
     'gas levels': 0,
     "py blue presence": False,
     "py yellow presence": False,
     "little malware presence": False
}


# Threats
py_blue = {
    'gas tolerance': 30,
    'ai': random.randint(1, 10)
}


py_yellow = {
    'gas tolerance': 60,
    'ai': random.randint(1, 10)
}
little_malware = {
    'gas tolerance': 90,
    'ai': random.randint(1, 10)
}
# Areas
E11 = {
    "present animatronics": {
        'py blue presence': False,
        'py yellow presence': False,
        'little malware presence': False
    },
    'gas levels': 0,
    'messages': ["A shadow has appeared in the door way",
                 "The shadow has left"]

}
E21 = {
    "present animatronics": {
        'py blue presence': False,
        'py yellow presence': False,
        'little malware presence': False
    },
    'gas levels': 0,
    'messages': ["A yellow figure stands in the hall", 
                 "The yellow object is gone"]

}
E31a = {
    "present animatronics": {
        'py blue presence': False,
        'py yellow presence': False,
        'little malware presence': False
    },
    'gas levels': 0,
    'messages': ["something little is standing on the left side of the cave area", 
                 "The tiny object has retreated back into the cave"]

}
E31b = {
    "present animatronics": {
        'py blue presence': False,
        'py yellow presence': False,
        'little malware presence': False
    },
    'gas levels': E31a['gas levels'],
    'messages': ["something little is standing on the right side of the cave area",
                 "The tiny object has retreated back into the cave"]

}
B2 = {
    "present animatronics": {
        'py blue presence': False,
        'py yellow presence': False,
        'little malware presence': False
    },
    'gas levels': 0,
    'messages': ["You here rustling behind the garbage cans",
                 "Rattling comes from the garbage cans"]

}
C2 = {
    "present animatronics": {
        'py blue presence': False,
        'py yellow presence': False,
        'little malware presence': False
    },
    'gas levels': 0,
    'messages': ["You feel a blue presence watching you", 
                 "You feel a yellow presence watching you", 
                 'Something little is in the tiny space behind you']

}
D2 = {
    "present animatronics": {
        'py blue presence': False,
        'py yellow presence': False,
        'little malware presence': False
    },
    'gas levels': 0,
    'messages': ["Something lunged behind the tool rack"]

}

Time = 0.0

while (Time >= 6.0 and
       not You["py yellow presence":True] and 
       not You["py blue presence":True] and 
       not You["little malware presence":True] and 
       not You['gas levels':10] >= 10):

    input(You['action'])

    if You['action'] == 'pg1' :
        amount = input('How much do you want to pump into this area')
        E11['gas levels'] += amount
        You['gas levels'] += amount / 30
        print("You pumped a {} amount of gas into the door way".format(amount))
        print("It is {} and your intoxication levels have reached {}.".format(Time, You['gas levels']))
    elif You['action'] == 'pg2':
        amount = input('How much do you want to pump into this area')
        E21['gas levels'] += amount
        You['gas levels'] += amount / 30
        print("You pumped a {} amount of gas into the hall way".format(amount))
        print("It is {} and your intoxication levels have reached {}.".format(Time, You['gas levels']))
    elif You['action'] == 'pg3':
        amount = input('How much do you want to pump into this area')
        E31a['gas levels'] += amount
        You['gas levels'] += amount / 30
        print("You pumped a {} amount of gas into the cave".format(amount))
        print("It is {} and your intoxication levels have reached {}.".format(Time, You['gas levels']))
    elif You['action'] == 'pg3':
        amount = input('How much do you want to pump into this area')
        E31b['gas levels'] += amount
        You['gas levels'] + amount / 30
        print("You pumped a {} amount of gas into the cave".format(amount))
        print("It is {} and your intoxication levels have reached {}.".format(Time, You['gas levels']))
    elif You['action'] == 'pg4':
        amount = input('How much do you want to pump into this area')
        C2['gas levels'] += amount
        You['gas levels'] + amount / 30
        print("You pumped a {} amount of gas into the door way".format(amount))
        print("It is {} and your intoxication levels have reached {}.".format(Time, You['gas levels']))
    elif You['action'] == 'mask':
        You['gas levels'] -= You['gas levels']
        print("You cleared out the gas in your lungs")
        print("It is {} and your intoxication levels have reached {}.".format(Time, You['gas levels']))
    else:
        print("You didn't do anything.")

    if py_blue['ai'] == 1 or py_blue['ai'] == 2 or py_blue['ai'] == 5 and not E11['py blue presence':True]:
        E11["present animatronics"]['py blue presence'] = True
        print(E11['messages'][0])
    elif E11["present animatronics"]['py blue presence'] == True and not E11['gas levels'] >= 30:
        E11['py blue presence'] = False
        You["py blue presence"] = True
    elif E11["present animatronics"]['py blue presence'] == True and E11['gas levels'] >= 30:


