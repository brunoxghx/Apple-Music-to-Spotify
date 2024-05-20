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

# Specify the path to your Apple Music XML library file
xml_file = 'Library.xml'

# Extract song names from the XML file
song_names = extract_song_names_from_file(xml_file)

# Sort the song names alphabetically
song_names.sort()

# Create a DataFrame and save it to an Excel file
df = pd.DataFrame(song_names, columns=['Song Name'])
excel_file = 'song_names.xlsx'
df.to_excel(excel_file, index=False)

print(f'Extracted {len(song_names)} song names, sorted them, and saved to {excel_file}')