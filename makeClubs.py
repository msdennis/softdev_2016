# Sample demonstration of Classes and Objects
# Selina Dennis, 2016

import random
# import the golf club class from the current working directory
from golfClub import *

### NEW FUNCTIONS                                                ###
# These functions sit outside of the club code, and aren't contained
# within a class. 
# ------------------------------------------------------------------

# Do damage to a club
# Input: the club being damaged
# Output: the club after it has been damaged
def damageClub(clubHit):
    print clubHit.getOwnerName() + "'s club takes some damage!"
    clubHit.reduceQuality()
    print clubHit.getFullDescription()
    return clubHit

# Function to handle what happens when a player uses a club
# Input: the club being used
# Output: the club after it has been used
def useClub(clubUsed):
    if clubUsed.getClubQuality() < 1:
        print clubHit.getOwnerName() +"'s club is broken!"
    else:
        print "You swing the club."
        # have a random chance that the club is damaged.
        if random.randint(0,100) < 10:
            clubUsed = damageClub(clubUsed)
    # return the club after it's been used
    return clubUsed

# Make some clubs, and use them

# instantiate the clubs with basic properties
clubOne = GolfClub(44.5, 5, "pleather", "wood")
clubTwo = GolfClub(45, 4, "fur", "bone")
clubThree = GolfClub(44.75, 1, "cotton", "glass")
# add them to a list of all clubs
allClubs = [clubOne, clubTwo, clubThree]

# change more of the properties in each club
clubOne.setDescription("This is the first club")
clubOne.setOwnerName("Bernard Cudmore")
clubTwo.setDescription("2nd Club yay!")
clubTwo.setOwnerName("Tom Lieu")
clubThree.setDescription("Third Club")
clubThree.setOwnerName("Ryan & Lauren")

# Display the full descriptions of each club after changes
print clubOne.getFullDescription()
print 75*"-"

print clubTwo.getFullDescription()
print 75*"-"

print clubThree.getFullDescription()
print 75*"-"

print 75*"-"

##print clubThree.intQuality
##print clubThree.__strHeadMaterial

# Use all of the clubs once. 
for eachClub in allClubs:
    print "Using " + eachClub.getOwnerName() + "'s club..."
    useClub(eachClub)

