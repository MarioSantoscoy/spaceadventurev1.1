import wikipedia, planets_spaceadventure, datetime

    
rooms = ['1) Cabin.', 
         '2) Hall', 
         '3) Dining room',
         '4) Laboratory'
         ]

cabin_options = ['1) Launch.', 
                 '2) Define route.', 
                 '3) Return to Select Menu.'
                 ]


hall_options = ['1) Talk with Karen.',
                '2) Look by the window.',
                '3) Return to select menu.'
                ]

karen_options = ['1) Distance to planets',
                 '2) Facts about the ISS.',
                 '3) More info about ISS',
                 '4) Return to Hall menu.'
                 ]

facts_about_ISS = ['1) How much time takes to ISS to do one orbit to Earth?.',
                   '2) How far is the ISS to Earth?.',
                   '3) More information',
                   '4) Return to Hall menu...'
                   ]


dining_room_options = ["1) Victor.",
                       "2) Lalo.",
                       "3) Wally.",
                       "4) Return to select menu."
                        ]

victor_talk_options = ["1) What we use as operating system?",
                      "2) Where is the location of the main server?",
                      "3) Return to Dining room menu."
                      ]

lalo_talk_options = ['1) What we use as program system?',
                     "2) Why we don't use other program system?",
                     '3) Return to Dining room menu.'
                     ]

wally_talk_options = ['1) To what do the maintenance system maintain?',
                      '2) Are all the systems OK?',
                      '3) Return.'
                      ]


laboratory_options = ["1) Calculate how many orbits complete the ISS around the Earth.",
                      "2) Start emergency system.",
                      "3) Return to select menu."
                      ]








