"""
IN THE NAME OF GOD

JALASE 12

@author: ALI PILEHVAR MEIBODY
3>2>1

"""

'''
python built in / keyword / dastoorat 
simple library --> datetime,math,cmth, random, statistics
numpy--> array , 
matplotlib--> plot 
pandas--->
'''

'''
review on matplotlib: how top read documentation
first search matplotllib on the google
mirim too site-->
https://matplotlib.org/

6 ta chizi dre , plot scatter va va va
'''

'''
file handling--chijori open konim
'''

#-----------
'''

pandas--> kar ba data (csv,excell)

'''
import numpy as np
import matplotlib.pyplot as plt



#yechizi dahstim bname list
a=list((1,2,3,4,5))
#numpy omad dota kar krd
#1-sorato bord bala gfo man 50 bareabar sari taram
#yani ychi drm bename array (araye) 50 barbara saritare 
#operating mohasebat .....

#dobodio se bodi


#se bodi--> vase yadgirie
#2D --> kh bekar miad
#chona ksare dathaaaa--> too azmayeshgah , too sanat , too business va va va
#2D--> yekseri radif dre (ina sample) #yekseri soton dre

a_list=list((30,40,50,60,70,80))
a_array=np.array([30,40,50,60,70,80])

#pandas gof khob 
#numpy > liste
#pandas omd gof man ychi bsazam bhtr az numpy bashe

#pandas > numpy > list
#gashtan donbale index baraye access skahyte

#[pasa chika rkonim? --> biaym label besazim
#ye oon sotone more nazar esm dashte bashe


#omad  moarefi krd
#Series
#list dashtim , Array dashtim , 
#hala drim bname Series


import pandas as pd
#aval k bayad improt krd va mokhafaf krd b pd
#sedash abyad zad pd
#noghte zad rft dakhel
#yek tabe bekeshim biron
#tamame tabe haye pandas horofe bozorg avaleshon dre **********
#yademon ham hast k python case sensetive has yani a ba A frgh dre

#Print #rngi nbmishe
print #rngi mishe

ali=4
Ali=6

#series=Series

#eshtebahhhhhhh************
#a_series=pd.series

a_series=pd.Series([30,40,50,60,70,80])



#moghayese in se ta----

a_list=list((30,40,50,60,70,80))
a_array=np.array([30,40,50,60,70,80])
a_series=pd.Series([3040,50,60,70,80])

,
#structure
#Series(data,index)
a_series=pd.Series([30,40,50,60,70,80],index=['a','b','c','DD','oon','akhari'])

#b che dard mikhore?


#bbin listo numpu mikhasi acces koni
#dovomio mikhasi

a_list[2] #Out[38]: 50
a_array[2] #Out[39]: 50

#hala fk kon 10000 ta index has 

a_series['akhari'] #Out[40]: 80
a_series['c'] #Out[41]: 50


#avalin chizi k sakht --> sereies ---> numppy 1D hast k indexash ma mitonim nam gozari konim

#assign
pd.Series([20,30,40],index=['ali','vahid','reza'])

#ye raveshe dg dare bename dict dictionary

#dictionary
#list []
#dict {}
calories_list=['day1','day2','day3']
calories = {"day1": 420, "day2": 380, "day3": 390}
#esme zarf = 



new=pd.Series([20,30,40],index=['ali','vahid','reza'])

new_dict={'ali':20 , 'vahid':30, 'reza':40}

#dict ro tbdl b serie

convertshode=pd.Series(new_dict)




#===========================
#kholase ye asli
#yechi dahstim bname list


#numpy , array ovord k sari tr bodo do bodi mishod


#pandas omd ychi ovord benaME Series k mitonesim b jaye index ha khodemon y chizi bzarim hala esm bashe adad

#2d?

#omd gof 
#ychizi drm bename DataFrame --> Serie 2  bodi


#********************************
#new=pd.DataFrame(data)

#mitoni dasti vared koni
#mitoni numpy, dictionary ya ...


a=np.array([[11,10],[12,20],[13,30],[14,40]])
b=pd.DataFrame(a)
b=pd.DataFrame(a,index=['a','b','c','d'])
#b=pd.DataFrame(a,label=['takane','dama'])

#yekare dg--> dictionary
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

c=pd.DataFrame(data)

c=pd.DataFrame(data,index=['data1','data22','data3'],columns=['ali','vali'])


#access-->
#BE oon radi brsi daghigh mes elisto
#list a[2]
#kasfie bnvisei esmeshpo va esme index

