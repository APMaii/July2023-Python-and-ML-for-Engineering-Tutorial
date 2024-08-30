"""
بسم الله الرحمان الرحمیم

جلسه سوم---------------
Created on Wed Jul 26 16:53:13 2023

@author: ALI PILEHVAR MEIBODY
gamlab.aut.ac.ir
alipilehvar1999@gmail.com
ai.course22.alipilehvar@gmail.com

"""

'''
خلاصه:

IDE (spyder) = yek safde chat dar nazsar begir
harchi mikhayn benevisin
* bad az class

2 ta onsore mohem dare :
    1- kalamate reservs shode
    2- dastoorat
    
    ** harchi benevisid sefid mishe ina rangian
    banafsh = dastoor
    narenji= tabe haye dakheli ( buil in )
  
structure ( badane):
    
1-voroodi ( data vared she)
2-body ( badane ye asli back bone) calculation,save, assign
3-khoroji ( file bashe , safe namayesh bde (print chap), tasviri bashe)

tabe , function makhsoosan : built in dakheli :
    
    esmi dare ( az shoma vorodi migire)
    *run bshe ye khoroji mide
'''
#
print('salam','KHOBI')
#negah konid be kadre khakestari k baz mishe va mige
#chiamigire che type haee migrie va optionale ya na ( ekhtiari)
#va shoma mitonid taghiresh bedid
#hamchenin pishfarz haro ham gofte
#baraye mesal fasele beyne value haee ke ma behesh dadim
print('A','L','I',sep='============')
print('salam \n khobi')
print()

#voroooodi===================================
#1-khodemon tarif kjonim ( assign= meghdardahi)
#2-open ( axz yek file ee vardarim , )
#3-downloaed krdn az site

#khodemon tarif krdn ( assign)
#avalin chizi ke yadmeon bashe ye zarf darim ye esm dare ye mohtaviat

#esm ro aval minevisim mosavi mizanim jolosh dakhele zarf
ali=
name=
whoo=
hgjhgy

#** bejoz chizhaee k reserv shode ( narenji banafsha)
# esm haye chnd harfio
name_second
NameSecond
#name.speed !!!!!!!!!!!!!!!!!!! #ghalat
# case sensitive = A barabar nis ba a

A=20
print(a)
#NameError: name 'a' is not defined
#a mage A nabod naa choon case sensetive e
#=============================
#ye zarf darim , injhori esm mizarim roosh ,
#ye mosavi mizanim ( mosavi ro mifhme k yani chi yani assign )
#ghesmate operator ha ro negah konid ---> + - =

#mohtaviate zarf : chan ta type drim ?
#1-numbers --> 1.1int 1.2float 1.3complex

num1=4
num2=4.4
num3=1j

#2-reshte ya string str ham gofte mishavad
#avalin ghanoon
#in ro bayad dakhele qout nevesht ******
#() parantez niaz ndre ama zadi eb ndre
name='ali'

#cheraaa ? cherraa too qout ?
#vaghty puython az bala be paeen az chap be rast khoond
#ag qout nadasht oono esme zarf ( variable name)
#dar nazar migire
#agar narenji9o ina shod dastooor migiratesh
#agar qout dasht kari ndre oono mohtaviate yek
#zarf m,idone yani oon ro be onvane yek
#kjalame, harf ya jomle dar nazar migirad
#javabe quiiizz
name='ali'
lname='pilehvar'
prog='python'

#taghir dar editor(haminja) mosavi ba run nis !!!
name=ali
#ino az chap mikhond
# name eee in ye esme moteghayere
#mosavie chie ?
# samte rast ham esme moteghayere
#mirf donbale moteghayri be name ali migasht

print('man hastam',name,lname,'va dars midam',prog)

# az chap mikhone mige ee print narenji 
#yek tabe hast
#tabe parantez mikhad tooye parantez value va megdhar ha hastan
#mire done done chappeshon mikone

#ravesh haye dg 
#+ , f'
name='name'

#raveshe vorodde dg = az karbbar begire
input
#narenjii shod = tabeye dakheli
#** aval ine ke yek esmi bzarim
name=input('اسم شما چیست؟')

