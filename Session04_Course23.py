"""
Created on Sun Jul 30 17:15:11 2023
@author: Ali Pilehvar Meibody
جلسه چهارم

kholse:
    
    variable ha va type hasho yad grftim
    built in function haro yad gereftim ( print,inpu,len,type, int())
    badesh rftim soraghe ADAD:
        assign, operator ha + - % * **,
        
    rftim soraghe str ha = '  'assign
    access= a[0] index
    goftim har cclass ( str,int)yekseri tabe dri method
    
    frghesh
    built in : rangti mishod , dakhele parantez value mizshtim
    ama method ha
    bayad rooye value ye noghte mizadim va badesh esme method
    parantez (setting)
"""

#assign meghdardehi
name='ali'


#access dastresi
name[0]
#az 0 shoro mishe adad akharo nmigire 3 ndrim 2 drim

#slice
name[0:1]

name[0:1:2]

len(name)
type(name)
print(name)
#yekseri method dashtim

#ma mese number operator drim

#jam
name='ali'
lname='pilehvar'
jadid=name+lname
print(jadid)

#*
zarb=4*name
print(zarb) #alialialiali

#@yeksei method
#masaln upcase

#structure : value ro minvisim badesh noghte badesh esme method 
#dakhele parrantez ya khali ya setting
#**** niaz b hefz nis methoda

name.upper()
#repeat: in miad ejra mikone save nmikone
#baraye save= moteghayer tarif konim

name2=name.upper()


#---------------
#oon bala file , open mishe open krd
#file save mishe save krd
#--------------------

#javabe quizzz:
text='hello, dear students, please interact with other studentd for improving your skills in programming and please note that this is really important and vital part of your life in the new life of programming'

upper_text=text.upper()
counta_text=text.count('a')
split_text=text.split(' ')
#frghi ndrn
split_text=text.split()
#str.split


#---------------------------------
num=input('insert your number :')
#besoorate str
#int
#mitonhi9m hamon aval int bzarimn ya dar calculation
new_num=int(num)/10
print(new_num)


num=input('insert 3 digity number:')
#str save mikone yani be cheshme yek reshte mibine
new_num=num[::-1]
#-1 chie ?
#-1 yani barax kon, bazi jaha mige yani ta akahr


#bsoorate dadi daryaft kone
#-----------
num=input('insert 3 digity number:')
#str has --> int konim ( chera? soal gofte)
num=int(input('insert 3 digity number:'))



num=267
#fek konim num=267
#a*100+b*10+c
#2*100 + 6*10 + 7*1
#decomposition ( tajzie)
#mesal ba adade khodemoin
a=num/100 #chi bema mide? sadgano
#267/100=2...... 
#int() gerdesh kone
a=int(num/100)
#hala a shod 2

#267- 2*100 = 267-200= 67
#hala taghsim bar 10
b=(num-a*100)/10 #6.7
#int mizaerim
b=int((num-a*100)/10)
#b ham dromad

#267-2*100-6*10=267-200-60=7
c=int(num-100*a-10*b)


#hala barax misazimesh
#c*100+b*10+a

finalnum=100*c+b*10+a
print(finalnum)

#kamel-----
num=int(input('insert your number that you want reserve it:'))
a=int(num/100)
b=int((num-a*100)/10)
c=int(num-100*a-10*b)
finalnum=100*c+b*10+a
print(finalnum)




#-----------password
password=input('please insert your pass:')
len_pass=len(password)
print(len_pass*'*')
#len pass andazeye passworddemone , * chie ?? zarbbee
#ama qoutation setare khode setaras



#frghe find ba count chie ?????--------------
#find()	Searches the string for a specified value and returns the position of where it was found
#count()	Returns the number of times a specified value occurs in a string

#find mire migarde bebine a kojas peytdash kone indexesho vbema mdie

name='mohsen'
#where is e?
name.find('e') #Mige e dar 4omin index hast
#indexo mide yani az 0



