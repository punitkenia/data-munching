from lxml import etree
import os
import argparse
import csv

def xml2csv(file_obj):
    obj = etree.parse(file_obj)
    root_tag = obj.getroot()
    writer = csv.writer('out_file.csv', 'w')
    for each in root_tag.iterchildren():
        print(each.text)
        print(each.tag)

parser = argparse.ArgumentParser()
parser.add_argument('filename', metavar='source file path', type=str, help='XML filename to be converted to CSV')
args = parser.parse_args()

if __name__ == '__main__':
    if os.path.exists(args.filename) and os.path.isfile(args.filename):
        with open(args.filename, 'r') as xml_file:
            xml2csv(xml_file)
