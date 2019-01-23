import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students


# find_one()得到单个结果
result = collection.find_one({'name': 'Mike'})
print(type(result))
print("*"*50)
print(result)













