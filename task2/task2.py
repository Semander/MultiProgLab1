from goto import with_goto

@with_goto
def program():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    maxWords = 100
    wordsPerPage = 235
    lettersPerPage = 1800

    with open("input2.txt", "r", encoding="utf8") as file:
        content = file.read()
    content += "$"

    str = ""
    i = 0
    label.edit
    if content[i] in lower:
        str += content[i]
    elif content[i] in upper:
        j = 0
        label.lowering
        if content[i] != upper[j]:
            j += 1
            goto.lowering
        str += lower[j]
    elif content[i] == "\n" or content[i] == " ":
        str += " "
    elif content[i] == "$":
        content = str + "$"
        goto.editEnd
    i += 1
    goto.edit
    label.editEnd
    
    word = ""
    currentPage = 1
    letterCounter = 0
    wordCounter = 0
    wordsInResult = -1
    result = [[None, 0, []]]
    i = 0
    label.counter
    if content[i] == " ":
        j = 0
        wordCounter += 1
        if wordCounter >= wordsPerPage or letterCounter >= lettersPerPage:
            currentPage += 1
            letterCounter -= lettersPerPage
            wordCounter = 0
        label.wordInserter
        if word == result[j][0]:
            result[j][1] += 1
            if currentPage not in result[j][2]:
                result[j][2] += [currentPage]
            word = ""
            i += 1
            goto.counter
        elif result[j][0] == None:
            result[j][0] = word
            result[j][1] = 1
            result[j][2] += [currentPage]
            result += [[None, 0, []]]
            wordsInResult += 1
            word = ""
            i += 1
            goto.counter
        else:
            j += 1
            goto.wordInserter
    elif content[i] == "$":
        result = result[:-1]
        goto.counterEnd
    else:
        word += content[i]
    i += 1
    letterCounter += 1
    goto.counter
    label.counterEnd

    i = 0
    label.wThrower
    if result[i][1] > maxWords or result[i][0] == "":
        wordsInResult -= 1
        del result[i]
    else:
        i += 1
    if i >= wordsInResult:
        goto.wThrowerEnd
    goto.wThrower
    label.wThrowerEnd

    i = 0
    label.sorter
    maxId = i
    j = i + 1

    label.sorterInner
    if result[maxId][0] > result[j][0]:
        maxId = j
    if j >= wordsInResult:
        goto.sorterInnerEnd
    j += 1
    goto.sorterInner

    label.sorterInnerEnd
    result[i], result[maxId] = result[maxId], result[i]
    i += 1
    if i >= wordsInResult:
        goto.sorterEnd
    goto.sorter
    label.sorterEnd

    i = 0
    label.printer
    print(f"{result[i][0]} - {result[i][2]}")
    if i < wordsInResult:
        i += 1
        goto.printer
    return

program()