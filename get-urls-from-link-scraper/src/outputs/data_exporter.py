thonimport json
import logging

def export_data(urls, output_file):
    try:
        with open(output_file, 'w') as f:
            json.dump({"urls": urls}, f, indent=4)
        logging.info(f"Data successfully exported to {output_file}")
    except Exception as e:
        logging.error(f"Error exporting data: {str(e)}")