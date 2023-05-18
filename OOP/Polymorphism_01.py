#polymorphism with class methods
class AndraPradesh():
    def capital(self):
        print("Amaravati is a capital od andtra pradesh.")
    def language(self):
        print("Telugu is the native language of Andra pradesh.")
    def type(self):
        print("Andra pradesh is developing state.")
class Karnataka():
    def capital(self):
        print("Bangalore is capital of Telengana.")
    def language(self):
        print("Kannada is primary language of karnataka.")
    def type(self):
        print("Karnataka is a developing state.")
obj_ap =AndraPradesh()
obj_ka =Karnataka()
for state in (obj_ap,obj_ka):
    state.capital()
    state.language()
    state.type()
