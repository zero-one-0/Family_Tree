# Family_Tree

Given an text file to run, the code will do the following 
  * Initialize the Family Tree (as given in problem statement)
  * Contain 'name' and 'relationship', the code outputs the person corresponding to the relationship in the order in which they are added to the family tree
  * Any new member can be added to the family
  
### Overview
 - **Person Class** 
   Stores all the information related to a Person and also returns various attributes corresponding to a person
 - **FamilyTree Class**
   Stores the family tree contents
 - **GetRelationship class**
   Get the relationships of the members

### Supported Relationships
 - **Son**
 - **Daughter**
 - **Siblings**
 - **Paternal Uncle**
 - **Paternal Aunt**
 - **Maternal Uncle**
 - **Maternal Aunt**
 - **Sister in Law**
 - **Brother in Law**

### User Input File supported operations
```sh
ADD_CHILD "mother_name" "child_name" "child_gender"
GET_RELATIONSHIP "name" "relationship"
```

### Execution
Use the following command to execute. _geektrust_ contains main function
```sh
$ python3 -m geektrust <absolute_path_of_input_text_file>
```

### Test
Go to the test directory and run the following command to run tests
```sh
$ python3 -m unittest
```
