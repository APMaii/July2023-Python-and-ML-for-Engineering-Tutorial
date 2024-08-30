"""
EVERYTHING COMES FROM GOD 
@author: Ali Pilehvar Meibody
"""

#----------------Library ha-------------
#chizaee k ta inja bayad khoob balad bashid
#Variable ha ( number int float, str , list --> assign,access[index], loop, methods)
#operator ha (+ - , comparison == > <)
#built in function ha ( narenjia), input, print, open 
#dastoorat--> if , if else, elif, for , while
#def (fdunction sazi vorodi khorji)

#ke fahmidim chijori yek function bsazim va oono dakhele lirbary bzarim
import datetime
import math
import cmath
import random
import statistics

#** hamishe library haro baayd avale bbarname import kard yani ye sections akht
a=2b #invalid syntax = . , + nahv ychizio ja gzoashti ezafe zadi va va
#pas samte chap too toolbar ya narenjie yani eshkali ndre fght remindere
#ag ghermez bood yanoi bug hast
#ag ejra konid dar consule error mdie
#SyntaxError: invalid syntax

#estefade az library ha chetor bod?

#esmeshos eda mzinim , dot miznim mire dakhele lkibrary
#esme functioni k mikhaym ro minvisim ( mitonim az tab estefade konim)
#kolan ketabkhone ha set achiz dare
#yani dot miznid seta chizmitonid bekeshid biron 

#1- adade sabet--------------------
math.pi #** neveshte variable , yani constante yani yek adade sbate
#nokteye mohem--> niaz b hichi pasarantezo ina ndre
#vaghty in ejra mishe python maid jaye kole "math.pi" adade pi ro mzire 

#2-----function-------------------------
random.randint(a,b) #1- mizne functione 
#hatmaanan partantez mikhad--> patrrantez b ch mani ee hast --> yani vorodi migire
#tozihatesham hamonja nvshte too kadre khakestari
#vaghty mzianimesh python miad mire too ketabkhone random,
#functione randint ro varmidre
#function chi bod ye box bod yeseri vorodi migrd
#vorodi haye shomaro vrmidre mziare too function, calculation too body anjam mide
#khoroji pas mide ( 1-print fght kone (kaman nesbatan) 
#2-return dashte bashe yani bjaye kole "random.randint(a,b)" ye adad pas bde)
#3- fght emal kone return ndshtebashe , masalan yek list az ma bgire
#rooye liste e taghirat ro ijad kone
a=[1,2,3,4,5]
a.append(6)
#yni ag bnvism
b=a.append(6)
#kheyli mohem--> farghe emal ( yani tabe ee k return ndre) ba tahvil ( yani return dre)
#fpas ag chizi pas nde va emal kone--> zarfe khali mimone --> Nonetype

#3-------class-------------------------------
#ye zarfe bzoorgtre ke tgoosh koli function dre
#bayad injuori bashe
#esme ketabkhone ro nam mibrim dot miznim
#esme class ro mizni
#**frgh--> badesh dobare dot mizni va esme tabe ro mairi

random.Random.random() #

#===================================================================
#quizo hal mikonim ---------------->
#migof bia ye adad computer had bzne ma ham ye adad bdim ok
#bbine shabihe ham has ya na 

#chijori minmvisim
#ye box e yek jabas vorodi dre ye body y khoorji
#aval bbin chi vorodi bgirim chi khoroji
#aval bbin ensana chikar mikonan bad b zaboon bnvis

cnumber=random.randint(0, 6)
hnumebr=int(input('please insert the guessed number:'))

#pas ye zarf sakhtim --> in beehsh mign vorodi

#aval ensani bbin chiak rbayad krd bad b zabojnemashin bnvis
#mpghayese --> yani shart mzirm --> if
#nokate in seta
#moghayese va shart gozari bood-->if
#age mikhasti bazresi koni peymayesh , ya yek kario hey tekrar koni-->for
#ag yek kario mikhay ta yek ja tekrar koni (atehs malom nis)-->while
'''

salam:
    .......

'''

if cnumber=hnumber:
    print('bordiiiiii')
