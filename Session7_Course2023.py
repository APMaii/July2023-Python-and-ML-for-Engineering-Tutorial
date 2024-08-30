# -*- coding: utf-8 -*-
"""
In the name of god
"""
#----------- structure
'''
vorodi: 
    az tabeye input()
    open yek file open()
    variable haro  bzrim assign
    def(vorodi)

body(calculation):
    mohasebate amalgarha + - * 
    traine hoshe masnooe
    preprocessign amade sazi data
    predict kardan
    if, if else, for , while
    
khoroji:
    print--> fgh chap mikone bma khoroji nmide estefade konim fght nshon mide
    returne def --> khoroji bde bebarim use konim
    savesh konim --> too folderamon
    plot ( rasm she)


#pas harmoghe khastim code bznim bayad in structuremon bashe

#tooo har marhale che konim?
#------vorodi input----
#too vorodi python buil in haro daryabid input() open()
#variable ha --> type ha mohem str,int ....
#badesh bayad rooye vorodi taghirati bdim shayad
#casting --> type()  int(input('adad bde:'))

#badesh miad vasate kar , hala ghrare rooye vorodimon
#raw nist ( kham nis roosh rpeprocess krdim amade krdimesh)
#ag mikhaym brim toosh ( iter bznim , peymayesh (bazresi))--> for
#agar bekhaym screening konim, gharbalgari yani biaym
#jolo dataharo bgirim shart bzrim mesle yek gharbalgar
#biad yeseri vorodi haro joda kone---> if , if_else
#if fght b onae k true bodn dastor mdiad
#if else miomd b onae ham ke sharteshon false bod ham dastoor midad

#age khastim yekchizio tekrar konim 'tekrar'__repeat-->loop
#for, while
#while vase zamanie k shartemon tahesho ndonim 
#az inja(start) ta vaghty ke shartemon true bashe yekkar ro hey tekrar kon
#for--> az start ta end inkaro anjam bde

#operator hamon + - / * **
#(parantez) > **> * > / > + > -
#a*b+2--> miad aval a*b mikone bad +2
#chikiar konimolaviat beshkonim--> parantez
#a*(b+2)
#tooye while ya if--> baraye shartemon az comparison-->
#== , =! , > , < , <= >=,

#khorojimone----
#baz mitronim yekseri taghirat bdim
#casting
#1-hichi fght biad print she-->fght in samte rast consule namayesh mishe
#vase chekari kolan bekar mire? baraye check krdn
#return--> yani biad meghdaro be ma bde baraye useeee ( estefade)





#--------chan no neveshtane in structure ro drim (vorodi,calculation,khoroji)


#pseducode(shebhe code) ta alan harkari kmikrdid

a=input()
c=a+b
if
for....
print(c)


#formal nis fght vae tamrino yad girie

#chikar konim?
#biaymaz class ya def estefade konim


#def-------
yek kaerkhone ro dar nazar bgirid ye esm dre
daghighan mese bala vorodi migire calculation mikone too body
va khoroji mide


def name(input):
    body (calculation)
    return output

#-------------------
*******nasihate doostane:
    ta alan shoma 50% e python ro yad grftid ama baghiash
    depend on your practice
    
    
'''

#structure def(function)
#1-tarif
#2-farakhani

#----------------tarif krdne tabe
#yek vorodi
def esmetabe( vorodiha):
    dastoorat
    
#do vorodi chi?
def jam(a,b):
    dastooor
    
#har esmi msihe gozasht? bale

#khoroji chi mide?


def jam(a,b):
    c=a+b
    
#in tabeye bala chie?
#sedash bzn
jam(4,5) #NameError: name 'jam' is not defined
#yani bayad aval tabe ro balatarin ghesmat ghabl az seda zadan tarif konim
#bad runesh konim
#bad sedash bznim

#vaghty run mzinim ,run nmishe ya ejra nmish ebalke sakhtare tabe ro save mikone
#hala k sedash miznim mire too tabe vorodi haro mizre\
jam(4,5) #hich kari nmikone

#python chikar mikone?
#miad aval jam ro mibine mige in chie? variable e chie ?
#mire barmigrde aghab donbale esme jam
#be yek tabe bar mikhore mifhme ke jam yek tabe hast
#mibine ke jam dota vorodi migire
#paas mire mibine dota vorodi migire miad check mikonbe too jaee ke
#sedash zadim aya too parantez dota vorodi gozashtim ya na

