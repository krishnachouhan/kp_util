"""PACKAGE UTILITIES :
Utilities

  Author: Krishna Chouhan
  E-mail: krishna.chouhan34@gmail.com

  help(): help function will list all the members and methods.

  About:

    Functionalities
        DisplayAllVariables:
            Displays all the variables in current program scope. Has various options as parameters.
        ReadPickle:
            Reads a pickle file provided as argument and return the object.
        WritePickle:
            Writes a object to given file.
        ListFiles:
            List all the files and folders at location provided at the parameter path.
        VarSize:
            Displays the approximate size of variable size. Variable is passed as parameter.
        ExecuteQuery:
            Execute the query and returns the result in a DataFrame.
"""

def help():
    """
        prints the help regarding the package.
    """
    print("""    Functionalities
        DisplayAllVariables:
            Displays all the variables in current program scope. Has various options as parameters.
        ReadPickle:
            Reads a pickle file provided as argument and return the object.
        WritePickle:
            Writes a object to given file.
        ListFiles:
            List all the files and folders at location provided at the parameter path.
        VarSize:
            Displays the approximate size of variable size. Variable is passed as parameter.
        ExecuteQuery:
            Execute the query and returns the result in a DataFrame.
""")


def DisplayAllVariables(    search_str="", 
                            packages=True, 
                            global_variable=True, 
                            system_variable=True, 
                            local_variable=True, 
                            max_tries=3):
    """DisplayAllVariables: Displays all variables.
            Parameters:     
                            search_str="",          "Search for a particular string in the variables." 
                            packages=True,          "print packages"
                            global_variable=True,   "print global variables"
                            system_variable=True,   "print system variables"
                            local_variable=Trye,    "print local variables"
                            max_tries=3           "Number of tries this fuction makes"
    """
    print("*"*35)
    i = None
    counter = 0
    while(ocunter < max_tries): #number of times this function willl try to run.
        counter += 1
        try:
            for i in globals().keys():
                if system_variable==True:                   # checking for conditions for parameter
                    if i.count('__')==2:                    # cheking if the variable is a system variable
                        if len(search_str)>0:
                            if search_str.lower() in i.lower() or search_str.lower() in str(type(globals()[i])).lower():
                                print(i, " "*(40-len(i))+str(type(globals()[i])))
                                continue
                        else:
                            print(i, " "*(40-len(i))+str(type(globals()[i])))
                            continue
                if packages==True:                          # checking for conditions for parameter
                    if str(type(i))=="<class 'module'>":    # cheking if the variable is a system variable
                        if len(search_str)>0:
                            if search_str.lower() in i.lower() or search_str.lower() in str(type(globals()[i])).lower():
                                print(i, " "*(40-len(i))+str(type(globals()[i])))
                                continue
                        else:
                            print(i, " "*(40-len(i))+str(type(globals()[i])))
                            continue
                if global_variable==True:                   # checking for conditions for parameter
                    if i==i.upper():                         # cheking if the variable is a system variable
                        if len(search_str)>0:
                            if search_str.lower() in i.lower() or search_str.lower() in str(type(globals()[i])).lower():
                                print(i, " "*(40-len(i))+str(type(globals()[i])))
                                continue
                        else:
                            print(i, " "*(40-len(i))+str(type(globals()[i])))
                            continue
                    elif local_variable==True:                   # checking for conditions for parameter
                            if len(search_str)>0:
                                if search_str.lower() in i.lower() or search_str.lower() in str(type(globals()[i])).lower():
                                    print(i, " "*(40-len(i))+str(type(globals()[i])))
                            else:
                                print(i, " "*(40-len(i))+str(type(globals()[i])))
            print("*"*35)
            return
        except:
            if counter == max_tries:
                print("ERROR: \tFailed to Print!!!")

def ReadPickle(filename):
    """ReadPickle: Read the pickle files and return the object.
            Parameters:
                            filename                "Filename that is to be read"
    """
    import pickle
    var = None
    with open(filename, 'rb') as handle:
        var = pickle.load(handle)
    return var
    print("Something went wrong!")
    return

def WritePickle(filename, var):
    """WritePickle: Write the 'var' object in the pickle file.
            Parameters:
                            filename                "Filename that is to be witten in object"
                            var                     "Object to be written into the file."
    """
    import pickle
    try:
        with open(filename, 'wb') as handle:
            pickle.dump(var, handle)
        return
    except:
        print("Something went wrong!!!")
        return

def ListFiles(path=".", substr="", max_lines=15):
    """ListFiles: List the files in provided directory.
                Parameters:
                            path                    "Path to the directory"
                            substr                  "Seach for the substring in the file"
                            max_lines               "Split filename into 2 columns if number of files are more than max_files"
    """
    import os
    dash_space = 18
    files = sorted(os.listdir(path))
    files = [x for x in files if substr.lower() in x.lower()]
    if Path == ".":
        print("=="*80, "CURRENT_FOLDER_LISTING")
    else:
        print("=="*80)
    if len(files)<max_files:
        if len(substr)>0:
            for y in files:
                if "." in y:
                    print(y.split(".")[len(y.split("."))-1], "-"*(dash_space-len(y.split)[len(y.split("."))-1]), y, " "*(65-len(y)))
                else:
                    print("", "-"*dash_space, "", y, " "*(65-len(y)))
        else:
            for y in files:
                print(y.split(".")[len(y.split("."))-1], "\t", y, " "*(65-len(y)))
    else:
        alternator=True
        for y in files:
            if alternator:
                if "." in y:
                    print(y.split(".")[len(y.split("."))-1], "-"*(dash_space-len(y.split(".")[len(y.split("."))-1])), y, " "*(65-len(y)), end="")
                else:
                    print("", "-"*dash_space, "", y, " "*(65-len(y)), end="")
                alternator = not alternator
            else:
                if "." in y:
                    print(y.split(".")[len(y.split("."))-1], "-"*(dash_space-len(y.split(".")[len(y.split("."))-1])), y, " "*(65-len(y)))
                else:
                    print("", "-"*dash_space, "", y, " "*(65-len(y)))
                alternator = not alternator
    print("\n"+"=="*80)

def VarSize(var):
    """VarSize:     Displays the size of variable.
        Parameters:
                    var         "Variable whose size is to be displayed."
    """
    from sys import getsizeof
    size = getsizeof(var)
    if int(size/1000)==0:
        print(size, " Bytes")
    elif int(size/1000000)==0:
        print("Approx", size/1000, " KB")
    elif int(size/1000000000)==0:
        print("Approx", size/1000000, " MB")
    else:
        print("Approx", size/1000000000, " GB")

def ExecuteQuery(   query,
                    host="", 
                    user="",
                    password="",
                    dbname=""
                ):
    """ExecuteQuery: Executes the Query
        Parameters:
                    query:      "Query to be fired"
                    host:       "Server hosting DB"
                    user:       "User-Id"
                    password:   "Password"
                    dbname:     "DataBase name on the server"
    """
    import psycopg2
    import pandas as pd
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)
    cursor = connection.cursor()
    cursor.execute("SET statement_timeout='400000s'")
    print("Pulling Data frin database...")
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall())
    if len(df)>0:
        df.columns = [i.name.upper() for i in cursor.description]
    return df

