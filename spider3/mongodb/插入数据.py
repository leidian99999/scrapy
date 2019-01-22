import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient(host='localhost', port=27017) # host地址 post端口

# client = MongoClient('mongodb://localhost:27017/') # 效果同上，也可以传入MongoDB连接字符串

db = client.test # 指定操作数据库test
# db = client['test'] # 同上

collection = db.students # 指定操作集合students
# collection = db['students'] # 同上

# # 插入数据
# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# # 调用insert方法插入数据
# result = collection.insert(student)
# print(result)

# 可以同时插入多行数据，只需以列表方式传递
# student1 = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }
#
# result = collection.insert([student1, student2])
# print(result)

'''
官方推荐insert_one()和insert_many()分别插入单条和多条数据
'''

# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)
#
# student1 = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }
#
# result = collection.insert_many([student1, student2])
# print(result)
# print(result.inserted_ids)


