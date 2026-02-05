"""
In the Name of the God
@author: Ali Pilehvar Meibody


#------Library documentation ****** Kh mohem

#ta alan ma numpy , random, math , time,statistics

#ama age bekhaym baghie ketabkhone haro yad bgirim chikar konim?


#mesle hamishe chan rah drim

1-esme keteaabkhone ro too google bznim --> google= numpy python
2-benevisim pip esme ketabkhone--> pypi.oprg miare mitonim hata too in site search bznim
3-too github search bznim---> hjaminjorie

az tarighe 3 site--> google/ pip / github mitonim
esme ketabkhone ya yek keyword kilidvazhe ee mortabet ro search bznim

ta inja mitonim dl konim ---> powershel--> (**havaset bashe too hamon environment)


pip---> bema pip ro mdie bsznim powershell kole ketabkhone dl mishe va install mishe ( hata version haye ghadimisham mitonim dasti dl konim)
github source--> kole oon file i k tooye pip bode ro code .py ro open-sore free mzire dastemon k dahste bashim


hjala ch tooye pip,github ch saite asli(google)--> kafie bzni documentation

documentation--> yani daSTOROLAMALESH , tutorial , instruction --> balad nisam

donbale--> Getting start begard va bzn roosh
documentation, user guid, beginner, getting start ( donbale ina bgrd too site e asli ya google)

harkodomo didi inaro zodtr boro toosh:
    
    absolute beginner > quickstart > user guid
    


#**** baraye downloade mostaghim
1-baraye verswion haye ghadimi--> tooye pip , relasse history , mizni ro oversioni k mikhya, file e .tar.gz ro dl mikoni
2-ya miri too khode sitesh, ghesmate download hamin file ro dl mikoni
3-too github
bad file ro copy kon bbr
user/admin/anaconda/env/ esme environmentet / Lib / Site-packages
inja pastesh kon



soal dashtan--> stack overflow
soaletono englisi bnvisid ya matne erro too consule ro copy paste konid



barname nevisi = 30% yadgirie cod / 40% tamrin / 30% nokate bala (documentation, search , stack overflow)


"""

import numpy as np

#bahash array miskahtim --> list
#assign
#0D
a=np.array((2))
#1D
a=np.array([1,2,3,4,5])

#2D
a=np.array([[1,2,3,4],[4,5,6,7]])


#chia dasht?
print(type(a)) #<class 'numpy.ndarray'>

print(a.ndim) #2 number of dimention

print(a.size) #tedade elementa yani chnta toshe 8

print(a.shape) #(2, 4)   #2 ta radif , 4 ta soton 

#hmishe vaal radife bad soton --> 2D 
#too 3d ==> avalk laye bad radif bad soton

#access -- []
#*** index az 0 shoro mishe az alan adsat kon bgo radife 0om

a=np.array([1,2,3,4,5])
a[0] #avali 1
a[4] #5




a=np.array([[1,2,3,4],[4,5,6,7]])
#kodom radif kodom soton [radif,soton]
#adade 4 kodome ? radifew 0 om , sotone 3 vom
a[0,3] #Out[10]: 4

#slicing -- [:] yanio chnta access
a=np.array([1,2,3,4,5])
a[0:2] #Out[13]: array([1, 2])
a[1:4] #Out[14]: array([2, 3, 4])


a=np.array([[1,2,3,4],[4,5,6,7]])
#[chanta radif,chanta sotonesh]
a[0:2,1:4]



#another way to assign 
#ag khastrim bgim az 1 ta 10 ro baramon bsaz chtor?



a=np.arange(10)
print(a) #[0 1 2 3 4 5 6 7 8 9] 
#vaghty y adad mziri mire az 0 ta yeki monde b on adado array mikone

#np.arange(start,end,step) az chant ta chant , chanta chanta brer(optional)

a=np.arange(0,6)
print(a) #[0 1 2 3 4 5]  end ro dr bar nmigire

a=np.arange(0,6,2)
print(a) #[0 2 4]

#ina k hamash 1 bodi bod ? chijori 2 bodish konim

