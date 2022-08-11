import os
import sys

""" get all the variables of the enviroment"""
def get_env_variables():
    env_variables = os.environ.keys()
    return env_variables

my_env = get_env_variables()

#for key in my_env:
#    print(key, os.environ[key])

## if else statement for a menu
my_input = int(sys.argv[1])

if my_input == 1:
    print (" the value of HOME is ", os.environ['HOME'])

elif my_input == 2:
    print (" the value of HISTFILESIZE is ", os.environ['HISTFILESIZE'])

elif my_input == 3:
    print (" the value of KAUST_NODETYPE is ", os.environ['KAUST_NODETYPE'])

elif my_input == 4:
    print (" the value of PWD is ", os.environ['PWD'])

elif my_input == 5:
    print (" the value of LOGNAME is ", os.environ['LOGNAME'])

elif my_input == 6:
    print (" the value of MPI_HOME is ", os.environ['MPI_HOME'])

elif my_input == 7:
    print (" the value of SHELL is ", os.environ['SHELL'])

else:
    print (" the value of USER is ", os.environ['USER'])


