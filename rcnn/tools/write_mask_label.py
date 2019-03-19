import cv2
import json, copy
import numpy as np
import base64
import os, sys, argparse, re
from PIL import Image
import time
import xml.dom.minidom

def read_palette_file(palette_file_path):
    palette_list = [0] * (256 * 3)
    label_list = [""]*256
    counter = 0
    with open(palette_file_path) as f:
        for line in f:
            line = line.rstrip()
            palette_list[counter:counter+3] = map(int, line.split(" ")[:3])
            label_list[int(counter/3)] = line.split(" ")[3:]
            counter += 3
            if counter >= (256*3):
                break

    if counter < 256*3:
        palette_list[-3:] = palette_list[counter-3:counter]
        palette_list[counter-3:counter] = [0,0,0]
        label_list[-1] = label_list[int((counter-3)/3)]
        label_list[int((counter-3)/3)] = ""

    print(palette_list)
    print(label_list)
    return palette_list, label_list

palette_list, label_list = read_palette_file("J:/code/maskrcnn/mx-maskrcnn/rcnn/tools/palette_v2.txt")
print(len(label_list))

def read_xml_shape(input_xml_file):
    dom = xml.dom.minidom.parse(input_xml_file)
    root =  dom.documentElement
    Objects=root.getElementsByTagName('object')
    dict_output = {}
    for item in Objects:
        label_segs = item.getElementsByTagName('segmentation');
        label_segs_points = label_segs[0].getElementsByTagName('points')
        label_name = item.getElementsByTagName('name')[0].childNodes[0].data;
        
        if not label_name in dict_output :
            dict_output[label_name] =[];
        
        point_list = [];
        for point in label_segs_points:
            x = point.getElementsByTagName('x')[0].childNodes[0].data;
            y = point.getElementsByTagName('y')[0].childNodes[0].data;
            xy_list = [x, y];
            point_list.append(xy_list);
            dict_output[label_name].append(point_list);
            #print("x:", x)
            #print("y:", y)
    return dict_output;



dict_output = read_xml_shape("Q:/dldata/qproject/20190203/xml/H_AGC_2018-05-11 15_05_20.xml")

print(dict_output)
