class Movie:
    def __init__(self, title, cast, category, release_date, budget):
        self.title = title
        self.cast = cast
        self.category = category
        self.release_date = release_date
        self.budget = budget

    def to_string(self):
        return f"Title: {self.title}\nCast: {self.cast}\nCategory: {self.category}\nRelease Date: {self.release_date}\nBudget: {self.budget}\n"
