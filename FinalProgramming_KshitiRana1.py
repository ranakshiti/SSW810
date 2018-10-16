from prettytable import PrettyTable
from collections import defaultdict
import os
import csv

class readr():
    def read_iot(self,dirname):
        data = defaultdict(lambda: defaultdict(list))
        pt = PrettyTable()
        pt.field_names = ["Sensor",'Day','Value']
        try:
            dirpath = os.listdir(path = dirname)
        except OSError:
            print("Unable to find directory")
        else:
            os.chdir(dirname)            
            for file in dirpath:
                if file.endswith('.iot'):
                    try:
                        fp = open(file, 'r')
                        with fp:
                            for line in fp:
                                nr = line.strip().split('|')
                                sensor,day,value = line.strip().split('|')
                                data[sensor][day].append(value)
                                pt.add_row(nr)                                  
                    except FileNotFoundError:
                        print("Unable to find file")
        #print(pt)
        return data    
    #print(l)

    def sumary(self,dd):
        table1 = PrettyTable()
        table1.field_names = ['Sensor','Count','Average','Min','Max','Distinct']
        table2 = PrettyTable()
        table2.field_names = ['Sensor','Day','Count','Average','Min','Max','Distinct']
    # gererating summary by senr by day
        for k,v in l.items():
            for k1,v1 in v.items():
                b = []
                sum_s = 0
                avg_s = 0
                min_s = 0
                max_s = 0
                dist_s = 0
                dist_s = []
                b.append(k)
                b.append(k1)
                b.append(len(v1))
                for x in v1:
                    x = int(x)
                    sum_s += x
                    avg_s  = sum_s/len(v1)
                    min_s = min(v1)
                    max_s = max(v1)
                    if x not in dist_s:
                        dist_s.append(x)
                b.append('{0:.2f}'.format(round(avg_s,2)))
                b.append(min_s)
                b.append(max_s)
                b.append(len(dist_s))
                table2.add_row(b)
        print('Summary by sensor by day:...')
        print(table2)

    # for generating summary by sensor
        for i,j in l.items():
            cnt = 0
            avg = 0
            sum_m = 0
            min_m = 0
            max_m = 0
            dist_m = []
            ds = 0
            a = []
            #print(j)
            for k,m in j.items():
                cnt +=len(m)
                for x in m:
                    x = int(x)
                    sum_m +=x
                    min_m = min(m)
                    max_m = max(m)
                    if x not in dist_m:
                        dist_m.append(x)
            avg = sum_m / cnt
            ds = len(dist_m)
            a.append(i)
            a.append(cnt)
            a.append(avg)
            a.append(min_m)
            a.append(max_m)
            a.append(ds)
            table1.add_row(a)
        print('Summary by sensor:...')
        print(table1)

def deftodic(d):
            if isinstance(d, defaultdict):
                d = {k: deftodic(v) for k, v in d.items()}
            return d 
dir = 'C:/Users/kshit/Documents/Stevens/Semester 2/SSW 810 - Special Topics - Python/HW/final/datafile/IOT_test'
obj = readr()
d = obj.read_iot(dir)

l = deftodic(d)