c['data1']


#2d
a2_array=np.array([[30,40,50,60,70,80],[5,6,7,8,9,10]])

a=pd.DataFrame([[10,20,30],[5,4,3],[1,2,3]]) 


#DataFrame hamon Numpy arraye e 2 bodi has
#fght indexo columns balash mitoni adad ya horof bzari




#yeki az rahaye moheme assign
data2 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

mydf=pd.DataFrame(data2)

mydf=pd.DataFrame(data2,index=['data1','data2','data3'])


#assign ro yd grftim
#baraye acces----

#mese list mese numpy
mydf[0] #KeyError: 0

mydf['data1'] #KeyError: 'data1'

#ina baraye numpy o list bood

mydf.loc['data1']
#calories    420
#duration     50
#Name: data1, dtype: int64


#agar indexat frgh nmikrd ham
mydf.loc[0]





#==================
#assigne value dastiiiiii
#ag yek file dahstim chi? masalan excell bashe ya ya ya


#ye formate kh kh mahboob --> csv
#aval openesh konid

#esme zarf mziri
mydf=pd.read
#inop k mizni harchi formate miare vbarat
import pandas as pd
mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')

mydf.dropna(0,inplace=True)

mydf.drop(columns='Duration',inplace=True)

#C:\\Users\\sunhouse\\Desktop\\data.csv

#az open estefadekoni b formate csav miad inja

#ama in pd.read_csv -->o oon csv ro mikone yek dataframe

type(mydf) #Out[71]: pandas.core.frame.DataFrame


print(mydf) #vaghty print bzni
#hamon csv file ro miare
#5 ta readife aval 5 ta radife akhar
#paenesham mige chanta radif dar chanta sotoon

#mian esme oon zarfi k zakhire krdno mizanan
#va chnta kar bahash mikonan

#analyse avalie
#mydf file e mane
mydf.head() #5 ta radife avalo
mydf.head(10) #10 taeo miare
mydf.tail()
mydf.tail(10)
#mhemtrin
mydf.info()

#4 ta column (soton drim)
#jolosh nvshte harkodom chanta non-null
#ma ba inkar mibinim k chanta sotonemon null hast ya nan hast
#null o nan yani kahli ya harhcizi --> naghs

#assign
#khodemon dasti midim
#dictionary
#liste --> series
#np array 
#file hast

a=np.array([[1,2,3],[4,5,6]])
b=pd.DataFrame(a,columns=['a','b','c'])

#dastresi
#dota dastresi
#ya mikhay b indexi brsi loc
b.loc[0]
#a    1
#b    2
#c    3
#Name: 0, dtype: int32

#age column sotonio mikham
#esme moteghayed yni dataframemon ye [] dakhelesh esme sotonm
b['a']
#0    1
#1    4
#Name: a, dtype: int32


#preprocesign --> ghable farayanad

#analys mikonim dataro

#--------initial analysis ( analize avalie )----------------------


#azinja bbad analyse nahaee -- DATA CLEANING - PAKSAZIE DATA-----------
#---DATA CLEANING-------
#hamishe datahmon baraye hsohe masnooe ya film ( nadeer) , ax 
#dataa ( hamon adad) --> formatesh chie? word, excell , csv(hjmishe)

#formatesh pas na array hast na pd hast na hichiii

#ama mitonim ba read_format --> tbdilesh konim bn dataframe

#aval initial analysis miznim

#naghs dr datahmon
#1-empty cfell ( khali bashe)
#2-wrong format
#3-wrong data 
#4-duplicated (tekrari)


#pas dar datahmon 4 ta naghs drim



#harja khali bashe moshkel dar convert open bashe 
#NAN= not a number

#ag bjaye str zade adsad -- wrong fromat

#baste b application , 

#wrong data
#masalan y kari mikonim bayad damaha hame beyne 20 ta 60 bashe

#ag jaee zade shode bashe 700 --> ghalate
#in ghalat shayd bkhtre dastgahe , nemname , kasi k type krde , convert , 
#mohem nis ressource manabe khata mohyem nis

#mohem ine ke yek naghsi dr data hast
#hala yki az in charta 1-empty cell (nan) 2-wrong format (bjaye str int)
#3-duplicated (tekrari has) 4-wrong data ( rangesh frgh mikone y aya)



#dr in soorat avalin akremon in bod k ba info mididm k chnta mpty drim

