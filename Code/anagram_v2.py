import time
from collections import defaultdict
def anagram(sample):
    """

    :param sample:file
    :return: None: writes in a file the output
    """
    dictionary_anagram = defaultdict(list)
    """
    with defaultdict(list) we don't need to create a list every time we add a new key
    #Exemple:{['a','s']=[]}
    """

    with open(sample, "r") as file:
        """
            open a file and iterate through the file and getting rid of the white spaces
            make a list of chars that will keep track of every letter that are present in the word 
        """
        for word in file:
            word = word.strip()
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            """
            make the key a tuple so it can't be changed and the value of the key will be the list of numbers where the number represent the letter 
            """
            key = tuple(char_count)
            dictionary_anagram[key].append(word)

        """
        {
        (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['act', 'cat'],
         (0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0): ['tree'], 
         (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0): ['race', 'care', 'acre'], 
         (0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0): ['bee']
         }
        """

    with open("result.txt", "w") as output:
        """
        create a file to write the output
        """
        for grup in dictionary_anagram.values():
            output.write(' '.join(grup) + '\n')
    return f'The result is stored in the file result.txt'

if __name__ == "__main__":
    print(anagram('sample.txt'))
