def sortStack(stack):
    # Write your code here.
    final_data=[]
    
    for i in range(0,len(stack)):
        if len(final_data)==0 or final_data[-1]<stack[i]:
            final_data.append(stack[i])
        else:
            rec_data=[]
            for j in range(i-1,-1,-1):
                if stack[i]<final_data[j]:
                    rec_data.append(final_data[j])
                    final_data.pop()
                    
            final_data.append(stack[i])
            
            for j in range(len(rec_data)-1,-1,-1):
                final_data.append(rec_data[j])
        
    return final_data
