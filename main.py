import os
from collections import namedtuple
import logging

dir = str(input('Введите путь: '))

def getContentInLog(dir):
    anslog = ""
    mas = namedtuple('mas', ['namefile', 'extension', 'flag', 'parentcatalog'])
    content = os.listdir( dir )
    for elem in content:
        maselem = mas('' , '', '', '')
        checkIsFile = elem.split(".")
        if ( len(checkIsFile ) == 2 ):
            maselem = maselem._replace(namefile = checkIsFile[0])
            maselem = maselem._replace(flag=False)
            maselem = maselem._replace(extension= checkIsFile[1])
        else:
            maselem = maselem._replace(namefile = checkIsFile[0])
            maselem = maselem._replace(flag=True)  
        parentcatalog = dir.split("/")  
        maselem = maselem._replace(parentcatalog= parentcatalog[-2] )           
        anslog += "namefile= " + maselem[0] + " extension= " + maselem[1] + " flag= " + str(maselem[2]) + " parentcatalog= " + maselem[3] + "\n"
     
    logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")
    logging.info( anslog )
    return anslog

print( getContentInLog(dir) )