#strructure ( sakhtar)
#esme zarf(moiteghayre) = input ( oon chizi ke mikhaym karbar bebine)
#** 1-hatman esme moteghayer bezarina
#**2 dakhele parantez stringe ha qout mikhad

input('اسم شما چیست؟')
#vaghty input run mishe ta javbesho nagire nemire
#bala rast morabaye ghermez = STOP
#KeyboardInterrupt: Interrupted by user
#** vaghtyt ruun tool keshid interrupt konid ( stop az tarighe dome ghermez)
input('اسم شما چیست؟')
#Out[18]: 'علی' 
#khoroji dadam na jaee save shod na ...

#ghable inpuut , esmesho tarif kon
namename=input('esme shoma chist?:')
#dovomin eshtebah qout nmiznim
namenamename=input(esme shoma chist?)
#SyntaxError: invalid syntax

#inpute maaaaaaaaaaaaaaaa
#==================================================

#DAR GHABLIHA  dakhele paranteze dakhele cadre khakestari
#migoft ke chia ro vared konid
print()
#*** این توضیحات مربوط به داخل کادر هلپ خاکستری هست
#dakhele parantez yani chia migire che type haee
#birone parantez yani chi mide
num1=1
num2='1'
num1==num2
#comparison operator chie ? moghayese mikoen ager doros bashe
#mige true age ghalat bashe mige false
#== , < > =< =>
#avalie adade
#dovomie str
#manteghi behesh fk nkonid
#********
#**********
password=input('لطفا پسورد خود را وارد کنید:')
password+2
#nemitonam mesle yek adad bahash abrkhord konam
#choon reshtas
#TypeError: can only concatenate str (not "int") to str
#fght str b str +, ya int b int
#ham no ba ham no type=type

password=input('یک عدد بدید من دوبرابر کنم:')
double=2+password
print(double)


#rahe hal?  CAST / CASTING
#taghire type
a='ali' #str
b=4 #int
c=4.4 #float
new=str(b)
#oon type i k mikjhay ro minevisim oon zarf ro
#mirizim too in zarf
print(new)
new
int(c)

#=========moshkiel hal shod ( sade trin code)
#1
password=input('یک عدد بدید من دوبرابر کنم:')
password=int(password)
double=2+password
print(double)

#2
password=int(input('یک عدد بدید من دوبرابر کنم:'))
double=2+password
print(double)

#3
password=input('یک عدد بدید من دوبرابر کنم:')
double=2+int(password)
print(double)

#sade tarin barnameye hoosh masnoeie
#yek vorodi dre ( 1-karbar bde[] 2-assign 3-open)
#yek calculate dare ( back bone - body)
#khoroji dare ( 1-save 2-pplot rasm 3-chap (print))


#================================================
#===============================================
#------ma fahmidim k vorodi badane khoroji
#.....>voorodi ...>number
#operator ha operators
#+jam -manfi *zarb **tavan /taghsim %baghimonde
#str chetor ?
#...>voroodi...>string ha STR
variable='ali'
#yek tabeye buil in 
type
type(variable)

variable=5
#----------------------------
a='ali'
b='pm'
a+b

a-b
#farghe inke inja bznm ya print
#joftesh yekie ama print oon outputo ...

a+b
a+b
print(a+b)

#-----------------
#kolan in type ha k goftam yechizan behesh migan CLASS
#python khafanish b ine ke class object orient
#shey gera has
#class ha do ta chiz daran 1-methods 2-values
#yekseri meghdar tooshone ya yekseri ravesh (method)
#!!method has mese built in function hastan ama 


