import httplib
import urlparse
import re
import string
from sys import stdout
# Unshortens URLs
def unshorten_url(url):
    if hasattr(url, 'group'):
        url = url.group(0)
    parsed = urlparse.urlparse(url)
    h = httplib.HTTPConnection(parsed.netloc)
    resource = parsed.path
    if parsed.query != "":
        resource += "?" + parsed.query
    h.request('HEAD', resource )
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        print response.getheader('Location')
        return unshorten_url(response.getheader('Location')) # changed to process chains of short urls
    else:
        return url


def get_gcm_key(url):
    ex = re.compile(r'goo.gl')
    if ex.search(url) != None:
        print('goo.gl URL found, unshortening.')
        print('Running unshorten with url ?',url)
        test = unshorten_url(url)
        if re.match(r'http://autoremotejoaomgcd.appspot.com/',test):
            print('Found Autoremote URL, getting key.')
            key = string.split(test,'=')
            return key[-1]
        else:
            return 'No key'