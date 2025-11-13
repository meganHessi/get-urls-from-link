thonimport xml.etree.ElementTree as ET
import logging

def extract_urls(input_file):
    try:
        logging.info(f"Parsing XML file {input_file}")
        tree = ET.parse(input_file)
        root = tree.getroot()

        urls = []
        for url in root.findall(".//url/loc"):
            urls.append(url.text)

        logging.info(f"Extracted {len(urls)} URLs from the XML file.")
        return urls
    except Exception as e:
        logging.error(f"Error extracting URLs: {str(e)}")
        return []