class india():
    def capital(self):
        print("New Delhi is the capita of INdia.")

    def language(self):
        print("HIndi is the most widely spoken language of INdia.")

    def type(self):
        print("INdia ia a developing country")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = india()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
