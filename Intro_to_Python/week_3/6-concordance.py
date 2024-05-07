"""A file concordance tracks the unique words in a paragraph and their frequencies. Write a program that displays a concordance for a paragraph. 
The program should output the unique words and their frequencies in alphabetical order. The program should be case insensitive (ignores whether capital or lowercase letters). 
Use the following paragraph:

\"Never give in — Never, never, never, never, in nothing great or small, large or petty, never give in except to convictions of honour and good sense. 
Never yield to force; never yield to the apparently overwhelming might of the enemy. O horror, horror, horror. Words, words, word. But you never know now do you now do you now do you.\""""
# this was a very difficult assignment but fun none the less

def concordance():
    unique_words = sorted(set(paragraph.lower().split()))

    # this expression iterates over each welemend of unique words and for each word, it sets the value 1 to start
    word_counts = {word: 1 for word in unique_words}

    for word in paragraph:
        if word in unique_words:
            word_counts[word] +=1
    
    for element in word_counts:
        print(f'{element}: {word_counts[element]}')

if __name__=="__main__":
    paragraph="Never give in — Never, never, never, never, in nothing great or small, large or petty, never give in except to convictions of honour and good sense. Never yield to force; never yield to the apparently overwhelming might of the enemy. O horror, horror, horror. Words, words, word. But you never know now do you now do you now do you."
    concordance()