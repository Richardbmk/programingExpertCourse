class ContactInformation:
    def __init__(self, first_name, last_name, email, phone_number, country=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = country


person1 = ContactInformation("Richard", "Castaneda", "rick98@gmail.com", "98479298384", "Spain")

person2 = ContactInformation("Richard", "Castaneda", "rick98@gmail.com", "98479298384", "Spain")