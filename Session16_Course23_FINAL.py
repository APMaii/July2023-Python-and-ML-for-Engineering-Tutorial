# -*- coding: utf-8 -*-
"""
In The Name Of God

@author: Ali Pilehvar Meibody
"""
'''
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

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#preprocessing(datamon)
#dade ye IRIS ro kar krdim hala mikhaym baz yadesh bioftim
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)
#**fght inja frgh dre ke model ro esme on modelemon mzirim


#model haro inja frgheshone
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=20)

model.fit(x_train,y_train)
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('our train score is :',train_score)
print('our test score is :',test_score)
x_new=np.array([6,2,3,1]).reshape(-1,1)
y_new=model.predict(x_new)



#===================================
#tamame inha rajebe classfiication bod
#bia reajebe regression mohmtrin amsasleye mohandesi sohbat kon


x=np.arange(0,20)

y=[]
for i in x:
    a=np.random.randint(30)
    y.append(3*i+ a)

#y=3*x + (beyne 0 ta 30)

    
#yek dataee drim ke yek x i dre y y i dre
#bekeshimsh behtar bfhmim

plt.scatter(x,y)  
plt.xlabel('x')
plt.ylabel('y')

#x ye settingi ya harchizi has k man mitonm taghiresh bdm
#y ychizi has k misanjamesh

#chra donbale rabete ee ?
#yeki mikham bbinm beyne range chi mishe
#balatar az 20 o bbinm

#ya yeja frght ye x nis shayad 7.8 ta x
#pas masale chie?---. x o y rabetashon

#0-preprocessing-------------------------
#1-b x o y tabdil mikonm
#2-miam b train o test taghsim mikonm
#3-model selection yani y modelo bzari ( tanha jaee hast k mdoel ha frgheshone )
#4-modeleto fit bdi b train ha ( yani azoon train datasdt ha bre moadeleye beyne x_train o y_train ro yad bgire)
#baD MIADM pishbini mikonim x_test ro k bhsh mign y_pred
#bad miaym y_pred o ba y_test moghayese mikonim --> k bbinim chghd nazdik hads zade
#score .. chijori moghayese mikonim? che ekhtelafisho moahseb emikonim b in migan metric

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
#bad azinja hatmane hatman
x_train=x_train.reshape(-1,1)
x_test=x_test.reshape(-1,1)


plt.scatter(x_train,y_train)
plt.scatter(x_test,y_test)
#abia traiNE , #narenjai test

#yani mdoele ma rooye in train mibine
plt.scatter(x_train,y_train)


#ina ro badan pushbini mikone
plt.scatter(x_test,y_test)


from sklearn.linear_model import LinearRegression
model=LinearRegression()


model.fit(x_train,y_train)


train_pred=model.predict(x_train)
plt.scatter(x_train,y_train)
plt.scatter(x_train,train_pred)    
    
#faseleye noghate abi ba narenij--train score
#yani nshon mdie chghd khob yad grfte

test_pred=model.predict(x_test)

plt.scatter(x_test,y_test)
plt.scatter(x_test,test_pred)  

#train score o test score k bfhmim chie ************
#hala k fhmidim pas 

#sturcture e nahaeeie yek mdoele regresion ( shabihe classfication ) 
 
#=====================================================   
#=====================================================
#import
# preprocesing
#x o y taghsim mikonim
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
#bad azinja hatmane hatman
x_train=x_train.reshape(-1,1)
x_test=x_test.reshape(-1,1)

#model
from sklearn.linear_model import LinearRegression
model=LinearRegression()

#fit b train ha
model.fit(x_train,y_train)

#1-rahe vaal
train_score=model.score(x_train,y_train) #yadgiriii namayandeye yadgirie
test_score=model.score(x_test,y_test) #faseleye beyne
#noghate pishbini shod eba vaghe ee
print('our train score is:',train_score)
print('our test score is:',test_score)
#our train score is: 0.6671571805500487
#our test score is: 0.9684783305882178

#mitoni rasm koni mitoni hezarat kar koni ama
#anaslysise asli ine bbini overfit o undefit nis
#yani train score nabayad kh paeen bashe nabayadam
#agar bala bashe nabayd test scoremon paeen bashe
#sweet spot= train score o test score bala bashan (holohoshi)

#----raveshe dovom?
#bbin raveshe aval miad az y raveshe defaulti estefade mikone
  #default r2 ro hesab mikone
#adadaye bala r2 e
#ama ma faseleye beyne prediction o true mitonim az chan tarigh hesab konim
#rtaveshe ghabl fasleeye predict o real true az r2 ya defaultesh mdie
#ag khasti metriceto avaz 
#yani meyare sanjeshet baraye oon faslee

y_pred=model.predict(x_test) #Noghte narenjia

from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score

r2_test_score=r2_score(y_test,y_pred)
mae_test_score=mean_absolute_error(y_test,y_pred)
mse_test_score=mean_squared_error(y_test,y_pred)
mape_test_score=mean_absolute_percentage_error(y_test,y_pred)
print('r2:',r2_test_score)
print('mae:',mae_test_score)
print('mse:',mse_test_score)
print('mape:',mape_test_score)

#print('mape:',mape_test_score)
#mae: 4.015495400392099 adady k pishbini krdm vasat ya +4 -4 e
#mse: 17.132027325303643
#mape: 0.13478849035722765  #holohoshe 13 darsad khata dre

#agha in test_score bod ma baraye analys trasion_score haM MIKHAYM K

y_pred=model.predict(x_train) #Noghte narenjia

from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

mae_train_score=mean_absolute_error(y_train,y_pred)
mse_train_score=mean_squared_error(y_train,y_pred)
mape_train_score=mean_absolute_percentage_error(y_train,y_pred)
print('mae:',mae_train_score)
print('mse:',mse_train_score)
print('mape:',mape_train_score)


#y=3*x + (beyne 0 ta 30) vageheie

#predict : y=2/75x + 15.55


b=model.intercept_ #Out[140]: 15.55481827778615
a=model.coef_ #2.75237521

x=np.arange(0,100)
y=a*x+b
plt.scatter(x,y)

#====================================
#import
# preprocesing
#x o y taghsim mikonim
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
#bad azinja hatmane hatman
x_train=x_train.reshape(-1,1)
x_test=x_test.reshape(-1,1)

#model
from sklearn.linear_model import LinearRegression
model=LinearRegression()

#fit b train ha
model.fit(x_train,y_train)

#1-rahe vaal
train_score=model.score(x_train,y_train) #yadgiriii namayandeye yadgirie
test_score=model.score(x_test,y_test) #faseleye beyne
#noghate pishbini shod eba vaghe ee
print('our train score is:',train_score)
print('our test score is:',test_score)


#ag rabete khati naboid ? 
#age logaritmi bod ?
#ag x hamon ziad bdoan x1,x2,x3
#ag x ha rangeshon frgh mikrd onmoghe chi>


#ag x ha ziad bood bjaye inke bere rabete y=a*x +b ro dr baire
#miad rabeteye y= a*x1 + b*x2 + c*x3......z*xn + alpha

#******
#ravesh haye linear --> khati dr maire ama 
#ravesh haye dg barash mohem nis maido ag gehyre khati bashe 
#logarithmy bashe ya hrchiiiiziii --
#ravesh haye dg mitone capture ekone relationship



#baraye rabete haye linear ya age modelemon harakri krdim ntones capture kone mitonim khodemon
#inakr ro anjam bdim

#rperprocesdsding do ghesmate 
#yeki onjaee ke dadaro clean mikrdi ba pandaso formolash va codash
#yekiam bad az train test split (chra?)

#baraye captrue non-linear ya logarithmy ya ... 
#y aham scale kardan


#hameye ina az ye pooshe e bname preprocessing mian
#------- scal

#4 ta mohemtrinash

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer


MinMaxScaler.fit(x_train)
scaled_x_train=MinMaxScaler.transform(x_train)
#vali dg fit nmikhad
scaled_x_test=MinMaxScaler.transform(x_test)


#bjaye inke model ro rooye x_tyrain y_train fit koni va
#rooye x_test score bgfiri
#rooye scale shodaahon inakro kon


model.fit(scaled_x_train,y_train)

model.score(scaled_x_test,y_test)


#===================
from sklearn.preprocessing import PolynominalFeature
poly=PolynominalFeature(degree=2)
poly.fit(x_train)
poly_x_train=poly.transform(x_train)
poly_x_test=poly.transform(x_test)

model.fit(poly_x_train,y_train)



#------structure nahaee
#import
# preprocesing
#x o y taghsim mikonim
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
#bad azinja hatmane hatman
x_train=x_train.reshape(-1,1)
x_test=x_test.reshape(-1,1)

from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=2)

poly.fit(x_train)

poly_x_train=poly.transform(x_train) #in x_trainame
poly_x_test=poly.transform(x_test)   #in x_test ame


#model
from sklearn.linear_model import LinearRegression
model=LinearRegression()

#fit b train ha
model.fit(poly_x_train,y_train)

model.score(poly_x_test,y_test)


#aksaran poly ro baraye
#masalan LinearRegresion , Ridge, Lasso , KNN , RF 


#====================================================
#scale rpo bishtar rooye ravesh ahee mesle SVR , MLP va deep learning
#joda azinke bhtr mikone frgh haro 
#balkeeee --> sorate yadgirie nemone ro bhtr mikone
#chon hame ham scale mishan baes mishe sari tar karkone

#import
# preprocesing
#x o y taghsim mikonim
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
#bad azinja hatmane hatman
x_train=x_train.reshape(-1,1)
x_test=x_test.reshape(-1,1)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

scaler.fit(x_train)

scaled_x_train=scaler.transform(x_train) #in x_trainame
scaled_x_test=scaler.transform(x_test)   #in x_test ame


#model
from sklearn.svm import SVR

model=SVR()

#fit b train ha
model.fit(scaled_x_train,y_train)

model.score(scaled_x_test,y_test)




#ghesmate mdoel ha baham frgh dasht yadeete ?/

#khgob bia fght inja bnvis



#KNN
from sklearn.neighbors import KNeighborsClassifier #baraye daste bandi
from sklearn.neighbors import KNeighborsRegressor #baraye regression
model=KNeighborsRegressor() #mitoni n o inaro entkehabvg koni
model.fit(x_trian,y_train)

#DT
from sklearn.tree import DecisionTreeClassifier #baraye daste bandi
from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor() #masalan omgh ro inja setting midim


#RF
from sklearn.ensembles import RandomForest
model=RandomForest() #n_estimator yani tedade derakht haee k mikhay --> har derakht omgho ina dre


#SVM Suppoirt vector machine --> 1)SVC support vector Classsifier 2)SVR support vector regrssor
from sklearn.svm import SVC #(yani classifier)
from sklearn.svm import SVR
model=SVR() #kerneleshe , va C




#--------------------------------------------------------
#classificsation va regression --> supervised ro yad grftim bsorate kamel

#avalin chiz ine
#vbaghty ma omdim b train o test taghsim krdim 
#masalan  az 100 ta data 20 atsho test krdim , 80 tasho jozve train ha krdim 

#kodom 20 ta ??? 

x=np.arange(0,10)
y=2*x
plt.scatter(x,y)

train_test_split(x,y,test_size=0.2)

#bahs bahse sanjeshe....

x=[0,1,2,3,4,5]
y=[0,10,20,30,50,20]
plt.scatter(x,y)


#test---> sanjesh --> validation


#cross_validation ---> yani inke fght yek ghesmato dr nzr ngiri --> kole dataro dr nzr bgiri
#meyare ma ghavi tre
#yani scori k migim ghavi tare -->ghabele estenad tare


#x o y ro drim
#x_train,x_test,y_train,y_test=train_test
#bjaye inke shabieh bala bnvisim
x=x.reshape(-1,1)

from sklearn.model_selection import KFold
#n_splits hamon ke yadete too trian test split minvsishti test_size
#tyeste size e 20% yani chi? yani kole dadee ro taghsim bar 5 kon yelkisho vrdar

fold=KFold(n_splits=5,shuffle=True,random_state=42)

from sklearn.svm import SVR
model=SVR()

from sklearn.model_selection import cross_val_score

score=cross_val_score(model,x,y,cv=fold,scoring='neg_mean_absolute_error')
score.mean()





#-------harchi ta alan goftyam vase vaght bod ke ye test_split mikrdim ykabar miomdi 20% joda mikrdi

#age bekhay sanjeshet kh ghavi bashe --> standard
#cross valdiation------
#structure---------------------------
#1-importe datya
#2-cleaning data
#3-taghsim b x o y
#4- x=x.reshape(-1,1)
#5-(optional) ag khasti scaler ya poly bzn roosh
#6-
from sklearn.model_selection import KFold #chizay edg ham darim masalan dota dota vr mdir vba va
fold=KFold(n_splits=5,shuffle=True,random_state=42) #n_split mige k chanta tiek konm hamon
# masalan 5 split mishe 5 ta data misaze too harkodom 20% esho mzire test 
#bad vase harkodom miad test score ro hesab mikone

#entekhabe model
from sklearn.svm import SVR
model=SVR()

from sklearn.model_selection import cross_val_score
score=cross_val_score(model,x,y,cv=fold,scoring='neg_mean_absolute_error')
print('our cross validation score is:', score.mean())
#in kar baraye sanjeshe

#aya mitonam baraye predict estefade konm? kjhey
#ma model ro fit nkrdim ke
#fghtt o fght omdim sanjidimsh 
from sklearn.model_selection import cross_val_predict
#har moghe miomd 20% ro vrmidash



#===============================================
#barmighrdim az aval migim ke mikhaym k y tabe ye svr ro bznim

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.svm import SVR
model=SVR(kernel='linear')
#model=SVR(kernel='linear')
model.fit(x_train.reshape(-1,1),y_train)


from sklearn.metrics import mean_absolute_percentage_error as mape


y_pred=model.predict(x_test.reshape(-1,1))


mape_score=mape(y_test,y_pred)

print('mape :',mape_score)

#in miad mige drdssad khatam

#mape : 1.6844503706640084
#yani sado 68 darsad khata drm kh badeeee kh 

#brmigrdm bala migm khob bayad biam 
#hyperparameter amon khob entekhahb konm

#vaghty kernelo krdm linear bhtr shod

#mape : 0.6247665534804756




#bshin halghe for bzn
param_list=['linear', 'poly', 'rbf']
#masalan adad ham mishe


max_score=0
for i in range(0,3):
    model=SVR(kernel=param_list[i])
    model.fit(x_train.reshape(-1,1),y_train)
    score=model.score(x_test.reshape(-1,1),y_test)
    
    if score>max_score:
        max_score=score
        max_param=i
print('the best param is:',param_list[max_param])


#ba for omdm oon hyperparameter hae k fk mikrdom hey gozshtm bardashtam


#b in migaer hyperparameter tuning


#agha in yedone bod
#ag bkham c masalan az 0 ta 1000 
#agmama az 0 ta 1000 va haamro baham konm chi?????


#sklearn odme gfote man ye tabe drm va amkhsose in kare

#=============================================
#=============================================
#*********************************************
#*************[1 hyperparameetr tuning]************
#hamin ytikassss 
#1-impiort
#2- b x o y mirizish
#3-x=x.reshape(-1,1)
x=x.reshape(-1,1)
#4-split ba cross valdiation
from sklearn.model_selection import KFold
fold=KFold(n_splits=5,shuffle=True,random_state=0)

#5-modelet
from sklearn.svm import SVR

model=SVR()


#6- ye list bename hyperparameter hat doros kon
myparam={'kernel': ['linear', 'poly', 'rbf'],
         'C': [0,10,100]}

from sklearn.model_selection import GridSearchCV
gs=GridSearchCV(model,param_grid=myparam,cv=fold,scoring='neg_mean_absolute_error')

gs.fit(x,y)

#yechizi drim bename gs , haminz arfe
#toosh adad nist ama yekseri khasiat has


gs.best_params_ #{'C': 10, 'kernel': 'rbf'}

#yani az beyne oon rangi ke bman dadi c 10 bashe kernel rbf bashe
#bhtrinnn yadgirio dri 

#yani yadgirim chghdre ? chan darsade ?

gs.best_score_ #Out[167]: -8.011967457042356

#ag khoobn bod besmela
#AG nabodo , hey bayad range ro taghir bdm


CV=gs.cv_results_



#vaghty inakro krdimmm



#vaghty bhtrin ro dr opvordi
#bgi
#dg gs mesemodele
new_X=np.array(10).reshape(-1,1)
gs.predict(new_X)



#============================================
#======sanjeshe=============
#minvisam bade class ----> high impacte



#=============================================
#-------structure---------------------------






#================================================
#===================================================
#yek nemone az deep learning miznm 

#grid searhc mikhaym konim
#x o y ro drim
x=x.reshape(-1,1)
from sklearn.model_selection import KFold
fold=KFold(n_splits=5,shuffle=True,random_state=0)

from sklearn.neural_network import MLPRegressor
model=MLPRegressor(random_state=0)

# (10,10) | (10,10,10) | (100,)  | (4,4)
    
myparams={ 'hidden_layer_sizes'  : [(10,),(10,10),(20,)] ,
'activation':['relu','tanh','identity'],
'solver':['adam','sgd']}
    
from sklearn.model_selection import GridSearchCV
gs=GridSearchCV(model,param_grid=myparams,cv=fold,scoring='neg_mean_absolute_error')
    
gs.fit(x,y)

gs.best_params_ #in bht mige az beyen oan ek gfoti kodom bhtrine

#hala ba in bhtrin setting bhtrinm score chie
gs.best_score_

#hala ye range entekhab kon

x_new=np.arange(0,100).reshape(-1,1)
predicted=gs.predict(x_new)



#===================================================

'''
Overview---------------------------------------------------------------

