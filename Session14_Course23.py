"""

IN GOD, WE TRUST. ALL OTHERS MUST BRING DATA...

@author: Ali Pilehvar Meibody

SESSION14

"""

'''
first project--> formula caluclation.--> porozheye aval (function)
second project-->  rasme dade haye azmayeshgahi



'''

#5 ta mesall
a=pd.read_csv('')
aa
x=a['stress']
x=a['stress']

plt.plot()

#fun
def stress_strain():

   
stress_strain(a)
#dalile function neveshtan in bod ke ye caspsule dashtebashim dar asl



#'C://Users//sunhouse//Desktop//2.csv'
#'C://Users//sunhouse//Desktop//nanofiber-stress-strain.csv'
#'C://Users//sunhouse//Desktop//S1Data.csv'
#'C://Users//sunhouse//Desktop//sample_f.csv'
#'C://Users//sunhouse//Desktop//b.pilehvar.txt'

#-----1------
#yek tabe besazim
#bayad bbinim chi vorodi bgire chi khoroi bgire
#vorodi bayad adrese file ro bgire
#mitone khodesho bgire

#mma mikhaym akr vase akrbar rahat she

#fa yek zarfe bename file address

#ghbla z harchizi import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import statistics


fa='C://Users//sunhouse//Desktop//2.csv'

#yadet bashe--->
#aval codesho bnvis
#bad tabdilesh kon b tabe
def magnet_curve(fa):
    mydf=pd.read_csv()
    

#yadet bashe--->
#aval codesho bnvis
#bad tabdilesh kon b tabe
fa='C://Users//sunhouse//Desktop//2.csv'

mydf=pd.read_csv(fa) 


#aval samte rast bala
#typesh chie ? DF
#sizesh chie? (radif,soton) yani chata (sample drim, chanta vizhegi)
#2000 ta radif yni smapel dahstim dar har rdif do vizhegi record shgode

#ghabl az rasm
#****in bhtrin halate yek file e

#mydf filame
#mikhay chio bar hasbe chi bkshi?
#masalan magnetic field o bar hasbe magnetization mikham bksham
#y x o y bsaz
#esm ro ag motmaen nbodi

mydf.columns
#Out[24]: Index(['Applied Magnetic Field', 'Magnetization'], dtype='object')

x=mydf['Applied Magnetic Field']
y=mydf['Magnetization']
#noghte ee
plt.scatter(x,y)

#khati
plt.plot(x,y)

#fun -->
#xlable mizari , ylabel mizri 
#rang mizari va va avaa

#pas kh sade ok krdmsh beram tabash konm

def magnet_curve(fa):
    mydf=pd.read_csv(fa)
    x=mydf['Applied Magnetic Field']
    y=mydf['Magnetization']
    plt.plot(x,y)
    plt.xlabel('Applied Magnetic Field')
    plt.ylabel('Magnetization')
    plt.show()
    
    
magnet_curve('C://Users//sunhouse//Desktop//2.csv')
    

#agha man mikham maximumo dar biaram

def maximum_magnet(fa):
    mydf=pd.read_csv(fa)
    x=mydf['Applied Magnetic Field'].max()
    return x
    
maximum_magnet('C://Users//sunhouse//Desktop//2.csv')
#Out[31]: 798.93052




#age ma dah ta kar bkhaaym konim dah ta tabe bnvisiM"???

#1- which
#2-class


#which--->
#bia yek tabe bsaz va yek chizi bname which ya harchi ye zarfge taeen

def magnetization(fa,which):
    mydf=pd.read_csv(fa)
    
    if which=='plot':
        x=mydf['Applied Magnetic Field']
        y=mydf['Magnetization']
        plt.plot(x,y)
        plt.xlabel('Applied Magnetic Field')
        plt.ylabel('Magnetization')
        plt.show()
        
    if which=='max':
        x=mydf['Applied Magnetic Field'].max()
        return x
        
