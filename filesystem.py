"""
Created on Tue Apr 21 2021

@author: Matteo Rama

Subject:
This Python program is used to simulate a file system 
that supports basic commands such as ls, mkdir, cd and touch. 
"""

#Define initial class
#Parameter parent is the parent directory
#Parameter name is the directory name
class FileSystem:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.dir = []
        self.file = []

#Global variables
root = FileSystem(parent=None, name='users')
cur = root
path = 'users'

#Create empty file
def touch(name):
    global cur
    if name in cur.file:
        return print("",end='')
    cur.file.append(name)

#Create directory
def mkdir(name):    
    global cur, path
    for i in cur.dir:
        if i.name == name:
            return print("",end='')
    newdir = FileSystem(parent=cur, name=name)
    cur.dir.append(newdir)

#Change current directory
def cd(name):
    global cur, path
    if name == '..':
        if cur.parent != None:
            path = path[:(len(path)-len(cur.name))-1]
            cur = cur.parent
    else:
        for i in cur.dir:
            if i.name == name:
                cur = i
                path = path + '/' + name

#List files and directories    
def ls():
    global cur
    for i in cur.file:
        print('    ',i)
    for i in cur.dir:
        print('    ', i.name)
        
#Run the main program
if __name__ == '__main__':
    while True:
        print(path, end='>')
        user_input = input().split(' ')
        if user_input[0] == 'touch':
            try:
                touch(user_input[1])
            except:
                print('touch: missing file operand')
        elif user_input[0] == 'mkdir':
            try:
                mkdir(user_input[1])
            except:
                print('mkdir: missing operand')
        elif user_input[0] == 'cd':
            try:
                cd(user_input[1])
            except:
                print('no such file or directory')
        elif user_input[0] == 'ls':
            ls()
        elif user_input[0] == '':
            print("",end='')
        else:
            print('Command "{}" not found'.format(user_input[0]))
