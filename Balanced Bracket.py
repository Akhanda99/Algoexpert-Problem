def balancedBrackets(string):
    # Write your code here.
    loaded_string=[]
    bracket_dict={
        ')':'(', '}':'{', ']':'[', '(':None,'{':None,'[':None
    }
    
    for i in range(0,len(string)):
        if not loaded_string and string[i] in bracket_dict:
            loaded_string.append(string[i])
            
        else:
            if string[i] in bracket_dict:
                if bracket_dict[string[i]]==loaded_string[-1]:
                    loaded_string.pop()
                else:
                    loaded_string.append(string[i])
        
            
    if len(loaded_string)>0:
        return False   
    
    return True

string="(141[])(){waga}((51afaw))()hh()"
print(balancedBrackets(string))
