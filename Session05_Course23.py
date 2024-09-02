"""
jalase 5
جلسه پنجم

"""
#numbers --> int,float,complex
#variable ha ro yad grftim
#assign mikrdim ( zarfo dakhele zarfo)
#badesh goftim chid rim built in function
type() #type
#casting= taghire type ya assign
int()
float()
str()
#size ya andaze
len()
#yekseri hayati
print()
input()
#khob ysri kar mikrdn
#kolan built ijn function ha ke narenjian
#minevisimeshon yek parantez dre
#tooye parantez value (variablke) ro mizarim
#ba comma mitonim variable haye dg ro bzrim
#va dar akahr yekseri setting ro tanzim konim

#numbers(int,fdloat-------------------------------------

#operator drim baraye number ha
#= + - * / % moghayese == < > <= =! / 
#baraye number ha bodan ( ama str ham estefade mishe)
#class= type
#har class masan int baraye kar krdn bahashon
#operatoir ke bala goftim baraye number
#method drim baraye har class

#buil in functiona baraye hame clasi ok bod anjam midad
#ama metyyhod ha fght mokhtas b yek noi class hastan

#str-------------------------------------
#assin a='ali'
#method--> 
#frgheshon ba buil in . rooye value ya variable
#noghte mizaznim va esme tabe va setting dakehel parantez


print(a,b,end='')
a='ali'
a.split('*')


#list----------------------
#koli variable ( az type haye ghabli) toshon jamishod
#assign
a=[232132,21,213]
#hame type i migire
a=list((1,2,3)) #dotaparantez
#methodsasho
a.append('salam')
a.insert()
a.pop()
a.remove()

#ma mitonim hata liste khali bzrim
a=[] #liste khali

#*** dar buil in function ha
#vaghty python az bala b paeen chap b rast mikhone
#fght ejra mikone

#dar method ha miad
#rooye oon variable ke samte rastesh noghte gozashtim
#yani masalan name dr mesale paeeni
name.
#miad roosh taghir ijad mikone


firstlist=[1,2,3,4]
firstlist.append(6)




#yad ddim
#index ha bod
#index yani ja, neshan gozari , dastresi , access
#ijndex yuadmon basdhe az 0 shoro mishe

#rooye name e variable miznim

name='amirali'
name[0] #a
name[1] #m
name[2]='k' #'str' object does not support item assignment

#vaghty run mishe miad fght ye khoroji mide
#Out[3]: 'a'
#save nmishe fght namayesh mide

#save mikhay koni?

horof=name[0]


name[0:4] #'amir'
#oon adad akahrie shamel nmishe
#0,1,2,3

name[:4] #az sef(ebteda)
name[4:] #ta akhar

#set touple dictionary
#frgheshon ba list ine yekseria
#duplicated ( tekrari) nmigire
#yteseria taghir pazir nistan\
firstlisy=['a','a','b']


#kolan tooo hameye type ha chi yadf grftim dr paeen kholase mishe
#yni int, float, str,list and....
#------------------------
#1-assign -------------
#name=be sotate khas dakhele zarf value mirizim
number=4 #fght adad
reshte='sss' #qout
listt=[2,43] #berucket
#ya az raveshe casting
a=list((23,3,4))

#2-access---------
#access=index
#vase iterable ha= yani yechi mese reshtan
#az chanta characteri horofi elementi chizi tashkil shodn
name='salam'
namelist=[1,4,65,2,56]
name[0] #b avalin element dast resi drid

#3-change------------
#kole zarfo mishe avaz krd hame ja
name1='ali'

#kafie fght dobrer bnvisid
name1='amirhossein'
#too list hrchiii
#k hata ravesh haye remove o ....

#chang e element (ajzaaa) important
#too str nadre
#too list mikhaym ye lement ro tyaghir bdim
#masalan user ha
#chan ravsh dre
#sade trin=
#aval acces konim step2, bad change
namelist=['user_a','user_b','user_c']

namelist[1]='user_new'
print(namelist) #['user_a', 'user_new', 'user_c']
#insert
#ina methode dg
#ke ina emal mishe rooye list
namelist.insert(2,'ali')

