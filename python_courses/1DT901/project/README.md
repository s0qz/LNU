# Mini-project report

Members: Samuel Berg and Love Billenius\
Program: Software Engineering\
Course: 1DT901\
Date of submission: 2022-11-XX

## Introduction

A brief introduction including a presentation of the project tasks. Present the
project as a part of the course 1DV501/1DT901.

## Part 1: Count unique words 1

||life_of_brian|swedish_news_2020|
|:--------------:|:---------:|:----:|
|**Unique words**|1997|380018|
|**Nr 1 word**|Brian|Säger|
|**Nr 2 word**|Crowd|Under|
|**Nr 3 word**|Centurion  |Kommer|
|**Nr 4 word**|Mother|Efter|
|**Nr 5 word**|Right|Eller|
|**Nr 6 word**|Crucifixion|Också|
|**Nr 7 word**|Pilate|Andra|
|**Nr 8 word**|Pontius|Finns|
|**Nr 9 word**|Rogers|Sedan|
|**Nr 10 word**|There|Skulle|

For the top ten function we used a dictionary and a list of all words. For each
new word, we added an entry with the value one, and for each existing we
incremented the existing value with one.

```python
for item in lst:
    items[item] = items.get(item, 0) + 1
```

Afterwards we sorted the dictionary after the values, and sorted the dictionary,
to then return the last ten elements.

## Part 2: Implementing data structures

```python
def get_hash(self, word: str) -> int:
    hash_value = 7
    for character in word:
        hash_value = hash_value * 31 + ord(character)
    return hash_value % len(self.buckets)

def rehash(self) -> None:
    old_buckets = self.buckets
    self.buckets = [[] for _ in range(len(self.buckets) * 2)]
    self.size = 0

    for bucket in old_buckets:
        for element in bucket:
            self.add(element)

def add(self, word: str) -> None:
    if self.size > len(self.buckets):
        self.rehash()

    if not self.contains(word):
        self.buckets[self.get_hash(word)].append(word)
        self.size += 1
```

The example output differs from out output in `hash_main.py`, which occurs due
to us using a more efficient hashing algorithm.

- Give a brief presentation of the given requirements

- For the hash based word set (HashSet), present (and explain in words):

  - Python code for function `add`, how to compute the hash value, and
    rehashing.

  - Point out and explain any differences from the given results in
    `hash_main.py`

```python
def put(self, key: Any, value: Any) -> None:
    if self.key == key:
        self.value = value
    elif key < self.key:
        if self.left is None:
            self.left = Node(key, value, None, None)
        else:
            self.left.put(key, value)
    else:
        if self.right is None:
            self.right = Node(key, value, None, None)
        else:
            self.right.put(key, value)

def max_depth(self) -> int:
    # Create variables for each sides depth
    left, right = 0, 0
    # If current nodes left or right is None ignore
    if self.left is not None:
        left = self.left.max_depth()
    if self.right is not None:
        right = self.right.max_depth()
```

- For the BST based map (BstMap), present (and explain in words):

  - Python code for the two functions `put` and `max_depth`.

  - Point out and explain any differences from the given results in
    `bst_main.py`.

## Part 3: Count unique words 2

||life_of_brian|swedish_news_2020|
|:--------------:|:---------:|:----:|
|**Unique words**|1997|380018|
|**Nr 1 word**|Brian|Säger|
|**Nr 2 word**|Crowd|Under|
|**Nr 3 word**|Centurion|Kommer|
|**Nr 4 word**|Mother|Efter|
|**Nr 5 word**|Right|Eller|
|**Nr 6 word**|Crucifixion|Också|
|**Nr 7 word**|Pilate|Andra|
|**Nr 8 word**|Pontius|Finns|
|**Nr 9 word**|Rogers|Sedan|
|**Nr 10 word**|There|Skulle|

```python
items = bst.BstMap()
    for item in lst:
        a = items.get(item)
        if a is None:
            a = 0
        items.put(item, a + 1)
```

- How did you implement the Top-10 part of the problem. Feel free to show code
  fragments.

- Present a unique word count and the Top-10 lists for each of the two files.

||life_of_brian|swedish_news_2020|
|:--------------:|:---------:|:----:|
|**Max bucket size**|8|7|
|**Zero bucket ratio**|0.37646484375|0.4847869873046875|
|**Max depth**|27|48|
|**Leaf count**|646|125341|

- What is the max bucket size and zero bucket ratio for HashSet, and the max
  depth and leaf count for BstMap, after having added all the words in the two
  large word files? (Hence, eight different Nrs.)

- Explain how max bucket size and zero bucket ratio can be used to evaluate the
  quality of your hash function in HashSet. What are optimal/reasonable/poor
  values in both cases?

- Explain how max depth and leaf count can be used to evaluate the efficiency of
  the BstMap. What are optimal/reasonable/poor values in both cases?

## Project conclusions and lessons learned

We separate technical issues from project related issues.

### Technical issues

- What were the major technical challanges as you see it? What parts were the
  hardest and most time consuming?

- What lessons have you learned? What should you have done differently if you
  now were facing a similar problem.

- How could the results be improved if you were given a bit more time to
  complete the task.

### Project issues

- Describe how your team organized the work. How did you communicate? How often
  did you communicate?

- For each individual team member:

  - Describe which parts (or subtasks) of the project they were responsible for.
    Consider writing the report as a separate task. Try to identify main
    contributors and co-contributors.

  - Estimate hours spend each week (on average)

- What lessons have you learned? What should you have done differently if you
  now were facing a similar project.
