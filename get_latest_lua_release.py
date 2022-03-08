# This scripts downloads Lua latest release

import json
import os
import tarfile
from urllib import request

if __name__ == "__main__":
    filename = None
    try:
        req = request.urlopen('https://api.github.com/repos/lua/lua/releases/latest')
        body = req.read().decode('utf-8')
        j = json.loads(body)

        download_url = j['tarball_url']
        filename, headers = request.urlretrieve(download_url)
        with tarfile.open(filename) as tar:
            tar.extractall()
            os.rename(tar.getnames()[0], './lua')
    except:
        print('Error')
    finally:
        if filename:
            os.remove(filename)