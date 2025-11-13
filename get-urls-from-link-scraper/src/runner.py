thonimport os
import logging
from extractors.url_extractor import extract_urls
from filters.path_filter import apply_filters
from outputs.data_exporter import export_data
import json

# Setup logging
logging.basicConfig(level=logging.INFO)

def run_scraper(input_file, output_file, max_urls=100, exclude_extensions=None, url_patterns=None):
    try:
        # Extract URLs from the provided file
        logging.info(f"Starting URL extraction from {input_file}")
        extracted_urls = extract_urls(input_file)

        # Apply URL filters
        logging.info(f"Applying filters to extracted URLs")
        filtered_urls = apply_filters(extracted_urls, exclude_extensions, url_patterns, max_urls)

        # Export the result
        logging.info(f"Exporting data to {output_file}")
        export_data(filtered_urls, output_file)

        logging.info("Scraping process completed successfully.")
    except Exception as e:
        logging.error(f"Error occurred during the scraping process: {str(e)}")

if __name__ == "__main__":
    input_file = "data/sitemap_sample.xml"
    output_file = "data/urls_output.json"
    run_scraper(input_file, output_file)