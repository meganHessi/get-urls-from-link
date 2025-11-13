thonimport re
import logging

def apply_filters(urls, exclude_extensions=None, url_patterns=None, max_urls=None):
    try:
        if exclude_extensions:
            urls = [url for url in urls if not any(url.endswith(ext) for ext in exclude_extensions)]

        if url_patterns:
            urls = [url for url in urls if any(re.search(pattern, url) for pattern in url_patterns)]

        if max_urls:
            urls = urls[:max_urls]

        logging.info(f"After filtering, {len(urls)} URLs remain.")
        return urls
    except Exception as e:
        logging.error(f"Error applying filters: {str(e)}")
        return []