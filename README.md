ENPM809X Project #1 Treaps
due March 28, 2024 04:00pm
In this project we will experiment with a data structure called treap, which is a combination of a binary search tree and a heap (see textbook Problem 13-4). Each node x in a treap has two main attributes: x.key and x.priority. The nodes in the treap are ordered as a binary search tree according to x.key and as a heap according to x.priority. More precisely, the following must be true for any two nodes u and v of a treap:
• If v is a child of u, then v.priority <= u.priority
• Ifvisaleftchildofu,thenv.key<u.key
• If v is a right child of u, then v.key > u.key
Note that we are using the convention that priorities are in max-heap order so that they are closer to the root; hence the first property above is the opposite of the corresponding property in Problem 13-4 description.
The motivation for treaps is making a binary search tree more balanced, so that search operations can be performed more efficiently. This is achieved by assigning random priorities to the nodes when they are added to the treap, which in turn randomizes the location of the node while still maintaining the binary search tree property. In this project you are asked to write functions to build and search a treap, and compare the search efficiency of two treap strategies against each other and that of a binary search tree.
Below are the required tasks for this project:
1) Write a TreapInsert function that can insert a new node into a treap, maintaining all treap properties. Your function should take two inputs: The root pointer of an existing treap (or NULL if this is the first insert operation); and the pointer to a new node. The new node should already contain the key and the priority values. Your function should add the new node to an appropriate location and return the root pointer of the treap (which can be different from the function input if the new node is added to the root).
Use the following structure for the treap nodes:
      struct tnode{
          char key;
int priority;
struct tnode *parent; struct tnode *left; struct tnode *right;
};

2) Write a TreapSearch function that searches a given key value in a treap, and returns an indication (true/false) of whether the key is found. The function should take two inputs: The root pointer of a treap; and the key value to be searched (char).
3) Use TreapInsert to build a treap using uppercase letters as keys, received in the following order:
  {'Z','Y','X','W','V','B','U','G','M','R','K','J','D','Q',
  'E','C','S','I','H','P','L','A','N','O','T','F'}
Use randomly generated treap priorities for each letter. You can use the standard rand() function of C for priorities, which generates random integers.
Verify that your treap indeed satisfies the binary search tree and heap priorities.
4) Write a program that will read the file “FellowshipOfTheRing.txt” character by character, which contains an excerpt from J.R.R Tolkien’s book. For each uppercase character (“A-Z”) that is read, use TreapSearch function to search your treap for that character (which should always find a match). For each lowercase character (“a-z”) that is read, convert it to uppercase and then use TreapSearch function to search your treap (again, it should always find a match). Skip all other characters that are read (i.e. no search). Measure the total time it takes for searching all letters in the file. You can use gettimeofday() function of C to measure time in microseconds:
#include <sys/time.h>
struct timeval start_t, finish_t;
...
gettimeofday(&start_t, NULL);
search_result = TreapSearch(Treap_Head, Letter_from_File); gettimeofday(&finish_t, NULL);
total_time = total_time + (finish_t.tv_usec - start_t.tv_usec);
Run your program 10 times to get 10 measurement values, and then calculate the average of your measurements.
5) Repeat steps 3 and 4 above, using the following priorities when generating the treap, instead of random priorities. These priorities roughly correspond to average frequency of each letter in English. When generating the treap, the characters should still be received in the order specified in step 3.
Characters: A,B, C, D, E, F,G, H, I, J,K, L, M, N, O, P,Q, R, S, T, U,V,W,X,Y,Z Priorities: 24,7,14,17,26,10,8,18,22,4,5,16,13,19,23,12,2,20,21,25,15,6,11,3,9,1

Run your program 10 times and calculate the average of your time measurements as in step 4. Does using priorities corresponding to letter frequency improve the running time?
6) Repeat steps 3 and 4 above, without using any priorities when generating the treap, thus generating a simple binary search tree. Depending on your implementation, one way to do this may be assigning the same priority to all characters when calling the TreapInsert function. When generating the tree, the characters should still be received in the order specified in step 3.
Run your program 10 times and calculate the average of your time measurements as in steps 4 and 5. Does using treaps improve the running time compared to a binary search tree?
Submit the following at the end of the project:
• Your program (in C or Python) including the TreapInsert and TreapSearch functions and the main function; this should be readily compilable for our testing.
• A graph (tree) that shows the resulting treap in step 5, including the keys and priorities of all nodes (no need to submit graphs for random-priority or no-priority cases in steps 4 and 6). You can draw this manually if you like, but it must be readable.
• Average running times measured in steps 4, 5, and 6
• Answers to questions in steps 5 and 6