Ta alan ma mohem tarin dastoorate python ro yad gereftim
python manande yek zaban ( masalan zabane englisi ya harchizi) yekseri
kalamat dare (python built in) va yekseri grammar ( dastoorat)

.......................................
mohem trin built in ha : zamani k minevisimeshon narenji mishan
print() --> baraye check krdno namayesh
input()--> baraye gereftan az karbar
open()--> baz kardane yek file
len()-->andaze ra midahad
range()-->yek range behet mide makhsose for o while
sum()--> jame kol ro mide
min() va max()--> mire kochiktrin ya bozorgtrin ro mide

.......................................
ma yekseri zarf drim k tooshon maghadir mirizim k behesh migan variable (moteghayer)
in zarf ha mitonan
adad bashan --> int (yani sahih) / float (ashari)
mitonan reshte horof bashan --> str
mitonan list bashan --> list


.................................
hala ma yekseri dastoorat darim , if , if else , for , while

if yani migim agar injori shod inkaro kon ag nashodam velesh kon

if shart:
    dastooor
    
if else, yani ag injori shod inakro kon ag nashod kare dg ee kon

if shart:
    dastooor
else:
    ye dastoore dg
    
for o while baraye yek halgeh hast ke terkar mishan, ag mikhayn baraye
yek tedade moayen yek kario repeat konid ya brid peymayesh konid az for

