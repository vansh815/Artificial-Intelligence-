#!/usr/local/bin/python3
#
# choose_team.py : Choose a team of maximum skill under a fixed budget
#
# Code by: [vansh(vanshah) prashanth(psateesh) kartik(admall)]
#
# Based on skeleton code by D. Crandall, September 2019
#
import sys
import itertools
def load_people(filename):
    people=[]
    
    with open(filename, "r") as file:
        
        for line in file:
            l = line.split()
            people.append([l[0]]+[ float(i) for i in l[1:] ])
    
    return people


def states_generator(peeps,budget):
    to_search=[]
    for L in range(1, len(peeps)+1):
        for subset in itertools.combinations(peeps, L):
            sum_rate=0
            for i in subset:
                sum_rate+=i[2]
            if sum_rate<=budget:
                to_search.append(subset)
    return to_search
                
                
# This function implements a greedy solution to the problem:
#  It adds people in decreasing order of "skill per dollar,"
#  until the budget is exhausted. It exactly exhausts the budget
#  by adding a fraction of the last person.
#
def total_skill_calculator(to_search):
    new_l=[]
    if len(to_search)==0:
        return "Inf"
    for i in to_search:
        sum_skill=0
        sum_rate=0
        for ele in i:
            sum_skill+=ele[1]
            sum_rate+=ele[2]
            
        new_l.append([i]+[sum_skill]+[sum_rate])
    return new_l

def approx_solve(list_to_search):

###https://stackoverflow.com/questions/17555218/python-how-to-sort-a-list-of-lists-by-the-fourth-element-in-each-list
    list_to_search.sort(key=lambda x: x[1])
    return list_to_search[-1]




if __name__ == "__main__":
    peeps=load_people(sys.argv[1])
    a=states_generator(peeps,float(sys.argv[2]))
    list_to_search=total_skill_calculator(a)   
    best_team=approx_solve(list_to_search)
    print("Found a group with",len(best_team[0]),"people costing",format(best_team[-1],'.6f'),"with total skill ",format(best_team[1],'.6f'))
    for i in best_team[0]:
        print(i[0],"1")
    
    
