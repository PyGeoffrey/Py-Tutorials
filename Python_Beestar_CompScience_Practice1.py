#type "#" to ignore. Delete the "#" on the next line to activate.
a=int(input('Unable to process dictonary. Please type 1 to continue.'))
#a=int(input("For dictionary type 0. For calculator type 1."))
while a==0:
    dict={}
    dict['5']='A five'
    dict[10]= 'A 10'
    
    dict['35']={'name': 'mercy' , 'code': 12444, 'dept': 'IT'}
    
print (dict['5'])
print (dict[10])
print(dict)
print(dict.keys())
print(dict.values())
while a==1:
    print('Type addition, subtraction, multiplication, or division.')
    CurrentFunction=int(input())
    if CurrentFunction!='addition' or 'subtraction' or 'multiplication' or 'division':
        print('Type addition, subtraction, multiplication, or division.')
        CurrentFunction=int(input())
    if CurrentFunction=='addition':
        c=float(input('Type done to quit, otherwise type anything. '))
        while c!='done':
            b=1
            Addend1=float(input('Type addend:'))
