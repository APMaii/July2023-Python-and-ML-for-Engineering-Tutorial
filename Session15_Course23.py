# -*- coding: utf-8 -*-
"""
In the name of GOD

**15**
@author: Ali Pilehvar Meibody

"""
#copy paste az jalase ghabl (14)
#chooon kheyli mohemeee...

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
               
               
#*** azinja bbad ro sklearn yek folder dare bename dataets mitoni data load koni

               
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


#raveshe LR --> Linear regression

#1- chantaa a o b hads mzid
#hey khat haye y=a*x+b ro mikshid
#miomd fadsele noghte haro (datamjono) ba in khat hesab mikrd --> cost function
#az beyen khat ha harkodom cost functione e kami dasht varesh midasht (optimization)
#migof in khate nahaeie mane Y=alpha*x + beta
#yani x bde behem man bht ba in formol y midam
#Khob ino omdn too ye shekrkati bename scikit learen --> sklearn

#in esme tabamone
#ye x o y vorodi migire (datae)--> aziin mikhad yad bgire
def linearregression(x,y):
    
    #200 ta khat misaze
    for i in range(0,200):
        a=np.random() #rndom as misaze
        b=np.random() #rndom b misaze
        #yy=a*xx+b #khatesh baraye harkodom az oon 200 khjat ha
        
    #miad mohasdebe mikone 
    #x haro mizre too in khate yy va miad moghayese mikone ba y 
    #yani noghat ro faseelashono ta oon khatre hesab mikone
    
    #yekseri cost function drim ehtemalan mirize tooye yek list
    #cost_function_list.append(cost_frunction)
    
    #min_cost=min(cost_function_list)
    
    #miad a o b isho vr midre
    
    return #(mige man in a o b ie nahaeime )


#sk learn miad in tabe ro mzire tooye ketabkhonash mige sedam bzn

from sklearn.linear_model import LinearRegression


#kare yek motekhasese hoshe masnoeeie dar algorithme sklearn

#==================================
#first note.......
#tamame dade ha bayad 3 marhaleye aval ejra bshe ama maa
#az sklearn esteafde mikonim
#sklearn yek dataseti dareke miad yek dataye khobo tartamiz
#bemaaaa tahvil mide (ytani bad az marhaleye sevom)




#........... 5 ta model (LR,KNN,DT,RF,SVM).......
#in model ha vase chian ? beehsh migan supervised
#yani ag yemon gosaste bashe --> classificatione masale
#be in model ha migan model classfire --> KNNclassfier

#ag peyvaste bashe ---> migan be masale regression
#b model ha migan KNNregressor


#==========================================================================
#==========================================================================
#==========================================================================
#==========================================================================
#==========================================================================
#==========================================================================

#-----------mesalemono az golhaye IRIS shoroo kon --> sklearn yek data dre be in nam

#mesal chie?
#yek fardi rfte 150 ta gol ro kande ovorde khoone
#pas 150 ta gol drim doone gol 
#in gol ha yekseri golbarg daran yekseri saghe drn 
#hala ham golbarg ham, saghe yekseri tool dre yekseri arz
#pas baraye har gol mitonim 4 tra feature ya vizhegi dr nzr bgirim

#toole golbarg, arze golbarg / toole saghe , arze saghe
#x1,x2,x3,x4

#150 ta radif dre 4 ta soton
#150 ta gol dshtim harkodom 4 vizhegisho nvshtim

#ye y ro ham misazim--->
#kole ina az 3 no tashkil shode avokia, rotsdheld , kalifari
#agha esm sakhte nmifhmam --> A B C --> 1 2 3 frghi mikone mage


#aghaye giahshenas lotdf kon joloye har gol bzn bgo kodom 1 e ya 2 e ya 3


#minvise o mdie behem

#datae k drm chie ?

#150 ta gole 4 ta vizehegi baraye hargol(golbargo sagahsh) va jolosham ye soton k che golie 

#150 ta radif dre , 5 ta soiton k 4 tash x an 1 ish y e


#age ye machin bshe behehs ino bdim yad bgire , badan mitonim y gol nbgirim behsh
#moshakahste in 4 taro ( arz o tole golbargo saghasho bgirim) bdim b in mashin
#mashin bma bge agha in ghole 1 2 3 