else:
    print('guess again')

#if     cnumber=hnumber:
#              ^
#SyntaxError: invalid syntax





cnumber=random.randint(0, 6)
hnumber=int(input('please insert the guessed number:'))
if cnumber==hnumber:
    print('bordiiiiii')
else:
    print('guess again')
    
    #tamoom shooddd--> chiakr konim chanbar bshe?
    
#soal--> hey hey repeat repeat --> tekrar

#for----> avalin fekr for
for i in range(0,5):
    cnumber=random.randint(0, 6)
    hnumber=int(input('please insert the guessed number:'))
    if cnumber==hnumber:
        print('bordiiiiii')
    else:
        print('guess again')



#harvaght hang krd ya khasti ejra nashe ya ya ya...
#dar balaye consule yek morabae ghermez 
#vaghty bzni stop misghe va ino miare
#KeyboardInterrupt: Interrupted by user

#moshkel--> ag mibrodim baz bayad najam mishod

for i in range(0,5):
    cnumber=random.randint(0, 6)
    hnumber=int(input('please insert the guessed number:'))
    if cnumber==hnumber:
        print('bordiiiiii')
        break
    else:
        print('guess again')

#IN AWLIE


#hala in nahayat 5 bar chiak rkonim k masalaan
#az while

#yani vaghty ma entehaye oon halgahmono nmidonim 
cnumber=random.randint(0, 6)
hnumber=int(input('please insert the guessed number:'))
#فارسیش کن
#تا وقتی که این دو عدد براربر نیستند
#تال وقتی که : while
#برابر نیستند !=
while hnumber!=cnumber:
    print('guess again')
    hnumber=int(input('please insert the guessed number:'))
    if hnumber==cnumber:
        print('to bordi')
    
    
#hala developlmenmtesho brim
#biad komakmon kone 
cnumber=random.randint(0, 6)
hnumber=int(input('please insert the guessed number:'))
while hnumber!=cnumber:
    hnumber=int(input('please insert the guessed number:'))
    if hnumber>cnumber:
        print('please gues ssmaller')
    elif hnumber<cnumber:
        print('gues more')
        
if hnumber==cnumber:
    print('to bordi')    

#1-python interpretability-----------


#==================
#keteabkhoneye numpy-----------

#--------------NUMPY------------
#bargshtim b list
#list chi bod?
#kolan variabl ha chanta kar bas bahash konim injori taghsiemsh konid

#1-assign ( megdhardehi) 2-access element (index) 3-iter (peymayesh) 4-method

#list chi bod?
#asign
#2 rah dre
#rahe avalo []
a=[4,5,6,7,7]
b=['user','ali','new']
c=[4,'user',True]
#rahe dovom estefade aaz built in fucntion
a=list((1,2,3)) #2 ta parantez

#acces chi bod ? yani mikham b yek elemenet ( onsoi , joz) az in list dastam brse
#yani bekeshamesh biron ya taghiresh bdm ya hazfehs konim
#esme on listo seda bzn [ ] indexesh **havaset basahe index az 0 shroo mishe na az 1111111
a=[4,5,6,7,7]

#masalna dovomin elemente liste a
#dovomin yani indexe 1
a[1]

#yani python maid jaye kole a[1] oon joz ro mizare
#khob mitonim savehs konim 
b=a[1]


#loop--ityer----peymayesh
a=[4,5,6,7,7]
for i in a:
    print(i+1)


#mikhaym yek list bnsazim done done elemente a ro +1 kone brize
#rtoo liste jadid
  
a=[4,5,6,7,7]
for i in a:
    b.append(i+1)

#in error mide
#AttributeError: 'NoneType' object has no attribute 'append'

a=[4,5,6,7,7]
for i in a:
    k.append(i+1)
#NameError: name 'k' is not defined
#ras mige miad b k ezafe mikone yekchizio , k chie ?


k=[] #yewwk liste khali
a=[4,5,6,7,7]
for i in a:
    k.append(i+1)
print(k) #[5, 6, 7, 8, 8]

