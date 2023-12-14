#This is an example of a model interface. It needs to include a few things
#1. Input Format
#2. Output Format
#3. Call Function: call()
#4. Test procedure under if __name == '__main__': (Reccomended)
#...and that's it!

#The remainder of the file should be used to specify how the model is loaded
#eg. from local storage, from cloud storage, from api connection, or interface code
#...it is up to you to store the model files, test-data, or other resources where you see fit!
# 

from pydantic import BaseModel

class Input(BaseModel):
    ...

class Output(BaseModel): 
    ...

if __name__ == '__main__':
    ... #test
