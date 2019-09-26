#week1b Exercises
#1: is even
def is_even(n):
    mod=n%2
    if mod==0:
      return(True)
    else:
      return(False)
print(is_even(3))
print(is_even(6))
#2: is cool
def is_cool(name):
    if name=="Abdullah" or name=="Waleed" or name=="Zaid":
        return True
    else:
        return False
print(is_cool("Abdullah"))    
print(is_cool("John"))  
#3: is lunchtime
def is_lunchtime(hour,is_am):
    return (hour==11 and is_am==True) or (hour==12 and is_am==False)
print(is_lunchtime(7,True))
print(is_lunchtime(12,False))
#4: is leap year
def is_leap_year(year):
    return(year%4==0 and year%100!=0 or year%400==0)
print(is_leap_year(2000))
print(is_leap_year(1996))
print(is_leap_year(1800))
print(is_leap_year(2013))
#5: interval intersect
def interval_intersect(a,b,c,d):
    return not((a>=c and a>=d and b>=c and b>=d )or (a<=c and a<=d and b<=c and b<=d))
print(interval_intersect(1,2,-1,-3))
#6: name and age
def name_and_age(name,age):
    if age<0:
        print("Error: Invalid Age")
        
    else:
        print("%s is %d years old."%(name,age))
name_and_age("Abdullah",20)
name_and_age("Abdullah",-2)
#7: print digits within 1-99
def print_digits(n1):
    if n1>=100 or n1<0:
        print("Error: Invalid Number")
    else:
        t=n1//10
        u=n1%10
        print("The tens digit is %d, and the ones digit is %d."%(t,u))
print_digits(104)
print_digits(36)
print_digits(-10)
#8 lookup name
def name_lookup(fname):
    if fname=="Joe":
        return ("Warren")
    elif fname=="Scott":
        return ("Rixner")
    elif fname=="John":
        return ("Greiner")
    elif fname=="Stephen":
        return ("Wong")
    else:
        print ("Error: Not an instructor")
print(name_lookup("Tahir"))
print(name_lookup("Joe"))
#9 Pig Latin
def vowel(L):
    if L=="a" or L=="e" or L=="i" or L=="o" or L=="u" or L=="A" or L=="E" or L=="I" or L=="O" or L=="U":
        return True
    else:
        return False
    
    
    
def pig_latin(word):
    first_letter=word[0]
    rest_letters=word[1:]
    is_vowel=vowel(first_letter)
    if is_vowel== False:
        temp=first_letter+"ay"
        temp1=rest_letters+temp
        return temp1
    else:
        temp=word+"way"
        return temp
def test(word):
    """Tests the pig_latin function."""
    
    print pig_latin(word)
    
test("pig")
test("owl")
test("python")    

#10 Challange: Smaller root of quadratic equations
def smaller_root(a,b,c):
    disc=b**2-4*a*c
    if disc==0:
        return 0
    elif disc>0:
        s=(-b-((b**2)-4*a*c)**.5)/(2*a)
        return s
    else:
        print("Error: No Roots")
        
def test(a, b, c):
    """Tests the smaller_root function."""
    
    print "The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:" 
    print str(smaller_root(a, b, c))
        

test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)    

    
    
    
    
    
    
    
    

    
    

    
    