#4-add-----------------
namelist.append('ali')

#5-remove---------
del 
#ya az methodha
namelist.pop(2)
namelist.remove()
namelist.clear()
#**khali krdn ba remove krdn frgh dre

#va mimone yekseri method ha....
#masalan replace,upper,....

#pas in shod hameye type va class az variable ha
#va kar krdn bahashon
#sort krdn , reverse krdn 

#ejra va emal------
#copy krdne
name1='ali'
name2=name1
name1=name1+'pilehvar'
print(name1) #alipilehvar
print(name2) #ali



list1=[1,2,3]
list2=list1
list1.append(4)
print(list1)
print(list2) #[1, 2, 3, 4]

#dar list ha harchi copy mikonid
#ta be in manie ke
#list1 vba list 2 ta abad yeksane

#automat har taghiri rooye list1 biad roo list2 ham maid
list1=[1,2,3]
list2=list1.copy()
list1.append(4)
print(list1) #[1, 2, 3, 4]
print(list2) #[1, 2, 3]

#ooni k ma made nzrmon bod baraye str o ,...

#ba copy( ) ok mishe
list1.append() #mige man fghr emal mishjam rooye list1 hamin
#chizi tahvil nmidm man yek emalam hamin
name.upper() #man tahvil midm emal nmishm
#emal mikonm rooye name ama taghiri ijad nmikonm
#dar asl oon taghiro behet tahvil midm to savesh kon
list1.copy() #copy tahvil dde mese str

#-----+___mohmtrin variabl haro
#--------------IF------------------------
if swhart:
    dastoor
    #aval if, bad shart bad donoghte
    #bad enter--> fasle bayad rayat shr
    #dastooremon ro mizrim
    #az dastor khstim biaym biron enter barmigrdim
#too shart az comparison operator estefade mikonim

a=50
if a==50:
print('ok')
#IndentationError: expected an indented block
a=50

if a==50:
    print('ok')
    #ta kojua??
    #tav vaghty dar in faslee gir oftade
    print('next')
    print(4)
    
       
print('hello') #asan kari b if ndre
#vaghty fasele hazf mishe dg if o ina dr kar nis
#mishe mamoli
a=50
if a==50:
    print('ok')
#out=ok

a=40
if a==50:
    print('ok')
#out= hichiiiiii

#choon dakhele shart true nshode
#yani jzovge shart nis
#hala ag bkhaym bgim onaee k too shrrt nistan felan kro konan
#else
a=40
if a==50:
    print('yes')
else:
    print('no')
    


#***else maid zire if va donoghte migire
#dastooresh miad yek fasele
a=40
if a==50:
    print('yes')
elif a==40:
    print('no')

#imagination: joloye if vaysadid vba migid
#koln dorahi dorost mikonid mese derakht
#while ya for
#halghe chie?
#yek shomarande dre k bas bgim chande ? masan 0 masan1
#starte shomarande
#miad yek end mizrim brash yani ta koja bshmor masan 10
#miad az 0 ta 10 : 0,1,2,3,4,5,6,7,8,9,10
#hey i=0 , i=1 bd i=2
#va dastoore paeen ro ejra mikone

for i in range(0,10):
    print('salam')
    
    
#for ke dastoore
#i yek shomarandas
#in ham yani dar in range
#range ham maid az start ta yeki monde be end misaze masalan 0,1,2,3,4,5,6,7,8,9 shod dah ta
#subject= i b ch drdi mikhor?
for i in range(0,10):
    print(i)
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

#javabe quiz

password=input('passeton chie:')
len_pass=len(password)
for i in range(0,len_pass):
    print('*')
#*
#*
#*
print(1)
print(2)
#1
#2
#chra 1 2
#choon ye settingi has bename /n
print(1,end='')
print(2,end='')
#12

for i in range(0,len_pass):
    print('*',end='')
    
#***

for i in range(0,len(input('passet chie:'))):
    print('*',end='')
    
for i in password:
    print('*',end='')
    #tooye password
#passwodrdemon chie? 356 
#khob mige fk kon yek reshtas
#baraye har I ee k dar password hasd
#yani 356 mitonimk bgim masalan 3 ta harfe
# yani 3 ta i 
#miad az 0,1,2

