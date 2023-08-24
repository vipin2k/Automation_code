import os
def htmlreportor(data,operation):
    Func = open(str(os.getcwd())+"Reports/htmlreports/Report.txt",operation)
    Func.write(data)
    Func.close()