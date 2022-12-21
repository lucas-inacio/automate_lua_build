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
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar)
            os.rename(tar.getnames()[0], './lua')
    except:
        print('Error')
    finally:
        if filename:
            os.remove(filename)