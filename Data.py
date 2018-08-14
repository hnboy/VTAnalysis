#!/usr/bin/env python
import os
import re
import matplotlib.pyplot as plt
import numpy as np
import math

'''
0.1 beta version
2018 7/26 developing by wq#
'''


'''
get the VTE & VTP data from current folder file
'''

file_list = []
vte = []
vtp = []
def file_name(path):
    for file in os.listdir(path):
        file_list.append(file)
    if len(file_list)<1:
        print("Can't get the file , please check the loction")


def get_data(filename):
    if filename[-3:] in "txt":

        f= open(filename,"r+")
        while True:
            content = f.readline()
            if not content:
                break
            if "Vte =" in content:
                pattern=re.compile(r'Vte =.*V')
                result = pattern.findall(content)
                result=str(result)
                data = result.split("=")
                result_temp = data[-1]
                try:
                    result_temp = float(result_temp[:-3])
                    vte.append(result_temp)
                except:
                    pass
                continue


                '''
                data = content.split()
                temp = data
                data = data[3]
                if data[:-2] in ',':
                    print("debug")
                    print(content)
                    pattern=re.compile(r'Vte =.*V, FAIL')
                    test = pattern.findall(content)
                    print(test)
                vte.append(data[:-2])
                '''

            elif "Vtp =" in content:
                data = content.split()
                data = data[-2]
                try:
                    data = float(data[:-2])
                    if (data<1)&&(data)>0:
                        vtp.append(data)
                except:
                    pass
                continue

        f.close()

def plain(title,vt):

    a = np.array(vt)
#    plt.xlim([-1, 1])
    plt.hist(a,bins=100,alpha=0.5,histtype="barstacked")
    plt.xlabel("vt (V)")
    plt.ylabel("count")
    plt.title(title)
   # plt.show()
    plt.plot()
    picturename = title+".png"

    plt.savefig(picturename,format="png")
    plt.close()



def write_to_file(filename,vt):
    print(filename)



if __name__ == '__main__':
    location = "C:\\Users\\luowenqi\\Desktop\\AS01009_#4\\"
    file_name(location)
    for file in file_list:
        filename = location + file
        print(filename)
        get_data(filename)

    #(map(float,vte))
    #(map(float,vtp))
    vtp.sort()
    vte.sort()

    name = "vte"
    vt = vte
    plain(name,vt)

    name = "vtp"
    vt = vtp
    plain(name,vt)
