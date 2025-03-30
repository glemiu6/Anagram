def anagram(sample:str) ->str:
    """
    :param sample:file
    :return: None -> writes in a file the output
    """
    dictionary_anagram = {}
    """
    read from the file (sample)
    """
    with open(sample, "r") as file:
        words = [line.strip() for line in file.readlines()] # [act,cat,tree,race,care,acre,bee]
    """
    add the letters from the words to the dictionary
    """
    for word in words:
        sorted_word = tuple(sorted(word.lower()))
        if sorted_word not in dictionary_anagram:
            dictionary_anagram[sorted_word] = []
    #add the word to it's key
        dictionary_anagram[sorted_word].append(word)
    """
    Create a file and add the anagrams
    """
    with open("result.txt", "w") as output:
        for grup in dictionary_anagram.values():
            output.write(' '.join(grup) + '\n')

    return 'The result are in the file result.txt'


if __name__ == "__main__":
    print(anagram('sample.txt'))
