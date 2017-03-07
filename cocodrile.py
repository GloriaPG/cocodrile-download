import os
import urllib2
from shutil import copyfile

"""
Dowload plugin
"""
# URL to download plugin.
source_plugin = "http://sf-c01.sentinel.la:5580/plugins/download/" 

# Name plugin wiht version
name_plugin = "test2-1.4"

# Extension file
extension = "zip"

url = source_plugin + name_plugin + "." + extension


file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()


"""
Copy file to Sentinella
"""
copyfile("{0}.{1}".format(name_plugin, extension), "../{0}.{1}".format(name_plugin,extension))

"""
Remove file to this directory
"""
os.remove("{0}.{1}".format(name_plugin, extension))