for (ye range midin):
    dastooor
    
while vase vaghtie ke entehaye range ro nmidonin va yek shrt mizrim

while shart:
    dastooor
    

..................................
badesh ma midonim ke list dota naghs dasht, sari nabod va inke do bodi nmishod
vase hamin omdim az numpy estefade krdim
import numpy as np

va bahash miomadim arraye misakhtim k 1 body, 2 body 3 bodi dashtim..

a=np.array([])


...................................
badesh goftim khob listo numpy baraye dastresi bayad az index estefaade mikrdim
age bekhaym bjaye index biaym esm bzarim baraye soton ha ya radif ha
pandas omd goft az data frame e man estefade konid

import pandas as pd

a=pd.DataFrame([])
va hamchnin mitonesim az ravehs haye cleaning data estefade konim ke
biad dade haye khali, dade haye ghalat , formate ghalat va ... ro pak kone
ya jaygozin kone



..................................
baraye rasm ham mitonesim az ketabkhoneye matplotlib estefade konim
import matplotlib.pyplot as plt

plt.plot()
plt.scatter()



..................................
bad az amoozeshe in ketabkhone haye mohem baraye mohasebato kar ba dade ha
va rasm , hala bayad varede machine learning beshim

machine learning 3 no hast 1) supervised 2)unsupervised 3)reinforcement
    
