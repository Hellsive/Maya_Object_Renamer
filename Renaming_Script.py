from maya import cmds

selection = cmds.ls(selection=True, long=True)

print selection

# Checks selected object
if len(selection) == 0:
    selection = cmds.ls(long=True, dag=True)

selection.sort(key=len, reverse=True)

# Declares name in selection for original object
for obj in selection:

    shortName = obj.split('|')[-1]

    print "Original: ", shortName

    children = cmds.listRelatives(obj, children=True) or []

# Checks if there are children to selected object.
    if len(children) == 1:
        child = children[0]
        objType = cmds.objectType(child)
    else:
        objType = cmds.objectType(obj)

# Object type and renaming suffix function
    if objType == "mesh":
        suffix = 'GEO'
    elif objType == "joint":
        suffix = 'JNT'
    else:
        suffix = 'Group'

    # Creates new shortened suffix
    newName = shortName+"_"+suffix

    # Adds new title to selected objects
    cmds.rename(obj, newName)

    print "New Name: ", newName