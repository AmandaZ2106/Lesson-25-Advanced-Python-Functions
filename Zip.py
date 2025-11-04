s1={1,2,3,4}
s2={"a","b","c","d"}
s3=list(zip(s1,s2))
print(s3)

list1=[10,20,30,40]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks=["reliance","tcs","infosys"]
prices=[1243,5774,3456]
new_dict={stocks: prices for stocks,
          prices in zip(stocks,prices)}
print(new_dict)