supervised be do bakhsh taghsim mishe yeki classification and regression

ma yek dade darim ke x o y dare va donbale inim ke biaym rabeteye beyne
x o y ro dar biarim, khob model haye hoshe masnooe mitonan inkaro anjam bedan

hala ag y emon gosaste bashe behesh migim daste bandi (classification)
age y emon peyvaste bshe behesh migim regrasion (regression)

khob model ha mian in rabete ro ba yek thriki dar miaran va mitonan befahmanesh
va ma mitonim baraye decision makig (tasmim giri), puishbini , daste bandi
estefade konim.

hala fek kon modelemon omd yad grft in ro az ye tarighi, az koja bdonim rast mige?
khob migim in 10 ta datey ma masalan javabe khobi mide, ama khob cheghad motmaene
dar more dade haee ke nadide ? bayad berim yedone dota azmayesh begirim begim
bia ino pishbini kon abd ma k azmayesh grftim baham dg moghayesash konim.

vase hamin miaym hoshmandane migim agha ghabl az harchizi bia data mon ro
b do bakhsh taghsim konim yeki train dataset yeki test dataset.
modielemon biad faghat train dataset ro bebine yad begire rabete x o y ro

x e test dataset ro bhsh bdim yechizi pishbini kone (y_pred) bad biad ba
y_test moghayese kone va in mishe sanjeshe modelemon.


