Import random

  def main():
  horrorbooks = [
   "It",1160,
   "The Raven",2,
   "Salem's Lot",439,
   "Dracula",431,
   "Frankenstein",280,
   "The Exorcist",340,
   "The Silence of the Lambs", 368,
   "Misery",300,
  ]

  randomfirstWord = [
  "Red",
  "The",
  "Deathly",
  "Silent",
  "It",
  "Someone",
  "Something",
  "Fluff",
  "Darkness",
  "Fallen",
  "Bone",
  "White",
  "Scream",
  "Wolf",
  "Monster",
  "Salvation",
  "Terror",
  "Horror",
  "A",
  "Underneath",
  "Before",
  "Conjure",
  "Creeper",
  "Starved",
  "Sleep",
  "Ghoul",
  "She",
  "Dark",
  "Shadow",
  "Grotesque",
  ]

  randomlastWord = [
  "Death",
  "Died",
  "Lurks",
  "Prowls",
  "Garden",
  "Winter",
  "Vanished",
  "Breathes",
  "Me",
  "Stolen",
  "Jolly",
  "Blood",
  "Massacre",
  "Cries",
  "Promise",
  "Promised",
  "Dawn",
  "Below",
  "Lost",
  "Innocence",
  "Slaughter",
  ]

  printHeader()
  selection = int(getUserSelection())
  if selection == 0:
      printhorrorbooksbyfirstWord(horrorbooks)
  elif selection == 1:
      printhorrorbooksbylastWord(horrorbooks)
  elif selection == 2
      printhorrorbooksbyPageNumber(horrorbooks)
  else:
      print ("SELECTION NOT RECOGNIZED")

  class Horrorbook:
      def __init__(self,firstWord, lastWord, pagenumber):
          self.firstWord = random.choice
          self.lastWord = random.choice
          self.pagenumber = random.choice

      def assignRandomfirstWord(self):
          self.firstWord = random.radint

      def assignRandomlastWord(self):
          self.lastWord = random.radint

      def assignRandompagenumber(self):
          self.pagenumber = random.radint(2,1000)