#---------------------------------------------------------
#str, number haro goftam , buil in fuinction haro goftim
#nobate chie?

#age khastim chantaa str ya chata number dashte bashim chji??

#sequences : donbale , radif = yani tedadi az type haye ghabli k mishnakhtim

#masalan man mikham 5 va 7 va 9 hamaro yeja zakhire konm
#yua masalan soale username man mikham kole user name hamo
#k masalana8 ta hast ro yeja zakhire konm


user1='ali'
user2='ami8r'
user3='amirali'
#mikham hamash bre dalkhele yek moteghayer ( zarf)

#list,set, touple, dictionary

#az beyen ina list mohmtrin va por karbord trine

#kare hamashoon ine ke donbale ee az moteghayer ha bsashand
#inha ram be cheshme type negah konid mese str numb int ,,,,,,

#Assign , define chijori tarifesh konim

#aval esme zarf bad mosavi bad mohtaviat ** yademon nre [] bzrim

firstlist=[7,8,4,2,9]
#esme zarf, mosavi , mohtaviate zarf dakhele yek beraket
#va tavasote comma joda shavad
#oon bala rast negah konid -->
#name=esmeshe type=list , size=5 , value=.....
#ye rAH DG HAS
type(firstlist) # type
len(firstlist) #size
#kafie bnvisimesh bnaraye value
print(firstlist) #value

#yek rahe dg baraye assign

firstlist=list(1,2,3,4)
#TypeError: list expected at most 1 argument, got 4
#parantez
firstlist=list((1,2,3,4)) #dovomin rahe assign

#set dictionary,touple hamashon yekian masalan frghaye jozi
#m,asalan yeseri ghabele taghir nistan
#yeksderia index bandi nashodn va beham rikhtan

#che type haee migire ? hamechi?
#fght adad ? nma begop hamechi

second=['ali','mehrzad','amir','amirali','mohammad']


#bayad yeki bashe , gharo ghati asan
third=['ali',3,'mehrzad',20,True]



#-----------------
#access---- yani dastresi
#daghighan mese str hast fght
#har value ro mese character mibine

a='ali'
a[1]
#migoft kolan 3 ta char( character) dre , bia az 0 na 1 yni dovomio brdar

#ama list nmige char mige oon element ro
a=['ali','mehrzad']
a[1]

#----------slcie drim

listt=[46,32342,747,124325,253734,     24626532,252625,2652]
listt[1:3]#[32342, 747]
#hata mitonid begid chanta chanta boro jolo
listt[1:5:2] #[32342, 124325]

listt[:4] # az 0 ta 3
listt[4:] # ta akahr
#-------------------
#change----------------
listt=['user0','user1','user2','user3','user4','user5']

#taghir bdim
#kodomo taguhir bdim? felan
#aval access bad change(modify)
listt[3]='AMIRHOSSEIN'


#taghir yafft
print(listt)
#['user0', 'user1', 'user2', 'AMIRHOSSEIN', 'user4', 'user5']

#MITONIM CHANTARO TAGHIR BDIM
listt[3:5]=['ali','amir']
print(listt)
#['user0', 'user1', 'user2', 'ali', 'amir', 'user5']

#ma hame karaye assign. accesss, slice , change ro yd grftim
#masalan set o ... baziashon taghir nmikone
#bayad tabdilesh krd b list ba list() taghir dad dobre tabdil krd
#bazia tekrari nmigire
#bazia index ndre

#---tebghe mamool ma yekseri method drim
#che no methodie ?
#str , int , ... chi bodan ? type
#behesh class ham gofte mishod
#har clas yekseri chizi dre bename methods
#list ham yek type ya yek class has va accordi9ngly 
#chi dre?
#methods

#-**methodha ziadan ama mohemasho nesbatan hefz shin ama niazi b hefz niss

#mesle har methodi aval value ro esmesho minvisim
#noghte miznim
#esme method
#dakhele parantez ehyanan setting
listt=['user0','user1','user2','user3','user4','user5']


