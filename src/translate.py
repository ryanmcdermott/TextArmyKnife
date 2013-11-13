import requests
from bs4 import BeautifulSoup
from languages import languages
import re
from write_tak import write_tak

#################################################################################
## Translations via querying Google translate. They give us Javascript data like so:
## [[["Hola mundo","Hello world","",""]],,"en",,[["Hola mundo",[4],1,0,497,0,2,0]],
## [["Hello world",4,[["Hola mundo",497,1,0],["Hello world",364,1,0]],[[0,11]],"Hello world"]]
## ,,,[["en"]],4]
##
## Google Translate splits up sentences and puts them into what look like JSON arrays
## WARNING: This function may violate Google's terms of service: No TAK developer is liable for any damages
#################################################################################
def translate(txt, from_language, to_language, output_file=None):
    from_language_abbrv = None
    to_language_abbrv = None
    sentences_unfiltered = list()
    sentences_list = list()
    original_punctuation = 0
    translated_punctuation = 0
    original_punctuation += txt.count('.')
    original_punctuation += txt.count('!')
    original_punctuation += txt.count('?')
    
    ## Google won't return results in our expected form without at least one punctuation mark. Strange...
    if original_punctuation == 0:
        txt += "."
        original_punctuation += 1
        
    ## Convert language name to Google's abbreviations
    for language, abbrv in languages.iteritems():
        if language == to_language:
            to_language_abbrv = abbrv
        if language == from_language:
            from_language_abbrv = abbrv
    if to_language_abbrv is None or from_language_abbrv is None:
        exit("Please enter a valid language. Check spelling!")
    
    ## Prepare the URL
    txt = txt.replace(" ", "%20")
    url = "http://translate.google.com/translate_a/t?client=t&sl=" + from_language_abbrv + "&tl=" + to_language_abbrv + "&hl=en&sc=1&ie=UTF-8&oe=UTF-8&ssel=0&tsel=0&q="
    url = url + txt
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5)'
    }
    ## Query Google and get back the unformatted JSON-like packets
    response = requests.get(url, headers=headers)
    unfiltered_tr = response.text
    
    pattern = re.compile(r'(?<=\[\")(.*?)(?=\",)')
    for (sentence) in re.findall(pattern, unfiltered_tr):
        sentences_unfiltered.append(sentence)
    
    for i in range(0, len(sentences_unfiltered)):
        ## Get an easier variable to work with
        sentence = sentences_unfiltered[i]
        ## Google has a tendency to add leading spaces between punctuation marks
        ## This is a lazy fix. NLTK fix for the future possibly?
        sentence = sentence.replace(" .", ".")
        sentence = sentence.replace(" !", "!")
        sentence = sentence.replace(" ?", "?")
        ######################################################################
        if translated_punctuation >= original_punctuation:
            break
        else:
            ## Count appearances of punctuation marks in the translated text
            translated_punctuation += sentence.count('.')
            translated_punctuation += sentence.count('!')
            translated_punctuation += sentence.count('?')
            sentences_list.append(sentence)
            
    sentences = ''.join(sentences_list).encode('utf-8')
    print sentences
    write_tak(sentences, output_file)
    return sentences
