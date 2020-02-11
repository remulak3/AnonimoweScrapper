class articleDto:
    def __init__(self, author, story, date, points):
        self.author = author
        self.story = story
        self.date = date
        self.points = points

    def Print(self):
        return ("Story by: {0}"
                " Date: {1} "
                "Points: {2} "
                "Story: {3}").format(self.author, self.date,
                                     self.points, self.story)