a='C://Users//sunhouse//Desktop//2.csv'
magnetization(a,'plot')

magnetization(a,'max') #Out[34]: 798.93052


#-------dar donyaye vaghe ei inghd data haye csv jazab nistan
#inghd taro tamiz nis yanichi?

#man 4 ta file drm mikham bbinidesh

a1='C://Users//sunhouse//Desktop//nanofiber-stress-strain.csv'
a2='C://Users//sunhouse//Desktop//S1Data.csv'
a3='C://Users//sunhouse//Desktop//sample_f.csv'
a4='C://Users//sunhouse//Desktop//b.pilehvar.txt'

data1=pd.read_csv(a1)
#ba estefade az pd.drop , radife 0 ta 30 ro hazf kon va baghiasham ksade

#avalesh tozihat minvisan , ya tozihate dastgahe ya tpzihate haghe copy righte va vava


data2=pd.read_csv(a2)
#266 992 ta radifd dre
#khob bbin nahatyhate file e dsc
#400 ta radif bishtr ndre

#bazi az dataha shayad poshte hami bashe

data2.columns

x=data2['Temperature']
y=data2['DSC']
plt.plot(x,y)

#moshkel = 3000 hzar radir o rasm mikone



#KHGOB bia bgo toye sotrone T ya dsc , fght 4090 taro rsm kon

x=data2['Temperature'][0:400]
y=data2['DSC'][0:400]
plt.plot(x,y)
#ok shod




#mitoni baraye dota polymer rasm koni
x1=data2['Temperature'][0:400]
y1=data2['DSC'][0:400]

x2=data2['Temperature'][400:800]
y2=data2['DSC'][400:800]
plt.plot(x1,y1)
plt.plot(x2,y2)

#kodom kodome?

#bename label

plt.plot(x1,y1,label='polymere 1')
plt.plot(x2,y2,label='polymere 2')
plt.legend()

#----hala ag 10 ta kahstim
#bbin pas bayad biaym
x1=data2['Temperature'][0:400]
y1=data2['DSC'][0:400]

x2=data2['Temperature'][400:800]
y2=data2['DSC'][400:800]x1=data2['Temperature'][0:400]
y1=data2['DSC'][0:400]

x2=data2['Temperature'][400:800]
y2=data2['DSC'][400:800]x1=data2['Temperature'][0:400]
y1=data2['DSC'][0:400]

x2=data2['Temperature'][400:800]
y2=data2['DSC'][400:800]

#sakht nis???
#az chi maiod ? tekrar --> for

for i in range(1,10):
    x=data2['Temperature'][i*400:(i+1)*400]
    y=data2['DSC'][i*400:(i+1)*400]
    plt.plot(x,y,ls='--')
    
#label gozari
    

for i in range(0,10):
    x=data2['Temperature'][i*400:(i+1)*400]
    y=data2['DSC'][i*400:(i+1)*400]
    plt.plot(x,y,ls='--',label='plot i ')
    
plt.legend()
#i frgh dre ba 'i'

#yek frvsh bname f'
#bjaye ' ' /  f' '

a=24

print('slama= a')

print(f'salam = {a}')




for i in range(0,10):
    x=data2['Temperature'][i*400:(i+1)*400]
    y=data2['DSC'][i*400:(i+1)*400]
    plt.plot(x,y,ls='--',label=f'polymer {i+1}')
    
plt.legend()

#chegone data ro nazarim besoze
a3='C://Users//sunhouse//Desktop//sample_f.csv'
data3=pd.read_csv(a3)



#flash back bzni b for o if o ina

data3.columns
#'Strain\tForce'

data3.drop(index=0,inplace=True)

for i in range(1,len(data3)):
    b=data3['Strain\tForce'][i]
    

b=data3['Strain\tForce'][2]
b
#str hast
#str yechi dahst b esme split

c=b.split()
c[0]
c[1]

#dg kari ndre