#pomadan goftan list sariii nist , biaym yek chzii bsazim kheyli sari bashe
#50 nbarabar sariiiii tarrrr
#numpyyyyyy
#hamchenin list fght yek bodie yani matriso ch bdonm matris haye chan bodi nmisyhe sakht

a=list((1,2,3,4))


#------------------------------------
#vahkleye importe numpy
import numpy

#agar zad numpy mdule is not fined --> bayad bri too environmenti ke
#spyder nasb hast , powershelesho bzni bnvsii install pip numpy 
#bbndi abrname ro dobare baz koni hala bzn

#ravesh haye dg ye import
#kolan se raveshe
import numpy


#vbase dastresi b yek tabe bayad dot mizdi m va chon tabe hast parantez dre


#aslan numpy baraye ine ke yechizi mesle list bsazi tahvil bde
#ba yek tabe ee benam array



numpy.array((1,2,3,4,5)) #ino k mizani maid kolesho vrmidre ye array mizare

#ma baayd savesh konim

#assign---------------------
new1=numpy.array((1,2,3,4,5))
new2=numpy.array([1,2,3,4,5])

#ag naszarim  parantz cvhi?

false_array=numpy.array(1,2,3,4,5)
#TypeError: array() takes from 1 to 2 positional arguments but 5 were given

#mige nahayatt yeki dota bgire chra panjta dadi?

#pas mesle tabe neveshtan ma taeen mikrdim chnta voprodi bgire
#ina ham too numpy taeen krdn chanta bgrie

#se raveshe assign---------
new1=numpy.array((1,2,3,4,5))
new2=numpy.array([1,2,3,4,5])
name_list=[1,2,3,4,5] #ya set, touple
new3=numpy.array(name_list)


#typesh chie ? masan ghadim int dshtim floast 

type(new1) #Out[31]: numpy.ndarray


#sakhte hey bnvisam numpy --> baraye hame skahjte
#pas avale barnamatonm mokhafaf import konid
import numpy as np

a=np.array((1,2,3,4))


#pas aasign ro yad grfim
#type ham yad grdim
#dimention chie ? mage nagtfoti matrisma msihe sakht va va va
#bahse dimention mishe

#chan no bod darim بعد

#0-D array (sefr bodi)--> hamoon adade khodemone---------------
#hamon numbere khodmone ama type e numpy
arr=np.array(58)
#frghesh ba adad ?
numb=58
#boro bala samte rast moghayese kon

print(type(numb),type(arr)) #<class 'int'> <class 'numpy.ndarray'>

#fght khastam bgm bdoni, ma estefade ye ziadi nmikonm azash


#mohmtrin ghesmat injas
#1-D array ( yek bodi)--> hamon liste
#bejaye ye adad mesle section ghabli bayad chanta bnvisi

arr=np.array(58,59,60) #--> bayad dota aprante basheeeeeeeee*****
arr=np.array((58,59,60)) #ya arr=np.array([58,59,60])



#in shod 
#ma list drim chra akhe ino misazim? chra hamon [58,59,60]
#yekish ine ke sarii tare 50 brabar sari tar hast 


#2-D (do bodi)--> matrissss
#yani mikham sotono radif dashte bashe fght yek soton nabashe

#yek parantez ke defaulte
#yek beraket bzanid
#har beraketi k tooye in beraket miznid yekkk radife

arr=np.array([[1,2,3],[4,5,6]])

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

arr=np.array([[1,2,3,6],[4,5,6,8],[7,8,9,11]])

#arr=np.array([[1,2,3],[4,5,6,8],[7,8,9,11]]) bja adad list mzire

#dast negah dar

#dota method yadet bdm,

#esme oon araye ro bzar dot bzn 
arr.ndim #in dimention (bod) ro mide  1

#size======
#oon bala samte rast 
#bad az type nvshte size yani chi
arr=np.array([58,59,60])

#(3,)
#yani man y soton drm 3 ta khone tooshe


arr=np.array([[1,2],[4,5],[7,8]])

#(3,2) #yani aval dota adadde yani man do boid9iam
# avalie tedade radifame dovomie tedade soton

#yani se ta beraket hast k too hrkodom dota adad hast


