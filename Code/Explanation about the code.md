# Summary:
1. [Explanation about the code](#explanation-about-the-code)
2. [Maintainability](#maintainability)
3. [Scalability,](#scalability)
4. [Performance](#performance)


## Explanation about the code

---
We are provided with a file named `sample.txt`, and the function outputs the result to a different file called `result.txt`.
I used a hashmap (dictionary) to track the letters of the words that are anagrams, using the sorted letters as the keys and pairing them with the anagrams as values.  
`dictionary_anagram = {}`

I used a list comprehension because it's faster the writing a `for` loop and after that to append to a list.    
` words = [line.strip() for line in file.readlines()]`

Used a tuple as a key for the hashmap , because the keys are immutable. Also , I’m converting all words to lowercase. If there’s a word that starts with or contains a letter that is capitalized, it should also be converted to lowercase. 
`sorted_word = tuple(sorted(word.lower()))`

After that we check to see if the letters from the word ar in the dictionary. If not , we make them as keys and inicialize the value with a empty list and append the word to the corresponded key.
```python
if sorted_word not in dictionary_anagram:
    dictionary_anagram[sorted_word] = []
dictionary_anagram[sorted_word].append(word)
```
The output of this function will look like this:

```python
{('a','c','t'):['act','cat'],
 ('e','e','r','t'):['tree'],
 ('a','c','e','r'):['race', 'care' ,'acre'],
 ('b','e','e'):['bee']}
```

I used the output to be stored in a file because it's easier to keep the result and we can rerun the program and add the new words to the list and it's easier to read.  
We use the variable `grup` to get the values from the dictionary and to give them some space between the words , by using `' '.join(grup)'` 
```python
 with open("result.txt", "w") as output:
        for grup in dictionary_anagram.values():
            output.write(' '.join(grup) + '\n')
```

---


## Scalability
...textul corespunzător...


## Maintainability

## Performance