#https://docs.python.org/3/library/functions.html
#یه سر بزنید هم هرو بخونید 
#** نیاز به توضیح بیشتر
'''
دوستان این سایت بسیار عالی هست و تمام تابع های داخلی پایتون در آن هست و به سادگی
میتونید ببینید هرچیزی که اینجا میزنید و نارنجی میشه رزو بقهمید معنیش چیه و این تابع ها چه کارایی هایی دارد
همچنین میتونید وقتی مینویسید اسم تابع رو و پرانتز میزنید یک کادر خاکستری هست و میتونه کمکتون کنه

#repeat
doostan in site awli hast va tamame buil-it function haye python has toosh
ina marboot be python hast va b sadegi mitonid berid bebinid chizaee ke 
narenji mishe ro bebinid ke manish chie va tabe he chikar mikone
va hamchenin inja (editor)  mitonid benevisid esme tabe ro va parantezo
bezanid va bebinid yek kadre khakestari baz mishe va bebinid
'''

#buil in vali behesh migan method
#str method
#yani methodi k be STR ha fght marboooote
#frghesh chie
#bejaye inke too parantezx value bezanid
#aval value minevisid ba ye noghte oon method ro minevisid

a='aliiiii'

#https://www.w3schools.com/python/python_ref_string.asp
#مطالع شود
#نیاز به توضیحات بیشتر

'''
پایتون دارای یکسری تابع داخلی بود و یکسری دستورات که وقتی مینوشتید رنگی میشدن ( بنقش دستورات - نارنجی تابع)
حالا این تابع ها مربوط به خود پایتونه و به عنوان اسم های رزرو شده معروفند اما میدونیم که در پایتون
یکسری متغیرها هستند که به عنوان کلاس شناخته مشوند
مثل کلاس عدد ها یا رشته ها یا بولیان 
این ها ددر اصل یکسری متود دارند و این متود ها فقط و فقط برای این کلاس مختص هست
یعنی متود یک رشته رو نمیتونید برای یک عدد بزنید
در سایت بالا راجب تمام متود های رشته ها نوشته شده همچنین انتهای متن کپی شدند
یادتون باشه فرق تابع های داخلی با متود ها این هست که تابع های داخلی رو مینویسید رنگی میشوند
و داخل پرانتز باید بنویسید مقدارهارو اما متود ها به صورت نقطه وصل میشوند به مقادیر,
مقادیری که حالا یک کلاس خاص هستند و داخل پراتنز تنظیمات اضافه هست

#repeat
python daaraye do element has, yeki buil in function ( narenji) yeki dastoorat (banafshj)
ke ina rangi mishan vaghty mikeshideshon, va ina marboo be hame calss ha mishavand
ama clas ha ( masalan adad ha (int,float), ya reshte ha (str)), in class ha
daraye yekseri method hastan ke in method ha fght makkhsose khodeshone
site e bala drmorede methodhaye str ha sohbat shode
frghe buil in function va method ha ine ke
buuil in function baraye pythone e va hame class ha mitonan estefade konan
ama method ha fght b oon class rbt dre
hamchenin buil in haro minvisid rangi mishan va value haro dakhele parantez minvisid
ama method ha tavasote yek noghte b value ha vasl mishan va dakhele parantez
tanzimate pishrafte tar hast
'''

#structure: esme moteghayer .noghte esme built in parantez
#mesal:
a.upper()
#Out[52]: 'ALIIIII'
#zakhirash nkrd
b=a.upper()
c=b.lower()
a.count('l')
a.count('i')
print(valuee injaaaa booood)
open(file)
article='The abstract of this artcile is about the effect of nanotechology on trhe world and the bio.....'
edited_article=article.split(' ')
#===============================================
#=======STRIMG=========
#asssing
#qoute yadet nare
a='dhsdgajg'

#hala age bekhaym be yek harfi {element}i beresim
#chikar konim?
a='salam khooobi'
#access element دسترسی به عنصر
len(a)
len(article)
#length toolesh chghdrer ? chanta element toosher
#cdhanta harf tooshe
#12 ta harf dare
#chra mige 13 ?
#space hesab krde hamechiooo hesaab mikone
#Mige kole in variable chegahd onsor dre

#accesss element--------
a[]
#aquald baraye access b index
#index= shomare gzoari 
# 13 hoorof ro shomaree gozarti mikone baraye khodesh ( index)