#classification......
#data ro az koja biari
#1-ag khodm sakhte bodm yani man moshtaghe gol --> excelesh bas moikrdm
#importesdh mikrdm ba read_csv bad preprocesing bad taghsim b x o y yeksrish too
#vizhegi ha yekseri ....
#2-sklearn omde hamin 3 marghalkaro anjam dade va gofte bia az in data estefade kon



#sklearn yek folder dare bename datsets k koli nemone dare****

from sklearn.datasets import load_iris
#yani boro az ketabkhoneye sklearn , madule (script) e datasets
#tabeye load_iris ro bde

#in yek tabas yani laod miokone pas yek khoroji dre bema data khgoroji 

#ye zarf msiazam bname iris
iris=load_iris()

#chiash mkoheme? #1- data featurenames 2-target target names

iris.feature_names
#['sepal length (cm)',
# 'sepal width (cm)',
# 'petal length (cm)',
# 'petal width (cm)']

iris.target_names
#array(['setosa', 'versicolor', 'virginica'], dtype='<U10')



x=iris.data
y=iris.target


#ch dataset import koni az sklearn ch khodet bayad
#dar nahayat yek x o y dashte bashi (marhale 3)

#pas in datamone ke mikhyam kar konim ( 3 marhale ro rftim)
#hooshe masnooe kolesh --> datmaono preprocess krdim
#omdim tabdilesh krdim b yek zarf x va yek zarf y

#split_train_test --> aval yekseriaro brizim yja test yeseriaro train
#rooyeseria bnamet train yad bgrie badan bbinim testaro doros pishbini mikone ya na

#chijori split konim? khode sklearn man ye3k tabe drm tabamo az dele ketabkhonam bekesh biropn

from sklearn.model_selection import train_test_split

#a=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)

#model selection
#hala vaghteshe brim rooye train dataset --> oonaee kmikhaym roosh train bbinemodel
#model ro fit konim , soal? ch modeli??--> 5 ta model drim
#1-lr , 2-knn , 3-dt, 4-rf, 5-svm
#alan #1-lr
#chijori b mdoel dast resi peyda konim
#model chiakr mikrd? y thricki mizad az x o y yad migrft
#uye tabe hast k x o y ro migire train mibine (class)

from sklearn.linear_model import LogisticRegression

#aval y zrf bsaz bname model
#chra mirizim too zrf va mostaghim estefade nmikonim?
#1- chon ziad estefade mikonimm esmesh toolanie 
#2- yekseri setting dre shayad bkhaym avazesh konim nmitonim hey seda bzni
#hey tosh setting bchini

model=LogisticRegression()

#ychizi drim bname model hamon box 

#1-fit mikonim rooye training dataset 
model.fit(x_train,y_train) #training
#vaghty in omd:Out[58]: LogisticRegression() yani tamom shod yad grf
#yani moadele ro drovord

#mitoni harchi mikhay predict koni tamom

#
import numpy as np
new_gol=np.array([6.2,2.4,4.1,1]).reshape(1,-1)

y_gol=model.predict(new_gol)
print(y_gol) #[1] omdf gof goel 1 e in chizi k kandii....

#sadegii

#soal mikone--> agha az koja man bdonm ras migire ???

#bahse evaluatriopn miad vasat...... score , metric , sanjeshe model
#yadete x_test y_test dashtim , estefade ee azash nkrdim ke ????

test_score=model.score(x_test,y_test)
print(test_score) #1.0
#hamaro doros gof

#scdore agha in chijroi hesab krde
#faseleye noghate pishbini shdoe ro ba noghate avgeh ei ro chijori hesab krde ?



#========================
#accuracy == chan dasrad doroste ? 1 --> 30 taee kd adim bhshsh , 30 taro doros pishbini krd

y_predicted=model.predict(x_test)
#yani x haye oon dadeye test ro ddim b model goftim [sshbini kon
#bema y e pishbini shode ro dad

#bachi moghayesash koni?

#ba y_real y_true y_test

#pas baayd dar asl y+predicted - y_test

#in menha mitone hezaran no bashe 

from sklearn.metrics import accuracy_score

