# -*- coding: utf-8 -*-
"""
IN THE NAME OF GOD
@author: Ali Pilehvar Meibody
"""

#review-----
#python built in function ha
#dastoorat ( if , if else , while , for )
#str,list + method
#random
#def
#numpy
#matplotlib
#pandas-----
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#frghe list numpy
a_list=list((30,40,50,60,70,80))
a_array=np.array([30,40,50,60,70,80])
a_series=pd.Series([3040,50,60,70,80])
a_series=pd.Series([30,40,50,60,70,80],index=['a','b','c','DD','oon','akhari'])
#assign--> dasti bnvbisi/ list bzar / numpy array bzari / data ro import koni / dictonary
#access
a_list[2] #Out[38]: 50
a_array[2] #Out[39]: 50

#pandas
#fght bjaye index esme on index
a_series['akhari'] #Out[40]: 80
new_dict={'ali':20 , 'vahid':30, 'reza':40}
new_dict={'ali':[20,30,40] , 'vahid':[30,40,50], 'reza':[40,50,60]}

#2d --> DataFrame too pandas / 1D--> Series
a=np.array([[11,10],[12,20],[13,30],[14,40]])

#ino tbdil konm b datframe chanta rah dre
#avalin rah--dasti
a=pd.DataFrame([[11,10],[12,20],[13,30],[14,40]])
#dovomin rah--> tabdile arraye b df
new_array=np.array([[11,10],[12,20],[13,30],[14,40]])
a=pd.DataFrame(new_array)
#sevomin rah--> tabdile dict be df
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
a=pd.DataFrame(data)
#4 omin rah--> open the file 
a=pd.read_csv('address')


#4 rtahe dataframe sakhtan ro ayd grftrim
#frghe df ba arr chie?
#mitonim [index radif row ]haro ya [label (column) soton]

#index
#yeki az ravesh haye bala assign kon value ro 
#badesh ....
df=pd.DataFrame([[11,10],[12,20],[13,30],[14,40]],index=['a','salam','taghire khoon','nemoneye4'])

#baraye column ha ya soton ha ya label
df=pd.DataFrame([[11,10],[12,20],[13,30],[14,40]],columns=['vizhegie 1','vizhegie 2'])


#hala cdhijori access konm?
#baraye np array ha-->
arr=np.array([[1,2],[3,4]])
#masalan acces b yek value mikhasim

#esm bad beraket arr[kodom radif, kodom soton]
arr[1,0]

#pd
#ya yek element bkshi biron , ya yek row , yek yek columns
#ag yek soton bekhaym
df['vizhegie 1']
#ag element khasi
df['vizhegie 1'][2]
df['vizhegie 1',2] #KeyError: ('vizhegie 1', 2) mnmitone

#radif mikhay
df.loc[0]

#element mnikham
df.loc[0]['vizhegie 1']
#or
df.loc[0,'vizhegie 1']


#mitonimmm hata az yechizi bname iloc estefade konim
#yani kari dg nadare chi esmesh chie dagghighan mese numpy amal mikoen
#esmefile.[kodom index][kodom soton] hamaro b adad bgo az 0 b badd

df.iloc[0][1]
#or
df.iloc[0,1]

#-------operator
#+
#-
df1=pd.DataFrame([[1,3],[2,4]])
df2=pd.DataFrame([[5,7],[6,8]])

#jam
zarfe_jadid=df1+df2
#df1-df2
#xarb dar yek adad df1*2
#be tavan df1**4

#na tanha kole dataframe ro operate mitoni koni balke mitoni har soton ro ya har radif ro

#dar hame ja baraye acces b 
#************
#tooye pandas ma
#4 ta chiz drim
#1-kole datframe--> df
#2-fght yek radif --> df.loc(9)
#3-fght yek sotonm --> df.['esm']
#4-yek element (yani yedon adad) df.iloc[0,1]

