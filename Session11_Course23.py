"""
IN THE NAME OF GOD

@author: Ali Pilehvar Meibody

ai.course22.alipilehvar@gmail.com


"""





#3 ta ketabkhoneye mohem ghabl az hoshe masnooe
#numpy ----> pip install numpy ( dakhele powershel ( environmenti k spyder run mishe))
#matplotlib--> pip install matplotlib
#pandas---> pip install pandas
#enter miznim __> wait --> download + install > refersesh sypyder
#badesh soragehe import mirim

#3 no import darim
import numpy #sade tarin import
import numpy as np #import + esme mokhafaf
from numpy import random #tabe keshidan biron az ketabkhone

#ketabkhone ( mesle math , random , statistics , cmath)
#havie koli tabe va class va adade sabet bodan va ma 
#esme ketabkhone ro mizdim , dot mizdim mirf toosh va az dakhele
#ketabkhone ye tabe miovord va oon ag adade sabet bod k hichi
#ag def (tabe) bood parantez dasht k too parantez vorodi migrf
#hala oon tabe ya emal mishod ya bema khoroji mdiAD return, ke mitonesim savesh konim
#ya class, khode class az hezaran tabe sakhte shode
#dot miznim mire dkahele ketabkhone , classo miznim dot miznim mire too class yeki az tabe haye clas ro seda miznim va va va


#mohem trin haye numpy
#------documentation --> hatman 

#import
import numpy as np
#shoma brid dakhele khone done done run she
a=np.arange(6) #0---6 
a = np.array([1, 2, 3, 4, 5, 6]) #yek bod9 , paramntez yadet nre
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) #2D bodi has bod=dimention , chanta parantez too hham
#1d--> fght ye rafdif bod 
#2d--> radif hae k soton daran
#array ychi mese list bod k behesh migan araye
#chanta adad sabet mitonim az array e mon bedast biarim k propertie(moshakahsetesh)
a.nndim #number of dimention yani mgie chan bodi
a.shape #ag 1 bodi (n) n tedae soton #2bod (radif,soton) #3bodi ( laye, radif, soton)
a.size #tedade element
a.dtype #noe va type e elementaro mige

#---assign
a = np.array([1, 2, 3, 4, 5, 6])
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#ya mitoni listo , df , .... mise np ish krd
b=list((1,2,3))
a=np.array(b)
#yadetonam bashe dakhele assign yechi drim bname dtype

c=list((1.0,2.0,3.0))
a=np.array(c,dtype='i')
#integer= i , boolean = b , complex= c, string = s , float=f


#chizaye dg mesle arrange
a=np.arange(6)# az 0 ta 6
#chizaye dg darim
a=np.zeros(10) #ba sefr por mikone vali 1 bodie
a=np.ones(10)
a=np.empty(10) #in miad ba adade random por mikone --> hamon 0 e , khali , soratesh az zero bishtre

#a=np.arange(start,end,step)
a=np.arange(1,60)
a=np.arange(1,60,2)

#ag bkhaym masalan beyne 0 ta 10 , taghsim bar 5 esh konim
a=np.linspace(0,10,num=5) #yani range e 0 ta 10 o taghsim bar 5 kon arrayesh kon
#*to hasmashon mitonid dtype bznid trype ro avaz koinid

#reshhape
#ag zeros khastam do bodi bashe chi #do radife 5 sotoni mikham

a=np.zeros(10)
b=a.reshape(2,5) #(chanta ardif,chanta soton)
#hata tabe ha mitonan poshte ham bashan

a=np.zeros(10).reshape(2,5)


#random mitonim bsazim
a=np.random.rand() #yek adad beyne 0 ta 1 mide
#chanta adad ?
a=np.random.rand(5)

a=np.random.randint(100,size=(2,3)) #0 ta 100 inetegr

