import pandas as pd
data=pd.read_csv("airlines.csv")
airportName=data['Airport.Name']
attr=list(set(airportName))
count=[0]*len(attr)
for i in range(len(attr)):
    for j in range(len(airportName)):
        if airportName[j]==attr[i]:
            count[i]+=1;
mini=min(count)  
maxi=max(count)
for i in range(len(attr)):
    if count[i]==mini:
        miniName=attr[i]
print("{")        
for i in range(len(attr)):
    print("\"",attr[i],"\":",count[i],"\n")
print("}")    
for i in range(len(attr)):
    if count[i]==maxi:
        maxiName=attr[i]
print(maxiName," ",maxi,"\n") 
print(miniName," ",mini,"\n") 
    
    