new_list=listt.insert()
#yani aval kodom index , va chi tosh bzrm?
listt.insert(6,'ali')
#ezafe krd
#nmiaz b zakhrie nist
#choon rooye current ( liste hal) taghirat emal mishe ( apply)

#agar khali bod ke hichi ezafe mikone
#agar por bood miad yedone mizare baghie ro be roo bala hol mide
listt.insert(3,'ali')


#mohemtrin
#in tabe haa miad taghirat ro rooye value emal mikone

#append yekioaz mohmtrin hast
listt.append('jadid')
#be akahresh miad ezafe mikone

pass_list=[1234,0000,234245,143432,3132423]
new_password=int(input('please insert your pass:'))
#miaym az append estefade mikonim
pass_list.append(new_password)


new_password=int(input('please insert your pass:'))
pass_list.append(new_password)
#farghesh ba insert ine ke insert niaz b index dare ke tarif konim ama
#in mizare tah karfi b index ndre

#---------------------------------
#dr ghabli ha fght ewlement ezafe mishod
#agar bekhahim yek sequence( mese list)
#kolesho ezafe konim chi?

#extend
#miad ye element fght 
list1=['a','b']
list2=['c','d']

new_list=list1+list2 #yek rah

list1.append(list2)
#dakhele list yek omde
#kole list ro rikhte na done done
#ma mikhastim c ro joda brize d ro joda brize ama kolesho be onvane ye lis


list1=['a','b']
list2=['c','d']
list1.extend(list2)

#remove chan ravesh dre
#AZ TARIGFHE ESME ELEMENT
list1.remove('a')
#az tarigfhe index
list1.pop(0)

#kodom ;list 1?? bbinid list 1 hezarta dshtim ama
#choon python az bala b paeen mikhone
#akharin taghiri k dadio yadesh mimone

#akhario ytadeshe python
#alan list1=[d]
#pas dobare asign bdid
list1=['a','b'] # va run
#az keyword python
del list1 #kolesh pak mishe
del list1[0] #oon element pak mishe
#kamel pak mishe moteghayer zarfo jasho tohsao hameja
list1.clear()
#list 1 yek zarfe ke liste ama toosh khalie

#del miznim kole list1 mipre
#cleasr tosho khali mikone


#========================
list1=['d','b','a','c']
list1.sort()
#yani miad tabeye sort ya hamon methode sort ro rooye listr 1 apply emal mikone
#va ahal tebghe adad ya alphabet miad moratab mikone

#reversde ham drim miad reverse mikone

#Mitonimk begim chijori moratab kon?
#bale ba tarife key

list.sort(key=str.lower)
#hamaro aval kochik kon bad inkaro anjsam bde
#ya  hata badan mitonim yek tabe bsazim va be onvane key bdim

#yek buil in function ham drim
sorted() #in vase hame bekar mire
#ini k ma migim bvaraye list



#==========================================
#--------IF------------------------


#yani chi yani migim
#do no drim yeki if / yeki if-else
#dar har dosoorat 
#bebini python miad az bala be paeen mikhoone
#vaghty mirese be if dg bahs avaz mishe miad ye algorithmio donbal mikone

#algorithme if injorie ke
#mirese be if yek sharti dare age shart true bashe (yani doros bashe)
#yekio ejra mikone
#age na rad mikone
#khodemoooni: mige age injori bod inkaro kon age nabod ham velesh kon

#if else hala chie?
#mige age injori bod inkaro kon age nabood yekare dg ro kon


#sakhtaresh shabihe zire
#** do no drim yeki if / yeki if else

'''
if (shart ):
    gozare ro (dastoor) dar soorate true bodane shart ejra shavad
    
'''
#miad mige age shart bargharar bod kare paeeni ro kon
#age nabood rad kon


'''
if (shart):
    age true bood ino ejra kon
else:
    age false bod shart ghablie ino ejra kon
'''
#if else yechize ezafi dre:
#in frghesh ine ke mige ag shart bargharar bod inkaro kon , age nabood
#mese ghablie ve nakon balke yekare dg ro kon


