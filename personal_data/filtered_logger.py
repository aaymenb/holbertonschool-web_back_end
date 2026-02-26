import re

def filter_datum(fields, redaction, message, separator):
    """ Obfuscates specific fields in a log message using regex """
    pattern = '|'.join([f"{f}=.*?{separator}" for f in fields])
    return re.sub(pattern, lambda m: f"{m.group().split('=')[0]}={redaction}{separator}", message)
