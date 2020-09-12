
"""
Just 
"""

First_file_path=raw_input("Enter path to First file:\n")
Second_file_path=raw_input("Enter path to Second file: \n")

file_1=open(First_file_path,"r")
file_2=open(Second_file_path,"r")

print "******************************************************************"

for item,item2 in zip(file_1,file_2):
    #print "-------"
    #print item.strip()
    #print item2.strip()
    try: 
        if item.strip()!=item2.strip():
            print prev1
            print "File 1 is Like :"+item
            print "File 2 is Like :"+item2
            print "******************************************************************"
    
        prev1=item
    except:
        print "Some Error has Occured"
        
raw_input("Press any button to Exit !!");
