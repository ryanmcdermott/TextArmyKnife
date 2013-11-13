from bs4 import BeautifulSoup
from write_tak import write_tak

#################################################################################
# Basic text processing
#################################################################################
        
def lower_case(txt, output_file=None):
    lowered = txt.lower()
    write_tak(lowered, output_file)
    return lowered

def upper_case(txt, output_file=None):
    uppered = txt.lower()
    write_tak(uppered, output_file)
    return uppered
    
## A naive way of compressing text by removing line breaks. 
## Useful for HTML and JS compression.
def compress_text(txt, output_file=None):
    txt = txt.replace('\n','')
    write_tak(txt, output_file)
    return txt

## Python's len() is used
def character_count(txt, output_file=None):
    cnt = len(txt)
    write_tak(cnt, output_file)
    return cnt

## Format HTML with BeautifulSoup
def format_html(txt, output_file=None):
    bs = BeautifulSoup(txt)
    formatted = bs.prettify().encode('utf-8')
    write_tak(formatted, output_file)
    return formatted