#operat ro rooye kol ya harkodom k bkhay anjham bdi
df1=pd.DataFrame([[1,3],[2,4]])

df3=df1+1



#biay bgi columne avalio inkaro konm baahsh
#**********aval access bad apply
zakhirer=df1[0] +1 
zakhire=df.loc[0]+1

df1=pd.DataFrame([[1,3],[2,4]],columns=['v1','v2'])
                 
#operator haye amari bzni

df1.max() #chonj dota soton drim vase harkodom maximume on sotrono mide

#access apply
df1['v1'].max()

df1.loc[0].max()


#dg harchi paeen miznm 
#shoam mitoni roye kole df , roye yek soiton , roye yek radif ya rooye yek element ejra koni

df1.max(axis=1) #inm baraye oona


df2=df1.T#resizew

#masalan fk kon yek dataframe drim bename air_quality
#chn nemoneye operation

#sakhte yek dsoton

df1['v3']=df1['v1']*2.45


air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)


#sort--> tartib ddn --> soal mishe man bar ch asas tartib bdm , bar asase kjodom columns

df.sort_values(by="Age")
#yani bia df emon ro sort kon bar asase sotone  Age


#cjoinn , chasbond

df3=pd.concat([df1,df2],axis=0)
#**
#axise 0 yani dar toole ofoghi
#axise 1 dar toole amoodi
mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')


#chikar mikone? kole sotone duration ro hazf mikone
mydf.drop(columns='Duration')

#tamame dSTOR HAYE pandas , emal nmishe balke ye df e jadid
#mide va bayad zakhirash koni
#vali hamashon yechi drn bename inplace ag True koni mishe emal
newdf=mydf.drop(columns='Duration')

#or
mydf.drop(columns='Duration',inplace=True)

#ina hazfe soton bod
#hazfe radif chtor?
mydf.drop(index=12)
#m,esle hamishe in dastor ye array pas mide bayad zakhire konim


mydf.drop(index=12,inplace=True)

#ag inplace False bashe true nabashe taghirat rooye df save nmishe




#====analyss================

#vared krdne data
mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')
mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv',index_col=0)
#ag 0 bzni in vase vaghtye ke
#ya mitoni joloye index_col= esme dsotoni kmikhay bar hasbe oon index gzoari bshe

#initiual analasys --> analize avalie
mydf.head() #5 radife avalo
mydf.head(10) 
mydf.tail()#5 taye akhar
mydf.tail(15)
mydf.info() #Initial analysis
#caval mige chanta row drim , entries yani chnta radif drim chanta sample drim chnat nemonde drim
#har soton chantash non-nulle
#bayad non-null ha ba entries barabar basher

#null== dadeye naghes

#===========================bahse cleaning data

#isna
pd.isna(mydf) #vase kochika harja true bashe yani naghese

#----Null chn type drn
#1-nan --> empty cell --> khalie 
#2-formatesh bade
#3-eshtebahe (yani masan damaha nmitonan zire 0K) damamon has -10
#4-dupliocated tekrary repeated

#-------empty
#1-remove
#2-replace ( 1- yek adad dasti , 2-ya mean modian bgiri , 3-methdohaye forward backward)

#remove
mydf.dropna(inplace=True)

#ag replace koni yani fill
mydf.fillna(120)
newdf=mydf.fillna(120)


mydf.fillna(120,inplace=True)


#yadete goftm az chand aspect janbe bbin #in vase kole df ha has
#ag bnkhaym rooye yek column ya yek soton taghir ijad konm chi?
#acces apply

mydf['Calories'].fillna(120,inplace=True)
#yni in soton , harchi khalie ro ba 120 avaz kon


#fotmat frgh kone chi
#miam migim kole oon soton ro b felan format tabdil kon
x=mydf['Calories'].mean()
print(x) #368.22248520710065
mydf['Calories'].fillna(x,inplace=True)