jam()
#TypeError: jam() missing 2 required positional arguments: 'a' and 'b'
#yani in tabe dota arqument, argoman, vorodi mikhad 
#miss shodan requirement ha , yani in dota shgart ha nis

jam(1)
#TypeError: jam() missing 1 required positional argument: 'b'

jam(3,4)
#a ro gozasht 3, b ro gozasht 4
#rft c = a+b = 7
#tamooom 
#mage ma nevehstim print ? na ya chizi naa
#soale badi , c koo?

#global drimo local
#barmigrdim hanonja k gfotm tabe ejra nmishe save mishe 

#local o global,
#yani har moteghayeri k darone tabe tarirf kridm fght tooye
#tabe sheankhte shdoe ast (local)
#na save mishe na biron mitonim sedash bznim

print(c) #NameError: name 'c' is not defined









c=15

def jam(a,b):
    c=a+b
    return c

jam(3,4)

print(c)

#in shod 15
##chra?--->chooon maghadir faghato faghat dakehele tabee rasmiat dre
#biron tabe nemishnasatesh ama vaghty az bala run msihe
#c=15 mizre 15 khob
#badesh tabe run nmishe fght save mishe
#vaghty sedash mikonim jam(3,4)
#mire bjaye a mzire 3 bjaye b4 miad c=3+4=7
#ama in c fght ye esme k mipare hamin
#va pas mide
#vaghty print(c) mirese c ie avalio nshon mide yani 15
#choon c ee k too tabe has fght too tabe rasmiat dre
#har moteghayeriiii

#age bekhaym baghie jaha ham bshnase 
#global c
#*************
c=15

def jam(a,b):
    global c
    c=a+b
    return c

print(c)
#15

#--------------------------

c=15

def jam(a,b):
    global c
    c=a+b
    return c

jam(3,4)

print(c)
#7

#--------------------------


def jam(a,b):
    global c
    c=a+b
    return c
jam(3,4)

#ta inja c=7

c=15


print(c)

#dALILESH MESE PAEEN
a=5
a=7

#dar akahr
#print(a)
#akahriaro

#----------------------------------
def jam(a,b):
    c=a+b
    
#vaghty seda miznim hichi nmiare
jam(2,3)



#chanta rah drim-->2 ta
def jam(a,b):
    c=a+b
    print(c)
    
jam(3,4)
#in kalame ee k inja neveshtam yek dastoooreee fght

#hata mitonm printaye dg bgirm

def jam(a,b):
    c=a+b
    print('our result is:',c)
    
    
    
jam(3,4)
#va ta oja mishe toosh nevesht?
#ta kole bodyyy ta vaghty space bashe


#2----
#return drim
#inja dg yek dastoor nis balke bar migrdone
#yani:

def jam(a,b):
    c=a+b
    return c  #koja barmigrdone??
#hamonjaee k sedash zdim


#tozhh*******
jam(3,4) #fill, por mione ino 


#ma mitonimk assign bdim ya useee

elastic=jam(3,4)
    
#aval elastic ro mibine jolosh ye mosavi mifhme ye zarfe ijn esmeshe
#jolosh chie? ag adad bod mizasht dakhel ag str bodmizasht
#ama ye esme
#in mitone esme yek variabl bashe ya yek def
#mire bala migrde donbale esme jam
#mibine yek tabe hast
#in tabe dotavorodi mikhad
#barmigrde vorodi haro migire
#mizare jaye a 3 jaye b 4 va c ro hesab mikone
#mirese be return
#c ro return mide
#koja? hamonjaee k bod
#yani python mibine
#elastic=7



#yek rahe dg baraye def haye sade

def jam(a,b):
    return a+b

def jam(a,b):
    c=a+b
    return c


#jofteshon yekian 
#ama dar ereal world --> ma bishtr az yek calculation drim

#deafult and others...........
#bjaye inke biam 4 ta def bsazam zarb,jham,taghsim va vava
#biam ye def bsazam be esme amalgar


def calculator(num1,num2,amalgar):
    
    if amalgar=='+':
        result=num1+num2
    if amalgar=='-':
        result=num1-num2
    if amalgar=='*':
        result=num1*num2
    if amalgar=='/':
        result=num1/num2
    #ta inja result hesab mishe bar hasbe amalgari k dadim

    return result


calculator(3,4,'+') #Out[16]: 7
    
calculator(4,5,'0-239')   
#UnboundLocalError: local variable 'result' referenced before assignment

