class Board:
  def __init__(self):
    self.difficulty = ''
    self.IndexList = []

  def setDifficulty(self):
    print("This method will allow a user to select the difficulty")
    print("The settings are: Beginner (10 tiles); Intermediate (15); Expert (20)")

  def randomizer(self):
    print("This method will randomize the ordering of the game symbols in the board")
    print("Uses IndexList")