sade tarin halate yek hoshe masnoee :
    
    #vorode data.....................
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
x=x.reshape(-1,1)
y=iris.target

    #taghssim b test o train....................
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)


    #entekhabe model.........................
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=5)

    #fit krdn ya hamon train yani bre yad bgire
model.fit(x_train,y_train)

    #hala mirim score ro dr mairim
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('our train score is :',train_score)
print('our test score is :',test_score)



#dar nahayat ma yek train_score darim k mia dmige cheghad toneste azon data hae
ke dide , yad gerefte
va test_score oon data haee hast k nadide yani neshon mide cheghad khob model mitone
pishbini kone
banabarain bayad test_scvore va train_score hardosh bala bashe
ag test_score paeen bashe train_score bala bashe --> overfittin
ag train_score paeen abshe --> underfitting



fasele beyne pishbini shode ba dataye vaghe ei ro mitonim hezaran ravesh ahs k hesab krd

baraye regression masan , r2 , mse , mae, mape , rmse va .....



midonim k ma miomdim masalan 20% e nemone ro var midshtimo behehs migoftim in
test data sete, ama soale kheyli mohem --> masalan ma 10 ta data drim
mikhaym 2 tasho bzarim test , kodomasho bzrim ? dotaye akahrio?
dota avalio ? ya .....
ba train_test_split vaghty migoftim shuffle=True yani bhm briz random vr dar

