"""
This program counts how mand vowels and consonants there are in a given sentence.
"""


def main():

    input_string = str(input("Enter a sentence:"))
    
    vowels = ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u")

    consonants = ("B", "b", "C", "c", "D", "d", "F", 
                  "f", "G", "g", "H", "h", "J", "j", 
                  "K", "k", "L", "l", "M", "m", "N", 
                  "n", "P", "p", "Q", "q", "R", "r", 
                  "S", "s", "T", "t", "V" , "v", "w", 
                  "w", "X", "x", "Y", "y", "Z", "z")

    count_vowels = 0

    count_consonants = 0

    for ch in input_string:
        if ch in vowels:
            count_vowels += 1
        elif ch in consonants:
            count_consonants += 1



    print(f"There are {count_vowels} vowels in that sentence.")
    print(f"There are {count_consonants} consonants in that sentence.")


if __name__ == "__main__":
    main()