data3.drop(index=0,inplace=True)
strain=[]
force=[]
for i in range(1,len(data3)):
    b=data3['Strain\tForce'][i].split()
    strain.append(float(b[0]))
    force.append(float(b[1]))

plt.plot(strain,force)
plt.xlabel('strain (%)',fontdict= #fontemon )
#ye fotn hamishe barfaye khdoet bsaaz dashte bashiii





plt.plot(strain,force)
plt.xlim(0,200)
plt.ylim(0,20)


#moraje e koid b siti k dar mabhase matplotlib gozshtm

import matplotlib.colors as mcolors
#ino hatman bayad impport koni

#bad chan no rng drim chan dataet ranmg
#YEKI AZ MAROF TRINESH ESMESH HAS CS
mcolors.CSS4_COLORS
#'r'
#'#FF00FF'
plt.plot(strain,force)

plt.title('STRESS - STRAIN Curve',c='#800080')
plt.xlabel('STRAIN (%)',c='#FF00FF')
plt.ylabel('FORCE (N)',c='#FF00FF')
plt.xlim(0,200)
plt.ylim(0,20)
#plt.legend()
plt.show()

def stress_strain(f_adsres,which):
    mydf=pd.read_csv(f_addres)
    
    if which=='plot':
        #plt.plot()
    if which=='max':
        #mitoni yek tabe e az ghabl nvsht bashi
        #esme tabe masalan stres_max
        a=stres_max(c,d)
        return a
    
#tabe haye too dar too
#nested functions



#============MACHINE LEARNING=============================








#25
#25
#30
#3
#0
83/5

#16.6
= train score = baraye dade hae ke roosh fitt krdim

#training score


#10
#test score





#-----------------------------------
#datahamon yekseri x dare yekseri y dare khob
#chanta radifan masalan 100 ta (100 ppont noghte)

#20 tashonpo vardar bokon test dataset --> yani asan enga rndrimesh ahzfeshon kone

#chanta mimone?



#80 ta --> b ina migan train dataset --> hala ba in 80 ta fk kopn kole nemonamone

#bia hey khataro rasm kon hey roo ina fit kon
#hey roo ina fit kon
#cost function baraye har khat dr biar

#$kamtarin cost function bbin a o bish chie

#y=ax+b --> rabetamonnnnnnnnnn

#hala bbin in noghati k dahstim yani 80 ta 
#x eshono bzaar too rabete bbin y chi mide

#y predicted chie? menahsh ckon az y e vaghe ei
#hame ye 80 ta maoedelsh mishe ---> train scoreee



#20 taro dashtim k nayovordim jolo
#20 ta x oi  y dshtim

# x ashpo bzar too in rabete he ke model darovorde
#bbin y chi mishe

#y e ino ba y e v aghei menha kon taghsim bar 20 
#test scoree



#train scorer--> fasele noghati k dadim model amzoesh dide ba noghate vaghe ei --> fitting o neshon mdie --> cheghad yad grfte

#test score--> yani onae k model nadside --> ma pishbnish krdim ---> test scorer --> prediction --> pishbini pazirti generalization , neshon mide




#========================
#mqachien elarning yani
#1-yad bgire az data 2-mantegh kasb kone 3-tasmim bgire


#1- yadgiri***********
#qaz data yad migire
#fdata chie ? yek dataframe ke koli x darwe o ydone y
#khob agar y ha peyvaste bashe migim supervised regression
#ag y ha gosaste bashe migim supervbised classfication

#supervised-----> 1-regression 2-classfvication



#2--- mantegh *******
#bad rabeyteye x and y ro yadmigire


#har x e jadidi behesh bdim baema y mide ****
#ye mon ya predict mikoen ya daste bandio mige
#tasmim migire





#-------ejraye dastooor chejorie ?

#- datamon ro dataframe drim
#midonim chanta radife yani chanta point ya noght edrim
#in noghat chanta x ya chanta y drn
#**y baya dbbinim ya classificatione e , regressione


#avalin kar--> daTAMONO taghsim mikonim
#yek darsadi (80) mizrim traININ DATASET 
#20 darsad ro mizrim test dataset



#model miad azin 80 ta train dataset , rabetey x o y ro dr miare
#bad mibine ina chijori fit shodsan ye score mide bname training_score --> fittingo nshon mide


#oon 20 darsadam hala x asho mzirim too in rabete y ro dr miarim va moghayes emikonim
#oon 20 a ro ndide --> test scorer = pishbinimon chghd ghaviee




#ba estefade az test score va train score mifhmim modelemon cheijorie




#KOILE CONCEPTE MACHINE LEARNING



#inke chijori rooye training dataset ( 80 ta)
#cxhijooori vagehan rabetey x o y ro dr maire
#noe model

#1- linear regression (LR)
#2-  KNN (K Nearest neigbourws)
#3- Decision tree (DT)
#4- randomk fporest (rf)
#5- svm (support vector machine)
#6- mlp (multy layer perceptrion)/ANN artificial neural network

#in model ha fght fargheshon ine ke
#yejoori rabeteye beyne x o y ro dr miaran ama raveshehson frgh dre baham

#ona ham mian yeseri kara mikone
#yechizaee bename cost function drn 
#vase hame hadsashon dr miaran
#bhtrrino peyda mikonan
#va migan inam rabetamon

#LR hey y=ax+b khat midad
#baghie ravehs haye dg





#----------avalin mesal gol haye iris--------------

#import sklearn
#in ketabkhon kheyli bozorgeeee hamasho nabaayd import krd sakhte


from sklearn.datasets import load_iris

iris=load_iris()

#INPUT, X , FEATURE --> VORODI
#OUTPUT, Y , TARGET --> KHOROJI


iris.feature_names
#Out[85]: 
#['sepal length (cm)',
# 'sepal width (cm)',
# 'petal length (cm)',
# 'petal width (cm)']

iris.target_names
#'setosa', 'versicolor', 'virginica'
#esme se ta gole


x=iris.data
y=iris.target

#too in mesalaye sklearn injorie 
#ama donyaye vaghe ei bayad yaek dataframe dri
#baayd jdoash koni  b x va y 

#in datamon
#*(**Tpozihat)


#hadaf chie?

#yek mdoel bsazim baid yad bgire 
#rabetey ebyen ex haro ba y 
#ke chi bshge

#ke vaghty ye goli ma grftim andaze giri krdim 4 ta vzihegisho
#gozaahtim too mdoel
#model behgemon bege jozvge kodom dastas (cxlassififcation)


#150 gol
#4 ta vizghegi dre k -->x
#1 done khoroji k noe gol ro nvshte --> y


#---avalin kar???
#preprocedssign---> yani dade haye parto hazf koni
#scaleshon doiros koni va a,.......


#vali dade haee k sklearn dre mhame preprocess hsodas


#vali ytdmon bashde bayad har datae ro preprocesing anjam bdim
#dovomi kar
#bayad datamono b test va train taghhism konim

#yani 80% train bnashan , 20% test
#vazeh tr bgm

#yani 80 % x bashe jolosh 80% y
#20 % x bashe 20% y



x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split

#aval bgo too koja brizm vaghtyy joa krdm

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)



