# Niels Keller
# Generate java getters/setters from and input txt file



def genget(varname):

        # Uppercase first letter
        varnameTitle = varname.capitalize()

        
        # return formatted string
        return  (f"""
/**
* get{varnameTitle}() gets {varname}
* 
* @return {varname}
*/
            
public String get{varnameTitle}()""" + "{" + f"\n\treturn {varname};\n" + "}")
        


def genset(typeName, varname):

        # Uppercase first letter
        varnameTitle = varname.capitalize()

        
        # return formatted string
        return  (f"""
/**
* set{varnameTitle}() sets {varname}
* 
* @param {varname}
*/         
public void set{varnameTitle}({typeName} {varname})""" + "{" + f"\n\tthis.{varname} = {varname};\n" + "}")




def main():
    infile = "input.txt"
    outfile = "output.txt"
    varNames = []

    with open(infile) as f:
        for i in f:
            #For each line in file pull first (type) and second (name)
            varNames.append(i.split())



    with open(outfile,"w") as f:

        #print everthing to file
        for i in varNames:
            f.write("\n\n")
            f.write(genget(i[1]))
            f.write("\n\n")
            f.write(genset(i[0],i[1]))


if __name__ == "__main__":
    main()