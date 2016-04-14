# Gets all files from a directory of a particular extension
# Selina Dennis, April 2016

import os

# Get all files of a particular type
# Input:    folder name, string
#           file extension, generally four character string
# Output:   List of files matching extension
def getAllFiles( folderName, fileType ):
    listValidFiles = []
    listAllFiles = os.listdir( folderName )
    for eachFile in listAllFiles:
        if eachFile.endswith( fileType ):
            listValidFiles.append( eachFile )
    return listValidFiles

print "\n".join(getAllFiles( "C:\\PythonDataFiles", ".csv"))
