import re, json

def replaceWords(originalString, replacementWords):
    if replacementWords == '':
            return originalString
    for replaceEntry in json.loads(replacementWords):
            originalWord =  replaceEntry['replace'].encode("ascii")
            newWord = replaceEntry['with'].encode("ascii")
            wordLengthDifference = len(newWord) - len(originalWord) 
            offset = 0
            regex = re.compile(r"[^a-zA-Z0-9]" + originalWord + "[^a-zA-Z0-9]", re.IGNORECASE)
            for match in regex.finditer(originalString):
                startIndex = match.start() + 1 + offset
                endIndex = match.end() - 1 + offset
                originalString = originalString[:startIndex] + newWord + originalString[endIndex:]
                offset += wordLengthDifference
    return originalString