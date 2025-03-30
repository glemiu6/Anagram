
from collections import defaultdict
def anagram(sample):
    """

    :param sample:
    :return:
    """
    dictionary_anagram = defaultdict(list)
    with open(sample, "r") as file:
        for word in file:
            word = word.strip()
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1

            key = tuple(char_count)
            dictionary_anagram[key].append(word)

    with open("result.txt", "w") as output:
        for grup in dictionary_anagram.values():
            output.write(' '.join(grup) + '\n')
    return f'The result is stored in the file result.txt'

if __name__ == '__main__':
    print(anagram("sample.txt"))