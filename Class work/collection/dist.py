# st={
#     "name":"ibrahim",
#     "email":"ibrahim@gmail.com"
# }

# print(st)
# print(st['name'])
# print(st.get('name'))

# st['name']= "abc"
# st.update({"subject":"python"})
# print(st)


st=dict(name="ibrahim",email="ibrahim@gmail.com",phone=12345678)

# print(st)
# print(st['name'])
# print(st.get('name'))
# print(st.keys())
# print(st.values())
# print(st.items())


# for i,j in st.items():
#     print(i,j)


# st["name"]="abc"
# st.update({"cource":"python"})
# st.popitem()


# print(st)


data={
    "student1":{
        "name":"ibrahim",
        "email":"ibrahim@gmail.com"
    },
    "student2":{
        "name":"my",
        "email":"my@gmail.com"
    }
}

for i,j in data.items():
    print(i)
    for a,b in j.items():
        print(a,b)