#dar shart az com[parison] operators estefade mikonim
#== mosavi ast ya na?  =! mosavi nist ?  > bzoorgtar < kochiktr
#<= >= ...

#aval yek adad mizrim
a=4

if a==4:
    a=a+2

print(a)
    #
    #
    #
    #
    #
    #
#6 , choon didi a are 4 hast = shartemon true shod
#statement ro ejra krd ( dakhele fasele (tab))
    
#----------
a=5

if a==4:
    a=a+2

#birone halghe
print(a) #5 yni ejra nshode



#--------------

num=int(input('please insert your number:'))
if num>2:
    print('this number is more than 2')


#dar ife khali ag true nabod ( false) mipare
#kari ndre
#ama dar if else yek statement mizrim baraye false





num=int(input('please insert your number:'))

if num>10:
    print('this number is more than 10')
else:
    print('no sorry')
    
    
    
#if va if-else

#yechize dg darim be esme ELIF

if num>10:
    print('this number is more than 10')
else:
    print('no')
    

#------ age doros bood inkaro kon
#ag doros nabod dobare ye sharte dige ro besanj


if num>10:
    print('this number is more than 10')
elif num>5:
    print('more than5')
else:
    print('less than 5')
    
    
    
#--------------------------
#felan if o if-else ro bdoonid




#ghab;li baraye ejraye exeption
#ma mikhaym yek filter bzarim
#begim yeseri chiza anjam bde nade

#====================
#halgeh hast ya 
#mikhaym ye kario tekrar konim
#do no halghe --> yeki while
#for

while
for
#minevisim banafsh mishe yani dastoore


#while aal mige ye adad bzar baraye shomarandamon
#yechi bname shomarande drim k aksaran i mizrn
i=1
#shomarande yani mishmore
#az chan shoro kone az 1
#bad benevis while va jolosh sharte edameye halghe

while i<6:
    #statement (hey dor mizne)

    #while yani ta zamni ke
    #ta zamani ke chi???
    #in shart sahih bashad
    
#t zamani k i kochiktar az 6 hast
#man oon statmente ke fasele dre oon zir ro
#ejra mikonm mese ye halghe

#hey brmigarde aval check mikone
#hey mibine true e okey

#khob inja
#run nakonid !!!!!!!!!!!!!!!!!!!!!!!!!!
'''
i=1
while i<6:
    print('salam')
    
'''
#i ro yek mizre
#hey check mikone
#check mikone mige zire 6e ? are
#pas ejra mikone
#hey dobare
#dobare
#dobare
#va khob be in migan
#endless loop yek halghe bipayan
#tamom nmoishe

#rahi ndre ke az halghe kharej she

#mian migan yek chize jadi bzar k biad kharej she

i=1
while i<6:
    print('salam')
    i=i+1

#avalin bar= i yek has
#sharte i<6 true hast pas mire too  halghe
#print mikone salam ro
#bad miad i ro +1 mikone
#i emon shod chan ? 2
#dobare check mikone
#i<6 bale
#print mikone salam ro
#i ro ezafe mikone +1 = i emon shod3
#.....
#i=5
#i<6 bale
#print mikone salam ro
#i ro mikone +1 = i=6
#hala miad mige i<6? hast? naaaa
#pas ejra nmikone va az halghe miad birooon

i=1
while i<6:
    print('salam')
    i=i+1



#khoroji:
    #salam
    #salam
    #salam
    #salam
    #salam
    

#sakhtare kolie while ?

#aval yek shomarande mizarim
#minevisim while
#badesh shart mzirim behehs migan  sharte khoroj az halghe
#yani ta vaghty true has edame bde
#dakhelesh uyek statement has k ejra mishe
#yek  i+.. ya har calculationi mizrim ke
#ezafe kone be I ta betonim az halghe brim biron
#behesh migan khoroj az halghe





#------------------FOR-------------
#for miad mige sade tar mikon m kareto
#hamino sade bnvis

