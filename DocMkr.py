#!/bin/python3
## DocMkr.py
### Description
# This script is sesinged to allow the creation of documentaton by using Markdown style writing in your comments
# by steel99xl
### Imports
import sys, getopt


### Main Function
# This handles  commandline argument parsing and the calling of other functions
def main(argv):
    language = ''
    inputfile = ''
    outputfile = ''
    commentmarker = ''
    try:
        opts, args = getopt.getopt(argv,"hl:i:o:",["language=","ifile=","ofile="])
    except getopt.GetoptError:
        print ('DocMkr.py  -l <language> -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if (opt == '-h'):
            print ('DocMkr.py  -l <language> -i <inputfile> -o <outputfile> \n')
            print(' Currently supported languages\n python')
            sys.exit()
        elif(opt in ("-l", "--language")):
            language = arg
        elif (opt in ("-i", "--ifile")):
            inputfile = arg
        elif (opt in ("-o", "--ofile")):
            outputfile = arg
    commentmarker = LanguageIndex(language)
    Parser(language, commentmarker, inputfile, outputfile)


### Language Index
# Adding additional language comment detection is as easy as adding the name and the marker for comments
# NOTE : The name for the language should the same as the markdown version
def LanguageIndex(language):
    if(language.upper() == "PYTHON"):
        return '#'


### Parser
# This is where the provided source code gets parsed and converted to a Markdown document
def Parser(language, commentmarker, inputfile, outputfile):
    try:
        MainFile = open(inputfile, 'r').read().splitlines()
        ExportFile = open(outputfile, 'w+')
        EmptyLines = 0
        TopBottom = True
        for i in MainFile:
            MarkCount = -1
            if(commentmarker in i):
                Buff = i
                if(commentmarker == "#"):
                    Buff = i.strip()
                    if(Buff[0] == commentmarker):
                        Buff = i
                        for x in i:
                            if(x == "#"):
                                MarkCount += 1
                        i = i.strip()
                        i = i.strip(commentmarker)
                        i = "#"*MarkCount + i
                    else:
                        Buff = ""
                else:
                    i = i.strip()
                    i = i.strip(commentmarker)
            else:
                if(Buff != ""):
                    ExportFile.write("```" + language +"\n")
                    TopBottom = False
                    Buff = ""
                if(i.strip() == ""):
                    Buff = i.strip()
                    EmptyLines += 1
                    if(EmptyLines == 2):
                        EmptyLines = 0
                        if(TopBottom):
                            TopBottom = False
                            ExportFile.write("```"+ language +"\n")
                        else:
                            TopBottom = True
                            ExportFile.write("```\n")
            ExportFile.write(i + "\n")
        if(TopBottom == False):
            ExportFile.write("```\n")
    except:
        print("Error no such file")


### Check if this program is main
if __name__ == "__main__":
    main(sys.argv[1:])
