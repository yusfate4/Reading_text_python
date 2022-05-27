# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



from itertools import count


def read_file_content(filename):
    # [assignment] Add your code here 
    with open("story.txt") as file:
        filename = file.read()
        return filename

# print(read_file_content("story.txt"))


def count_words():
    str = read_file_content("./story.txt")
    counts = dict ()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
                counts[word] = 1
    return counts
print(count_words())                
   





