from goto import with_goto

@with_goto
def program():
    ignoredWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves",
                    "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself",
                    "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs",
                    "themselves",
                    "what", "which", "who", "whom", "this", "that", "these", "those",
                    "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                    "does", "did", "doing",
                    "a", "an", "the", "and", "but", "if", "or", "because", "as",
                    "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
                    "into", "through", "during", "before", "after", "above", "below", "to", "from",
                    "up", "down", "in", "out", "on", "off", "over", "under", "again", "further",
                    "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only",
                    "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"

    with open("input1.txt", "r") as file:
        text = file.read()
    text += "$"
    
    str = ""
    i = 0
    label.edit
    if text[i] in lower:
        str += text[i]
    elif text[i] in upper:
        j = 0
        label.lowering
        if text[i] != upper[j]:
            j += 1
            goto.lowering
        str += lower[j]
    elif text[i] == "\n" or text[i] == " ":
        str += " "
    elif text[i] == "$":
        text = str + "$"
        goto.editEnd
    i += 1
    goto.edit
    label.editEnd

    word = ""
    result = [[None, 0]]
    i = 0
    label.counter
    if text[i] == " ":
        if word in ignoredWords:
            word = ""
            i += 1
            goto.counter
        j = 0
        label.wordInserter
        if word == result[j][0]:
            result[j][1] += 1
            word = ""
            i += 1
            goto.counter
        elif result[j][0] == None:
            result[j][0] = word
            result[j][1] = 1
            result += [[None, 0]]
            word = ""
            i += 1
            goto.counter
        else:
            j += 1
            goto.wordInserter
    elif text[i] == "$":
        result = result[:-1]
        wordCount = j
        goto.counterEnd
    else:
        word += text[i]
    i += 1
    goto.counter
    label.counterEnd
    
    i = 0
    label.sorter
    maxId = i
    j = i + 1

    label.sorterInner
    if result[maxId][1] < result[j][1]:
        maxId = j
    if j >= wordCount:
        goto.sorterInnerEnd
    j += 1
    goto.sorterInner

    label.sorterInnerEnd
    result[i], result[maxId] = result[maxId], result[i]
    i += 1
    if i >= wordCount:
        goto.sorterEnd
    goto.sorter

    label.sorterEnd
    i = 0
    label.printer
    print(f"{result[i][0]} - {result[i][1]}")
    if i < wordCount and i < 4 - 1:
        i += 1
        goto.printer
    return

program()