test_score=accuracy_score(y_test,y_predicted)
print(test_score) #1.0

#dar asl bjaye inke inhame kar konm sklearn khodesh anjam mide



#lkare paeni hamon kare baaleie
test_score=model.score(x_test,y_test)
print(test_score) #1.0

#chra khob balaeeie ro yad di

#chon tabeye score fght yejor mire fadsele ro dr miare
#sahayd ma bkhaym az sanjesh haye dg estefade konim



#bbin fk komn az 30 ta 10 tash ghalaty bashe
#vaghty accuracy --> 20 ta doros bode --> 20/30= 0.66 doroste

#dade haye saratani ro ydt bashe
#dota javab ya saratn dre 1 ya ndre 0
#30 --> 10 ta ghalat pishbini krde --> aya inke ch ghalatie moheme? are moheme

#do no ghalat momkene biofte-->
#1- sarartand dare trf ama mige saratan ndre
#2- saratan ndre ama mige saratan dare




y_predicted=model.predict(x_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predicted)



#----------------
y_predicted=model.predict(x_test)
from sklearn.metrics import f1_score
f1_score(y_test,y_predicted,average='micro')


#dr ghesmate evaluationa kamel bhsh miopardazim




#yadete goftm **************
#2 ta score dirm?
#yeki vase training yeki vase test


#ykish train_score yani onae k dide ro chghd fassele dre
#yani nshon midad chghd yad grfteeeee



#yki ham dashtim test _score yanbi onae k nadide --> pishbinio nshon midad



#bayad train_score , test_score bad tahlil koni
#ag train_score paeen basshe --> underfitting--> yad ngrft ekhgob
#ag train_scorre kh bala bashe --> test_score biad paeen-->overrfitiing -->biased --> taasobi rfte genralization 

#bhtrin--> ham train score ham test score bala bashe

#--------------------kole kar ine----------
#1-Logistic regresion-------------------
#----load data
from sklearn.datasets import load_iris
iris=load_iris()
#----taghsim b x o y 
x=iris.data
y=iris.target
#----taghsim b train o test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)

#entekahbe model
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

#train va fit midimesh rooye trainingemon
model.fit(x_train,y_train)


#evaluation
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)

print('our train score is :',train_score)
print('our test score is :',test_score)

#our train score is : 0.9666666666666667
#our test score is : 1.0

#tmam --> tahlil --> mige man 150 ta gol bod 120 ta training
#30 taro gozshtim nabine

#Mige az in 120 ta k dadi bhm man modelam mitone holohoshe 96% eshono doros bege
#azoon 30 tae k ndidam --> 30 tasho doros goftm
#pas x_train balast ham x_test --> mdoelemon awlie
#inja accuracy ro bhmon gfote harfi az
#deghato sehatpo ina nazade ag bkhaym bayad x_test haro
#pishbini konim va bzarim too oon formol


#yek new x bssazam
#---pishbini
x_new=np.array([6,2,3,1]).reshape(-1,1)
y_new=model.predict(x_new)

#+ rasm jolo mire


#hrchi goftim modele LR bood
#modele KNN, DT , RF , SVM frgheshon fght onjas k 
#bjaye moidel on mdoelo mizrim
#hjmchi yeksane
#==============================================
#------------KNN----------------------
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)
#**fght inja frgh dre ke model ro esme on modelemon mzirim

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=5)

model.fit(x_train,y_train)
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('our train score is :',train_score)
print('our test score is :',test_score)
#ag k=1
#our train score is : 1.0
#our test score is : 1.0

#ag k=10
#our train score is : 0.9666666666666667
#our test score is : 1.0

#k=20
#our train score is : 0.95
#our test score is : 1.0

#k ag kheyli kam bashe --> modelemon kh sade ishe shayad ppishbinish khob dr nayad
#ag k kh ziad bashe --> kh biased mishe --> kh piochide model --> test 
#yechizi beyne hamon 4,5


#x_new=np.array([6,2,3,1]).reshape(-1,1)
#y_new=model.predict(x_new)


#1-----ravesho goftm 
#moshekle model --> complexity bala banabarin 
#test score momkene biad paeen 
#bishtar baraye classsification khobe
#kh cost computational --> tool mikshe 