#gharoghati kon tartib

#shuffle

#daddd ro taghsim konim b test dataset va train dataset
#ke mdoel bre yad bgire az train dataset va biad bge 
#psihbnini kone test dataset ro

#ta inja baraye hame ravesh ha yeksaen

#alan ye mdoel mkihaym roye training dataset  yad bgire
#in mdoel az ye raveshi mire k hala felan yedonasho bldim

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()



#--------------
#hala yek model drim
#mikhaym bgim model bioro rooye traina dataset ha
#oon 80% e yani oon 120 ta noghte yad bgir rabetey x o y ro


model.fit(x_train,y_train)

#@ychi drim bname model, hamin variable e model
#alkan rfte yad grfte

#tooo delehszh yeseri chizas

#ghabla z inke predict bznim mikhaym bbinim
#modele k sakhte yani rfte yad grfte

#test datasetaro onae k ndide ro chijori mitone predict kone

score=model.score(x_test,y_test)
print('our accuracy is :',score)
#our accuracy is : 1.0






#mikham ydchize jdid bdm k pishbini kone
#yek golo drm 4 ta vzihegisho grftm mikham bdm behesh

new_data=np.array([5.9,2.7,5.2,2.4]).reshape(1,-1)
preddcited_data= model.predict(new_data)

print(preddcited_data)