def minutes_hours_days(minutes_calculated):
  hours = (minutes_calculated // 60)
  days = (hours // 24)
  extra_hours = (hours % 24)
  extra_minutes = (minutes_calculated % 60)
  return f"{days:02d}:{extra_hours:02d}:{extra_minutes:02d}"
  
def main_menu():
  print('Returning...')
  for room in rooms:
    print(room)
    
def select_rooms():
  select_room = int(input('Where do you want to go?:  \n'))
  
def room_selected_cabin():
  print("Moving to cabin...") 
  print()
  print("---------- Cabin ----------")
  print()
  print("Welcome to Cabin Captain " + str(user_name) + ".")
  print("These are the options we have: \n")
  
def room_selected_hall():
  print("Moving to the hall...")
  print()
  print("---------- Hall ----------")
  print()
  print("Welcome to the Hall Captain " + str(user_name) + ".")
  print("These are the options we have: \n")

def room_selected_dining():
  print("Moving to dining room...")
  print()
  print("---------- Dining Room ----------")
  print()
  print("Welcome to Dining room Captain " + str(user_name) + ".")
  print("These are the options we have: \n")
        
def room_selected_laboratory():
  print("Moving to Laboratory...")
  print()
  print("---------- Laboratory ----------")
  print()
  print("Welcome to Laboratory Captain " + str(user_name) + ".")

distance_between_iss_earth = 250
time_to_do_one_orbit = 90


print()
print("---------- Space Adventure ----------")
print()

user_name = input("Enter your name: ")
print()

print(" Hi Captain " + str(user_name) + " welcome on board.\n", "I'll explain you how is devised the ship: \n")
for room in rooms:
  print(room)

# cabin = 1
# hall = 2
# dining_room = 3
# laboratory = 4
# main_menu = 5

select_room = int(input('Where do you want to go?: '))
while select_room != (1, 2, 3, 4):
  if select_room == 1:
    room_selected_cabin()
    for option in cabin_options:
      print(option)
  
    action_selected = int(input('What do you want to do?: \n'))
  
    while action_selected != (1, 2):
      if action_selected == 1:
        print('Launch now?\n',
          '1) Yes.\n',
          '2) No.')
    
        num=3
        launch_now = int(input())
        if launch_now == 1:
          for x in range (1,num+1):
            print("Launch on", num-x)
          print("Launch!")
          print()
        else:
          room_selected_cabin()
          for option in cabin_options:
            print(option)
        action_selected = int(input("What do you want to do?: "))
    
      elif action_selected == 2:
        print('Where we go?: \n',
            '1) Moon.\n',
            '2) Mars.\n',
            '3) Return to Cabin menu.')
      
        num=10
        define_route = int(input())
        print()
        if define_route == 1:
          print("Moving to the Moon...")
          for x in range(1,num+1):
            print("     ",num-x)
          print("Arrived to the Moon!")
          print()
                    
        elif define_route == 2:
          print("Moving to Mars...")
          for x in range(1,num+1):
              print("     ",num-x)
          print("Arrived to Mars!")
          print()
        
        else:
          room_selected_cabin()
        for option in cabin_options:
          print(option)
          action_selected = int(input("What do you want to do?: "))
          
      else:
        main_menu()
        select_room = int(input('Where do you want to go?: '))
        break
        
  
  elif select_room == 2:
    room_selected_hall()
    for option in hall_options:
      print(option)
      
    action_selected = int(input("What do you want to do?: "))
    
    while action_selected != (1, 2):
      if action_selected == 1:
        print('Karen: Hi Captain ' + str(user_name) + '. \n' "My name is Karen and I'll give you important info. This are the options:")
        for option in karen_options:
          print(option)
        navigation_info = int(input("What information do you want?: "))
        print()
        
        if navigation_info == 1:
          print("These are the options: \n")
          for planet in planets_spaceadventure.planets_options:
            print(planet)
          
          planet_distance = int(input('Select the planet: '))
          if planet_distance == 1:
            print('Karen: The distance from Earth to ' + planets_spaceadventure.mercury.name + ' is' + planets_spaceadventure.mercury.distance + '\n')
          
          elif planet_distance == 2:
            print('Karen: The distance from Earth to ' + planets_spaceadventure.venus.name + ' is' + planets_spaceadventure.venus.distance + '\n')
          
          elif planet_distance == 3:
            print('Karen: The distance from Earth to ' + planets_spaceadventure.mars.name + ' is' + planets_spaceadventure.mars.distance + '\n')
          
          elif planet_distance == 4:
            print('Karen: The distance from Earth to ' + planets_spaceadventure.jupiter.name + ' is' + planets_spaceadventure.jupiter.distance + '\n')
          
          elif planet_distance == 5:
            print('Karen: The distance from Earth to ' + planets_spaceadventure.saturn.name + ' is' + planets_spaceadventure.saturn.distance + '\n')
          
          elif planet_distance == 6:
            print('Karen: The distance from Earth to ' + planets_spaceadventure.uranus.name + ' is' + planets_spaceadventure.uranus.distance + '\n')
          
          elif planet_distance == 7:
            print('Karen: The distance from Earth to ' + planets_spaceadventure.neptune.name + ' is' + planets_spaceadventure.neptune.distance + '\n')
          
          else:
            print("Returning...")
            navigation_info = int(input("What information do you want?: "))
            print()
        
        elif navigation_info == 2:
          print("Karen: What do you want to know about the ISS?")
          for fact in facts_about_ISS:
            print(fact)
          fact_iss = int(input('Enter the option selected: '))
          
          if fact_iss == 1:
            print('Karen: For the ISS takes about 90 minutes to complete ONE orbit around the Earth. \n' 'To calculate how many orbits complete the ISS around the Earth on certainly time go to Laboratory. \n')
          
          elif fact_iss == 2:
            print("Karen: The ISS it's about 250 miles above sea level. \n")
          
          else:
            print("Returning...")
            for option in karen_options:
              print(option)
            navigation_info = int(input("What information do you want?: "))
        
        elif navigation_info == 3:
          print(wikipedia.summary('International Space Station'))
          
        else:
          print("Returning...")
        room_selected_hall()
        for option in hall_options:
          print(option)
        action_selected = int(input("Enter the option: "))
      
      elif action_selected == 2:
        print("You look out the window and see the vast darkness of space.\n""You can see the Earth glow against the contrast of space.\n""Maybe we're not alone on universe...")
        print()
        room_selected_hall()
        for option in hall_options:
          print(option)
        action_selected = int(input("Enter the option: "))
      
      else:
        main_menu()
        break
  
  
  elif select_room == 3:
    for option in dining_room_options:
      print(option)
      
    npc_talk = int(input('Who do you want to talk?: '))
      
    while npc_talk != (1, 2, 3):
      if npc_talk == 1:
        print("Victor: Hi Captain " + str(user_name) + ". My name is Victor. \n""Victor: I'm the manager of the operating system.")
        print("Victor: I can provide you infor about this: ")
        for option in victor_talk_options:
          print(option)
        
        victor_info_options = int(input('Which info do you want?: '))
        
        if victor_info_options == 1:
          print("We use Linux for operating system. That's because it's an open system.")
          print()
        elif victor_info_options == 2:
          print("The main server is on Earth and we've a local server operating on laboratory.")
          print()
        else:
          print('Returning...')
          for option in dining_room_options:
            print(option)
        npc_talk = int(input('Who do you want to talk?: '))
        
            
      elif npc_talk == 2:
        print("Lalo: Hi Captain " + str(user_name) + ". My name is Lalo. \n""Lalo: I'm the manager of the program system.")
        print("Lalo: I can provide you infor about this: ")
        for option in lalo_talk_options:
          print(option)
        
        lalo_info_options = int(input('What do you want to know?: '))
        
        if lalo_info_options == 1:
          print("We use Python 3.8 for program system")
          print()
          
        elif lalo_info_options == 2:
          print("That's because Python it's a friendly system, easy to learn and get started")
          print()
          
        else:
          print('Returning...')
          for option in dining_room_options:
            print(option)
        npc_talk = int(input('Who do you want to talk?: '))
        
        
      elif npc_talk == 3: 
        print("Wally: Hi Captain " + str(user_name) + ". My name is Wally. \n" "Wally:I'm the manager of the maintenance system.")
        print("Wally: I can provide you infor about this: ")
        for option in wally_talk_options:
          print(option)
          
        wally_info_options = int(input('What do you want to know?: '))
        
        if wally_info_options == 1:
          print("The maintenance system mantains all the alerts, security and emergency systems.")
          print()
          
        elif wally_info_options == 2:
          print("Yes, we launch the maintenance system everyday in the morning and night.")
          print()
        
        else:
          print('Returning...')
          for option in dining_room_options:
            print(option)
        npc_talk = int(input('Who do you want to talk?: '))
        
      else:
        main_menu()
        break
      
  
  elif select_room == 4:
    room_selected_laboratory()
    print("To show the menu, please enter the PIN")

    access_pin = int(input("PIN: "))
    while access_pin != 1234:
      access_pin = int(input('Access deny. Please enter PIN again: '))
    
    if access_pin == 1234:
      print("Access complete!")
      print()
    
      print('This are the options we have:')
      for option in laboratory_options:
        print(option)
      action_laboratory = int(input('What do you want to do?: '))
      
    while action_laboratory != (1,3):
      if action_laboratory == 1:
        orbits = int(input("How many orbits do you want to calculate: "))
        calculated_time = (orbits * time_to_do_one_orbit)
        miles_traveled = (orbits * distance_between_iss_earth)
        print()
        print("In " + str(orbits) + " orbits, we travel " + str(miles_traveled) + " miles on " + str(calculated_time) + " minutes.")
        print()
        print("Do you want to know the simplified time?")
        print("1) Yes. \n""2) No.")
        print()
                    
        simplify_time = int(input("Yes / No: "))
        if simplify_time == 1:
          minutes_calculated = int(input("Please enter how many minutes: "))
          print(minutes_hours_days(minutes_calculated))
          break
        
        else:
          print("Returning...")
          print('This are the options we have:')
          for option in laboratory_options:
              print(option)
          action_laboratory = int(input('What do you want to do?: '))
          
      elif action_laboratory == 2:
        print("Start emergency system?")
        print("1) Yes.\n""2) No.") 
        num=4
        launch_now = int(input("Enter option: "))
        print()
        if launch_now == 1:
            for x in range (1,num+1):
                print("Starting on", num-x)
            print("Started!")
            print()

        else:
            print("Returning...")
            for option in laboratory_options:
              print(option)
            action_laboratory = int(input("What do you want to do?: "))
            print()
      else:
        main_menu()
        break
    
  else:
    print("Wrong answer, please choose again.")
  select_room = int(input('Where do you want to go?: '))