#yedone return fght drim? naaa 
def calculator(num1,num2,amalgar):
    
    if amalgar=='+':
        result=num1+num2
        return result
    if amalgar=='-':
        result=num1-num2
        return result
    if amalgar=='*':
        result=num1*num2
        return result
    if amalgar=='/':
        result=num1/num2
        return result
    
    
calculator(4,5,'0-239')   
#hichi nmide #mipare mire

def calculator(num1,num2,amalgar):
    
    if amalgar=='+':
        result=num1+num2
        return result
    elif amalgar=='-':
        result=num1-num2
        return result
    elif amalgar=='*':
        result=num1*num2
        return result
    elif amalgar=='/':
        result=num1/num2
        return result
    else:
        print('correct your operator')
    
calculator(4,5,'0-239')   

#case e jadi
#--default saziiii
def calculator(num1,num2,amalgar):
    
    if amalgar=='+':
        result=num1+num2
        return result
    if amalgar=='-':
        result=num1-num2
        return result
    if amalgar=='*':
        result=num1*num2
        return result
    if amalgar=='/':
        result=num1/num2
        return result
calculator(4,5)
#TypeError: calculator() missing 1 required positional argument: 'amalgar'
   
  
def calculator(num1,num2,amalgar='+'):
    
    if amalgar=='+':
        result=num1+num2
        return result
    if amalgar=='-':
        result=num1-num2
        return result
    if amalgar=='*':
        result=num1*num2
        return result
    if amalgar=='/':
        result=num1/num2
        return result
    
calculator(4,5) #= calculator(4,5,'+')
    
#harki az vorodi ha k = nadare yani ejbarie
#oonae ke = dare ekhtiari (yani ma jash yek default pishfarz mizrim)

#bia fght baraye plate ha bsazim
#V=pi r**2 h

def nanoparticle_volume(h,r):
    pi=3.14
    volume=pi*h*(r**2)
    return volume
    
def nanoparticle_volume(h,r):
    volume=3.14*h*(r**2)
    return volume
 
def nanoparticle_volume(h,r):
    return 3.14*h*(r**2)

# har 3 ta yekie

gold_volume=nanoparticle_volume(2,3)

print(gold_volume) #56.52

#hala yeki mige agha biaym baraye ona ke cubic ham hastan bsazima
def plate_nanoparticle_volume(h,r):
    return 3.14*h*(r**2)

def cubic_nanoparticle_volume(d):
    return d**3

#-----------------ghashang nis asan herfe ee nis
#hamaro bayad bary too ye tabe

def nanoparticle_volume(shape,h,r,d):
    
    if shape=='cubic':
        #dastoor vase cubic ha
        V=d**3
        return V
    
    if shape=='plate':
        #agha inkaro kone
        V=3.14*h*(r**2)
        return V
        
nanoparticle_volume('cubic',d=4)

#TypeError: nanoparticle_volume() missing 2 required positional arguments: 'h' and 'r'


#h o rchie man d drm fght


#fedault sazi

def nanoparticle_volume(shape,h=1,r=1,d=1):
    
    if shape=='cubic':
        #dastoor vase cubic ha
        V=d**3
        return V
    
    if shape=='plate':
        #agha inkaro kone
        V=3.14*h*(r**2)
        return V
    
nanoparticle_volume('cubic')
#Out[34]: 1
#hmaishe d ro 1 migeiore magar inke ma taghir bdim dr farakghani
nanoparticle_volume('cubic',d=5)
#Out[35]: 125


#======tozihat 
#mitonim tozihat ezafer kojnim b tabamon
def nanoparticle_volume(shape='cubic',h=1,r=1,d=1):
    
    if shape=='cubic':
        #dastoor vase cubic ha
        V=d**3
        return V
    
    if shape=='plate':
        #agha inkaro kone
        V=3.14*h*(r**2)
        return V
    
nanoparticle_volume()

#def dakhelesh ma hame kr mikonim if mizrim for mizrim va vava


#----------def
#mitonim tozih ezafe konim
def tafrigh(a,b):
    '''
    

    Parameters
    ----------
    a : int
        avalin adad.
    b : int
        dovomin adad.

    Returns
    -------
    c : int
        tafrigh mikone dotaro.

    '''
    c=a-b
    return c
    



tafrigh

def tafrigh(a,b):
    '''
    this function substrate numbers
    a is first number and b is second number
    
    '''
    c=a-b
    return c

tafrigh()

