import argparse
import xml.etree.ElementTree as ET
import pandas as pd

def extract_song_names_from_file(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    song_names = []

    # We need to keep track of whether the last key was "Name"
    last_was_name_key = False

    # Iterate through all elements in the root
    for elem in root.iter():
        if last_was_name_key and elem.tag == 'string':
            # The last key was "Name", so this element should be the song name
            song_names.append(elem.text)
            last_was_name_key = False
        elif elem.tag == 'key' and elem.text == 'Name':
            # This key is "Name", so the next string element should be the song name
            last_was_name_key = True
        else:
            last_was_name_key = False

    return song_names

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract song names from an Apple Music XML library file.")
    parser.add_argument("xml_file", type=str, help="Path to the Apple Music XML library file.")
    parser.add_argument("output_file", type=str, help="Path to save the Excel file with extracted song names.")
    args = parser.parse_args()

    xml_file = args.xml_file
    output_file = args.output_file

    # Extract song names from the XML file
    song_names = extract_song_names_from_file(xml_file)

    # Sort the song names alphabetically
    song_names.sort()

    # Create a DataFrame and save it to an Excel file
    df = pd.DataFrame(song_names, columns=['Song Name'])
    df.to_excel(output_file, index=False)
    print(f'Extracted {len(song_names)} song names, sorted them, and saved to {output_file}')

if __name__ == "__main__":
    main()