ama yek chizi has bname cross_validation yani bia validation(sanjesh) ro cross kon
yani bia in data ro fek kon 5 ta lap tab dri
too yek laptab bia 2 taye aval ro az dah data test kon
too laptabe dovom doyta badi
....

va too har laptab model ro fit kon roo train bad test_score bgir

har laptab yek test score mide behet , miangine in test score haro bhsh mign
cross_validation_score ---> ba inkar sanjeshemon kheyli ghavi mishe
yani fght dota dade ro var ndshtim balke done done hame dade ha yek bar test shodan


baraye inkar kafie bnvisi
.........
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
x=x.reshape(-1,1)
y=iris.target
#in tyabe miad mige b chanta taghsim konam ? yni mgiim 5 tash kon
#yani 20% esho test vardar va khob engar 5 ta dade drim
#yani baraye modlemon, hey miad 20% e avalio test miokone test score
#bvad 20% e dovom ta ... 20% e akahr
#injori ma 5 ta test_score drim, mianginesh mishe cross_score
from sklearn.model_selection import KFold
fold=KFold(n_splits=5,shuffle=True,random_state=0)

#modeleto entekhab mikoni
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=5)

#niazi b fit krdn ndre balke x o y eto in zir mizari bva oon kfold ro inja mizari
from sklearn.model_selection import cross_val_score
cross=cross_val_score(model,x,y,cv=fold,scoring='neg_mean_absolute_error')
#in tabe miad x o y ro migire, bad mige chijori jodashon konm? cv=fold
#too fold oon bala nevehstim k bia 5 ta datash kon engar to harkodm 20% e sho vrdar
#bad maid mige khob man predict krdmo ba aslie khastam moghayese konam az che raveshi?
#raveshesho tooye scoring='neg_...' neveshtim
#banabarin yek array mide k 5 ta error toshe yani hamon 5 ta error k gfotm
#kafie bnvisim cross.mean() va in miangine kol ro mide
#*** inkar baraye sanjeshe model hast







