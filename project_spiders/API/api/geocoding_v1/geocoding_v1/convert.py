#coding=utf-8

import math

x_pi = math.pi * 3000.0 / 180.0
ee = 0.00669342162296594323
a = 6378245.0

#将百度坐标转成国测局坐标
def bd2gcj(point):
    bd_lon = point[0]
    bd_lat = point[1]
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)    
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    return (z * math.cos(theta), z * math.sin(theta))


#将国测局坐标转成百度坐标
def gcj2bd(point):
    x = point[0]
    y = point[1]
    z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * x_pi)    
    theta = math.atan2(y, x) + 0.000003 * math.cos(x * x_pi)
    return (z * math.cos(theta) + 0.0065, z * math.sin(theta) + 0.006)


#将国测局坐标转成GPS坐标
def gcj2gps(point):
    c_point = gps2gcj(point)
    d_lng = c_point[0] - point[0]
    d_lat = c_point[1] - point[1]
    return (point[0] - d_lng, point[1] - d_lat)


#将GPS坐标转成国测局坐标
def gps2gcj(point):
    if outOfChina(point[0], point[1]):
        return point
    dLat = transformLat(point[0] - 105.0, point[1] - 35.0)
    dLon = transformLon(point[0] - 105.0, point[1] - 35.0)
    radLat = point[1] / 180 * math.pi
    magic = math.sin(radLat)
    magic = 1 - ee * magic * magic
    sqrtMagic = math.sqrt(magic)
    dLat = (dLat * 180.0) / ((a * (1 -ee)) / (magic * sqrtMagic) * math.pi)
    dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * math.pi)
    return (point[0] + dLon, point[1] + dLat)


def outOfChina(x, y):
    if x < 72.004 or x > 137.8347:
        return True
    if y < 0.8293 or y > 55.8271:
        return True
    return False


def transformLat(x, y):
    ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(math.fabs(x))
    ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(y * math.pi) + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 /3.0
    ret += (160.0 * math.sin(y / 12.0 * math.pi) + 320 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0
    return ret

def transformLon(x, y):
    ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(math.fabs(x))
    ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(x * math.pi) + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 /3.0
    ret += (150.0 * math.sin(x / 12.0 * math.pi) + 300.0 * math.sin(x / 30 * math.pi)) * 2.0 / 3.0
    return ret
