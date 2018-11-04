# It's distributed under the MIT license (https://choosealicense.com/licenses/mit/)
def read(filename, createFileIfNotExist=False):
    try:
        f = open(filename, 'r')
        text = f.read()
        f.close()
    except:
        if createFileIfNotExist:
            write(filename)
        
            text = read(filename)
        else:
            return None
        
    return text

def write(filename, data='', increment=False):
    data = str(data)

    if increment:
        text = read(filename, createFileIfNotExist=True)
        data = text + data + '\n'
        
    f = open(filename, 'w')
    n = f.write(data)
        
    f.close()

    return n

def find(filename, multipleFiles=False, path = "."):
    import os, re

    files = {}
    
    for f in os.listdir(path):
        if re.match(filename, f):
            if not multipleFiles:
                return {f:read(f)}
            
            files[f] = read(f)
    
    return files