#Khob nokteye asli in hast ke model ha yekseri setting daran bename hyperparameter
ya hamon fara parameter k baya dghabl az training va ghable modelling biaym behesh
bedim. va in hyperparameter ha tasir mizaran rooye yadgirie model va roye
test score o train score tasir drn va ma range e ziadi drim.


baraye inke befahmim kodom hyperparameter behtare, masalan KNN yechi dre bename
K--> k yani chnata hamsaye dar nazar bgire, baste be har data yek k i khobe
khob ma masalan mitonim bgim boro az k=1 bzar ta k=20 bbin kodom behtare va
ba in kar hey mire hey mire test mikone hey testo bar migrdone
ba inkar moghayese mikone kodom k , kamtarin test_score ro mide va mige bia in 
bhtrine

b in ka rmigan --> hyperparameter tuning ke ba tabeye gridsearch anjam mishe

#hala shoma mitonid mese raveshe aval train_test split konid bad biayd
#gridsearch bznid fght rooye yek test dataset
#ama kar ghashang inke ke az gridsearchCV estefade konid yani
#ham cross validation konid ham hyperparameter ro bsanjid


#gridsearch........................
#dade hatoon ro miarid
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
x=x.reshape(-1,1)
y=iris.target

#miayd migid cross validation chijori bashe, yani chijori taghsim b train test kone
from sklearn.model_selection import KFold
fold=KFold(n_splits=5,shuffle=True,random_state=0)


#Modeleton ro entekhab mikonid --> inja niazi nist setting bnvisid
from sklearn.neural_network import MLPRegressor
model=MLPRegressor(random_state=0)

# (10,10) | (10,10,10) | (100,)  | (4,4)
   

#oon setting haee k mikhyad bere begarde beyeneshon behtrino vardare ro minvisid
myparams={ 'hidden_layer_sizes'  : [(10,),(10,10),(20,)] ,
'activation':['relu','tanh','identity'],
'solver':['adam','sgd']}
 

#in tabeye zir az shoma model ro mifgire, miad az shoma modeletono mige bvad 
#ychizi bname param_grid yani kodom hyperparameter ha va dar ch rangi ro brm test konam
#mige chijori test dataseteto taghsim konm k shoma gfoti oon bala too fold nvshti
#hala mige chijori biad fasele ro hesab kone k too scoring goftin

   
from sklearn.model_selection import GridSearchCV
gs=GridSearchCV(model,param_grid=myparams,cv=fold,scoring='neg_mean_absolute_error')
    