#yekseri setting dare
#mohemtrinesh n_neighboure --> 
#**** n_neighbour yani chanta hamsaye


# az halghe for estefade kon **gridsearch 


#==============================================
#------------DT----------------------
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)
#**fght inja frgh dre ke model ro esme on modelemon mzirim

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(max_depth=3)

model.fit(x_train,y_train)
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('our train score is :',train_score)
print('our test score is :',test_score)
x_new=np.array([6,2,3,1]).reshape(-1,1)
y_new=model.predict(x_new)

#max depth ro taghir midid vba mibinid kodom bhtre


#complexity

#hartchi omgh bre bala --> hey dare sakht gir trmishe hey dre complex 
#nesbat b dataye ma shayad in khob bashe
#shaya din baES bshe bias bshe yani moteaseb bshe natone predict kone

#mohmtrina........
#max_depth
#min_samples_split
#max_features

#vizhegie in method....
#kh kh khobe baraye classfication ama baraye refgression
#beshedat complex mishe yani bshdt biased 
#tewst_scoee .... 0---> train khob mibine
#kh khgob masalan nazdik b 1 

#test --> 0.3

#yni rfte noise haram yad grfte 

#averag egiri --> 30 ta derkahte--> noise e hazf mishe
#generalization ---> tamim
#



#==============================================
#------------RF----------------------
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)
#**fght inja frgh dre ke model ro esme on modelemon mzirim

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=20)

model.fit(x_train,y_train)
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('our train score is :',train_score)
print('our test score is :',test_score)
x_new=np.array([6,2,3,1]).reshape(-1,1)
y_new=model.predict(x_new)

#computational cost



#==============================================
#------------SVM----------------------
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)
#**fght inja frgh dre ke model ro esme on modelemon mzirim

from sklearn.svm import SVC
model=SVC()

model.fit(x_train,y_train)
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('our train score is :',train_score)
print('our test score is :',test_score)
x_new=np.array([6,2,3,1]).reshape(-1,1)
y_new=model.predict(x_new)


#kernel

#kernel = linear ---> yani ehtemalan khatie rbaeye x  o y
#kernel = poly ----> gheyre khatie --> degree -->
#kernel rbf

#C ---> control mikone yad girisho yanio harchi bsihtr bSHE BISHTRR YD MIGIRE

#bazi jaha naiz ndrim kh kh yad bgire baya dholo hosh miangin yad bgire

#ma hamashono hey test mikonim




#---kole ravesh yeksane
#1-impoorte dtaa
#2-taghsim b x o y
#3- split b train o test
#4-entekhabe model ( 5 model)
#5- fit krdn rooye train ha
#6- score test o train ro migirim va moghayese mikonim 


#in  5 model rabete x o y ro ba ye thrick yd migiran 
#ma vase classficiation ( yani vcaght y goisaste hast )
#jalase badi regression ro yad midim




#-------baraye alaghe mandan----------------- 


#az sklearn az madule e datasets
#tabeye load_breast_canser ro miarim biron
from sklearn.datasets import load_breast_cancer
#mirizimesh too ye zarf bname cancer

cancer=load_breast_cancer()
#in data omade az 569 ta bimar data grfte
#har bimar 30 ta parametr az azameysheshon ro nvshte

#bad joloye har bimar neveshte 0 ya 1
#ag 0 bashe yani malignant yani badkhim
#ag 1 bashe yani bengin yani khosh khim

#in esme 30 ta vizhegi ro miare
cancer.feature_names

#in nshon mide 0 yani chi 1 yani chi too y ha
cancer.target_names


#khob haala bayad inkararo koni
#b x o y brizidishon
#bad train o test jodashon konid
#bad model entekhab konid
#bad fit konid
#bad test_score va train_score ro hesab konid
#hala vaghty model entekhab krdid 
#hey setting ro taghir bdid

#soali bood email bznid
#Moafagh bashid
#Alipilehvar1999@gmail.com
#ai.course22.alipilehvar@gmail.com



#hamchenin datahaye dg k mitonid estefade konid
#baraye classification

#dar mroede daste bandie nooshidani ha hast
from sklearn.datasets import load_wine

#darmorede dastkhat hast k kheyli sakhte....
from sklearn.datasets import load_digits






