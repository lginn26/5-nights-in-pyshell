import random

# Me/Atributes
You = {
     "action": input('type "pg" then a number 1-4 to pump gass into a certian part of the room, and type.'
                     'You can also type "mask" to clear out your gass levels'),
     'gass levels' : 0,
     "py blue presence" : False,
     "py yellow presence" : False,
     "little malware presence" : False
}


#Threats
py_blue = {
    'path': None,
    'gass tolerents': 30,
    'ai':random.randint(1,10)
}
py_yellow = {
    'path': None,
    'gass tolerents': 60,
    'ai': random.randint(1,10)
}
little_malware = {
    'path': None,
    'gass tolerents': 90,
    'ai': random.randint(1,10)
}
#Areas
E11 = {
    "Present_animetronics":{
        'py_blue_presents': False,
        'py_yellow_presents': False,
        'little_malware_presents': False
    },
    'gass_levels':0,
    'messages':["A shadow has appeared in the door way", "The shadow has left"]

}
E21 = {
    "Present_animetronics":{
        'py_blue_presents': False,
        'py_yellow_presents': False,
        'little_malware_presents': False
    },
    'gass_levels':0,
    'messages':["A yellow figure stands in the hall", "The yellow object is gone"]

}
E31a = {
    "Present_animetronics":{
        'py_blue_presents': False,
        'py_yellow_presents': False,
        'little_malware_presents': False
    },
    'gass_levels':0,
    'messages':["Somthing little is standing on the left side of the cave area", "The tiny object has retreated back "
                                                                                  "into the cave"]

}
E31b = {
    "Present_animetronics":{
        'py_blue_presents': False,
        'py_yellow_presents': False,
        'little_malware_presents': False
    },
    'gass_levels': E31a['gass_levels'],
    'messages':["Somthing little is standing on the right side of the cave area", "The tiny object has retreated back "
                                                                                  "into the cave"]

}
B2 = {
    "Present_animetronics":{
        'py_blue_presents': False,
        'py_yellow_presents': False,
        'little_malware_presents': False
    },
    'gass_levels':0,
    'messages':["You here rusiling behind the garbage cans", "Rattiling comes from the garbage cans"]

}
C2 = {
    "Present_animetronics":{
        'py_blue_presents': False,
        'py_yellow_presents': False,
        'little_malware_presents': False
    },
    'gass_levels':0,
    'messages':["You feel a blue presence watching you", "You feel a yellow presence watching you", 'Somthing little is'
                                                                                                    'in the tiny space'
                                                                                                    'behind you']

}
D2 = {
    "Present_animetronics":{
        'py_blue_presents': False,
        'py_yellow_presents': False,
        'little_malware_presents': False
    },
    'gass_levels':0,
    'messages':["Somthing lunged beind the tool rack"]

}
Time = 0.0



while Time >= 6.0 and not You["py yellow presence":True] and not You["py blue presence":True] and not You["little malware presence":True] and not You['gass levels':10] >= 10:
    You["action"]


