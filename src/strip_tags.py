from HTMLParser import HTMLParser
from write_tak import write_tak
#################################################################################
## HTML Strip courtesy of a kind StackOverflow answer. 
## I can't trace the source beyond this.
################################################################################# 
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html, output_file=None):
    s = MLStripper()
    s.feed(html)
    write_tak(s.get_data(), output_file)
    return s.get_data()