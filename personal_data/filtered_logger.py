import re

def filter_datum(fields, redaction, message, separator):
    """ Obfuscates specific fields in a log message using a single regex """
    return re.sub(f"({'|'.join(fields)})=.*?{separator}", f"\\1={redaction}{separator}", message)
