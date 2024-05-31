def words(string):
    words = string.split()
    return len(words)
string = "hi i am hariharan, so you?"
word_count = words(string)
print("Number of words:", word_count)