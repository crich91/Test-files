


def Brackets_Check(Input_String):
    # List for checking open brackets
    list_of_Brackets = []
    # Key value pair for open and closed brackets
    BracketKeyValue = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    for Char in Input_String:
        # Append all opening brackets to a list
        if Char in BracketKeyValue.values():
            list_of_Brackets.append(Char)
        # Check if a closing bracket
        elif Char in BracketKeyValue.keys():
            # Check if an open bracket is in the list
            if len(list_of_Brackets) == 0: 
                return False
            # Check key/value, if in list of brackets then pop out
            else:
                if BracketKeyValue.get(Char) in list_of_Brackets:
                    list_of_Brackets.pop()
                continue   
        else:
           continue
    # if list still has values, then there is a miss match somewhere in the string
    if len(list_of_Brackets) == 0:
        return True
    else:
        return False
    




Text = "This is (a) {test}[]"
str(Text)
print(Brackets_Check(Text))