#chra fght inetger ?
#do no distribution --> yani beyne 0 ta 100 computer ke mikhad vardare random
#har adad too range3 0 ta 100 ye shansi drn vase vardashtan
#ag mikhay shans hame ja yeksan bashe yani hame adad--uniform
#ag na mikhay dore yek adadi (seed) beyne y adadi ehtemale bishtri dashte bashe vrdare --> noraml gussian
#ye siz emidi ( chnata rasdif, chanta soton)
#boro tooosho , beyne felan range por kon
#computer mige khob beyne in adad man chghd ehtemal ebrdahstano hesab konm
x=np.random.uniform(size=(2,3))

x=np.random.normal(size=(2,3))
#frgh dre ba balaee
x = random.normal(loc=1, scale=2, size=(2, 3)) 
#loc == oon jaee k mikhay bishtr doresh vrdashte she
#possion, exponteional --> mitonid bbinid

#----access--> dastresi b elemeent
#shabihe llist
#havasemon bashe index az 0 shoro mishe

a=np.array([45,46,47,48,49,50])
#avali? --> index=0
a[0]
#slice -> chanta element
a[1:5]

#2d
a=np.array([[45,46,47,48,49,50],[4335,231,2255,25,34,35]])
a[1,1] #Out[19]: 231
a[1,3] #Out[20]: 25

#slice
a[0:1,2:4]

#copy view
x=a.copy() #hr tghir roye a roye x tghir nmikone
x=a.view() #barax

#sort
np.sort(a) #az 0 ta 9 , az a ta z moratab mikrd emal mikrd
b=np.where(a==4) #shart ro dakhele paranetz ba comparison operator == , > <

#too matrisa taranahade dahstim

a=np.array([[1,2,3],[4,5,6]])
b=a.T #t e bozorg


#---split k biad jhoda
a=np.zeros(40)
new=np.split(a,10) #mishkonatesh

#filter
a=np.array([[1,2,3],[4,5,6]])
b=a[a==4] #sharteto tooye parantez bzari
#shartaro ghashnagehs konid a%2==0

#operator gha--> amalgarha
#hrchizi k roo adad mishod rooye numpy ham mishe ama bayad size a yeki bashe
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
b=arr1+arr2
c=arr1-arr2
d=4*arr1
e=arr1/arr2
#ya az tabe estefade koni
newarr= np.add(arr1,arr2) #+
newarr = np.subtract(arr1, arr2) #-
newarr = np.multiply(arr1, arr2) #*
newarr = np.divide(arr1, arr2) #/
newarr = np.power(arr1, arr2) #**
newarr = np.absolute(arr1) #motlagh

#round
arr = np.floor([-3.1666, 3.6667])
arr = np.ceil([-3.1666, 3.6667])


a=np.array([1,2,3])
#mikhyam max ya min ya sum dr bairim

a.max() #3
a.min() #1
a.sum() #6

#baraye dobodi ha yechi drim bname axis
#axis=0 hamishe yadet bashe miad toole soton amoodi anjam mide
#axis=1 hamishe yadet bashe miad toole radif --> ofoghi
a=np.array([[1,2,3],[4,5,6]])
a.max() #6
#gahi vagghta mikham bgm too kdoom soton kodoma maxe

a.max(axis=0) #amoodi #Out[25]: array([4, 5, 6])

a.max(axis=1) #ofoghi #Out[26]: array([3, 6])
#sum va join ha
#axioos fght baraye do bodi has
#default axis=0 e yani amodi 
#1 bodi ham bbinid amodi nvshte shode dg

#join--dota array ro bchasbonim

arr = np.concatenate((arr1, arr2))
arr = np.stack((arr1, arr2), axis=1)
arr = np.hstack((arr1, arr2))
arr = np.vstack((arr1, arr2))
arr = np.dstack((arr1, arr2))
#mitoni dakhele parnatez axis bzzari

#tamnom shod ma hata mitonim savcesh kponim biron az spyder

#np.save ( 'esmi k mikhay save she' , kodom array)
np.save('filename', a)

#badna k khasti laodesh koni
#load
b = np.load('filename.npy')