#****************************************
#IMPORTANT= az 0 shoro mikone
#ta yeki monde b akhar
#******************************************
a='mohammad'
len(a)
b=a[0]
print(b)
b=a[1]

b=a[8]
#IndexError: string index out of range **yeki monde b akhar
#inyedone bod ke ma chnta mikhaym

b='mehrzad'
type(b)
len(b)
#kole 3 khatre bvala dar rast bala variable explorer has
st=b[0]
mid=b[4]


b[0]
b[4]
b[0:4]
#1- : yani TAAAA
#2** kolan jaee ta shenidid akhario hesab nmikonan aksaran

b[0:]
#agar chizi nnvisim khodesh tashkhis mide yani goftim boro ta tahesh
b[:6]
#az aval b akahresh boro ( excepty6)
b[:7]

#negative indexing = mige bjaye inke
#az 0 shoro koni az -1 shoro kon
b[0:7:2]
#mige az [start,end,space]
#az koja shoro konm koja brm chantaaee
#***mehrzad sharifi **

#===============================

#-------kholaase string=======

#type,print,len,input
#assign
#str,int casting car krdim
#str methods goftim(yekseri ro)
#opersatora

#str___>
#assign
#access index
a=4
a.upper()
#AttributeError: 'int' object has no attribute 'upper'

#yani adade maa hamchin methodi nadare
#in method ya asan vojod ndrre ( eshtebah krdi, ghalatye emlaee,capsluck)
#koja dorose? bayad rooye khode oon class
a='ali'
a.upper()

#=============================
#alll methods
#str methods has yani fght rooye STR

'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''

#مهمترین ها نوشته بشود بعغد از کلاس


#======================================================
#python Booleans

#mesle adad ha mesle reshte ha
#adad ha ma dashtim
#string ha k dashtim
#yechizi darim بولی
True
False
#** harfge adad bozorg
a=True
type(a) #bool
len(a)

#koja bekar mire ?
#javabe com[parison operator ha hast]

a=b #frgh dre ba
a==b

a=b #assign yani migi a ro khali kon b ro briz toosh
a==b # yani dri miporsi a barabar ast ba b?
#pas montazere chi e ? javab
#javab chie? booly

a=2
b=2
print(a==b) #True

a=2
b='2'
print(a==b)#False
#ma fahmidim bejoz int,float comples, str clas ha va type ha
#class=type
#haye dg ee ham darim mesle boolean
#mohmtrinashon int,float,str,boolean
#ychiz dg darim sequence ( radif ya donbale) ke shamel shode az chanta
# azin variables

#====================================================================
#====================================================================

#====================================================================
#====================================================================

# 3 no quiz darim 1-hatmi 2-pishrafte(ekhtiari) 3-fun(ekhtiari)
#کوییییززززززز

#این کوییز یک---------------------------
text='hello, dear students, please interact with other studentd for improving your skills in programming and please note that this is really important and vital part of your life in the new life of programming'
#این متنمون هست , کار اول : کل متن رو تبدیل به حروف بزرگ کنید
#کار دوم این هست که ببینید چند تا حرف a داخل این متن هست
#و کار آخر این هست که کل کلمات متن را جدا کنید

#راهنمایی:
#باید از متود method های رشته هاstr استفاده کنید
کلش رو تبدیل به بزرگ کنید

#این کوییز دو------------------------------
#یک برنامه بنویسید که از کاربرد یک عدد بگیرد 
#و عدد رو تقسیم بر ده کند 


#-----------------------------------------------


#پیشرفت-----------------------------ه 
#یک عدد سه رقمی از دوستان بگیرید و برعکسش را تحویل بدهید


#فان------------------------------------
#از کاربر یک پسورد بگیرید و ستاره چاپ شود
#سختی موضوع: تعداد ستاره به اندازه ی تعداد پسورد باشه



#==============payan=======================
#AI.COURSE22.ALIPILEHVAR@GMAIL.COM
#==========================================
user=input('نام کاربری را وارد کنید')
password=input('لطفا پسورد خود را وارد نمایید:')
k=len(password)
print(k*'*')
print(user,'خوش آمدید کاربر')
