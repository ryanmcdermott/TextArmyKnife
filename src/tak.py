import argparse
import re
from strip_tags import strip_tags
from translate import translate
from write_tak import write_tak
from basic_text_processing import *
from sentiment_analysis import sentiment_analysis

#################################################################################
## Argument declarations
#################################################################################
parser = argparse.ArgumentParser(description='Text Army Knife (TAK) \n ')
parser.add_argument('-t','--text', help='Text input', required=False)
parser.add_argument('-f','--file', help='Input file', required=False)
parser.add_argument('-o','--out_file', help='Output TAK text to a file', required=False)
parser.add_argument('-lc', action='store_true', help='Convert text to lowercase', required=False)
parser.add_argument('-uc', action='store_true', help='Convert text to uppercase', required=False)
parser.add_argument('-compress', action='store_true', help='Compress text by eliminating line breaks', required=False)
parser.add_argument('-sentiment', action='store_true', help='Perform sentiment analysis on the text using NLTK', required=False)
parser.add_argument('-count', action='store_true', help='Count characters', required=False)
parser.add_argument('-strip', action='store_true', help='Strip HTML tags', required=False)
parser.add_argument('-translate', action='store_true', help='Translate your text', required=False)
parser.add_argument('-format', action='store_true', help='Prettify your HTML to be properly formatted', required=False)
parser.add_argument('-from','--from', help='Translate from', required=False)
parser.add_argument('-to','--to', help='Translate to', required=False)
args = vars(parser.parse_args())

#################################################################################
## Initializers
#################################################################################
text = None
file = None

if args['out_file']:
    output_file = args['out_file']
else:
    output_file = None

if args['text'] and args['file'] is not None:
    exit("Cannot process both text and a file")

if args['text']:
    text = args['text']

if args['file']:
    f = open(args['file'])
    text = f.read()

#################################################################################
## Handle arguments
#################################################################################
if text is not None:
    if args['lc']:
        print lower_case(text, output_file)
 
    if args['uc']:
        print upper_case(text, output_file)

    if args['strip']:
        print strip_tags(text, output_file)
    
    if args['compress']:
        print compress_text(text, output_file)
    
    if args['count']:
        print character_count(text, output_file)
        
    if args['format']:
        print format_html(text, output_file)
        
    if args['sentiment']:
        print sentiment_analysis(text, output_file)
        
    if args['translate']:
        if args['from'] and args['to'] is not None:
            from_language = args['from'].lower()
            to_language = args['to'].lower()
            translate(text, from_language, to_language, output_file)
        else:
            exit("Needs a language to translate from and to")
            
else:
    exit("Text or input file required to parse")