#==========matplotlib
#protocol--> inmport, xy , plt draw

import matplotlib as mpl
import matplotlib.pyplot as plt

#kolan bahse x o y e
#x vorodimon 
#y khorojimon
#mitone adad bashe ? KHEYR
#yani fght yechi shyabihe list, array, dataframe
#beshe ye listi az x ha

#hm mitonji liost bashe
x=[1,2,3,4,5,6,7]
y=[45,43,32,2,23,23,43]

#mitone numpuy bashe
x=np.array([1,2,3,4,5,6,7])
y=np.array([45,43,32,2,23,23,43])

#bayad t5edade x ha va y ha brabar bashe--> bbin kolan bahse rasme noghats
#har noghte dar mokhtasat ye x ee dare y y ee dare


#start-----
x=np.array([0,6])
y=np.array([0,100])
#ch mani ee mide
#yani do noghte dreim 
#yeki mokhtasatesh hast (0,0)
#yeki hast (6,100)


#sade trin dastoor
#plt= seda zdm ketabkhone ro besorate mokhafaf
#dot yani boro dakhele ketabkhone
#tabeye plot ro
#tabe hast? --> pas parantez dre pas voirodi mnigire
#vorodi chie ?? kh chiza ama ejbari vfght y hast


#aval x badan y
plt.plot(x,y)

#kolan miad noghato bhm vasl mikone

x=np.array([0,3,6])
y=np.array([0,200,100])
#se noghte , (0,0) , (3,200) , (6,100)
plt.plot(x,y)

#fght y ro bdi
plt.plot(y) #miad x haro noghye aval 0 mdie , nogyteye badi 1 mide va va

#default miad noghato vasl mikone


#hey naizi nis x o y o bznim chon dg save shode too variablamon
plt.plot(x,y,'o') # se noghte khali dad
plt.plot(x,y,'*')

#g bkhaym ham khat bashe ham line
plt.plot(x,y,marker='o') #ham kjhat mikeshe ham noghato

#aval fhmidim linee e kahli, bad noghate khali , bad noghato khat baham
# o , * , . (,) x X + p s

#ms=marker size
#*** x o y fght ejbarie inaro mitoni tanzim koni

plt.plot(x,y,marker='o',ms=20)
#size e markero pointemon noghtmono taghir mide

plt.plot(x,y,marker='o',ms=20,mec='r') #dore point
# red= r, 

plt.plot(x,y,marker='o',ms=20,mfc='r') #tooye point


plt.plot(x,y,marker='o',ms=20,mfc='r',mec='r') #tooye point

#r , k , b , g , y ,w qutation bd esmo bnvisid
#noghat hyam o , * +

#ta inja settinge noghato dadi
#settinge line o chikarf
#y khat , andaze dre, rang dre , noghte noghte ee chijorie , size

#ls = line style
#: ,  - , -- , -. , ""
plt.plot(x,y)
plt.plot(x,y,ls=':')
plt.plot(x,y,ls='-')
plt.plot(x,y,ls='--')
plt.plot(x,y,ls='-.')


plt.plot(x,y,color='r')
#or
plt.plot(x,y,c='r')

#hame chiz joz x , y ekhtiarie
#masalan yek khate range siah , nogte chin
plt.plot(x,y,c='k',ls=':')


#linewidth

#in fght adad ro hm bayad dar qutation
plt.plot(x,y,linewidth='20')


#===================
#fght bayad x o y bdim? na mitoni tabe bdim

x=np.array([1,2,3,4,5,6])
#mitoni az random , arrange estefade koni

y=x+2
plt.plot(x,y)


#mikhay rangi bashe
x=np.array([0,100])
y=x**2 #0, 10000

#yni dastore paeen maid do noghte peyda mikone bvasl mikone

plt.plot(x,y)
#vase hmain ma az arrange estefadde mikonim


# 0 ta 100?
x=np.arange(0,100)
y=x**2

plt.plot(x,y)


