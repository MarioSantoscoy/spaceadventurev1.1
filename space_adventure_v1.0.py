print()
print("---------- Space Adventure ----------")
print()

user_name = input("Enter your name: ")
print()

print("Hi Captain " + str(user_name) + " welcome on board." )
print("I'll explain you how is devised the ship:")
print("1) Cabin")
print("2) Hall")
print("3) Dining room")
print("4) Laboratory")

cabin = 1
hall = 2
dining_room = 3
laboratory = 4
main_menu = 0

main_menu = int(input("Where do you want to go: "))
while main_menu != (1, 4):
    if main_menu == 1:
        print("Moving to cabin...") 
        print()
        print("---------- Cabin ----------")
        print()
        print("Welcome to Cabin Captain " + str(user_name) + ".")
        print("What do you want to do?")
        print("1) Launch.")
        print("2) Define route.")
        print("3) Return to select menu.")
        
        action_cabin = int(input("Enter the option: "))
        print()
        
        while action_cabin != (1,3):
            if action_cabin == 1:
                print("Launch now?")
                print("1) Yes.")
                print("2) No.")
                
                Yes = 1
                No = 2
                num=3
                launch_now = int(input())
                print()
                
                if launch_now == 1:
                    for x in range (1,num+1):
                        print("Launch on", num-x)
                    print("Launch!")
                    print()
                else:
                    print("Returning...")
                action_cabin = int(input("What do you want to do?: "))
                print()

            elif action_cabin == 2:
                print("Where we go?: ")
                print("1) Moon.")
                print("2) Mars.")
                print("3) Return to Cabin menu.")

                moon = 1
                mars = 2
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
                    print("Returning...")
                action_cabin = int(input("What do you want to do?: "))
                print()
                
            else:
                break
                print()

    elif main_menu  == 2:
        print("Moving to the hall...")
        print()
        print("---------- Hall ----------")
        print()
        print("Welcome to the Hall Captain " + str(user_name) + ".")

        print("What do you want to do?")
        print("1) Talk with Karen.")
        print("2) Look by the window.")
        print("3) Return to select menu.")
        print()
        action_hall = int(input("Enter the option: "))
        print()
        
        while action_hall != (1,3):
            if action_hall == 1:
                print("Karen: Hi Captain " + str(user_name) + ".")
                print("Karen: My name is Karen and I'll give you important info. This are the options:")
                print("1) Distance to planets.")
                print("2) Facts about the ISS.")
                print("3) Return to select menu.")
                navigation_info = int(input("What information do you want?: "))
                print()
                
                if navigation_info == 1:
                    print("Select the planet:")
                    print("1) Mercury.")
                    print("2) Venus.")
                    print("3) Mars.")
                    print("4) Jupiter.")
                    print("5) Saturn.")
                    print("6) Uranus.")
                    print("7) Neptune.")
                    print("8) Return to Hall menu.")
                    print()
                    
                    planet_distance = int(input("Enter the option: "))
                    if planet_distance == 1:
                        print("Karen: The distance from Earth to Mercury is 56.97 Mill. miles.")
                        print()
                        
                    elif planet_distance == 2:
                        print("Karen: The distance from Earth to Venus is 25.7 Mill. miles.")
                        print()
                        
                    elif planet_distance == 3:
                        print("Karen: The distance from Earth to Mars is 140 Mill. miles.")
                        print()
                        
                    elif planet_distance == 4:
                        print("Karen: The distance from Earth to Jupiter is 140 Mill. miles.")
                        print()
                        
                    elif planet_distance == 5:
                        print("Karen: The distance from Earth to Saturn is 792 Mill. miles.")
                        print()
                        
                    elif planet_distance == 6:
                        print("Karen: The distance from Earth to Uranus is 1.7 Bill. miles.")
                        print()
                        
                    elif planet_distance == 7:
                        print("Karen: The distance from Earth to Neptune is 2.703 Bill. miles.")
                        print()
                        
                    else: 
                        print("Returning...")
                        navigation_info = int(input("What information do you want?: "))
                        print()
                
                elif navigation_info == 2:
                    print("Karen: What do you want to know about the ISS?")
                    print("1) How much time takes to ISS to do one orbit to Earth?.")
                    print("2) How far is the ISS to Earth?.")
                    print("3) Return to Hall menu...")
                    print()
                    facts_iss = int(input("Enter the option: "))
                    
                    if facts_iss == 1:
                        print("Karen: For the ISS takes about 90 minutes to complete ONE orbit around the Earth")
                        print("Karen: To calculate how many orbits complete the ISS around the Earth on certainly time go to Laboratory")
                        print()
                    elif facts_iss == 2:
                        print("Karen: The ISS it's about 250 miles above sea level.")
                        print()
                    else:
                        print("Returning...")
                        navigation_info = int(input("What information do you want?: "))
                        print()
                else:
                    print("Returning...")
                    action_hall = int(input("Enter the option: "))
                    print()
            
            elif action_hall == 2:
                print("You look out the window and see the vast darkness of space.")
                print("You can see the Earth glow against the contrast of space.")
                print("Maybe we're not alone on universe...")
                print()
                action_hall = int(input("Enter the option: "))
                
            else:
                print("Returning...")
                break
    
    elif main_menu == 3:
        print("Moving to dining room...")
        print()
        print("---------- Dining Room ----------")
        print()
        print("Welcome to Dining room Captain " + str(user_name) + ".")
        print("Who do you want to talk?")
        print("1) Victor.")
        print("2) Lalo.")
        print("3) Wally.")
        print("4) Return to select menu.")
        action_dining_room = int(input("Enter the option: "))
        print()

        while action_dining_room != (1,4):
            if action_dining_room == 1:
                print("Victor: Hi Captain " + str(user_name) + ". My name is Victor.")
                print("Victor: I'm the manager of the operating system.")
                print("Victor: What do you want to know?")
                print("1) What we use as operating system?")
                print("2) Where is the location of the main server?")
                print("3) Return to Dining room menu.")
                victor_talking = int(input("Victor: please enter your option: "))
                print()

                if victor_talking == 1:
                    print("We use Linux for operating system. That's because it's an open system.")
                    print()
                elif victor_talking == 2:
                    print("The main server is on Earth and we've a local server operating on laboratory.")
                    print()
                else:
                    print("Returning...")
                    action_dining_room = int(input("Enter the option: "))
                print()

            elif action_dining_room == 2:
                print("Lalo: Hi Captain " + str(user_name) + ". My name is Lalo.")
                print("Lalo: I'm the manager of the program system.")
                print("Lalo: What do you want to know?")
                print("1) What we use as program system?")
                print("2) Why we don't use other program system?")
                print("3) Return to Dining room menu.")
                lalo_talking = int(input("Enter the option: "))
                print()

                if lalo_talking == 1:
                    print("We use Python 3.8 for program system")
                    print()
                
                elif lalo_talking == 2:
                    print("That's because Python it's a friendly system, easy to learn and get started")
                    print()
                    
                else:
                    print("Returning...")
                action_dining_room = int(input("Enter the option: "))
                print()
            
            elif action_dining_room == 3:
                print("Hi Captain " + str(user_name) + ". My name is Wally.")
                print("I'm the manager of the maintenance system.")
                print("What do you want to know?")
                print("1) To what do the maintenance system maintain?")
                print("2) Are all the systems OK?")
                print("3) Return.")
                wally_talking = int(input("Enter the option: "))
                print()
                
                if wally_talking == 1:
                    print("The maintenance system mantains all the alerts, security and emergency systems.")
                    print()

                elif wally_talking == 2:
                    print("Yes, we launch the maintenance system everyday in the morning and night.")
                    print()
                
                else:
                    print("Return...")
                    action_dining_room = int(input("Enter the option: "))
                    print()
            else:
                break
    
    elif main_menu == 4:
        print("Moving to Laboratory...")
        print()
        print("---------- Laboratory ----------")
        print()
        print("Welcome to Laboratory Captain " + str(user_name) + ".")
        print("To show the menu, please enter the PIN")
        
        access_pin = int(input("PIN: "))
        while access_pin != 1234:
            access_pin = int(input('Access deny. Please enter PIN again: '))

        if access_pin == 1234:
            print("Access complete!")
            print()

            action_laboratory = 0
            while action_laboratory != (1,3):
                print("What do you want to do?")
                print("1) Calculate how many orbits complete the ISS around the Earth.")
                print("2) Start emergency system.")
                print("3) Return to select menu.")
                print()
                action_laboratory = int(input("Enter the option: "))
                
                distance_between_iss_earth = 250
                time_to_do_one_orbit = 90
                if action_laboratory == 1:
                    orbits = int(input("How many orbits do you want to calculate: "))
                    calculated_time = (orbits * time_to_do_one_orbit)
                    miles_traveled = (orbits * distance_between_iss_earth)
                    print()
                    print("In " + str(orbits) + " we travel " + str(miles_traveled) + " miles on " + str(calculated_time) + " minutes.")
                    print()
                    print("Do you want to know the simplified time?")
                    print("1) Yes.")
                    print("2) No.")
                    print()
                    
                    simplify_time = int(input("Yes / No: "))
                    minutes = 0
                    while simplify_time == 1:
                        if simplify_time == 1:
                            minutes_calculated = int(input("Please enter how many minutes: "))
                            def minutes_hours_days(minutes_calculated):
                                hours = minutes_calculated // 60
                                days = hours // 24
                                extra_minutes = (minutes_calculated - (minutes_calculated % 60))
                                return f"{days:02d}:{hours:02d}:{extra_minutes:02d}"

                    else:
                            print("Returning...")
                            action_laboratory = int(input("Enter the option: "))
                elif action_laboratory == 2:
                    print("Starting emergency system")
                    num=3
                    launch_now = int(input())
                    print()
                
                    if launch_now == 1:
                        for x in range (1,num+1):
                            print("Starting on", num-x)
                            print("Started!")
                            print()
                    else:
                        print("Returning...")
                        action_laboratory = int(input("What do you want to do?: "))
                        print()
        
    else:
        print("Wrong answer, please choose again.")

    main_menu = int(input("Where do you want to go: "))