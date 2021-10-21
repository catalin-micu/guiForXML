import time
from xml.etree import ElementTree
from tkinter import filedialog
import json
import re
import lxml.etree as ET
import os


class FileParser:
    def __init__(self):
        self.xml_path = None
        self.basic_xml_root = None

        self.json_path = None
        self.json_dict = None

        self.xsl_path = None

    def browse_for_xml(self):
        file_path = filedialog.askopenfilename(initialdir='/guiForXML/data_files', title='Select the XML file',
                                               filetypes=(('xml files', '*.xml'), ('all files', '*.*')))
        self.xml_path = file_path
        self.basic_xml_root = ElementTree.parse(self.xml_path).getroot()

        return self.xml_path

    def display_xml(self):
        if not self.basic_xml_root:
            return 'No XML file has been loaded.\n'
        output = ''
        for child in self.basic_xml_root:
            output += '\n***********************************************\n'
            output = output + self.format_node_as_string(child)
            output += '\n'

        return output

    def format_node_as_string(self, node):
        output = ''
        for n in node.getchildren():
            if n.tag == 'titlu_spectacol':
                s = re.sub(r'\s{2,}', '', n.text)
                output = output + f'\nTitlu: {s}'
            if n.tag == 'adresa':
                s = re.sub(r'\s{2,}', '', n.text)
                output = output + f'\nAdresa: {s}'
            if n.tag == 'participanti':
                output = output + '\nComedianti: * '
                for nn in n.getchildren():
                    s = re.sub(r'\s{2,}', '', nn.text)
                    output = output + f'{s} * '
            if n.tag == 'pret_bilet':
                output += '\nPret bilet '
                output += '{tip}: {val}'.format(tip=n.attrib['tip'], val=re.sub(r'\s{2,}', '', n.text))
            if n.tag == 'data':
                s = re.sub(r'\s{2,}', '', n.text)
                output += f'\nData: {s}'

        return output

    def browse_for_json(self):
        file_path = filedialog.askopenfilename(initialdir='/guiForXML/data_files', title='Select the JSON file',
                                               filetypes=(('json files', '*.json'), ('all files', '*.*')))
        self.json_path = file_path
        with open(self.json_path) as path:
            data = json.load(path)
        self.json_dict = data

        return self.json_path

    def display_json(self):
        if not self.json_dict:
            return 'No JSON file has been loaded.\n'
        output = '\n'

        for item in self.json_dict['evidenta_spectacolelor']:
            output += '----------------------------------------------------------------\n'
            output += 'Titlu: {}\n'.format(item['titlu'])
            output += 'Adresa: {}\n'.format(item['adresa'])
            output += 'Data: {}\n'.format(item['data'])
            output += 'Ora: {}\n'.format(item['ora'])

            output += 'Comedianti:\n'
            for d in item['participanti']:
                s = '\t{com}, {rol}\n'.format(com=d['comediant'], rol=d['rol_in_spectacol'])
                output += s

            output += 'Preturi:\n'
            for d in item['preturi']:
                s = '\t{tip}, {val} {mon}\n'.format(tip=d['tip'], val=d['pret'], mon=d['moneda'])
                output += s

            output += '\n'

        return output

    def browse_for_xsl(self):
        file_path = filedialog.askopenfilename(initialdir='/guiForXML/data_files', title='Select the XSL file',
                                               filetypes=(('xsl files', '*.xsl'), ('all files', '*.*')))
        self.xsl_path = file_path

        return self.xsl_path

    def dynamic_query(self, comediant=None, oras=None, pret=None):
        if not self.json_dict:
            return 'No JSON file has been loaded.\n'

        obj = self.json_dict.copy()['evidenta_spectacolelor']
        matched_items = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

        if comediant != '-':
            temp = set()
            for item in obj:
                for c in item['participanti']:
                    if c['comediant'] == comediant:
                        temp.add(obj.index(item))

            matched_items = matched_items.intersection(temp)

        if oras != '-':
            temp = set()
            for item in obj:
                if oras in item['adresa']:
                    temp.add(obj.index(item))

            matched_items = matched_items.intersection(temp)

        if pret != '-':
            price = int(re.sub(r'[^\d]', '', pret))
            temp = set()
            for item in obj:
                for p in item['preturi']:
                    if int(p['pret']) < price:
                        temp.add(obj.index(item))
                    # break

            matched_items = matched_items.intersection(temp)

        output = '\n'
        if len(matched_items) == 0:
            return output + 'There are no shows that match the selected criteria.\n'
        for index in matched_items:
            item = obj[index]
            output += '----------------------------------------------------------------\n'
            output += 'Titlu: {}\n'.format(item['titlu'])
            output += 'Adresa: {}\n'.format(item['adresa'])
            output += 'Data: {}\n'.format(item['data'])
            output += 'Ora: {}\n'.format(item['ora'])

            output += 'Comedianti:\n'
            for d in item['participanti']:
                s = '\t{com}, {rol}\n'.format(com=d['comediant'], rol=d['rol_in_spectacol'])
                output += s

            output += 'Preturi:\n'
            for d in item['preturi']:
                s = '\t{tip}, {val} {mon}\n'.format(tip=d['tip'], val=d['pret'], mon=d['moneda'])
                output += s

            output += '\n'
        return output

    def render_xsl(self):
        if not self.xml_path:
            return 'No XML file has been loaded.\n'
        if not self.xsl_path:
            return 'No XSL file has been loaded.\n'

        dom = ET.parse(self.xml_path)
        xslt = ET.parse(self.xsl_path)
        transform = ET.XSLT(xslt)
        new_dom = transform(dom)

        f = open('xsl_html.html', 'a')
        html_string = re.sub(r'\\n|\\t|b\'', '', str(ET.tostring(new_dom, pretty_print=True)))
        f.write(html_string)
        f.close()

        os.startfile('xsl_html.html')
        time.sleep(1)
        os.remove('xsl_html.html')

        return 'The stylesheet page has opened up in browser.'


if __name__ == '__main__':
    thing1 = FileParser()
    # thing1.dynamic_query('-', '-', 'sub 100 ron')
    thing1.render_xsl()
    # print(ElementTree.dump(a))
    b=2
