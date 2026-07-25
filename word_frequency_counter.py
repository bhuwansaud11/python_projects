#Python Word Frequency Counter 
import os
import string
from collections import Counter

def clean(word):
    return word.strip(string.punctuation+"\n\r").lower()
def main():
    print("---------------------------")
    print("  WORD FREQUENCY COUNTER   ")
    print("---------------------------")

    filename = input("Enter the file name: ")
    stoppage_words = {"is", "and", "a", "can", "has"}
    word_freq = []
    word_freq1={}

    if os.path.exists(filename):
        with open(filename,'r') as file:
            lines = file.read().split()

            #// COUNTER METHOD
            # for word in lines:
            #     raw = clean(word)
            #     if not raw or raw in stoppage_words:
            #       continue
            #     word_freq.append(raw)                 
            # word_count = Counter(word_freq)
            # # print(word_count)

            # highest_freq = Counter(word_freq).most_common(10)
            # print(highest_freq)
                
            #NORMAL METHOD
            for word in lines:
                raw = clean(word)

                if not raw or raw in stoppage_words:
                    continue

                word_freq1[raw] = word_freq1.get(raw,0) + 1
            print("---------------------------")
            print("WORDS FREQUENCY")
            print("---------------------------")
            for keys, values in word_freq1.items():
                print(f"{keys}:{values}")

            top_ten = dict(sorted(word_freq1.items(), key = lambda item: item[1], reverse=True)[:10])
            print("-------------------------------------")
            print("TOP 10 WORDS WITH HIGHEST FREQUENCY")
            print("-------------------------------------")
            for keys,values in top_ten.items():
                print(f"{keys}:{values}")

    else:
        print("Invalid file name...Please try again!")


main()