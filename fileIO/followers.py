import json
import random

try:
    with open("follow.json") as f:
        data=json.load(f)
        print(data)


    all_user=[user["id"] for user in data]
    my_followings=[user["followers"] for user in data if user["username"]=="akhil"][0]
    my_id=[user["id"]for user in data if user["username"]=="akhil"].pop()
    to_follow=set(all_user)-set(my_followings)
    to_follow.remove(my_id)
    print(to_follow)
    suggestions=random.sample([*to_follow], 2)
    print(to_follow)

except Exception as e:
    print(e.__class__)

st=[10,11,12,13,14]
lst=[*st]
print(lst)

lst=[10,11,12,13,14]
st={*lst}
print(st)