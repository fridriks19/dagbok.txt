from services.class_EmployeeRepository import EmployeeRepository
from services.class_Aircraft_typeRepository import AircraftRepository
from services.class_PastFlightsRepository import PastFlightsRepository
>>>>>>> 708d67af4563841a61faaaf28ae51c9fa4cd5b8a
#from services.class_upcoming_flightsIO import Upcoming_flightsIO

class GetUI():
    def __init__(self):
        self.WITDH = 50
        self.BORDER = "*"
        self.QUIT = "'q' - Hætta"
        self.GO_BACK = "'r' - Til baka"
        self.PICK = "Veldu skipun:"
        self.USER_INPUT = ("Valin skipun: ")
        

                
    ###########################################################################
    ############################### get sub menu ##############################
    ###########################################################################
    def get_menu(self):
        get_input = ""
        while get_input != "r":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja"))/2)*" " +  "Sækja"  +   "\n" + self.BORDER * self.WITDH )
            print(self.PICK +"\n")
            print(self.QUIT+ " "*5 + self.GO_BACK +"\n")
            print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
            get_input = input(self.USER_INPUT)
            print()
            if get_input == "1":
                pass
                
            if get_input == "2":
                pass
            if get_input == "3":
                pass
            if get_input == "4":
                pass
            if get_input == "5":
                pass
        else:
            return ""