#---------------
#dta khat?

x=np.array([1,2,3,4])

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(x,y1) #intoo taghirato bde
plt.plot(x,y2) #intoo taghirat ro bde

#---
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([2, 3, 4, 5])
y2 = np.array([6, 2, 7, 11])

plt.plot(x,y1) 
plt.plot(x,y2)


#ya hamshooo dakhele yek plot bnvis

plt.plot(x1, y1, x2, y2) #tanzimat rooye kol ejra mishe ha
plt.show()


import math
x=np.arange(0,100)


sin_list=[]

for element in x:
    y=math.sin(element)
    sin_list.append(y)

final_sin=np.array(sin_list)

plt.plot(x,final_sin)



#ya sade tar
'''

sin_list=[]
for i in range(0,100):
    y=math.sin(i)
    sin_list.append(y)

'''
    



#===============================
#ina ke aan chioe? x esh c hie y esh chie ?
#masalan xc emon tempreture damae, khob man az koja bdonm ?
#bahse lable
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title('POLYMER CONDUCTIVITY')
plt.xlabel('average MWN')
plt.ylabel('conductivity')
plt.show()


#fonto mitonid taghir bdid
#yek dictionary minvisan
#yechi mese liste
a={ 'nam1' :'ali'  ,'name2' :'vahid' , 'name3' :'hamid'     }

#mese list , bjaye index 0 1 2 , samte chape paranetzo mzire

#font
font1 = {'family':'serif','color':'blue','size':20}
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


plt.title('POLYMER CONDUCTIVITY',fontdict=font1)
plt.xlabel('average MWN')
plt.ylabel('conductivity')
plt.show()
#fght title? na harchizi k bkhay






#--------
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()




#title yechi dre benam loc
plt.title("Sports Watch Data", loc='left')


#inaro bayad b kole structure codetone zaf konid

#age gridbkham 
plt.grid()

#meesal
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)
plt.title('POLYMER CONDUCTIVITY')
plt.xlabel('average MWN')
plt.ylabel('conductivity')
plt.grid()
plt.show()

#plt.grid(axis = 'x') #amodi mikeshe , y = ofoghi


#tanzimatesh ham msihe tagir dad
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)
plt.title('POLYMER CONDUCTIVITY')
plt.xlabel('average MWN')
plt.ylabel('conductivity')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()




#====================================================
#====================================================
#====================================================
#scatter-------------------
#bishtar baraye rasme noghat bekar mire
#masalan 13 ta noghte drim va rasmehs mikonim b hamin sadegi
import numpy as np
import matplotlib.pyplot as plt


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.plot(x,y,'o')

plt.scatter(x, y)
plt.show()


#------------------------------------------------------
#ag dota data dashte bashim yani 10 ta az yek type 10 ta az yek type e dg
#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()
#------------------------------------------------------
#mitoonid rang ro taghir bdid b sadegi
#baraye har data begid che rangi mikhayd

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'r')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = 'k')
plt.show()
#------
#gahi vaghta mikhahid ke yek shedatii bedid
#yani masalan yekseri noghte darim k harkodom yek x o y darand
#tozihat ro bekhonid

#aval 13 ta noghte misazim
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

#miaym migim k y emoon rangesh beyne maalan 70 ta 100 hast
#migim agha bia az 0 ta 100 done doone b 0 yek adad bde
#b 10 yek adad bde b ..
#yani mikhaym shedate Y ro bbinim
#pas yek numpy az colour misazim
colors = np.array([0, 10, 20, 30, 40, 100, 50, 55, 60, 70, 80, 90, 100])


#bad migim bekesheshon
#tooo tanzimat joloye c , colour ro mizrim 
#cmap ham yani hala k shedate ranagro gofti
#mane matplotlib biam masalan az 0 ta 100
#chio taghir bdm ? abi b ghermez ? siah b sefid ?
#hame ina yek esmi dre va mitonid dar matplotlib bznid 
#scatter colour va bbinid
#https://matplotlib.org/stable/gallery/color/colormap_reference.html
plt.scatter(x, y, c=colors, cmap='viridis')


