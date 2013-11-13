## Write out the output_file from TAK parsing
def write_tak(txt, output_file=None):
    if output_file is not None:
        f = open(output_file,'w')
        f.write(txt)