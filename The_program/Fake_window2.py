WITDH = 30
HEADER_MAIN = "NaN AIR"  
HEADER_SUB_A = "Breyta" 
HEADER_SUB_B = "Nýskrá"
HEADER_SUB_C = "Sækja"
BORDER = "*"

CHANGE = "'1' - Breyta"
MAKE = "'2' - Nýskrá"
GET = "'3' - Sækja"
QUIT = "'q' - Hætta"
GO_BACK = "'r' - Til baka"
PICK = "Veldu skipun:"
USER_INPUT = ("Valin skipun: ")
EMPLOYEE = "'1' - Starfmann"
PLACE = "'2' - Áfangastað"
WORK_FLIGHT = "'3' - Vinnuferð"
AIRPLANE = "'4' - Flugvél"
WORK_TIME = "'5' - Vinnustund"
AIRPLANE_TYPE = "'5' - Flugvélategund"
FLIGHT_ATTEND = "'2' - Flugþjónn
FLYER = "'1' - Flugmaður"
Name_Input = "Nafn: "
SSN_Input = "Kennitala: "
ADDRESS_Input = "Heimilisfang: "
GSM_Input = "GSM-Sími: "
EMAIL_Input = "Netfang: "

user = " "
########HEADER  main menu 
while user != "q":
    
    print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_MAIN))/2)*" " +  HEADER_MAIN  +   "\n" + BORDER * WITDH )
  
    print(PICK +"\n")
    print(QUIT+ "\n")
    print(CHANGE)
    print(MAKE)
    print(GET)
    print()
    user = input(USER_INPUT)
    print()
    
    if user == "1":
        user1 = user 
        while user1 != "r":
            print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_SUB_A))/2)*" " +  HEADER_SUB_A  +   "\n" + BORDER * WITDH )
  
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print(EMPLOYEE)
            print(PLACE)
            print(WORK_FLIGHT)
            print()
            user1 = input(USER_INPUT)
            print()


    elif user == "2":
        user2 = user 
        while user2 != "r":
            print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
  
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print(EMPLOYEE)
            print(PLACE)
            print(WORK_FLIGHT)
            print(AIRPLANE)
            print(AIRPLANE_TYPE)
            print()
            user2 = input(USER_INPUT)
            print()
            if user2 == 1:
                user2.1 = user 
                while user2 != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
  
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    print(FLYER)
                    print(FLIGHT_ATTEND)
                    print()
                    user2 = input(USER_INPUT)
                    print()



    elif user == "3":
        user3 = user 
        while user3 != "r":
            print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_C))/2)*" " +  HEADER_SUB_C  +   "\n" + BORDER * WITDH )
  
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print(EMPLOYEE)
            print(PLACE)
            print(WORK_FLIGHT)
            print(AIRPLANE)
            print(WORK_TIME)
            print()
            user3 = input(USER_INPUT)
            print()