#---type e tahvile porozhe
def tafrigh(a,b):
    '''
    #yek tozihe ye kjhati
    Parameters
    ----------
    a : int
        avalin adad.
    b : int
        dovomin adad.
    -----------
    c : int
        polymer viscosity.

    '''
    c=a-b
    return c

tafrigh()

#in az atbe hq


#-------madule chie?


#dghifghan hamin safe ee k man toosh nvshtm behesh migan madule
#savesh konm mishe name.py

#dar madule
#3 ta chiz dakheleshe
#1- constant --> adade sabbet va variable has
#2-def
#3-class ( class tashkil shode az tedade ziadi def)



#mesal--> firstmadule.py

#misazim toosh adad sabet mizrim
#tabe mzirim
#savesh mikonim

#hala yeja dg mikhaym estefade konim --> import


#first way:
import firstmadule
#ModuleNotFoundError: No module named 'firstmadule'


#yek rahe dg ham hast

firstmadule.pi
#3.14


#ag tabe khastim chi? parantez dydt nare

firstmadule.zarb(3,4)
#Out[43]: 12

#yek rahe sade

import firstmadule as f

#yani mokhafafesh konim
f.pi
f.zarb(3,4)




#pas fhmidim madule chie

#ketabkhone chie??
#yek foldere mese yek ketabkhoone
#por az maduleeeeeee koli madule dre
#-- har madule kioly function, class o .. dre


#sade trin madule

import math
#ag import shod ok ok ag na harfaye akhare jalase ro fgosdh bdid
#masalan radikal bgirm
#** ....

math.sqrt(4) #Out[48]: 2.0
#dar halate adi
#bayad yek functionbsazim
def sin(a):
    #dfonbale ye ssin ro bsazim
    #p hro bznim
    #n bgirim
    #radiano tbdilk konim
    #bargardonim
    s=43*a
    return s

#bjaye sakhte in hame def
#rahat yeki bode 
#math ro skhte
#yek tabe bename sin sakhte
#kafie aval esme ketabkhone bad oon tabe ro seda bznim

math.sin(30)



math.pow(2,4) #Out[50]: 16.0
#constant adade sabet

#k dfg niazi b parantez



math.e

math.pi



#in shdo math
#cmath ham drim k ykm pishrafte tare

import cmath
#arc cosin hyperbolic o ina ham dre


math.floor(4.15)


#----------------------------

#ketabkhone haye default k dre aksaran
#math
#cmath
#random
#statistic
#date


import #esmeshon



#hala ketabkhone haye maroof k ghrare kar konim
import numpy #bartaye moahsebat
import matplotlib #baraye rasm
import pandas #baraye kar ba dade preprocess
import sklearn #baraye hooshe masnoee

#inaro ndre default bayad brim brizim


#yadetone yekseri environment dashtim???
#rooot --> khey7lia hanoz roo root drn run mikonan

#anacvonda

#******
#-----------
#search name pip


#avalin sait ba esme pypi
#copy konid
#paste dar powershell


#har mohit dota chiz dre
#1-spyder
#2-powershel

#vaghty mikham vared shyam naizi b abaz krdne anaconda nis
#hamin chasp paeen start 
#havasam bashe ke ()


#baraye jalase dg
import math
import cmath
import random
import statistics



import numpy


#** ehtemalkan 4 taye balaro drid niazi b pip o install nis
#ama baraye numpy bayad search bznid

#=====================================================================
#=====================================================================
#=====================================================================
#=====================================================================
#-----------------baraye jalasate bad-----------------------

#1- import haro check konid:
    math,cmath,random,statistics inaro ehtemalan drid

#2-brid numpy ro import konid ag nadarid ya harkodom az balaharo ndrid 
#search konid pip esme library, bad avalin sait
#oon tike ke neveshte pip install numpy ro copy konid


#oon mohiti ke hamishe run mikonid spyder(esme mohit)
#search konid anaconda powershell , hatman too parantezesh esme
#mohiti bashe ke hamishe spyder ro run mikonid
#bznid yek safe siah miare
#vaysid load she va bad paste konid pip install ro 
#enter ro bznid
#vaysid download she va install bshe
#badesh biad import numpy bznid va bbinid ovord ya na





#3------
#tabe haro nahayat ta jome bdid + do tabeye jadid
#hatman tozihat bznid
#hatman esm ha doros bashe
#hatman converter ha dotarafe bashe yani masalan
#cantimeter to meter , va ham meter to cantimeter



#GOOD LUCK!!!
#=====================================================================
#=====================================================================
#=====================================================================
#=====================================================================



