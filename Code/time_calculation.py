import time
from anagram import anagram
import anagram_v2

if __name__ == '__main__':
    start = time.time()
    anagram('sample.txt')
    end = time.time()

    print(f"Time of execution: {end - start:.5f} seconds")


if __name__ == '__main__':
    start = time.time()
    anagram_v2.anagram('sample.txt')
    end = time.time()
    print(f"Time of execution: {end - start:.5f} seconds")