#masaslan
a=np.arange(0,6)
print(a) #0,1,2,3,4,5
#mikham 0,1,2 bala bashe , 3,4,5 paeen
#aval bayad hesab koni --> 
#array jadid chanta radif dre chnta soton

#yani 2 ta radif dre va 3 ta soton ==> (2,3)

#esme oon araye ee k mikhgay reshape esh koni ro seda mzini

a.reshape(2,3)
#zadam roo a taghir nkrd ??
#dar asl in emal nmikone balke pas mide

b=a.reshape(2,3)

#ya ag bkhaym shabihe emal nbashe yani zarf kasif nakoni
a=a.reshape(2,3)

#EMAL CHI BOD YADAM RF
a=list((1,2,3,4))
a.append(5)
print(a) #[1, 2, 3, 4, 5]
#ma chizi zakhire nkrdim k too zrfi chra injori shod ?
#a taghir krd chra ?? chon in tabe emal mishe pas nmide

#ag zadi out dad ya too zrf rikh yani emal mishe
b=a.append(5)
#b=Nonetype ---> yani emal mishe chizi pas nmide


#change------
#kafie access konim va taghirewsh bdim
arr = np.array([1, 2, 3, 4, 5])
arr[0]=42 #(42,2,3,4,5)





#noktye ye dg copy view
#ama 
arr = np.array([1, 2, 3, 4, 5])
arr2=arr
arr[0]=42
print(arr) #[42  2  3  4  5]
print(arr2) #[42  2  3  4  5]
#vaghty mosavi mziri har taghiri emal bshe roo onytekiam mishe

arr = np.array([1, 2, 3, 4, 5])
arr2=arr.view()
arr[0]=42
print(arr) #[42  2  3  4  5]
print(arr2)


#agar nmikhaymmm taghgirat emal bshe
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0]=42
print(arr) #[42  2  3  4  5]
print(x) #[1 2 3 4 5]
#yani .copy() miad ye copy migirer va hgarkari ba aslie bokoni kari ndre

#yechi dg dare bename -1 reshape
a=np.array([1,2,3,4,5,6])
#mikham bgm boro 2 ta radif kon
#hosele ndrm beshmorm bbinm dota radif chnta soton mishe
#fghht mikham bgm do radifash kon
#rahakr= n-1
b=a.reshape(2,-1)
#ya barax
c=a.reshape(-1,2)



#iterating and loop i access in the ndrray
#agha mikham bbinm for chie --> bazrresi --> peymayesh

a=np.array([1,2,3,4,5])

for i in a:
    print(i)
#1
#2
#3
#4
#5
#yani mire tooye array done done ro mikeshe biron
#hala harkari dri anjam bdi ro too bopdy bnvis

#masan mikham bre chek kone hrkodom 4 hasto bokpone 8

a=np.array([1,2,3,4,5])


a=np.array([1,6,6,3,4])

for i in a:
    if i==4:
        print(i)
        
        
        
        
print(a) #[1 2 3 4 8]


#rahe hal printe
a=np.array([1,2,3,4,5])

for i in a:
    if i==4:
        i=8

a=np.array([1,2,3,4,5])

for i in a:
    if i==4:
        i=8
        
#2 ta rahkar
a=np.array([1,2,3,4,5])

for i in a:
    if i==4:
        a[i-1]=8
     
        
     
a=np.array([1,2,6,4,5])

#az rahe dovom





for i in range(0,len(a)):
    if a[i]==4:
        a[i]=8

print(a) #[1 2 6 8 5]

#shomarande ba element overlapp nakone



arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)
 
#baraye do bodi ha injori access mikonim

for x in arr:
  for y in x:
    print(y)


#hala ag bkhaym bgim random bsaz bramon chi?
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

#goftm 1 bodi dorose mizni rosh sotonie yama yek rradife
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2),axis=0)
print(arr)

#axis=0 hamon defaulte 


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2),axis=1)
print(arr)
#AxisError: axis 1 is out of bounds for array of dimension 1


#---baraye dobodi ha
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)

