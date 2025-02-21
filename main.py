def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    #print(file_contents)

    words = file_contents.split()
    num_words = len(words)
    print( f"{num_words} words found in the document")
    char_num(path_to_file)

def char_num(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    lower_file_contents = file_contents.lower()

    char_count = {}
    
    # Loop through each character in the string
    for char in lower_file_contents:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If it's not in the dictionary, add it with count 1
        else:
            char_count[char] = 1
    sorted_dict = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

   

# Iterate through the dictionary
    for key, value in sorted_dict.items():
        if key.isalpha():  # Check if the key is a letter in the alphabet
            print(f"The '{key}' character was found {value} times") #The 'e' character was found 46043 times


    #return sorted_dict
    #return char_count


main("books/frankenstein.txt")