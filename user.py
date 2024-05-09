class User:
    def __init__(self, email, name, age):
        self.email = email
        self.name = name
        self.age = age
        self.favorites = []

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}\nEmail: {self.email}\n"

    def to_string(self):
        user_details = self.get_details()
        if self.favorites:
            favorites_details = "\nFavorites:\n"
            for movie in self.favorites:
                favorites_details += movie.to_string() + '\n'
        else:
            favorites_details = "\nNo favorites added.\n"

        return user_details + favorites_details