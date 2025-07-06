print(type(True))

# 扇形面积函数
def sector_area(angle, radius):
    area  = angle / 360 * 3.14 * radius ** 2
    print(f"扇形面积为： {area}")
    return area

area1 = sector_area(160, 30)

print(area1)