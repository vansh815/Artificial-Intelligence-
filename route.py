#!/usr/local/bin/python3
# Code by: [vansh(vanshah) prashanth(psateesh) kartik(admall)]
# put your routing program here!
import sys
import itertools
import copy
import time

# loading our file into a list line by line
def load_segments(filename):
    segments=[]
    
    with open(filename, "r") as file:
        
        for line in file:
            l = line.split()
            segments.append([i for i in l[0:]])
    
    return segments
segments=load_segments("road-segments.txt")
# loading the coordinates i.e longitudes and latitudes of a city into a Set.
def load_latitudes_longitudes(filename):
    lat_long_data={}
    
    with open(filename, "r") as file:
        
        for line in file:
            l = line.split()
            lat_long_data[l[0]]=[float(l[1]),float(l[2])]
    
    return lat_long_data
lat_long_data=load_latitudes_longitudes("city-gps.txt")
# since bidirectional data is not given, we reversed the cities and appended it to our original list.
def two_way_segments(segments):
    temp_segments=copy.deepcopy(segments)
    for i in temp_segments:
        i[0],i[1]=i[1],i[0]
       
    total_segments=temp_segments+segments
    
            
    return total_segments
# function to find the euclidean distance between two cities using latitude and longitude
def dist_bw_cities(city_1,city_2):
    try:

        dist=((lat_long_data[city_1][0]-lat_long_data[city_2][0])**2+(lat_long_data[city_1][1]-lat_long_data[city_2][1])**2)**0.5
        return dist
    except KeyError:
        return 0
total_segments=two_way_segments(segments)
# This will return a list that contains the information about two cities.
def add_distances(end_city):
    for i in total_segments:
        i.append(0)
        i.append(dist_bw_cities(i[1],end_city))
        i.append(0)
        i.append(0)
        i.append(0)
        i.append("")
        i.append(0)
    return total_segments
# successor function  
def successors(cityname,end_city,final_total_segments,curr_dist,curr_mpg,curr_time,segs,curr_direction):
    succ=[]

    for i in final_total_segments:
        if i[0]==cityname:
            i[5]+=float(curr_dist)
            i[7]+=float(curr_mpg)
            i[8]+=float(curr_time)
            i[9]+=segs
            i[10]+=curr_direction
            succ+=[i]
    return succ
# to check if our goal state is reached or not
def is_goal(reached_state,end_city):
    if reached_state==end_city:
        return True
    else:
        return False
##x[5] distance is the metric
##x[6] distance to destination from start
##x[7] mpg is the metric
##x[8] is the time elapsed
##x[9] is the segments traversed
##x[10] is the direction of travel

# main function 
def search_segments(start_city,end_city,metric):
  final_total_segments=add_distances(end_city)
  visited=[]
  fringe=successors(start_city,end_city,final_total_segments,0,0,0,0,"")

  #print(fringe)
  
  while (len(fringe)>0):
            if metric=="distance":
                fringe.sort(key=lambda x: x[5])
            elif metric=="segments":
                fringe.sort(key=lambda x: x[6])
            elif metric=="mpg":
                fringe.sort(key=lambda x: x[7])
            elif metric=="time":
                fringe.sort(key=lambda x: x[8])
                
            temp=fringe.pop(0)
            if is_goal(temp[1],end_city):
                    temp[5]=float(temp[2])+temp[5]
                    temp[7]=(float(temp[2])/(400*((float(temp[3]))/150)*(1-float(temp[3])/150)**4))+temp[7]
                    temp[8]=(float(temp[2])/float(temp[3]))+temp[8]
                    temp[9]+=1
                    temp[10]+=" "+temp[1]
                    return temp
                    
                    
            a=successors(temp[1],end_city,final_total_segments,float(temp[2])+temp[5],(float(temp[2])/(400*((float(temp[3]))/150)*(1-float(temp[3])/150)**4))+temp[7],(float(temp[2])/float(temp[3]))+temp[8],temp[9]+1,temp[10]+" "+temp[0])
            for s in a:
                if s[1] not in visited:
                    fringe.append(s)
                    visited.append(s[1])
  return "Inf"
  

name_list=[]
if __name__ == "__main__":
    for i in total_segments:
        name_list.append(i[0])
    if sys.argv[1] not in name_list or sys.argv[2] not in name_list:
        print("there is no such city")
    final=search_segments(sys.argv[1],sys.argv[2],sys.argv[3])
    if final != "Inf":
        print(final[9],int(final[5]),format(final[8], '.4f'),format(final[7], '.4f'),final[10].lstrip())
    else:
        print("Inf")

    
    
    
    
    

