import xml.etree.ElementTree as xml_helper

def convert_from_xml_to_dict(xml_file):
    """Converts a xml file to a dictionary"""

    tree = xml_helper.parse(xml_file)
    root = tree.getroot()

    return _get_dictionary(root)



def _get_dictionary(node):
    """Iterate over xml tree recursively. It's like a DFS algorithm (Depth First Search)"""

    children = node.getchildren()

    if not children:
        # if there are no children, that means we got a leaf
        return {node.tag: node.text or ''}

    # if is not a leaf, it will continue recursively
    return {
        node.tag: [_get_dictionary(child) for child in children]
    }
