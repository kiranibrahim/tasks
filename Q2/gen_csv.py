import csv  
import random



with open('data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    
    for i in range(0,100000):
        data=[]
        for j in range(0,4):
        
            data.append(random.randint(0,1500))
        writer.writerow(data)

    # write the header
    #writer.writerow(header)

    # write the data
    


