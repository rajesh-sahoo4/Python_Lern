'''Pratice Question of Slice,Split and join'''
# txt='python'
# print(txt[0:4])
# print(txt[2:])
# print(txt[:3])
# print(txt[::2])
# print(txt[::-1])
# print(txt[-2:-5:-1])

# easy
 
msg='i love python'
msg1=msg.split()
msg2=' '.join(msg1)
msg3=msg[::-1]
print(msg3)
# Q1
exm='programming'
exm1=exm[0:7]
print(exm1)
# Q2
exm2='Python'
print(exm2[::-1])
# Q3
exm3='apple mango banana'
print(exm3.split())

# medium
# Q4
num='10-20-30-40'
print(num.split("-"))
# Q5
wrd=['Hello','World']
print(' '.join(wrd))
# Q6
wrd2='softwareTesting'
print(wrd2[8:])

#Hard
# Q7
wrd3='2026/02/04'
wrd4=wrd3.split('/')
wrd5='-'.join(wrd4)
print(wrd5)
# Q8
sen='I_am_learning_Python'
sen1=sen.split('_')
sen2=' '.join(sen1)
print(sen2)
# Q9
tch='Technology'
print(tch[0:4:])
# Q10
dv='Developer'
print(dv[::-1])
# Q11
anm='dog cat cow goat'
print(anm.split())
# Q12
lng=['Python','is','easy']
print(' '.join(lng))
# Q13
clr="red,green,blue,yellow"
print(clr.split(','))
# Q14
word='ManualTesting'
print(word[6::])
# Q15
nm=['10','20','30']
print(':'.join(nm))
# Q16
usr='user-name-email'
print(usr.split('-'))
# Q17
dte='2026|03|15'
dte1=(dte.split("|"))
dte2=('-'.join(dte1))
print(dte2) 
# Q18
s1='Python is very simple and easy to learn' #simple and easy
s2=s1.split()
s3=s2[3:6:]
s4=(' '.join(s3))
print(s4)
#Q19
lang='Java_is_very_powerful'
lang1=(lang.split("_"))
lang2=(' '.join(lang1))
print(lang2)
#Q20
rev='I love Python'
rev1=(rev.replace('Python','Python'[::-1]))
print(rev1)
# Q21
sft='Software-Testing-Manual'
sft1=(sft.split('-'))
sft2=(' '.join(sft1))
print(sft2)
# Q22
numb='123-456-789'
# numb1=(numb.split('-'))
# numb2=(' '.join(numb1))
# print(numb2)

# or
print(" ".join(numb.split('-')))
# Q23
text='programmingLanguage'
print(text[11:])
# Q24
text1='India_is_my_country'
sent=' '.join(text1.split('_'))
print(sent[::-1])

'''Pratice question of List'''

l=[10,20,30,50,'good','is','what',50]
print(len(l))
print(l.count(50))
print(l.index('good'))
l.append(50)
print(l)
l1=[40,70,60]
l.extend(l1)
print(l)

l.insert(5,58)
print(l)

l.remove('good')
print(l)

l.pop(5)
print(l)

l.reverse()
print(l)

x=l.copy()
print(x)

# xl=[10,20,50,'raju']
# x1.clear()
# print(x1)
x1=[10,50,35,98,74,25,89]
print(max(x1))

print(min(x1))

x1.sort()
print(x1)

x1.sort(reverse=True)
print(x1)

x2=[10,20,30,50]
del x2[1]
print(x2)
# nested list
list=[10,20,[30,40],50]
print(list[2])
print(list[2][0])
print(list[2][1])

li=[10,20,[30,40],50]
print(li[2][1])

li1=[[1,2],[3,4],[5,6]]
print(li1[2][0])
li2=[1,[2,[3,4]]]
print(li2[1][1][1])

li3=[[10,20,30],[40,50],[60]]
print(len(li3))

