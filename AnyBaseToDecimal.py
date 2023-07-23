def any_base_to_decimal(num,base):

    dec=0
    i=0
    while num>0:
        last=num%10
        n=last*base**i
        dec+=n
        num=num//10
        i+=1
    return dec

number=int(input())
base=int(input())
print(any_base_to_decimal(number,base))