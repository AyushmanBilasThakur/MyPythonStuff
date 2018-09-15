import pathlib
import os

def execute(path_in_string, soucrce_code_name, input_file_name, output_file_name):
    if(path_in_string != ""):
        #----Creating the path According to windows standards----#
        path = pathlib.PureWindowsPath(path_in_string)
        #----If the programme is executed from other drive then this will change the drive letter----#
        os.chdir(str(path)[:2])
        #----Used to go to the destination directory----#
        os.chdir(path)
    
    #----Google Code Jam Style Execution, taking input.in as input and giving output.out as output----#
    os.system("python " + str(soucrce_code_name) + " < " + str(input_file_name) + " > " + str(output_file_name))

    print("Execution Done!!")
    
    
#----Source Directory----#
director = input("Enter source code directory(leave blank for this directory): ")

#----Input of Source Code Name----#
pyfile = input("Enter python file name(Default: main.py):")
if(pyfile == ""):
    pyfile = "main.py"

#----Input of input fiile name----#
inpfile = input("Enter input file name(Default: input.in):")
if(inpfile == ""):
    inpfile = "input.in"

#----Input of output fiile name----#
outfile = input("Enter output file name(Default: output.out):")
if(outfile == ""):
    outfile = "output.out"

#----Execution of the function containig the main piece of code with required values----#
execute(director, pyfile, inpfile, outfile)