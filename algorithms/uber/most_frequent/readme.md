Uber
======
__Question date:__ January 04, 2018

Uber Interview Question for Software Engineers
Find the Kth most Frequent Number in an Array.

E.g. 
	
	```python
	arr = {1, 2, 3, 2, 1, 2, 2, 2, 3}
	k = 2
	Result: 3```

	Because '3' is the second most occurring element.

__Question address:__
<https://www.careercup.com/question?id=4955803575386112>

# Solution idea 

__See it running at:__
<https://goo.gl/GsdHGj>

## Personal comment:
My doubt is about interpretation between 'most frequent' and 'longest sequence'.
In the list [1,2,3,3,3,4,5,4,6,4,7,4,8,4,9], have the number 4 with higher frequence, but 3 with longest sequence.

And i have a question too, if there is more elements with the same frequency? Should i return a list of them? Anyway, my propose see to solve using the _'most frequent'_ concept.