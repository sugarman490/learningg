person = {"name": "lisi",
          "age": 15,
          "gender": True,
          "height": 1.75,
          }
person2={"weight":75,
         "height":1.7}
print(person)
# 取值
print(person["name"], person["age"])
# 增加/修改,key不存在则增加，key存在则修改
person["weight"] = 60
print(person)
person["age"] = 18
print(person)
# 删除
person.pop("weight")
print(person)
#统计
print(len(person))
#合并(如果包含已经包含的键值对，则会覆盖)
person.update(person2)
print(person)
#清空
person2.clear()
print(person2)
#循环遍历
for k in person:#k是每次循环中的key
    print(k,":",person[k])