print(arr)
#concat k mizni dota ardif ro dar toole ham michasbone
#man mikham roye ham bndazatesh
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


#ravesh haye dg
#axis== dar toole ham ya na

#baraye 1 bodiconcat nmitone kari kone ama alan mitone

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=0)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)





#---split

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

#miad yek array ro tabdil mikone be chand array

#hala bkhay6n dastresi peyda konid
#soal bporsid===> chandomin array ro mikham?
#masaalan set atagsim krd, kodomo mikham? avalio ? dovomip?

newarr[0] #Out[69]: array([1, 2])





#===========
#yadfetone man for zdm k yechizio masalan peytda konm?
#--where
arr = np.array([1344, 2434, 34, 34432, 534, 423, 41])

x = np.where(arr == 1344)

print(x) #(array([0], dtype=int64),)
#yani mige injdexe 0 adadi k mikhay


arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x) #(array([3, 5, 6], dtype=int64),)

#yek arrayi mide
#toosh index ro mige k kodom index ha
#oon chizi k madn made nazarame ro dre


#mitonid sharto avaz konid --> masalan kodom zoje
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x) #(array([1, 3, 5, 7], dtype=int64),)



#=============
#sort
#ke miad 
#az 0 - .... 
#az A - Z a - z
#moratab

arr = np.array([3, 2, 0, 1])
np.sort(arr)
#pas mdie yani bas zakhire konim sort ro


print(np.sort(arr))
#[0 1 2 3]




arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr)) #['apple' 'banana' 'cherry']



arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))


#filter
#yani bgim yseriaro bardar ysreia ro brndre

arr = np.array([41, 42, 43, 44])

#baayd ye x i bsazim
#xze toosh chie? True False 
#badan migim treu haro brdar falsarpo bdnaz dor

x = [True, False, True, False]

#structure:
newarr = arr[x]

print(newarr) #[41 43]


#yani ma bshinim done done bgim kodoma true ? na shart bzar
#masalan mikhay bgi zoj haro negah dar

arr = np.array([1, 2, 3, 4, 5, 6, 7])
#ag tolani bashe cdhi?

filter_arr=[]

for element in arr:
    if element%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
print(filter_arr)  
#[False, True, False, True, False, True, False]
#structure:
    #new_array= hamon_array[liste filterr]
    
newarr = arr[filter_arr]
print(newarr)
#[2 4 6]




#arrange ro?
#ag kkhastim random bsazim chi?
#yanji yek array bsazim toosho az wadade random por konim
#flash back <----
import random
x=random.random()
print(x)
#yeki adady beyne 0 ta 1 reandom mide

#ag mikhasam baze bdm
x=random.randint(1,8)


#numpyu mige bia man hamino drm
#bja yek adad yek arraye ro por mikonmn barat az adade random


x=np.random.rand()
print(x)
#in hamoone


x=np.random.randint(100)
print(x)


#hala k frghi nkrd?
#size

#yani y array mikhay bsaZI BBIN CHANTA RADIF CHNTA SOTON
#(RADIF,SOTON)

x=np.random.randint(100,size=(2,3))

#fght int hastan
#float mikham
#rand beyne 0 1 mide
#randint range dre


x=np.random.rand(5) #in yek numpyy mide 5 sizeshe
x=np.random.rand(3,4)


#+ - *2
#=================quiz====================

#yek file e python b esme khodeton minvi9sid
#5 ta numpy array misazid ham 1 bodi ham 2 bodi ham 3 bodi bashe

#rooshon tamame tabe haee k emroz gofte shod ro tamrin bznid
#nahayat bshe 40,50 khat
#ta charshanbe........

#dar akahr rasmesh konim
#importesh konid ya brid pip instal konid
#matplotlib
#tooye powrshel ( hamon environment)

#pip install matplotlib

import matplotlib.pyplot as plt


x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,6,7,10,13,16,18,20,43]


plt.plot(x,y)


#hala x va y mitone array ham bashe
#array haee k 40,50 khat bahash tamrin zadido rasm konid









