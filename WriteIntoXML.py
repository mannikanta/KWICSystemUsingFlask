# import xml.etree.ElementTree as ET
#
# def saveToXMLfile(sentences):
#     root = ET.Element('root');
#     subRoot = ET.SubElement(root, 'originalSentence');
#     subRoot.text = sentences[0];
#     for i in range(1, len(sentences)):
#         sorted_Sentences = ET.SubElement(subRoot, 'sentence');
#         sorted_Sentences.text = sentences[i];
#     tree = ET.ElementTree(root)
#     tree.write('./sentences.xml')

import xml.etree.ElementTree as ET

def saveToXMLfile(sentences):
    try:
        # Parse existing XML file if it exists
        tree = ET.parse('resources/sentences.xml')
        root = tree.getroot()
    except FileNotFoundError:
        # If the file doesn't exist, create a new root element
        root = ET.Element('root')

    # Create a new subRoot element for the original sentence
    subRoot = ET.SubElement(root, 'originalSentence')
    subRoot.text = sentences[0]

    # Create subelements for sorted sentences and append them
    for i in range(1, len(sentences)):
        sorted_Sentences = ET.SubElement(subRoot, 'sentence')
        sorted_Sentences.text = sentences[i]

    # Write the updated XML back to the file
    tree = ET.ElementTree(root)
    tree.write('./resources/sentences.xml')

def readDataFromXML(filePath, actualSearchSentence):
    sentences_list = []
    tree = ET.parse(filePath)
    root = tree.getroot()
    for original_sentence in root.findall('originalSentence'):
        original_text = original_sentence.text.strip()
        if actualSearchSentence in original_text:
            sentences_list.append(original_text);

        # Iterate through each <sentence> element within <originalSentence>
        for sentence in original_sentence.findall('sentence'):
            sentence_text = sentence.text.strip()
            # print(" - Sentence:", sentence_text)
            if actualSearchSentence in sentence_text:
                sentences_list.append(sentence_text);

    return sentences_list;
