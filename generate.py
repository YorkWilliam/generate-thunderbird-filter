import json
from urllib.parse import quote
import argparse

def cat_to_folder(cat):
    return "".join(word.capitalize() for word in cat.split(" "))

def json_to_thunderbird_dat(json_source):
    protocal = json_source['protocal']
    email = json_source['email']
    server = json_source['server']
    folderdir = json_source['folderdir']
    filters = dict(sorted(json_source['filters'].items()))
    
    output = ['version="9"', 'logging="yes"']
    for folder, keywords in filters.items():
        print(f'\r Converting {folder}', end="")
        conditions = ' OR '.join([f'(from,contains,{keyword})' for keyword in keywords])
        filter_block = [
            f'name="{folder}"',
            'enabled="yes"',
            'type="17"',
            'action="Move to folder"',
            f'actionValue="{protocal}://{quote(email)}@{server}/{folderdir}/{cat_to_folder(folder)}"',
            f'condition="OR {conditions}"'
        ]        
        output.append('\n'.join(filter_block))
    output.append('')
    print('\r', end='')
    
    return '\n'.join(output)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='Input file path')
    parser.add_argument('-o', '--output', required=True, help='Output file path')
    args = parser.parse_args()
    
    try:
        print(f"Reading input file: {args.input}")
        with open(args.input, 'r') as infile:
            json_source = json.load(infile)
    except Exception as e:
        print(f"Error reading input file: {e}")
        return
    
    try:
        print(f"Converting to Thunderbird filter format")
        filters = json_to_thunderbird_dat(json_source)
    except Exception as e:
        print(f"Error converting to Thunderbird filter format: {e}")
        return
    
    try:
        print(f"Writing output file: {args.output}")
        with open(args.output, 'w') as outfile:
            outfile.write(filters)   
    except Exception as e:
        print(f"Error writing output file: {e}")
        return

if __name__ == "__main__":
    main()
