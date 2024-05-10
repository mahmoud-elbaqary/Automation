'''
this pyhton script for files classification
script process:
1- at source path scan for files every folder and subfolder  at this path 
2-at destination path create a folder for each file type and rename it with extention name
4-make a copy from this file to its folder catigory

How to run :
run script from CLI ex: python filesclassification.py sourcePath destinationPath
change sourcePath , destinationPath with your paths

Note:
Not appropriate for all data types

Auther :Mahmoud Elbaqary
'''

#import os library
import os
import shutil
import typer

app=typer.Typer() # use typer to run the code from CLI 

@app.command()
def filesClassification(src:str,des:str):   
    

    # srcPath='C:\\Users\\user1\\Desktop'
    # desPath='d:\\classification'
    srcPath=src #get source path 
    desPath=des #get destination path
    typesList=[]#list to register file types
    for pathName,folders,files in os.walk(srcPath): #loop for walk throw every available path and return path name as a string , folders names and file names as a list 
        for fileName in (files): # loop on a list of files 
            extention=fileName.split('.')[-1] #get file extention
            if extention not in typesList : # if extention have not been registered before
                typesList.append(extention) # add extention to the list
                os.makedirs(os.path.join(desPath,extention),exist_ok=True) # make a folder with extention name , we use join to create a complete path [path+filename.extention]
            elif extention in typesList :   # if not -> means that the extention have been registered before
                os.chdir(os.path.join(desPath,extention)) # go to the extention folder
                #Both src and dst need to be the entire filename of the files, including path.
                src=os.path.join(pathName,fileName) 
                dst=os.path.join(desPath,extention)
                print(f'Copy file {src} - to - {dst}')#print the process indecator
                shutil.copy(src,dst)#make a copy from source to destination


if __name__=="__main__" :
    app()



