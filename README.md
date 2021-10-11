#### Input Convention
```
O - Obstacle  
S - Storage  
B - Block  
R - Robot
```

#### How to compile and execute

All the algorithms are in separate files . To run every file use the command as given below:
1. python3 <name_of_the _file.py> -f <input_text_file_Name.txt> -- this will take your custm input to run the program
2. python3 <name_of_the _file.py> -- this will run the file with sample input file


#### Manhattan Heuristic:
* Greedy best first search and A* search are implemented using Manhattan distance between blocks and the nearest storage spaces. In this  only the distance from blocks to storage spaces is considered.

#### Non trivial Heuristic:
	In addition to the above,
* Distance of robot and boxes and
* Number of storage spaces left at any time 
	are considered to calculate the heuristic value for each board state
		heuristic value = Manhattan(box - storages) + Distance(box - robot) + storageSpacesLeft * 2;

		2* storageSpacesLeft is used to provide more weightage to storageSpacesLeft because  
		it's always a lesser number compared to other two.