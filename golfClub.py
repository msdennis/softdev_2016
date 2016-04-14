###############################################################################
# This is a Golf Club
# Golf clubs have the following properties:
#   - description: string
#   - owner: string
#   - material: string
#   - quality: integer
#   - length: float
# Author: Selina Dennis
# Year: 2016
###############################################################################

class GolfClub:
    ###############################################################################
    # these are two global variables. They can be accessed at any time.
    # these are called "class variables" and can be accessed even if the class
    # hasn't been instantiated into an object.
    ###############################################################################
    strDesc = "This is a stylish golf club."
    strOwner = "Nobody owns this golf club yet"

    ###############################################################################
    # Initialises all of the variables used.
    # Required Arguments:
    #   - grip length: float
    #   - club quality: integer
    #   - grip material: string
    #   - club head material: string
    # Return Value:
    #   None
    ###############################################################################
    def __init__(self, fGLen, iQual, sGMat, sHMat):
        ###########################################################################
        # these variables are local, but by using 'self' we make them
        # visible to the rest of the class. These can only be used
        # if the object has been instantiated.
        ###########################################################################
        self.intQuality = iQual
        self.strGripMaterial = sGMat
        self.flGripLength = fGLen
        ###########################################################################
        # if you use a double underscore, you can hide a variable from any
        # code that uses your class. This is useful if you want have code
        # check things before allowing a variable to be set or changed.
        # For this example, let's pretend we never want a player to swap out
        # the head of the golf club.
        ###########################################################################
        self.__strHeadMaterial = sHMat

    ###############################################################################
    # Reduces the quality of the club
    # Required Arguments:
    #   None
    # Return Value
    #   None
    ###############################################################################
    def reduceQuality(self):
        if self.intQuality > 1:
            self.intQuality = self.intQuality - 1
        else:
            self.intQuality = 0
    
    ###############################################################################
    # Gets the quality of the club
    # Required Arguments:
    #   None
    # Return Value
    #   the grip quality: integer
    ###############################################################################
    def getClubQuality(self):
        return self.intQuality
    
    ###############################################################################
    # Sets the grip material of the club
    # Required Arguments:
    #   - new material: string
    # Return Value
    #   None
    ###############################################################################
    def setGripMaterial(self, strNewMat):
        self.strGripMaterial = strNewMat
    
    ###############################################################################
    # Gets the grip material of the club
    # Required Arguments:
    #   None
    # Return Value
    #   the grip material: string
    ###############################################################################
    def getGripMaterial(self):
        return self.strGripMaterial

    ###############################################################################
    # Gets the club head material 
    # Required Arguments:
    #   None
    # Return Value
    #   the club head material: string
    ###############################################################################
    def getHeadMaterial(self):
        return self.__strHeadMaterial
    
    ###############################################################################
    # Sets the description of the club
    # Required Arguments:
    #   - new description: string
    # Return Value
    #   None
    ###############################################################################
    def setDescription(self,strText):
        self.strDesc = strText

    ###############################################################################
    # Gets the description of the club
    # Required Arguments:
    #   None
    # Return Value
    #   the description of the club, with an indication of its condition: string
    ###############################################################################
    def getDescription(self):
        if self.intQuality == 5:
            strCondition = "perfect"
        elif self.intQuality == 4:
            strCondition = "very good"
        elif self.intQuality == 3:
            strCondition = "good"
        elif self.intQuality == 2:
            strCondition = "okay"
        elif self.intQuality == 1:
            strCondition = "terrible"
        else:
            strCondition = "unuseable"

        strAddedDesc = "This club is in " + strCondition + " condition."
        return self.strDesc + "\n" + strAddedDesc
        
    ###############################################################################
    # Sets the owner name of the club
    # Required Arguments:
    #   - new owner: string
    # Return Value
    #   None
    ###############################################################################
    def setOwnerName(self,strText):
        self.strOwner = strText

    ###############################################################################
    # Gets the owner of the club
    # Required Arguments:
    #   None
    # Return Value
    #   - name of the owner: string
    ###############################################################################
    def getOwnerName(self):
        return self.strOwner

    ###############################################################################
    # Gets the grip length of the club
    # Required Arguments:
    #   None
    # Return Value
    #   the grip length: floating point
    ###############################################################################
    def getGripLength(self):
        return self.flGripLength

    ###############################################################################
    # Gets the full description of the club
    # Required Arguments:
    #   None
    # Return Value
    #   A formatted description of all of the elements of the club: string
    ###############################################################################
    def getFullDescription(self):
        strFullDescription = [ self.getDescription(),
                               "- Owner: "+self.getOwnerName(),
                               "- Grip Material: "+self.getGripMaterial(),
                               "- Head Material: "+self.getHeadMaterial(),
                               "- Grip Length: "+str(self.getGripLength()) ]
                               
        return "\n".join(strFullDescription)

