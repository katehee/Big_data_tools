#!/usr/bin/env python

import sys
import operator

#create dictionary for each genre
Sports = {}
Platform = {}
Racing = {}
Puzzle = {}
Misc = {}
Shooter = {}
Simulation = {}
Action = {}
Fighting = {}
Adventure = {}
Strategy = {}

for line in sys.stdin: 
    inputs = line.split('\t')
    name = inputs[0]
    genre = inputs[1]
    sale = inputs[2]
    try: 
        if genre == "Sports":
            Sports[name] = sale
        elif genre == "Platform":
            Platform[name] = sale
        elif genre == "Racing":
            Racing[name] = sale
        elif genre == "Puzzle":
            Puzzle[name] = sale
        elif genre == "Misc":
            Misc[name] = sale
        elif genre == "Shooter":
            Shooter[name] = sale
        elif genre == "Simulation":
            Simulation[name] = sale
        elif genre == "Action":
            Action[name] = sale
        elif genre == "Fighting":
            Fighting[name] = sale
        elif genre == "Adventure":
            Adventure[name] = sale
        elif genre == "Strategy":
            Strategy[name] = sale
    except: 
        continue

print '%s\t%s\t%s' % ("Sports", max(Sports, key =Sports.get), Sports[max(Sports, key =Sports.get)]) 
print '%s\t%s\t%s' % ("Platform", max(Platform, key =Platform.get), Platform[max(Platform, key =Platform.get)]) 
print '%s\t%s\t%s' % ("Racing", max(Racing, key =Racing.get), Racing[max(Racing, key =Racing.get)]) 
print '%s\t%s\t%s' % ("Puzzle", max(Puzzle, key =Puzzle.get), Puzzle[max(Puzzle, key =Puzzle.get)]) 
print '%s\t%s\t%s' % ("Misc", max(Misc, key =Misc.get), Misc[max(Misc, key =Misc.get)]) 
print '%s\t%s\t%s' % ("Shooter", max(Shooter, key =Shooter.get), Shooter[max(Shooter, key =Shooter.get)]) 
print '%s\t%s\t%s' % ("Simulation", max(Simulation, key =Simulation.get), Simulation[max(Simulation, key =Simulation.get)]) 
print '%s\t%s\t%s' % ("Action", max(Action, key =Action.get), Action[max(Action, key =Action.get)]) 
print '%s\t%s\t%s' % ("Fighting", max(Fighting, key =Fighting.get), Fighting[max(Fighting, key =Fighting.get)]) 
print '%s\t%s\t%s' % ("Adventure", max(Adventure, key =Adventure.get), Adventure[max(Adventure, key =Adventure.get)]) 
print '%s\t%s\t%s' % ("Strategy", max(Strategy, key =Strategy.get), Strategy[max(Strategy, key =Strategy.get)]) 
