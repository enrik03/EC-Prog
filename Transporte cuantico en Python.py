
# Programa en python para transporte electronico 

import math as m 
import numpy as np
#import matplotlib as pt
#import pandas as pd 

# !Parameters
# !--------------------------------------------------------------------------
# real*8,parameter                       ::Pi       = 3.14159265358979323846d00
# real*8,parameter                       ::Ech      = 1.0d0                           
# real*8,parameter                       ::Hp       = 1.0d0                           
# real*8,parameter                       ::Kb       = 8.6173324d-05                        
# real*8,parameter                       ::CF       = 27.2116d00                        
# real*8,parameter                       ::delta    = 1.0d-12
# real*8,parameter                       ::test_E   = -5.50d00
# contains 
NL = int 
NM = int
NC = int 
Cicle = int 
LHX = int 
LHXY = int 
HOMOX = int
HOMOXY1 = int
HOMOXY2 = int 
NS = int
NB = int
Tp = float 
Ef = float
DC_volt = float 
Gm = float
MuL = float
MuR = float 
Lead = str*2 
Project = str*10
afileN = str # Tiene que ser un array de caracteres
IntSub = int 
ifileN = int 


# 1:First subroutine: input the initial data. will be stored in the input_data.dat file 

ifileN = int(input()) 
afileN = str 
i,j,k,stat = int 
inidata = str
seqfile = str

chart_int(ifileN,afileN)
## inidata= 'input_data-'//trim(adjustl(afileN))//'.dat'
#open(UNIT=10,file=trim(inidata),status='old',action='read',IOSTAT=stat)

open()
if (stat != 0): 
    print("Main: error opening ini file")

FindTagA(10, "System =", Project)
FindTagA(10, "Electrode =", Lead)
FindTagI(10, "Number of levels =", NL)
FindTagI(10, "Number of monomers =", NM)
FindTagI(10, "Number of cicles =", NC)
FindTagR(10, "DC bias voltage =", DC_volt)
FindTagR(10, "Scape rate =", Gm)
FindTagR(10, "Temperature =", Tp) 

close()