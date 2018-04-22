print("Hello World")
diva = "jinyc76"
print(diva)

str_raw = r"'\r\n\t\s\""
print(str_raw)

str_multi = """
            this is multi\
            line\
            message
            line end add \\ \
            shows one line 
            """
print(str_multi)

str_multi2 = '''this shows also \
multi line
with quot
'''

print(str_multi2)

str_exe1 = "this is execution "
str_exe2 = "string line"

print(str_exe1*3)
print(str_exe1+str_exe2)

print(dir(str_exe1))
print("Capitalize : ",str_exe2.capitalize())
print("is 'first sound' end with g : ",str_exe2.endswith("e"))
print("join string with 'str_exe2' str : ", str_exe2.join(["multiline","joinline","resultline"]))


list1 = [1,2,3]
list2 = ["a","b","c"]
list3 = list("list element")
list4 = list(list1+list2)

print(list1)
print(list2)
print(list3)
print(list4)
print(list4[2])
print("negative index reverse list3[-1] , list3[-5] : " , list3[-1] , "," , list3[-5])
print(list3*2)

print("list4 to 3th index element list4[:3] : " , list4[:3])
print("list4 from 4th index element list4[4:] : " , list4[4:])
print("list4 from every 1th index element list4[::1] : " , list4[::1])
print("list4[start:stop:step] list4[0:5:2] : ", list4[0:5:2])

print("string like list str_exe1[3:15:3] : ", str_exe1[3:15:3])


if True :
    print("Yes True")

if False :
    print("No False")

if False :
    print("No False")
else:
    print("No False Else Place")


ex_num1 = 11

if ex_num1 < 10 :
    print("less than 10")
elif ex_num1 >= 10 :
    print("more than 10")
else:
    print("not number")


print(not True)
print(not False)

t1 = (1,2,3,4,5)
print(3 in t1)
print(7 in t1)

d1 = {"one":1 , "two":2 , "three":3}
print(2 in d1.values())

w1 = d1["three"]
print(w1)

while w1 > 0:
    print("w1 is : ",w1)
    w1 -=1

for i in range(10):
    print(i)

ex_arr = ["aaa" , "bbb" , "ccc"]
for name in ex_arr:
    print(name)

ex_d1 = {"name":"test","version":3,"company":"mycompany","like number":7}
for title in ex_d1:
    print(title," : ",ex_d1[title])

for k in range(1,30,3):
    print(k)

for k in range(10):
    if k == 3:
        print("find ",k," and end")
        break
    else:
        print(k)











