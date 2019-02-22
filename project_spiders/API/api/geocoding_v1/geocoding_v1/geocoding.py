#coding=utf-8

import sys

import publicfun
import convert
from baidumap import BaiduMap

default_encoding = 'utf-8'
conf_path = r"conf.bcp"
result_path = r"result.bcp"


def writeToFile(f, lists):
    for point in lists:
        str_point = point[0] + "\t" + str(point[1]) + "\t" + str(point[2]) + "\t" + str(point[3]) + "\n"
        f.write(str_point)
        f.flush()


def start(bdmap, f):
    res_list = []
    content = publicfun.readFile(conf_path)
    print "content.size:" + str(len(content))
    
    linecount = 0
    for line in content:
        linecount += 1
        
        line = line.replace("\r", "")
        line = line.replace("\n", "")
        if linecount % 1000 == 0:
            print line
        
        #json解析时可能出现问题，加个try捕获语句
        try:
            bd_point = bdmap.getLocation(line)
        except Exception as e:
            print line + "---bdmap error!! info:" + str(e)
            continue

        if bd_point is None:
            continue
        
        #print "%s---%s,%s %f" % (line, bd_point[0], bd_point[1], bd_point[2])
        gcj_point = convert.bd2gcj(bd_point)
        #print "%s,%s,%s" % ("bd2gcj", gcj_point[0], gcj_point[1])
        gps_point = convert.gcj2gps(gcj_point)
        #print "%s,%s,%s" % ("gcj2gps", gps_point[0], gps_point[1])
        #地点名称,经度,纬度,可信度
        point = (line, gps_point[0], gps_point[1], bd_point[2])
        res_list.append(point)
        if linecount % 1000 == 0:
            writeToFile(f, res_list)
            res_list = []
        
    return res_list

def run():
    bdmap = BaiduMap("潍坊")
    try:
        with open(result_path, "ab+") as f:
            lists = start(bdmap, f)
            writeToFile(f, lists)
            '''for point in list:
                #print "%s---%s,%s %s" % (point[0], point[1], point[2], point[3])
                str_point = point[0] + "\t" + str(point[1]) + "\t" + str(point[2]) + "\t" + str(point[3]) + "\n"
                f.write(str_point)'''
    except Exception as e:
        print "run error!! info:" + str(e)
                
        
       

if __name__=='__main__':
    if sys.getdefaultencoding() != default_encoding:
        reload(sys)
        sys.setdefaultencoding(default_encoding)
    
    run()

    
