import re, json

def replaceWords(originalString, replacementWordsJson):
    if replacementWordsJson == '':
            return originalString
    for replaceEntry in json.loads(replacementWordsJson):
            originalWord =  replaceEntry['replace'].encode("ascii")
            newWord = replaceEntry['with'].encode("ascii")
            wordLengthDifference = len(newWord) - len(originalWord) 
            offset = 0
            regex = getWordRegex(originalWord)
            for match in regex.finditer(originalString):
                startIndex = match.start() + 1 + offset
                endIndex = match.end() - 1 + offset
                originalString = originalString[:startIndex] + newWord + originalString[endIndex:]
                offset += wordLengthDifference
    return originalString
    
def getWordRegex(word):
    return re.compile(r"[^a-zA-Z0-9]" + word + "[^a-zA-Z0-9]", re.IGNORECASE)
    
def numberOfMatches(originalString, replacementWordsJson):
    numberOfMatches = 0
    if replacementWordsJson == '':
        return numberOfMatches
    for replaceEntry in json.loads(replacementWordsJson):
        originalWord =  replaceEntry['replace'].encode("ascii")
        regex = re.compile(r"[^a-zA-Z0-9]" + originalWord + "[^a-zA-Z0-9]", re.IGNORECASE)
        regex.findall
        numberOfMatches += len(regex.findall(originalString))
    return numberOfMatches