# Summary:
1. [Explanation about the code](#explanation-about-the-code)
2. [Maintainability](#maintainability)
3. [Scalability,](#scalability)
4. [Performance](#performance)


## Explanation about the code

---
### Version 1 ([anagram](https://github.com/glemiu6/Anagram/blob/master/Code/anagram.py))
We are provided with a file named `sample.txt`, and the function outputs the result to a different file called `result.txt`.
I used a hashmap(dictionary) to track the letters of the words that are anagrams, using the sorted letters as the keys and pairing them with the anagrams as values.  
`dictionary_anagram = {}`

I used a list comprehension because it's faster the writing a `for` loop and after that to append to a list.    
` words = [line.strip() for line in file.readlines()]`

Used an immutable tuple as a hashmap key. Also , I’m converting all words to lowercase. If there’s a word that starts with or contains a letter that is capitalized, it should also be converted to lowercase. 
`sorted_word = tuple(sorted(word.lower()))`

After that we check to see if the letters from the word ar in the dictionary. If not , we make them as keys and inicialize the value with an empty list and append the word to the corresponded key.
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

I used the output to be stored in a file because it's easier to keep the result. We can rerun the program and add the new words to the list, and it's easier to read.  
We use the variable `grup` to get the values from the dictionary and to give them some space between the words , by using `' '.join(grup)'` 
```python
 with open("result.txt", "w") as output:
        for grup in dictionary_anagram.values():
            output.write(' '.join(grup) + '\n')
```
### Version 2 ([anagram_v2](https://github.com/glemiu6/Anagram/blob/master/Code/anagram_v2.py))

This is an improved version of the [anagram](https://github.com/glemiu6/Anagram/blob/master/Code/anagram.py) function for larger files.  
This function uses `defaultdict` from the library `collections`. The reason for using this instead of a classical dictionary `{}`, it's because the `defaultdict(list)` automatically initialize the key with a list, making the code cleaner and faster.
```
 dictionary_anagram = defaultdict(list)
```
We open a file and read from it. We iterate through the file and remove the white spaces from the word.
Make a variable `char_count` that has the same size as an alphabet. The reason for making a frequency count it's because it's faster than a sorting algorithm, making it a better use for large input files.
After that we iterate through the word and subtract the value of the word's letter and the value of letter `a` , giving us the position of the letter in our value `char_count`.
```python
        for word in file:
            word = word.strip()
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
```
The output will look like this for now:
```
{
        (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['act', 'cat'],
         (0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0): ['tree'], 
         (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0): ['race', 'care', 'acre'], 
         (0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0): ['bee']
}
```

To store the values of the dictionary , we create a file named `result.txt` and using the ` ' '.join(grup)+/n` we get rid of the list's brackets and the comma.
```python
 with open("result.txt", "w") as output:
        """
        create a file to write the output
        """
        for grup in dictionary_anagram.values():
            output.write(' '.join(grup) + '\n')
    return f'The result is stored in the file result.txt'
```


--- 

## Maintainability

- For the code [anagram](https://github.com/glemiu6/Anagram/blob/master/Code/anagram.py), I added some comments about the meaning of every line.  
- The documentation about this code is writen above in [Explanation about the code](#Explanation-about-the-code).  
- For version control I use Git.

---

## Scalability
The program [anagram](https://github.com/glemiu6/Anagram/blob/master/Code/anagram.py) is a better approach if the input file has a small number of words.  
But if the file size is getting bigger this program won't be too efficient.  
That's why I made an improved version of the program that has a better time complexity:
- [anagram_v2](https://github.com/glemiu6/Anagram/blob/master/Code/anagram_v2.py)  
The main difference between the two programs is that one uses a frequency method and the other uses a sorting algorithm. 






---
## Performance
The code [anagram](https://github.com/glemiu6/Anagram/blob/master/Code/anagram.py) has a time complexity of `O(N * M log (M))` where:  

- N is the amount of words that are in the file
- M  is the average length of a word

 But if we approximate , the time complexity will be `O(n log(n))`.  
 In this code we used a sorting algorithm, that's the reason why the time is `log(n)`

But the code [anagram_v2](https://github.com/glemiu6/Anagram/blob/master/Code/anagram_v2.py) has a better time complexity :` O(M*N)`.  
If we were to approximate it,we will have a time of `O(n) `.  
The reason for this better time complexity is that we use a frequency count instead of a sorting.   

To see the difference in time for the following input file , I make a function that calculates the time of execution of the function [time_execution]().  
- For the [anagram](https://github.com/glemiu6/Anagram/blob/master/Code/anagram.py) we got:
- 