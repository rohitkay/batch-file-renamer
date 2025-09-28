#import operating system module
import os

#Function to change the directory
def batch_rename():
    #set current directory path
    #get inputs from user for folder directory
    directory = input("Please provide the path to the directory you would like to batch rename within")

    #get input for prefix to use
    prefix = input("Plese type in the prefix to add to all files")

    #check if file path is valid
    if os.path.isdir(directory) == False:
        print("Error: the directory path is invalid")   
    
    #folder_items
    folder_items = os.listdir(directory)

    for file in folder_items:
        old_path = os.path.join(directory,file)
        new_name = prefix + file
        new_path = os.path.join(directory,new_name)