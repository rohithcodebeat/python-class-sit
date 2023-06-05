a = [ 
    {
        "name" : "john",
        "age" : 22
    },
    {
        "name" : "mark",
        "age" : 26
    },{
        "name" : "mike",
        "age" : 25
    }, {
        "name" : "mosh",
        "age" : 21
    }, {
        "name" : "cris",
        "age" : 24
    }, 
    {
        "name" : "marry",
        "age" : 23
    }
]

for i in range(len(a)):
    for j in range(len(a)):
        if a[i]["age"] < a[j]["age"]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp 

print(a)