ffil_df=mydf.fillna(method='ffill')
bfill_df=mydf.fillna(method='bfill')


#-----------------
#flash back
#taghire yek element

#103 bod mikham konm 106
mydf.loc[2,'Pulse']=106

#----vaghty yek element eshtebah bshe dakhele data mitoni injori aqvazesh koni

#soal=--> man yad grftm chijori dadeye ghalato wrong data 
#taghir bdm ama khob datam 1 millyard value dre chikar konm

#for o if o ina inja mian bkar

#ghablesh dota chizo yad bgir


mydf.index #listye indexaro mide
mydf.columns #listi az column hato


for x in mydf.index:
    if mydf.loc[x,'Pulse']>200:
        mydf.loc[x,'Pulse']=100
        

#masalan dama

for i in mydf.index:
    if mydf.loc[i,'Tempreture']<-273:
        mydf.loc[i,'Tempreture']=0
        
#repeated ya duplicated
print(mydf.duplicated()) 

mydf.drop_duplicates(inplace = True)




#-----------------------akharin marhale pas az analysis

#vaghty drop mishan index ha bham mikhore *****
mydf.drop(index=4,inplace=True)

#indexa bhm mirize
mydf.reset_index(drop=True,inplace=True) 




#==================
#yechizi drim bname corr
mydf.corr()


#age rabetey soyon haro bkhaym bbinim azin estefade mikonim
#pulse ba pulse / ya x ba x ch rabete ee dre
#x=x / pulse = pulse = pulse = (1)* pulse

#1- rabete mostaghim
#0 yani hcih rabete ee beyneshon nist



#===================
#plot

#mitoniaz matplotlib estefade koni 
#mitoni xnadi
y=mydf['Pulse']
x=np.arange(len(y))

plt.plot(x,y)
plt.show()


#ya mitoni az khode pandas estefade koni
mydf.plot()
plt.show()


#in ke fght plot e sadas ma scatter dahstim vba va

mydf.plot(kind = 'scatter', x = 'Calorie', y = 'Calories')


#=======================================================
#Machine learning beshavim-------------------


#farghe hoshe masnoee va automation

for i in range(0,5):
    print(i)


#do generation ( nasl) darim

#machine--> 0 , 1 mifhme va hichii nmifhme hich shooor hich dark maghz hichhh csimplke salculator

#hadaf goal--> machinemon mesle yek ensan yadbegire, va fekr kone va amal kone

#3 ta moalefd 1- yadgrftn 2-fekr krdn 3-tasmim grftn




#2 ta generation --->

#first generation---> hjoshe masnoe ha --> if else e khodemone
#mesal

telegram.input() #mire migire text ro az trf

newchat=telegram.input()
newchat='salam chetori'


newschat=input('salam man robotAM JAANam')
if newschat=='salam':
    print('salam janam?')
if newschat=='khobi':
    print('mersi to chtori')
if newschat=='gheymat chande':
    print('345')
    
#in shdo firsdt egeneration

#thrick mizdn

#momekne rtaraf salam o Salam #sAlam

newschat=input('salam man robotAM JAANam')
l=newschat.lower()
if l=='salam':
    print('salam janam?')
if l=='khobi':
    print('mersi to chtori')
if l=='gheymat chande':
    print('345')

#htmn trrf nminevise salam
#shayd bge salama agha
#ssalam fdelani



#----------
newschat=input('salam man robotAM JAANam')
text=newschat.lower()

if 'salam' in text:
    print('salam')
    


#=====================
#ROBOT /#10000000 khat ---> robot


#sisteme khebre ---> miomdn vase harsoale shimi , ya hrchi injori if o else misakhtahn




#hamin alanesh --> too insta
#5 ta soal bnvisi , bgi roo harkoidm click krd ch jagvabi bde


a=input('number:')
if a==1:
    print('تخفیف های ما .....')
    
    
    
    
#=================
#moshkele first generation chi bod?