#or i in password=for i in range(0,len(password)):

#i chie???
name='ali'
#yek str hast
name[0] #a
name[1]#l
name[2]#i

for i in name:
    
#yani name cheghadre andazash? mige 3 ta element ali a l i
#i ro miad az 0 ta 3 0,1,2 
#i in name= i in range(0,len(name))

#b ezaye se ta chikar konm?
name[i] #NameError: name 'i' is not defined
i=0
name[i] #=name[0]=a

for i in name:
    name[i]
#mige baraye harchi element dar name hast i bzar rangesho
#darf name ali drim seta elemente a l i
#miad i ro az a,l,i mizre hey tekraer mikone ynichi
#yni mige i=a khate paeren ejra mishe
#bad mige i=l khate paeen ejra mishe
#i=i khate paeen ejra mishye
#maid biron

for i in name:
    print(i)
    
#aval mikhone mige yani baraye i haee k dar name hast
#name 3 ta hast yani i az 0,1,2 ejra konm
#i=0 mizre mige name[0]=a print mikone
#i=1 mizr emige name[1]=l
#i 
#ali

#----for------------
for i in name:
     print(i)  
     #str

     

#-------farghe in dota
for i in name:
    print(i)
 
for i in range(0,len(name)):
    print(i)
    
for i in range(0,len(name)):
    print(name[i])
    
#noketey payani
#i mitone ba estefade az len ya range adadi bshe in shomarande
#yni az yek adad ta yek adad dg hey i ro bzaare

#ya ag bgim i in name
#biad i ro hey bzare horof ha ya element haye daroone oon namer



#jalaseye bad========
#1- def ro yad midim va mirim soraghe
#madule ha
#numpy
#matplotlib

  
    
#----------farghe emal(apply) ya ejra (run)
a='ali'
a.upper()
#Out[15]: 'ALI'
#mige ejra krdm
print(a) #ali
#yanhi ma apply nmikone bishtare methodhaye str
#ejra mikone
#shoma baraye apply ye step dgh niaz drid
#asign
new_pass=a.upper()
oldlist=[1,2,3,4]
oldlist.append(5) #vaghty ejra krdm
#chizi be onvane Out[felan] nadad---> yani
#emal shode na ejra(tahvil)
newlist=oldlist.append(7)
#newlist=Nonetype




#LAST DEADLINE=YEKSHANBE------
#ai.course22.alipilehvar@gmail.com
'''
حتما مطمین شوید ایمیلتان ارسال شده تا زمانی که 
پیام دریاف شد برایتان ارسال شود
موفق باشید

'''
#---------QUIZ--------------------------
#------QUIZ1--------
'''
barname e benevisid ke ba az karbar adad bgire
va ba estefade az halgheye for , factoriele adad ro hesab kone

برنامه ای بنویسید که از کاربر عدد بگیره و فاکتوریل آن را با استفاده از حلقه فور حساب کنه


'''
#-------QUIZ2------
"""
yek barname ee benevisid ke az user password begire va age
password adade bozorg  ya adad toosh nabashe behesh bege avaz kone
va age monaseb bood print kone sabt shod

یک برنامه ای بنویسید که از یوزر پسورد بگیره و اگر پسورد دارای اعداد و حروف بزرگ باشه
ثبتش کنه اگه نه به یوزر اخطار بده که عوض کندش

"""

#-----FUN------(veryyy optional)
'''
yek barname e benevisid ke betone tashkhis bede adad zoje ya fard
'''


'''
yek barname benevisid ke biad az karbar jomle begire va jomle ro 
kalame ee barax benevise yani masalan
hello world :
    biad benevise world hello

'''


'''
yek barname benevisid ke az karbar jomle begore va biad
tedade har kalame dar kole matn ro hesab kone va
10 ta kalame ke bishtarin tekrar ro dashte ba tedade tekrarewshon ro
chap kone

'''


'''
yek barname benevisid ke email address begire az karbar
va tebghe email rule haye maroof bebine ke aya email
vgaghe eie ya alaki ( validation)
'''