#on bala rast type dare o size
print('our type is : ' ,type(arr))
print('our dimention is : ' ,arr.ndim)
print('our size(shape) is : ' ,arr.shape)

#3D----------------


#yek bodi doros emiznim roosh yek sotyon nshon mdie
#ama yadet bashe yek radifeeee

#vaghty too 2d chan ta mizrim kenare ham mishee radif ha roye ham

a1=np.array([1,2,3,4])

a2=np.array([[1,2,3,4],[5,6,7,8]])

#se bodi yanjhi bia in dobod ro

a1_1=np.array([1,2])
a1_2=np.array([3,4])


a2_1=np.array([[1,2],[3,4]])
a2_2=np.array([[5,6],[7,8]])


a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])


#------------assign ro yad grfim
#ndim , type, shape ham yad grfim 

#access element----------------
arr=np.array([1,2,3,4])
#access yani ye  element ro az delesh bkshm bironn

#masalan dovomioo
#mesle list
#esmo bnvis ba ye beraket toye beraket index
#***** az 0 shoro mishe index haaaaaaa

print(arr[1]) #2

arr=np.array(['ali','vahid','hamid','reza'])
print(arr[1]) #vahid



#ino k balad bodim too list yademon dadi

#bia sakht tar vasat drm--> do bodi chi>

arr=np.array([[1,2],[3,4]])

#aval b zabone farsi bego chie bad mashinish kon

#masalan adade 4 elemente mikhaymesh chi migim farsi
#migim aval migim radife chandom abd soton


#chon haminjori bod dg dobodi miomd yek bodi haro besorate radif radif roo ham mizasht

#pas chi migim radife 1 soton1
arr[1,1] #Out[64]: 4


arr=np.array([[1,2,3],[4,5,6]])
#adade 5 ro mikhaym

#radife chand , sotone chand ???
#hamino bnvisi
#*** radif haro az 1 nshmor az 0 bshmor indexxxx

arr[1,1] #Out[67]: 5

#masalan 6
#radife 1 sotone 2
arr[1,2] #Out[68]: 6


#------
a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#age adade 7 ro bekhaym chibznim?

#aval bas begi kodom safe bad mese ghabli
#bad begi kodomr adif kodom soton



#overall: kodom safe, kodom radif , kodom sotooon

#@7 kojas
#too safeye 1 e , radife 1 e , sotone 0

#esmo minvisi jolosh
a3[1,1,0] #Out[70]: 7



#------slice
#too gahbli goftim ye element bekeshim biuron
#ag chanta bkhaym bkshim chi ? slicing

#sade tarin-->1 D

arr=np.array([1,2,3,4,5])
#mikham az 2,3,4 ro vrdare
#yani indexe 1,2,3 
#mishe az 1 ta 4 **5omio hesab nmikone
arr[1:4] #Out[74]: array([2, 3, 4])


arr[:4] #yani poshte do noghte chizi nzri yani az aval
arr[2:] # ag bad az donoghte chizi nzre yani az felan(2) ta akahgr
arr[1:5:2] #yani az indexe 1 ta 5 2 ta 2 ta 

arr[::2] #yani az aval ta akahgr dota dota vrdar







#2D-------
arr=np.array([[1,2,3],[4,5,6]])
#ye radif 1,2,3 bala dre ye radif 4,5,6 paeen
#mikham4 o 5 ro bde

arr[a,b]

#inja a o b dasht
#a shomare khone ye radifemon bod 0 yani radif bala 1 yani radif paeen
#b ham shomare khoneye sotoon
arr[1,0:2]

#masan 2,3 ro mikhaym

arr[0,1:]


#--
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])





#--------------------
#numpy assign , access , slice ro yad grftiimm
#brid + - konid bbinid mishe ?


#inaro emtehan konid
#aya in chizi pas mide yani mitonim savesh konim too ye variable e dg ?
#ya inke fght emal mishe rooye arr 

arr.copy()
arr.view()
np.concatenate()
np.stack()
np.vstack()
np.dstack()
np.array_split()
np.sort()
np.where()
np.searchsorted()
   
#********
    