#inja fit mikonid
gs.fit(x,y)

gs.best_params_ #in bht mige az beyen oan ek gfoti kodom bhtrine

#hala ba in bhtrin setting bhtrinm score chie
gs.best_score_

#dar asl shoma fek konid 5 ta data darid yani 5 ta x 5 ta y
#in maid 5 ta laptab dre
#yekish miad mige x1 ro mzirim test x2,3,4,5 ro mizrim train
#rooye train yad migire , ba 10 ta hyperparameter yani masalan k ro az 1 ta 10 mzire

#bad maid vase dovomin laptab miad x2 ro mizare test va rooye x1,3,4,5 yad migire 
#bad haminjori k ro az 1 ta 10 mizare

#bad dar akahr baraye harkodom az K (yani hyperparameter hamon) 5 ta test score dre
#ke miangine mishe cross_score --> harkodom paeen tar bashe yani oon hyperparameetr
#Behatrinnnneee











#------------------------------------------kheyliiii pishraftee (ekhtiari)
#nested cross validation..................................

#dar pichidide tarin halat --> balatarin impact haye momken
#migan bejaye inke datatono taghsim b test_train konid
#biayd tabdil konid b train , valid , test yani 3 ghesmat
#biad yad bgire az train, ba valid biad hey hypeparameter ro peyda kone
#behtarin hyperparameter ro k poedya krd biad rooye test besanje

from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
x=x.reshape(-1,1)
y=iris.target


#yeki baraye train,valid misazim esmesho mziarim fold1
#yeki batraye kole train+valid va test msiazim esmesho mziarim fold2

from sklearn.model_selection import KFold
fold1=KFold(n_splits=5,shuffle=True,random_state=0)
fold2=KFold(n_splits=6,shuffle=True,random_state=0)

#model
from sklearn.neural_network import MLPRegressor
model=MLPRegressor(random_state=0)
   

#oon setting haee k mikhyad bere begarde beyeneshon behtrino vardare ro minvisid
myparams={ 'hidden_layer_sizes'  : [(10,),(10,10),(20,)] ,
'activation':['relu','tanh','identity'],
'solver':['adam','sgd']}


from sklearn.model_selection import GridSearchCV
gs=GridSearchCV(model,param_grid=myparams,cv=fold1,scoring='neg_mean_absolute_error')
    

from sklearn.model_selection import cross_val_score
cross=cross_val_score(gs,x,y,cv=fold2,scoring='neg_mean_absolute_error')



#inja farghehs ine dr cross_val_score bejaye model omdim gs ro gozashtim



#chika rmikone ?

#masaln fek kon 6 ta data darim x1,2,3,4,5,6 va y1,2,3,4,5,6

#miad yek laptab drim masa;an
#miad fold2 mige 6 ghesmatesh kon hamaro yani yedone ro bardar vase test

#bad masalan too laptabe aval x1 ro be onvane test var midre

#hala beyne x2,3,4,5,6 fold1 miad mige az beyne ina yedone ro bzari valid
#masalan x2 ro mizare valid

#pas x3,4,5,6 mishe train

#miad rooye train yad migire , hey hytperparameter ro taghir mdie 
#hey valid ro pishbini mikone va moghayese mione va mibine kodom hypepramater
#balatarine va behtarine

#hala ke peyda krd miad kole model ro roye train+valid yani
#x2,3,4,5,6 train mide va x1 ro k az aval nadide bod (test) pishbini nahaee mikone

#hala soale aval ine chra dar avalin dore beyne x1,2,3,4,5,6 chera test ro x1 
vardashtim?? khob fold2 miad done done harkodom ro barmidare yani cross_validation mikone


#hala soale dovom/ vase harkodom masalan x1 ro test bar midarim az beyne x2,3,4,5,6
kodom ro valid bardarim? crossvalidation fold1 miad yekbar x2 avr mdiar eva .....


ba in kar dar asl 5*6=30 yani 30 bar model kardimmmmm---> kheyli pichidas


moafagh bashid

Alipilehvar1999@gmail.com
'''

