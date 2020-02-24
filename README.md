
                                            
<h1>Problem 1:</h1>
<h5>Aim</h5> To sole given the 15 puzzle with an efficient method for 3 cases.
    case 1: Normal
    case 2: Circular 
    case 3: Luddy(L-shape moves)
    
<h5>State space</h5> The given intital board (the initial board that was given to us).

<h5>Successor function</h5> 
Normal case: All the pssible states from the current position. We can move a row towards left or right or move a column up and down and all these states should be valid based on the validity conditions.
        
<h5>Circular case</h5> Same concept must be used but with a few changes in the constraints. The cases where the elements are in the corners or edges, the constraints are relaxed. Example: If the element is in 0th row and Cth column it can go to 3rd row and cth column and if the element is in the rth row and 0th column it can go to rth row and 3rd column. 
        
        
<h5>Luddy</h5> Successor function is the same as the original case. We used BFS to search for the successor states of a particular number.
        
        
<h5>Edge weights</h5> The edge weight is 1 to move from one state to another state.

<h5>Goal state</h5> The final solved puzzle is the goal state .
            1 2 3 4
            5 6 7 8 
            9 10 11 12
            13 14 15
            
<h5>Search Strategy</h5> 
1.We used BFS here with priority queue. 
2.We also made use of Permutation inversion to reduce the numbero of states from successor function                   for optimal search.
3.Used A* (A star) search 
Maintained a list of visited states in order to not traverse through duplicate states. This improved the time complexity.
              
<h5>Heuristics Used</h5>
<h6>Normal</h6> We used manhattan distance here as it is both admissible and consistent. 
        
<h6>Circular</h6> We used Misplaced tiles here as it worked better and faster in this case. We used Permutation inversion as states reducing method after recursive trials where it did not fail for any case.
        
<h6>Luddy</h6>We first used manhattan distance as heuristic which turned out to be overestimating, then we swtiched the misplaced tiles but it was heavily underestimating. So went for the heuristic-disjoint pattern heuristic that was discussed in the class and modified it to suit this problem. Since L shape movements are only allowed, the problem becomes complicated. Our heuristic calculates the sum of all the paths from initial positions of each number to final position of the numbers(goal state) and finds the shortest path which is the heuristic. We also found that permutation also works for this and works well when we need to show Inf.

<h5>Additional Note</h5>

Challenges faced and devlopment of solution: We started of by using Misplaced tiles to reduce the number of states to search. But for the normal case we switched to Manhattan distance and it worked well when used with permutation inversion.
For the Circular case misplaced tiles heuristic was used.

<h1>Problem 2</h1>

<h5>Aim</h5> This problem has 4 goals.
     1. To find the shortest distance between two cities.
     2. To find the minimum number of segments needed to go to the destination.
     3. To find the minimum time taken to reach the destination.
     4. To find the minimum number of gallons it takes to go from one place to another place.
     
<h5>state space</h5> It is the initial place from where we will start our journey. 
Successor function: The successos function is same for all the goals but the way we sort them changes based on the requirement.

<h5>successor function</h5> gives all the cities that our connected to our initial city. 
Heuristic We used the different heuristic for each goal to reduce the number of states to be searched.
For distance we used euclidean distance to select the next best state. 
Similarly we used distance of segment, time (distance of segment/ max velocity) and MPG for the rest.

<h5>Search strategy</h5>
From a given city, there will be multiple cities we can go to and reach our destination. But searching all of them will increase our cost. TO tackle it, we used the coordinates of the cities ot find the euclidean distance between the initial cities and its successor states and chose the next state which has the lowest euclidean distance to our destination.
In case of segment, we sorted all the states based on segment length and chose the one that had the lowest length.
Similary we chose lowest time and MPG for the other parts of the problem.

<h5>Heuristic</h5> We used euclidean distance calculated using the lattitude and longitude values as our heuristic.

<h5>Additional Note</h5> Using the heuristic of euclidean distance for segments drastically reduces the search which is very useful when finding the parameters of the cities which are very far away otherwise would take a long time for our code to run as it uses BFS. For cities that are closer to the source city(when you are travelling short distances) we donot need to use the heuristic as it would already run very fast giving accurate results. In a scenaria where low latency is of utmost importance, time becomes a very crucial criteria than travelling a little bit of extra number of segments. For example: If we go from Bloomington to San Francisco, If we use the heuristic we get the results within a second but a suboptimal answer with minimum error, but if we dont use a heuristic it gives us an optimal answer but it takes around 15 seconds which is not good for low latency systems.
If you change line 101 from fring.sort(key=lambda x: x[6])(with heuristic) to fring.sort(key=lambda x: x[9]) you can see the difference that was claimed above. 

Using heuristic it takes 41 segments whereas not using heuristic gives 34 segments for Abbyville,_Indiana to Bloomington,_Indiana
     
                
<h1>Problem 3</h1>
<h5>Aim</h5> To maximize the skill and minimize the budget.
    minimize(budget + 1/skill)<--loss function
    
<h5>State space</h5> The state space is all the combinations of different people that fit our constraint of minimizing the loss function.

<h5>example</h5> If we have to make combinations out of 3 people 
         1. Bob 
         2. Dylan
         3. Tom 
         Combinations: (Bob),(Dylan),(Tom),(Bob, Dylan),(Dylan, Tom),(Bob, Tom),(Bob, Dylan, Tom)
         
<h5>Heuristic</h5> This is a problem where all the states must be searched to find the optimal solution. 
We cannot use the shortest path approach in this case as doing that may fetch us a suboptimal path. So, it is necessary to traverse thorugh all the states.
          
<h5>Goal state</h5> The state with the maximum skill and minimum budget under the given constraint.

<h5>Heuristic</h5> The loss function is our heuristic. It is admissible because, we can never overestimate it as we already have a contraint attached to it.

<h5>Simplifications</h5> Used a python function iterative.combinations() that returns all the possible combinations of input that we give in. It is much faster than loops.



```python

```
