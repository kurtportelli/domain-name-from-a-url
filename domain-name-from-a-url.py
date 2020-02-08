def domain_name(url):
    from urllib.parse import urlparse
    import re
    if not re.match('http', url):
        url = 'http://' + url
    netloc = urlparse(url).netloc
    if not re.match('www', netloc):
        netloc = 'www.' + netloc
    return netloc.split('.')[1]
