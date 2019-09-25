#functionsweek1a
def miles_to_feet(miles):
    feet=5280*miles
    return(feet)
def total_seconds(h,m,s):
    Tsec=3600*h+60*m+s
    return(Tsec)
def rectangle_perimeter(w,h):
    p=2*(w+h)
    return(p)
def rectangle_area(w,h):
    area=w*h
    return (area)
def circle_circumference(r):
    c=2*3.14*r
    return (c)
def circle_area(r):
    area=3.14*r**2
    return(area)
def future_value(pv,ar,y):
    fv=pv+ar*y
    return(fv)
def name_tag(fn,ln):
    print("My name is "+fn+" "+ln+".")
def name_and_age(name,age1):
    age=str(age1)
    print(name+" is "+age+ " years old." )
def point_distance(x0,y0,x1,y1):
    dis=(((x0-x1)**2)+((y0-y1)**2))**.5
    return(dis)
def triangle_area(x0,y0,x1,y1,x2,y2):
    L1=point_distance(x0,y0,x1,y1)
    L2=point_distance(x0,y0,x2,y2)
    L3=point_distance(x2,y2,x1,y1)
    s=(L1+L2+L3)/2
    A=(s*(s-L1)*(s-L2)*(s-L3))**.5
    return (A)
def print_digits(n):
    tens=n//10
    t=str(tens)
    units=n%10
    u=str(units)
    print("The tens digit is "+t+", and the ones digit is "+u+".")           
def powerball():
    import random
    n1=random.randrange(1,59)
    n1=str(n1)
    n2=random.randrange(1,59)
    n2=str(n2)
    n3=random.randrange(1,59)
    n3=str(n3)
    n4=random.randrange(1,59)
    n4=str(n4)
    n5=random.randrange(1,59)
    n5=str(n5)
    pbnum=random.randrange(1,35)
    pbnum=str(pbnum)
    print("Today's numbers are %s, %s, %s, %s, and %s. The Powerball number is %s."%(n1,n2,n3,n4,n5,pbnum))         
    
    
    