#1- niaz b cod haye ziadd boood( programmed)
#2- birona az mahdode ro nmifhme (out of data) = prediction ndre pishbini ndre
#3- yad nemitone begire ( mohemtrinn eshkal)

#ghoveye yadgiri ndre--------
#banabrin fkr krdn bia yechi bsazim k yad bgie

#hooshe masnooe --> bozorgtrin shakahsho moarefi krd--> Machine learning ( yadgirie mashin)
#yek mashin betoone yad bgire


#hooshe masnooe chata shakhe dre
#1-sisteme khebre 
#2-robotic
#......

#machine learning o jozve shakhe ha nmidonan
#balke machine learning 80% e hoshe masnoe hast k dar tamame shakhe ha ifaye naghsh mikone



#NLP
#


#Macxhine learning---->
#Data-driven --> mobtani bar dade
#ye box hamishe drim


#box --> bhsh ye data midim ( film, ax ,e excell)
#az roosh yad migire ( relationship)
#hala tebghe oon tasmnim migire , fekr mikone amal mikone

#2 phase
#1-fazesh training
#2- amalklard



#-----YAD GEREFT ===> GHOVEYE YADGIRI DADIM B MASHIN 
#yadgiri ba rpayeye data bood***


#hamishe yqdet bashe

#ma data hamonn yek excelle yek dataframe yek arraye e
#hamvareeeeeeeeeeeeeeeeeeeeeeeeeee******

#radif dre o soton dre

#har dataeee dar jahan--> yek vorodi dre yek khoorji ( optional)

#vorodi --> yani ma mirtonim tanzimesh konimo taggiresh midim 
#khoroji--> partameteri ahs k bartaye ma moheme 

#in datmone yek vorodi yek khgoroji dre

data=pd.DataFrame([[0,30,200],[4,43,300],[8,56,453],[16,65,478],[32,71,589]],columns=['DARSADE GRAPHENE','Temprature','PAYDARIE FESHAR'])



data2=pd.DataFrame([[0,30,200],[4,43,300],[8,56,453],[16,65,478],[32,71,589]],
                   columns=['DARSADE GRAPHENE','Temprature','PAYDARIE FESHAR'])


#[pas yek vorodi ee drim yek khoroji



#khorojiiimon---> 3 ta halat dre
#1- ya peyvaste hast --> yani adade injori--->Regresssion
#2-ya gosastas--> 1,2 'a' 'b' -->classification



data=pd.DataFrame([[0,30,'y'],[4,43,'n'],[8,56,'n'],[16,65,'n'],[32,71,'n']],columns=['DARSADE GRAPHENE','Temprature','PAYDARIE FESHAR'])

#chantaeesh mikonim
#y o n
#bale o na
#0 o 1
# 1 o 2 3
#A B C
#tabaghe bandi--> daste bandi--> classificatiomn




#---------------------
#machine learning------------------------
#1-regression
#2-classification



data=pd.DataFrame([[0,30],[4,43],[8,56],[16,65],[32,71]],columns=['drsd','feshar'])

x=data['drsd']
y=data['feshar']

plt.scatter(x,y)\
    
    
#regression-->
#1- data migire(vorodi khorojhi)--? 
#2-initial guess -->
#2-zigma---. cost function 
#4-hey taghir mide --> COST FUNCTIONE E B PAEEN TARIN HADESH BRSE KAMTRIN FASELE --> OPTIMIZATION
#5-YEK KHAT --> aX + B --> khat--> relatyionship between x and y
#prediction , modeling estefade konid

