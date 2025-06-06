import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to the specified filename.
    
    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML to.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.
    
    Args:
        filename (str): The name of the XML file to read.
    
    Returns:
        dict: The deserialized dictionary.
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
