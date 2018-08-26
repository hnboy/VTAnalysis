#!/usr/bin/env python3
import os


file_list = []
def file_name(path):
    for file in os.listdir(path):
        file_list.append(file)
    if len(file_list)<1:
        print("Can't get the file , please check the loction")


def get_data(filename):
    if filename[-3:] in "txt":
        result_temp_vte = []
        result_temp_vtp = []
        result_vtp = []
        result_vte = []
        f= open(filename,"r+")
        while True:
            content = f.readline()
            if not content:
                break
            if "Vte =" in content and "*2*" in content:
                data = content.split(",")
                result_temp_vte.append(data[0] + ' ' + data[-2])
            if "Vte =" in content and "*10000*" in content:
                data2 = content.split(",")
                for a in result_temp_vte:
                    if data2[0] in a:
                        a = a+' ' +data2[-2]
                        result_vte.append(a)

            if "Vtp =" in content and "*2*" in content:
                data = content.split(",")
                result_temp_vtp.append(data[0] + ' ' + data[-2])
            if "Vtp =" in content and "*10000*" in content:
                data2 = content.split(",")
                for a in result_temp_vtp:
                    if data2[0] in a:
                        a = a+' ' +data2[-2]
                        result_vtp.append(a)
        filename_result = filename+"result.txt"
        filew = open(filename_result,"w")
        result_vte.sort()
        result_vtp.sort()
        for a in result_vte:
            filew.write(a+'\n')
        for a in result_vtp:
            filew.write(a+'\n')
        f.close()




def write_to_file(filename,vt):
    print(filename)

if __name__ == '__main__':
    location = "./"
    file_name(location)
    for file in file_list:
#        vte=[]
#        vtp=[]
        filename = location + file
        get_data(filename)