#deoone donne mikhaym brim bbinim chjikaresh konm

#-----empty cell------------------
#aval info miznim mibinim khob dare dg
#marhale1-bfhmim null darim ya na---> info
#marhale 2- agha asan fhmidim hala chikarwesh konim?

#hazdfesh konim?--ag are ok haazf kon
#ya replace konim? --bachi??

#hazf
#kole oon datframeto bnvisi

mydf.dropna(4) #yani drop kon na number
#ino bzni bayad savesh koni dakhele ye variable e dg

#ama vase rahati
mydf.dropna(inplace=True)
#miad rooye khode mydf emal
mydf.info() #baraye chek krdne

#az 169 ta row , 164 
#hgaashonam shdoan non-null

#be sadegii


#agha nmitonim rotye felan soton inakro konim?
#baraye hazf na********


#replace --> jaygozin kon --> ba chi? chi jahs bzrm?

#jaye tamoome null ha bia

mydf.info()

mydf.fillna(120) #ba in mitoni fill koni 
#tamame noghate khalio ba 120

#ama in khdoesh yek datfrsame e jadid mide emal nmishe

mydf.fillna(120,inplace=True)

mydf.info()
#hamon 160  ta radif monde ama 
#calories , 164 non -null boid alan shode 169 ta yani poresh krdim ma


#masalan fght yek sotono biad empty cell hasho por kone
mydf['Calories'].fillna(120,inplace=True)
mydf['Pulse'].fillna(200,inpalce=True)
#aval ino mzini b kjole soton dastresi peyda mikone


#overview: ya roo kole columnha yani kole dataframe harchi empty cell dre por koni
#y bgi felan soton felan adad felan...

#karhaye ghashngtar
#mean() / median() / mode()


x=mydf['Calories'].mean()
print(x) #368.22248520710065

mydf['Calories'].fillna(x,inplace=True)

#--------------

mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')


ffil_df=mydf.fillna(method='ffill')
bfill_df=mydf.fillna(method='bfill')

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
#method{‘backfill’, ‘bfill’, ‘ffill’, None}, default None
#Method to use for filling holes in reindexed Series:
#ffill: propagate last valid observation forward to next valid.
#backfill / bfill: use next valid observation to fill gap.


#-----------2wrong format
#str bashe bokonm int
#fek kon yek df drim 
#charta soton dre 1000 ta radif
#yeki az soton ha date hast
#bayad hame injori bnashan '2/6/8'
#ama bazia momkene 2/6/8 adad bashan na str

#minvisi
#avalk mirm toye sotonm
#pd.to yani ino hamashono in format kon
mydf['Date']=pd.to_datetim(mydf['Date'])

#ya hat miutoni az remove estefade koni
#in remove frgh dre

df.dropna(subset=['Date'], inplace = True)


#** tozih




#-----------
import sklearn




#-------QUIZ-----
#VOICE TROZIHESH

'''
bebinid bayad yek tabe besazid ke az taraf
file e csv bgire

yani aval biad ba dastoore zir oono tabdil kone be yek pd.DataFrame

name=pd.read_csv(input)


#badesh yekseri calculation anjam bde ( ya khodesh ya tahiresh bdid b numpy)


va sepas an ra nasb kone

hameye ina bayd dar yek tabe bashe 

mesal: azmayeshe tensile yek testi hast ke miad nemone ro mikeshe
va dar har stress , strain ro andaze giri mikone

nahayat yek file e csv mide ke

1000 ta radif hast k har radif do sotone yek soton strain , yek soton stress

tabeye zir file ro migire va monhanie stress-strain roi mikeshe

va yekser chizaro mananande modole young ham hesab mikone



'''

def Stress_Strain_Curve(input_file,which):
    '''
    This function is belonged to stress strain
    Parameters
    ----------
    input_file : .csv format
        the file must be inserted in csv.
    whcih : str
        please say which work we do ( plot or calculate?).

    '''
    #convert the file
    mydf=pd.read_csv(input_file)
    
    if which=='plot':
        #get the data on each columns
        stress=mydf['stress']
        strain=mydf['strain']
        
        #plotting data
        plt.plot(stress,strain)
        plt.title('stress-strain curve')
        plt.xlabel('stress')
        plt.ylabel('strain')
        plt.show()
    
    
    if which=='max stress':
        #calculat the stress_max
        stress_max=mydf['stress'].max()
        return stress_max

    if which=='young modul':
        #calculate young modul and .....
        return young_module
    
        
    










