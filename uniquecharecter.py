def count(string):
    unique_chars = set(string)
    return len(unique_chars)
string = " hey hello guys ,welcome to github."
unique_count = count(string)
print("unique characters:", unique_count)