#coding=utf-8


#读取文件，存到列表中
def readFile(path):
    if path == None:
        return ""
    
    content = None
    try:
        with open(path, "rb") as f:
            content = f.readlines()
    except Exception as e:
        print "%s :文件不存在" % path

    return content
