def word_count(s):

    #create cache
    cache = {}

    #make s all lowercase
    newS = s.lower()

    #split characters with a space
    ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    # for all characters in ignore
    # replace s with no spaces
    for character in ignore:
        newS = newS.replace(character, "")

    # for the words in s
    # if the word is equal to no space then keep going
    # if the word is not in the cache then add it
    # otherwise keep going 
    #then return the cache
    for word in newS.split():
        if word == "":
            continue
        if word not in cache:
            cache[word] = 1
        else:
            cache[word] += 1
    return cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))