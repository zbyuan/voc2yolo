import xml.etree.ElementTree as ET
import os
from os import getcwd
 
sets = ['train', 'test']
 
classes = ['holothurian','echinus','scallop','starfish']
data_path = '/home/yb/project/yolov7/data/'  #设置你的数据集路径
 
 
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)
 
 
def convert_annotation(image_id):
    in_file = open(data_path+'Annotations/%s.xml' % (image_id))
    out_file = open(data_path+'labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        try:
            difficult = obj.find('difficulty').text
        except AttributeError:
            difficult = '0'
        cls = obj.find('name').text
        if cls not in classes or int(difficult) >= 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
 
 
wd = getcwd()
print(wd)
for image_set in sets:
    if not os.path.exists(data_path+'labels'):
        os.makedirs(data_path+'labels')
    image_ids = open(data_path+'ImageSets/Main/%s.txt' % (image_set)).read().strip().split('\n')
    list_file = open(data_path+'%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write(data_path+'images/%s.jpg\n' % (image_id))
        print(image_id)
        convert_annotation(image_id)
    list_file.close()
