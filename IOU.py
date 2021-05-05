def iou(boxA, boxB):
    # 顺序：左、上、右、下
    left_max = max(boxA[0], boxB[0])
    top_max = max(boxA[1], boxB[1])
    right_min = min(boxA[2], boxA[2])
    bottom_min = min(boxA[3], boxA[3])
    # 交集：
    intersection = max(0, (right_min - left_max)) * max(0, (bottom_min - top_max))
    # 并集：
    Sa = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    Sb = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    union = Sa + Sb - intersection
    iou = intersection / union

    return iou


def iou2(boxA, boxB):
    # 计算重合部分的上、下、左、右4个边的值，注意最大最小函数的使用
    left_max = max(boxA[0], boxB[0])
    top_max = max(boxA[1], boxB[1])
    right_min = min(boxA[2], boxB[2])
    bottom_min = min(boxA[3], boxB[3])
    # 计算重合部分的面积
    inter = max(0, (right_min - left_max)) * max(0, (bottom_min - top_max))
    Sa = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    Sb = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    # 计算所有区域的面积并计算iou，如果是Python 2，则要增加浮点化操作
    union = Sa + Sb - inter
    iou = inter / union
    return iou

# https: // blog.csdn.net / zhicai_liu / article / details / 107855375
#
# 目标检测标签（坐标）转换

# 不同的标注格式
# 目标检测的标签格式有XML，TXT，JSON等；
#
# 目标检测的坐标格式有：
#
# VOC(XML)
# 格式：
# (Xmin, Ymin, Xmax, Ymax)，分别代表左上角和右下角的两个坐标；
# YOLO(TXT)
# 格式：
# (Xcenter, Ycenter, W, H)，其中x, y, w, h为归一化后的数值，分别代表中心点坐标和宽、高；
# COCO(JSON)
# 格式：
# (Xmin, Ymin, W, H)，其中x, y, w, h均不是归一化后的数值，分别代表左上角坐标和宽、高；
# 坐标格式转换
# （Xmin，Ymin，Xmax，Ymax）– > （X，Y，W，H）

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

# （Xmin，Ymin，W，H）– > （X，Y，W，H）

def convert2(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = box[0] + box[2] / 2.0
    y = box[1] + box[3] / 2.0
    w = box[2]
    h = box[3]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


# 标签格式转换
# 参考：https: // github.com / ssaru / convert2Yolo
