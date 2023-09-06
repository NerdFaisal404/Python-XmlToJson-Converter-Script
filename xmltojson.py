import json
import xmltodict

def convert_xml_to_json(xml_file, json_file):
    with open(xml_file, 'r') as f:
        xml_content = f.read()
        json_content = json.dumps(xmltodict.parse(xml_content))
        with open(json_file, 'w') as f_json:
            f_json.write(json_content)

if __name__ == "__main__":
    # Change these file paths as per your requirements
    xml_file_path = '/Users/faisalahmed/Desktop/python automation/file/file_name.xml'
    json_file_path = '/Users/faisalahmed/Desktop/python automation/file/file_name.json'
    convert_xml_to_json(xml_file_path, json_file_path)