#inam nshon mide shedatesho samte raste tasvir
plt.colorbar()

plt.show()

#** mitonid title va .. ham mesle plot bznid

#-------------------------------------------------
#mitonid bgid az noghteye aval ta noghte ye akahr
#har noghte ch sizi dashte bashe
#yek array misazid baraye har noghte az dataton
#yek adad b onvane size midid 
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

#size ro inja avred konid
plt.scatter(x, y, s=sizes)

plt.show()


#ychiuzi dare bename alpha k mitonid bgid cheghad kamrang bashe beyne 0 ta 1 e
plt.scatter(x, y, s=sizes, alpha=0.5)



#====================================================
#====================================================
#====================================================
#bar--------------------
#dar asl baraye rasme dade haye sotoni hast
#mesal -->

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()


#0------mitonid ofoghi ham rasm konid hamino
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
#bejaye bar() az barh() estefade konid
plt.barh(x, y)
plt.show()


#**********************
#dakhle plt.bar() mitoonid tanzimat bdid
#color rang hast , width andaze zekhamat hast
#hrcvhizi joz x , y baghiash ekhtiarie va fght settinge
plt.bar(x, y, color = "r", width = 0.1)



#====================================================
#====================================================
#====================================================
#histogram-------------------------------------------
#in baraye distribution hast yani baraye توزیع
#vase inke bebinid tozih ha chijorian
#masalan fk konid hamchin chizi drid
#in cxhie? 
#ye x drim k omade mige
#250 ta adad sakhte dar yek array k hamashon 
#+ - 10 ta nazdike 170 adad vardashte random va tooye
#in array ro por krde
x = np.random.normal(170, 10, 250)



#hala age bekhyam bbinim har adad cheghad shans dashte k bardashte shode
#یعنی توزیع عدد هارو ببینیم کافیه پایین رو بزنیم

plt.hist(x)
plt.show() 
#hamantor k didid mige ke 170 bishtrin shanso dre
#badesh 160,180 bnishtr 
#va ....
#in ax chiuo neshon mide ? mige tooye in x 
#x chie ? ye data hast yek zarfe toosh 250 ta adad hast
#mige az beyne in 250 ta adad , masalan aksareshon nazdike 160 ta 180 hast valueshon




#====================================================
#====================================================
#====================================================
#pie chart-----------------------------------------
#baraye rasme nemoodar haye dayerre eee
#masalan ma mikhaym bgim yek dayere ro 
#be charghesmat taghsim kon
#35% , 25% , 25 % , 15%

#kafie injori bnvisim
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show() 



#agar bbinid in rangaro khodesh tartibi gozshte 
#chizi tozih ndde
#khob age joloye har ghesmat bkhaym tozih bnvisim kafie
#be tartib benevisim
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.show() 



#mitonid dar kenare label ha , begid harkodom be tartib che rangi bashan
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 


#------mitonid yekodom ro bkshid biron
#kafie yek list  bzarid va harkodom k bayad sare jash abshe bezarid 0
#ooni k mikhayd bkshid bironm yuek adad az 0 ta 1 bdid , yani
#chan darsad biad biron
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0] #inja mighim avalie , yani oni ke 35 darsade yani oni ke apple hast 0.2 az hame bishtrr biad biron
#ama baghie 0 , yani sare jashon bashand

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()




#=================================
#ketabkhoneye seaborn --> doicumentation bekhonid
#bar rooyte matplotlib neveshte shode va ykm khoshgeltare
#https://seaborn.pydata.org/tutorial/introduction.html





#===============================
#file-------------------------
#ta alan vorodimono khodemon misakhtim ya assign mikrdim
#chijori vorodi vardarim"
#az desktopi jaee chzii
#data chie? 1-text .txt / 2.ax .jpg,.png, asp / 3-video
#4-excell .csv--> 90% e datahaee k analysize
#tooye azmayeshgah yek excelle
#yani soton dare va ....

