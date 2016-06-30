import random

# Me/Attributes
You = {
     "action": input('type "pg" then a number 1-4 to pump gas into a certain part of the room, and type. ' +
                     'You can also type "mask" to clear out your gas levels,' +
                     'or type anything else to sit and wait.'),
     'gas levels': 0,
     "py blue presence": False,
     "py yellow presence": False,
     "little malware presence": False
}


# Threats
py_blue = {
    'path': None,
    'gas tolerance': 30,
    'ai': random.randint(1, 10)
}
py_yellow = {
    'path': None,
    'gas tolerance': 60,
    'ai': random.randint(1, 10)
}
little_malware = {
    'path': None,
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

    input(You['gas levels'])

    if You['action'] == 'pg1':
        E11['gas levels']
