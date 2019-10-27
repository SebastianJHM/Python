import sys
import json
from operator import attrgetter

## -------------------------------------------------------------------------
def principal( argv ):

    ## Declarations tuples and list
    tuple1 = ("disco",2,3.4) ## tuple
    print("1: ",tuple1)
    print("2: ",tuple1[0])

    ## Add Tuples
    tuple2 = tuple1 + ("vallenato",5,5.8)
    print("3: ",tuple2)

    ## Tuple of tuple
    tuple3 = ("vallenato",(2,3),5,5.8,(8,5),("vallenato",(2,3),5,5.8,(8,5)))
    print("4: ",len(tuple3)) ## len is a function tath return the length of th tuple
    print("5: ",tuple3[len(tuple3)-1]) 
    print("6: ",tuple3[5][0])
    print("7: ",tuple3[5][1][1])

    print("-----------------------------------------------------")
    ## --------------------------------------------------------

    ## Lists
    list1 = ["disco",2,3.4] ## Vector or List
    print("8: ",list1)
    print("9: ",list1[0])

    ## Add List
    list2 = list1 + ["vallenato",5,5.8]
    print("10: ",list2)

    ## Extend: Add list to another list
    list2.extend(["vallenato",["hola",False],5.8])
    print("11: ",list2)

    ## Append: Add elemento to alist
    list2.append(5)
    print("12: ",list2)

    ## del(): delete element
    del(list2[1])
    print("13: ",list2)

    ## Remove
    list2.remove("vallenato")
    print("14: ",list2)

    list2.remove("vallenato")
    print("15: ",list2)

    list2.remove(list2[len(list2)-1]) ## In this case remove the first 5 tath found.
    print("16: ",list2)

    list2.remove(list2[0])
    print("17: ",list2)
    

    ## Pop
    list2.pop(0)
    print("18: ",list2)

    list2.pop(-1)
    print("19: ",list2)

    list2.pop(len(list2)-1)
    print("20: ",list2)

    ## Split
    text1 = "A;B;C;D"
    text2 = "A#B#C#D"
    
    list3 = text1.split(";")
    print("21: ",list3)

    list3 = text2.split("#")
    print("22: ",list3)

    print("-----------------------------------------------------")
    ## --------------------------------------------------------
    ## Sets
    set1 = {"rock","metal","punk",1,"rock"} ## Delete the duplicated element
    print("23: ",set1)

    ## Convert list in a Set
    list1 = ["pop","rock","metal","punk",1,"rock"]
    set1 = set(list1)
    print("24: ",set1)

    ## Operations whith sets
    set1 = {"rock","metal","punk",1,"rock"}
    set2 = {"rock","champeta"}

    set2.add("vallenato")
    print("25: ",set2)

    set1.remove("punk")
    print("26: ",set1)

    b = "rock" in set2
    print("27: ",b)

    ## Intersection
    set3 = set1&set2
    print("28: ",set3)

    ## Union
    set3 = set1.union(set2)
    print("29: ",set3)

    print("-----------------------------------------------------")
    ## --------------------------------------------------------
    ## Dictionaries
    keys = ["a", 'b', 'c']
    values = ['hola', 2, 3]
    dictionary = dict(zip(keys, values))
    print("30: ",dictionary)
    print("31: ",dictionary['a'])

    ## json.dumps() converts a dictionary to str object
    ## json.loads() as a retrieve method
    app_json = json.dumps(dictionary)
    print("32: ",app_json)
    y = json.loads(app_json)
    print("33: ",y)
    print("34: ",y["a"])

    list5  = []
    list5.append(y)
    list5.append(y)
    print(json.dumps(list5, indent = 1))

    ## Vector Json
    jsonList = []
    a = ["USA","France","Italy"]
    b = [10,5,6]
    for i in range(0,len(a)):
        jsonList.append({"country" : a[i], "wins" : b[i]})
    #rof
    print(json.dumps(jsonList, indent = 1))
#fed


if __name__ == "__main__":
    principal( sys.argv )
# fi