#chijori open konim?

#[pas nakeshimesh]
#choon mikhyam openesh konim va yeja savehs konim bahash kar konim
#python yek puthon built in function , tabeye daskheli 
open #narenji shod
#built in function --> tabe hast
#chi mikhad parantez ---> vorodi mire dakhelesh
#structure

#bayad yek variable yani yek zarfg bsazid
#mosavi bsazid va open ro bznid va haerchi open krdid
#bre too zarf zakhire she

#dota vroodi migire
#f= open ( address , chikar mikhaym konim?)


#address= jaee k hast , ** too qutation baayd bashe , #\\ 
#.format bashe

f=open('data_c.txt')
#in addres kafi nis
#chanta rahe
#raftam onja click rast too filam
#properties
#location ro cpy krdm
#C:\Users\sunhouse\.spyder-py3\codha\2023COURSE
#ama niaz b tagiir drre
#har \ --> \\
#va format bzni tahesh

f=open('C:\\Users\\sunhouse\\.spyder-py3\\codha\\2023COURSE\\data_c.csv')

#1--> \ tbdim krmd b \\
#2--> tahesh esme filamo bznm
#3. format yadewt nre

#oomad y texti sakht
#hala y arg dg bas bhsh ezazfe koni

f_loc='C:\\Users\\sunhouse\\.spyder-py3\\codha\\2023COURSE\\data_c.csv'
f=open(f_loc,)

#ag mikhay bkhooni read --> 'r'
#mikhayt bnvisi --> 'w'
#ye file has mikhay chizi bhsh ezafe koni append --> 'a' 
#'x' ham shabihe 'a' hast ama ag oon file vojod ndshte bashe error mide


#--mikham bkhonm
f=open(f_loc,'r') #mire dakhe locationi k dadam behesh be gahsde khodnban bazesh mikone

f=open(f_loc,'w') # be ghasde neveshtan

f=open(f_loc,'a') #b gahsde ezafe krdne chizi

#C:\Users\sunhouse\Desktop
f=open('C:\\Users\\sunhouse\\Desktop\\ali.txt','r')

#mikhay bkhoni bkhon

print(f.read())

#mikhay panjta caracter bkhone
print(f.read(5))

#yek line bkhone
print(f.readline())


#ag se bar bnvisi
print(f.readline()) #in khate vaalo mikone
print(f.readline()) #mire khate badi ( dobare az aval nmikhone ha)





#*****mohmtrin chiiiiiz
f.close()
#ag nakonid na save mishe na hichii asan hang


#bastamesh haal mikham bnvism

f=open('C:\\Users\\sunhouse\\Desktop\\ali.txt','w')

f.write("Now the file has more content!")

f.close()
#hamaro pak krd va nevesht


f=open('C:\\Users\\sunhouse\\Desktop\\ali.txt','a')

f.write("aya ezafe shod ya na?")
f.close()



#remove
import os
os.remove('C:\\Users\\sunhouse\\Desktop\\ali.txt')

#inam azin








#----------------------
import pandas


#pip install pandas




#=================LISTE RANG HAYE MOHEM ====================
#----ranh ha / color-------
'''
'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White


همچنین برای رنگ ها کافیه برید سایت زیر
sitte e zir rangaro keshide va jolosh esmeshon
yani masalan bejaye 'r' kafie esme onaro bnvisid va rnagesh zaher mishe
https://matplotlib.org/stable/gallery/color/named_colors.html



#baraye colour map ha --> oonaee ke rangaye shedati hast
#yani bayad shedat bedid ham mitonid berid paeen begid
masalan az 0 ta 100 / biad gehrmez ba abi ya masalan zard b sabz ya ....

https://matplotlib.org/stable/gallery/color/colormap_reference.html


'''



#---- Shekle marker ha / marker style-----
'''
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline


'''

#----- Shekle khat / line style -----
'''
'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'

'''