#benevis baraye felan ta felan yani
#start ta end ye kario man hey tekrar konm
'''
for (shart):
    statement ( dakehle halghe loop)
    '''
    
    #frgh ine ke dakhele shart shoma miayn
    #start o endi k too while mziashtino mizrim

#aksaran mian az tabeye dakhelie range estefade mikonim


a=range(0,5)

range(0,5)
#in adad nis motyeghayer nis yek range e
#beyne 0 ta 5

for i in range(0,5):
    print('salam')
    
    #mige ma yek range drim az 0 ta 5 (khode panj hesab ni)
    #0,1,2,3,4,5
    
    #mige done done bia i ro yebnar 0 bzar yebar 1 yebar 2....
    #va hey ejra kon
    
    
#be kalame sade
#az 0 ta 5 = 0,1,2,3,4 (5 BAR) in kare paeeno bokon


for i in range(0,5):
    print('salam')
    



for i in range(0,10):
    print('ali')
    


#=======================================
'''
ai.course22.alipilehvar@gmail.com


به تمام ایمیل ها کلمه دریافت شد ارسال میشود اگر ارسال نشد یعنی دریافت نشده است

همچنین برای راهنمایی سوالات زیر میتوانید به این ایمیل پیام دهید
موفق باشید

'''
#=====quiz1(ejbari)===============================================

'''
---------------------user saver-------------------
yek barname benevisid:
ebteda yekseri user dashte bashad manande user1,user2,user3 va ...
username az karbar begirad va an ra be liste username ha ezafe konad

یک برنامه بنویسید که ابتدا یکسری یوزر داشته باشد و از کاربر یوزر بگیرد و آن را به لیست
یوزر ها اضافه کند

'''
#=====quiz2(ejbari)==========================================

'''
-------------------simple calculator----------------
yek mashin hesab besazid ke az karbar do ta adad begire be tartib
va badesh beporse che amalgari ( operatori) mikhahad va 
oon amalgar ro roye do adad piade kone va manande mashin hesab javab ra
namayesh dahad

یک ماشین حساب بسازید که از کاربرد به ترتیب دو عدد بگیرد و بپرسد چه عملی را میهخواهد
روی عدد ها انجام دهد و انجام دهد

مثال:
adade aval=2
adade dovom=5
amalgar= + 
javab=7

'''

#=====quiz3(ejbari)==========================================

'''
-------------BMI CALCULATOR-----------------------
yek barname besazid ke vazn va ghad ro begirad az karbar
vazn ro taghsim bar ghad be tavane 2 kone ( yani aval vazn ro be tavane 2 kone
                                           badesh ghad ro taghsm bar oon adad kone)
agar oon adad kochiktar az 18.5 bood bege under weight, ag beyne18.5 ta 25 bood bege normal
age beyne 25 ta 30 bashe bege over weight agar beyne 30 ta 35 bood bege obese agar
balaye 35 bood bege very obese




یک برنامه بنویسید که وزن و قد رو از کاربر بگیرد و قد رو به توان دو کند و وزن رو تقسیم بر آن کند
اگر زیر 18.5 بود بگه کم وزن اگر بین 18.5 تا 25 بود بگه نرمال اگر بین 25 تا 30 بود بگه اضافه وزن
اگر بین 30 تا 35 بگه چاقی و اگه بزرگتر از 35 باشد بگه چاقی مفرط

'''
#======fun (optional) ======
'''
haman barnameye gereftane password va zadane setare ro ba estefade az for
bezanid

همان برنامه گرفتن پسورد و ستاره زدن رو با استفاده از حلقه فور بزنید

'''

#====development (optional) ===================================
'''
yek barname ee benevisid ke biad az karbar password begirad va 
biad hamono bargardone ama harjaye in password agar 'a' dasht bejash
setare bezane

یک برنامه بنویسید که از کاربر پسورد بگیرد و به جای حروف الف بیاد
ستاره بزنه و نمایش بده

'''





    