#5








#=============




from sklearn import datasets

#https://scikit-learn.org/stable/datasets.html#datasets

data1=datasets.load_iris()
data2=datasets.load_boston()
data3=datasets.load_breast_cancer()
data4=datasets.load_linnerud()
data5=datasets.load_wine()
data6=datasets.load_diabetes()
data7=datasets.fetch_california_housing()




#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================


#overview--------


'''

Pas kolan machine learning 3 no hast
1-Supervised learning
2-Unsupervised learning
3-reinforcement learning


khode supervised learning b do no taghsim mishe 1-Regression 2-classification
va unsupervised yani khooshe bandi (clustring)

khob bebinid kolan machine learning Model ha mesle ye BOX hast
dota faz dre


1-Train dadane BOX:
in Box data migire va in data ( Ye x dare ye Y dre)
In box be yek tarighi rabeteye beyne X va Y ro bedast miare (yani yad migire train)

2-predictioNE BOX (pishbini):
hala ye x e jadid behesh bdim tebghe rabete ee k balade y ro behemon mide (pishbini)



.......
hala in datamon ( ke x o y dare) ag y emon adade peyvaste bashe 1.43,3.543,6,..
be masalamon migan supervised regression
age datamon Y esh gosaste bashe yani case1,case2,case3 behesh migan
classification ( dastebandi)

dar har sorat data ro k beehsh midim miad rabeteye beyne x o y ro yad migire
age regression bashe: miad mige in x ha ch rabete e ba y daran k x e jadid 
migire betone y ro pishbini one
age classification abshe: miad mibine in x ha ba y ch rabete ee drn k x e jadid
migire betone bege Y esh kodome ( yani jozve kodom daste hast)

agar dar masaele daste bandi Y ro b model nadim va bgim khodet boro too x ha
begardo begard bbin frghashon chie va khdoet khoshe bandishon kon behesh mign
unsupervised



......
pass dobare mitonim begim kole machine learning shabihe derakhte zire


..............................Machine learning.......................................
.....1-supervised.............2-unsupervised...........3-reinforcment................
...1.1.Regression..............clustring................(IN dar mohit train mibine)..
...1.2.classification...................................(bar asase padasho azab).....
.....................................................................................

Pas ye Box (modele machine learning) darim ke do faz dare yeki 1-train bbine
2-badesh k hala yad grft btone pishbini kone

khob chijori train mibine? yani chijori mitone yad bgire rabete ro ?
hezaran rah hast 1-lienar regression (hamoni k tozih dadim) 2-K Nearest Neighbour
3-Decision Tree 4-Random Forest 5-Support vector
bebini hameye in model ha ham baraye regressionhast ham baraye classification
hameye in model ha ye thrick mizanan va rabeteye beyne x o y ro bedast miaran
faghat harkodom raveshi k estefade mikone fargh dare(behesh mipardazim...)

khob hala fk kon yad grft tamom , aaz koja bdonim doros pishbini krde?
khob bayad brim ye x i azmayesh konim bbinim y chie / bad x ro bzarim too in model
bbinim y ro chi pishbini mikone va badesh bebinim ke in Y ha chghdr shabihe hame

Bejaye inke aval train bdim model ro roo kole data ha bad ye noghte jadid 
brim begirim
miaym migim az aval bia dade haro taghsim kon be dobakhsh 1-train 2-test

model rooye dade haye aval train bbine (yani rabete ro peyda kone) bad
biad oon test haro x esho bzare too model ye y i migire ba y i k vaghena dre
moghayese kone va bbine model cheghadr nazdiek ( be in migan score ya metric ya error)

khob Hala ma fhmidim chishdoe.

hala mikhaym biaym too code nevisi bbinim ch konim.

Bebinid kolan dataye ma ye Dataframe hast yani chanta soton drim chanta radif
radif ha yani tedad nemone hamon ama yekseri sotonemon X emon (vorodimon) has
va yek soton Y (khoroji) hast



888888888888888888888888888888888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888888888888888888888888888888888

Kole hooshe masnoee chnta marhale dare:
    

Marhale (1)--> datamono biarim too barname spyder 


Marhale (2)--> preprocessing : yani bayad ba oon ravesh haye pandas
              kamel analysesh konim tamame jahaye khali , ghalat va ... ro hazf konim
             
              
Marhale (3)--> bayad in datamono soton haye x ro brizim dar Yek varibale e X
               va sotooone y ro brizim too yek variable bename Y
            
               
Marhale(4)---> hala datamono be do bakhsh taghsim konim yek darsadi ro bokonim
               training yekdastaro bokonim test

**gharare model biad az rooye x o y haye Training dataset , rabete ro yad begire
ba in rabete biad x haye Test dataset ro bgire va yek y BENAME Y_PREDICT pishbini 
kone va ba y haye test dataset moghayese kone va in moghayese behesh migan
error, metric , score --> ke neshangare khata va deghate modelemone



Marhale(5)--> Hala yek model entekhab konim ( felan yek modele linearregression
                                             va Logisticregresion baladim)
**ama ma model haee mesle KNN, DT, RF, SVR darim ke hamashon mian az rooye
training dataset rabeteye beyne x o y ro yad migiran va badesh ba oon x e jadid 
migiran va y ro pishbini mkonan
farghe in mdoel ha baham fght dar raveshe yadgiri ee hast k poshte tabashon emal
shode, dar natije hamashoon fght rabeteye beyne x o y ro dr miare


Marhale(6)---> hala in modelemono migim boro fght az training-dataset 
rabete beyne x o y ro dr biar va yad bgir ( kari b test dataset ndshte bash)
va mire o yad migire tamaaaaam!!

Marhale(7)---> hala midonim yek test dataset drim k yekseri x dre yekseri y dre
be y haye in migan true_y yani vageh eie. hala ma fght x e in test dataset ro
midim be modelemon ( modelemon az training dataset , rabete ro yad gerefte)
va hala migim y ro pishbini kon va y ro pishbini mikone va bema yek
y_predicted mide va ma miaym y_predicted va y_real ro baham moghayese mikonim



Marhale(8)-->  Dar marhaleye moghayese ma bayad bedonim he vaghty model
miad az training dataset rabeteye x o y ro dr miare, vaghty hamoon x haro bhsh mdiim
ye y e taghribi mide be ezaye har x, khataye in y haee ke mide ba vaghe e haro
behesh migan deghate fitting ya training_score yani chegahd toneste in rabete ro
dorost mdoelling kone
hala in, marboot be oon x o y haee bood ke dide bood
miaym behesh x_y e test_dataset behehs midim ke nadide va mikhyam bebinim
pishbinish chtore
miad x haro migire va yek y i pishbini mikone va moghayese mikonim va b in migan
train_score

pas kolan yek train_score drim ke namayangare yadgirie model ya fittingo modelingeshe
yek test_score ke neshangare tavanaeeie pishbinie model baraye datahayee ke nadide hast




Age train_score kh paeen bashe --> Underfitting -> yani doros natonese yad bgire
Age train_score kh bala bashe va test_score paeen bashe--> overfitting--> yani
kh dige yad grfte yani ba inke yekseri khata has dar dataha , oon nois ha ham yad grfte
va hamishe in ziad yadgrftn khob nis chon baes mishe natonim datahaye jadid ro
khoob pishbini konim ( behesh migan generalization yani ooomomi sazi)


9999999999999999999999999999999999999999999999999999999999999999999999999999999
9999999999999999999999999999999999999999999999999999999999999999999999999999999
Pas kolan 8 ta marhale darim che baraye regression ch classification
alan mikhaym code nevesisho bgim
**esmashono yad bgirid**



Marhale 1--> (IMPORTING)------------------------------------------------------
miaym az Open() ya pd._read estefade mikonim  ya az dataset haye sklearn k amade hast

Marhale2--> (Preprocessing)------------------------------------------------------
az rasvesh haye cleaning data dar pandas esteafde shavad mesle pd.drop va ...

Marhale3--> (taghsim b x o y)------------------------------------------------------
Kh sade ba ['esme soton'] inaro brizim too dota zarf yeki X yeki Y

Marhale4-->(train test split)------------------------------------------------------
Mitonim az tabeye train_test_split ke yeki az tabe haye ketabkhone sklearn
hast estefade konim k datahamono miad taghdim mikone be test o train
inke chan darsad vardare taghsim kone ham daste mast 


Marhale5--->(Model selection)------------------------------------------------------
Kh sade ba seda kardane oon modeli k mikhaym va rikhtnsh too yek zarf
mitonim azash estefade konim
mymodel=SVR()  ya  mymodel=DecisionTree()
#chra nmiaym mostaghim estefade konim? choon dakhele parantez mitonim yekseri
settinge model ro tanzim konim hamon aval setting ro tanzim mikonim va mirizmsh too
yek zarf, beja inke hey sedash bznim va hey biaym tanzim bechinim

Marhale6-->(training / fitting)------------------------------------------------------
Hala vaghteshe be modeli k entekhab krdim bgim boro az train dataset yad bgir
yani train bbin
kh sade esmesho seda miznim migim fit sho

mymodel.fit(x_train,y_train)

y x_train o y_train drim k hamonaee has k dar marhale 4 taghsimesh krdim
hala migim modelemon k dr marhale 5 entekhab krdim bre az x o y e
training , rabete beyne x  o y ro befahme

Marhale7--->(Prediction)------------------------------------------------------
Hala modelemon yad grfte va kh sade mitonim hamin model ro seda bznim va bgim
felan x ( x i k made nazaremone) behesh bdim va bgim bnzrt y chi mishe? (pishbini)

mymodel.predict(new_x)
in yani mymodel k modele mane k train dide yani yad grfte hala x bhsh midim 
va yek y ro predict mmikone


Marhale8--->(Scoring / Error / Metric )------------------------------------------------------

Hamontor k goftam do no score drim
yek score migan train_score yeki test_score

train_score yani midonim training dataset yek seri x_train dre ye y_train
model yek rabete ee beyne ina peyda krde (rabete he ke 100% doros nis)
yani yechizi beyneshone ( fek konid b oon khate ke beyne noghat rad shode bood)
khob bayad bbinim in model age in x haye train ro bhsh bdim ch y ro predict mikone
yani cheghad khoob toneste model beshe ya fiitt bshe

yedone hasm test_score drim yanii oon test dataset ke negah dashte boodim k pishbinie
model ro bahash besanjim
yek x_test dre ye y_test/ y_test emon dr asl behesh migan y_true yani in vaghe eiate
hala ma in x_test ro midim k modelemon predict kone va bema yek y_predicted
mide va hala ba moghayese krdne y_predicted ba y_true
yani y hayee k model pishbini krde ba y haee k bayad mishode yani entezar dshtim inshe
behesh migan test_score ke neshangare tavanaeeie pishbinie mdoelemone


kafie az code e zir estefade she

model.score(y_true,y_predicted)









Moafagh bashid,
Alipilehvar1999@gmail.com
Ai.Course22.Alipilehvar@gmail.com



'''