#-----------------------------------------------------------
#============================================================
#OVERAL
'''
YEK computer yek mashin hesabe sade hast k az koli 'bit' tashkil shode ke
mohasebat ro ba in bit ha anjam mide yani miad mige har khone (yek khaneye 
jamed) age bargh vasl bashe 1 hast age bargh vasl nabashe 0 hast.
ba in technique e 0 o 1 i (binary) tonestim be yek jesme jamed 0 o 1 yad
bedim vad ba tabdile donyae paye ye 10 be paye ye 2 tonestim hame adad haro
barash besazim.

khob in computer na fahm dare na mitone yad begir na ..
faghat yek mashin hesabe pishraftas hamin.

omadan goftan ma niaz darim kari konim ke machine (computer) betone 
1-yad begire 2-fekr kone 3-tebhe oonn tasmim begire(amal kone)
khob in 3 ta paye ye hooshe masnoee shod

dota nasl hooshe masnooe darim:
    1-nasle aval miomadan migoftan bia ba if-else koli shorot bezarim
    va ba in shart ha betonim yek barname ye control shode besazim
    ba in kar system haye khebre (ke javabe soalaro midad) 
    chat bot haye avalie ke masalan age (if) benevisi salam mige salam
    va hata robot haee k sensorash age masalan felan signalo bede onam
    felan signalo mide va tabdil be harekate mechanici mishe
    
    2-nasle dovom: in nasl ba omadane machine learning oomad yani gfotan 
    bia ye kari konim computer ha betonan yad begiran va khob ba inkar
    soale aval--> az chi yad begiran ? khob az data (badan migim datachie?)
    khob fek kon machine ha betonan az data yad begiran(1*) va badesh tavasote
    yad gerefte hash ba manteghi ke bedast ovorde (2*) betonan pishbini
    konan ya daste bandi konan (tasmim begiran)
    ba in kar system haye khebre kareshono dadan b ChatGPT ba machine learning
    robotic ha ba inakr dg yad grftn yani b morore zaman hata behtar mishan
    
    
khob pas midonim k 70-80% e hooshe masnoee az machine learning omade
in machine learning yani chi ? goftim hoshe masnoe yani
1-yad bgire 2-mantegh kasb kone 3-tasmim bgire
chijori inkaro mikone?

machine elarning yani data driven ( mobtani bar dade)
khob yani data migire --> data ha chian?
data ha daghighan yek data frame hastan ya yek array hastan va ina
chanta radif dare ( tedade nemoone)
hameye in nemone ha chanta soton daran

dar beyne in sotonha , yekserihash vorodi hast yani (x) yani oni ke
ma mitonim taghireh bedim
va yek soton (k mamolan akharin soton) hamon khorojimon (y) hast yani hmaon
parametere mohemi k baramon moheme va oon parametere mohemo mikhaym
besanjim ya .....
khob pas midonim k in x o y beham bastegi daran yani y fght marbote b x
ba taghire x , yek rabete ee beyne x o y hast k y ham taghir mikone nesbat
be hamoon rabete.
mesal: y=2x+1 yani age x=0 bashe, y mishe 1/ hala x o taghir bdi
ba hamin formol y ham taghir mikone pas beyne y va x yek rabete hast
va in rabete hamin formoool hast.

mesale pazhoheshi:
    dar har reshte ee ma dastgahi darim ke yek setting dare ke ma mitonim
    taghiresh bedim va in yechizi khoroji mide k hala khorojish yek adade
    moheme ya oon khoorji ma yek moalefe ee azash ro baraye sanjidane 
    quality (keifiatesh) ya behaviour(raftaresh) dar nazar migirm
    
    masalan dastgahe 3d printing yek chizi dre yek setting ke mitoni
    taghiresh bdi. yek adade beyne 300 ta 400 mitoni taghir bdi
    'taghir'= pas yani in parameter vorodimone (x)
    
    khob ma ba in dastgah masalan ostokhone masnoe, ya organ haye
    masnooe misazim. khob in jesme masnoee ke ma misazim ehtemalan
    mitonim moshakhasate moshakhasi ro biaym azash dar nazar 
    begirim ( characterization) ta betonim befahmim keifiatesh chijorie
    (quality).
    khob in yani khorojimone (y), masalan estehkamesho mikhaym bbinim
    mishe y
    
    khob pas ma yek setting drim taghiresh midim (x emon) k az 300 ta
    400 mtionim taghiresh bedim va module e estehkamesh ham ma mikhaym
    bbinim har dafe ke setting avaz mishe (x) dar asl ostokhoni k sakhte mishe
    estehkamesh baz frgh dre (y)
    
    khob ma miaym hododan 10 ta setting dr nazar migirm hey azmayesh mikonim
    hey khorojiro k estehkamesh has ro misanjim
    yani masalan setting ro 10 ta adad mizarim , 300,310,320,330,340
    350,360,370,380,390
    khob har dafe k setting avaz mishe ehtemalan estehkam avaz mishe
    masalan settinge dastgah ro mizrim 310, estehkam mishe 10000
    bad mikonim 330 masan mishe 20000
    pas datamon chi mishe ? DATA chie?
    yek Data Frame hast k 10 ta radif dare ( tasavoresh konid)
    chera 10 radif? choon 10  ta nemone drim dg yani 10 bar azmayesh ro 
    anjam dadam
    khob in dah radif dota soton dare 
    yek soton settingemone (300-400) hamon x hamon vorodimon
    yek soton estehkmemone yani hamonn y hamn khoroji
    
    data=pd.DataFrame([[300,2000],[310,2300],[320,2600],[330,2800],
                       [340,2900],[350,3200],[360,3400],[370,3600],
                       [380,3800],[390,4000]],
                      columns=['Setting(x)','Estehkam(y)'])
    ino run bznid mishe data framemon dgahighan
    
    khob pas data yani x darim o y [** x ha mitone masalan 3,4 ta soton bashe
                                    yani masalan 3,4 ta setting drim]
    
    hooshe masnooe miad in rabete ye beyne x o y ro yad migire.(chijori?->migim alan)
    khob vaghty in rabete ro yad migire mitone pishbini kone va tasmim bgire
    pas 1-yad grft (az data ha) 2-moadel sakht(mantegh yad grft)3-bar hasbe manteghesh
    mitone pishbni kone (tasmim bgire o amal kone)


    khob khorojimon do no hast 1- mesle mesale bala adade peyvaste yani 
    1230,323032,21231,313,311 ya hata 14,14.22,14.7,14.9
    be in khoroji ha be mosheklemon migim regression

    hala bazi jaya x hamon hamone ama y emon khorojimon adadi nist
    balke masalan mikhaym begim in ostokhon ha gorohe 'a' bazia gorohe
    'b' yani oon 10 ta ostokhon ya gorohe a hastan ya gorohe b

    ya masalan aya mishakann ya na ag beshkanan (yes) ag nashkanan (no)
    ya a o b o yes o no k frgh dnre msn begim 0 ya 1 bashan
    yani in 10 ta data ya gorohe 1 hastan ( gorohi k msihkanan) ya
    gorohe 2 hastan ( gorohi ke ghavian nemishkanan)

    mesal:
        data=pd.DataFrame([[300,'yes'],[310,'no'],[320,'no'],[330,'yes'],
                           [340,'no'],[350,'no'],[360,'yes'],[370,'yes'],
                           [380,'yes'],[390,'no']],
                          columns=['Setting(x)','mishkane?(y)'])
    khob age khoroji gosaste bashe yani maasalann chantae chantae
    khob be in problem ha migan classification (daste bandi)
    

Kholase (summary):
    machine learning yani machine biad az data(?) yad begire(?)va
    
    data chie? yekseri x dare yani vorodi yani chizi k taghiresh 
    mitonim bedim . yekseri y dare yani khoroji yani chize nahaee k moheme
    baramon. va midonim x o y baham yek rabete ee daran yani ag
    x ro taghir bdim y taghir mikone
    
    khob khorojimon ag peyvaste bood --> regression
    age khorojimon gosaste bood---> classification
    


khob berim bebinim regression chie?
***in regressione sadast rabti b hooshe masnooe ndre
#oon bala regression va classification yani regression va classifcione e
hoshe masnooeee/

ama alan mikhaym rajebe regressione sade harf bezanim bebinim chie



Farz konid yek microbubble darim, yani chi yani yek hobabe kheyli kochik
darim ke in hobab ro mikhaym bahash karaee konim. in hobab az esmesh malome
hobabe, yani zood mitereke. yek azmayeshi darim k feshar behesh emal mikonim
yani mizarimesh zire press va miterekonimsh, ye adad mide in dastgah be name
omega. omega yani cheghad tahamol dare in microbubble, hrchi balatar bashe in
omega yani hobabe ghavi tare, yani tahamole bishtari dare yani paydarie
fesharesh bala hast.
ama avalin test ke migirm rooye yek hobab behemon 200 midde omega ke in adad
kheyli kame.
ma nemitonim ba in moghavemato paydari az hobab ha estefade konim dr donyaey vaghe ei
application o karbordesh chie? masalan mikhan toye hobab daroo bezaran bere too
badan. ya azash estefade konan toosh nano mavad ro besazan ya masalan toosh
baraye haffario CO2 captur o ina estefade beshe.
motasefane dar tamame in application ha bayad paydar bashe va khode hobab
age bezarim too kar yeho mitereke.
vase hamin ma miaym tooye in hobab ha yechizi bename 3D graphene mizarim
yani yek made ee fek konid chanta noghte o mavade kochik hast
tazrigh mikonim dakhele micro hobab ha ta paydarish bere bala.

midonim ke khode microbubbl khob dakhelesh graphene nist az aval yani dar asl
0% graphene toshe. khob ma chan drsad graphene toosh vared konim?
aya 10 %? aya 80%? chii?
nemishe goft.
choon shayad masalan age 10 darsad berizim moghavemat ziad she
ama age masalan 40 darsasd berizim. momkene sangini ijad kone toye hobab
va hobab ro beterkone pas yani moosalaman ba afzayeshe graphene hatman
paydari afzayesh nemiabad.
pas yek rabete ee beyne darsade geraphene va paydarie fesharie bubble ha hast.

ma mitonim darsade geraphene ro 'tagghir bdim'--> yani settingesho taghir
bdim->yani in vorodimone --> yani in X emone.
vasamon paydarie feshari ke hamon omega hast moheme--> keifiate nahaee ro
moshakhas mikone--> pas in khorojimone --> yani Y hast

pas ye x o y darim k harmoghe x ro taghir bdim y ham taghir mikone va nemidonim
ke rabete beyne x o y chie daghighan khob ma donbale yek machine hastim ke
betoone in 'rabete' beyne  x o y ro 'yad begire'.

khob khorojimon choon omega hast va peyvaste hast yani 3000,34324,1231 yani
moshekelmon chie ? machine learning regression.

ghabl az inke varessh beshim mikhaym bedonim khode regression che mani ee mide
badesh berim soraghe machine learning regression chon in dota frgh daran.


dar regression, in miad mige khob ma panja dade darim

x=np.array([0,4,8,16,32])
y=np.array([200,310,420,560,630])
ya hata mitone besorate excelo dataframe bashe :
    data=pd.DataFrame([[0,200],[4,310],[8,420],[16,560],[32,630]],columns=['darsad','paydari'])
    #injori x o yemon mishe har kodom az sotonash --> access
    x=data['darsad']
    y=data['paydari']
    
    
baraye rasmesh do rah drim:
    1-plt.scatter(x,y)
    ya
    2-plt.plot(x,y,'o')



rasmehs konido bebinidesh. khob ma midonim ke vaghty x emon yeki az 0 ,
4,8,16,32 bashe khob midonim chie y emon ama khob age bekhaym bbinim x emon 10 bashe
chi?? --> daronyabi behesh migan

age bekhaym bbinid masalan 40 darsad geraphene , paydari chghd mishe ?
behehs migan boron yabi.

khob sade tarin kar ine k biam noghat ro beham dg vasl konim:
    plt.plot(x,y)
khob moshkel ine ke fk konid khodeoton mikhayd har noghte ro b enoghte dg vasl konid
mesle shekle bala
khob vase noghte 40,50 ya balatar mikhayn noghte 32 ro b chi vasl konid?
pas yani boron yabi nmitoni ba inkar konid


#***********************
regressione sade miad mige:

mige bebinid man bekham yek khat bekesham. formole yek khat mishe in
Y=aX+b

mitonid rasm konid bbini

masalan:
    
    x=np.arange(5)
    a=1
    b=1
    y=a*x+b #y=x+1
    plt.plot(x,y)
    
    --------
    x=np.arange(5)
    a=1
    b=0
    y=a*x+b #y=x
    plt.plot(x,y)
    
    --------
    x=np.arange(5)
    a=2
    b=0
    y=a*x+b #y=2x
    plt.plot(x,y)
    
    --------
    x=np.arange(5)
    a=3
    b=4
    y=a*x+b #y=3x+4
    plt.plot(x,y)
    
    
    -----------------------------
    
khob ma faghat ba taghire a va b mitonim hezaran khat bekeshim.
regression mige man miad 1000 ta khat rasm mikonam ba taghire a o b.
chijori? miad aval yek hads mizne yani miad hsansi yek a o b entekhab mikone
masalan a=4 , b=2 masalan formol mishe y=4*x+2 va in khat ro rasm mikone
va haminjori be tartib a o b ro hey rasm mikone.
(soal?= khob chera inhame kaht rasm mkone? ke chi?)

mige man miad inkaro mikonam bad har khat ke rasm krdm . miad faseleye
har noghte ro ta in khat migiramesh R.
badesh vase inke kole fasele haro bebinam
zigma= R1**2 + R2**2 +......
pas in tabeye zigma omade faselehame noghat ro ta in khat hesab krde
be in tabe migan --> cost function

bad inghd hey a o b ro taghir mdie inghd mizare hesab mikone
va paeeen tarin zigma yani chi? paeen tarin zigmna yani
oon khati k paeen tarin zimgma ro dre yani b hame noghat nazdikk tre az beyne
hame khat ha

pas b in kar migan --> optimization ( behine sazi)

pas ba in kar mitone yek khat bedast biare ke a o b sh ro peyda krde
(chijori? hzarta a o b avaz krde hey zigma ro hesab krde
 az beyne oonhame khat oon khati ke kamtarin zigma ro dre omde
 dide ke a o b ish chie va gofte hala in khat
 masalan y=ax+b khate awlie mane)

dg bejaye oon panja noghte ma in khato drim y=ax+b
masaan fk kon a=1 , b=2 in kamtarin fasele ro dashtan ba noghat

miad mige azin bebad har noghte ee
har noghte ( yani beyne range daroon bashe masalan 10 k beyne 8 o 16 e)
ya biron az baze ( yani masalan 40)

mitoni b onvane x bzari too in formol va bdast biari y ro.


ba inkar oomad dar asl yek khat drovord
in khat chie???
nazdiktrin khat be noghat.
khat yani chi?--> yani formol yani hamon y=ax+b
pas dar asl chikar krde??-->omade 'rabete ' beyne x o y ro ' yad gerefte'
in kar kare hosh masnoe nis?



pas hala fahmidim chetro ba riazio amar yek model mitone rabete beyne x o y
ro yad bgire.


hala in regressione sade hast.

regresione machine learning chie???

jalase bad sohbat mishe



Alipilehvar1999@gmail.com
ai.course22.alipilehvar@gmail.com


GOOD LUCK!!!!!!




'''













