import tarfile
import io
import unicodedata

# Parses out the content string to lines
def countContent(contents : str, min_str_length : int = 8, max_str_length : int = 40):
    splitContents = contents.split("\\r\\n")
    totalCounts = {}
    for line in splitContents:
        lineNoCC = remove_control_characters(line)
        cnts = countStrings(lineNoCC,min_str_length,max_str_length)
        totalCounts.update(cnts)
    return totalCounts

#
def countStrings(contents : str, min_str_length : int = 8, max_str_length : int = 40):
    counts={}
    for i in range(0,len(contents)-min_str_length+1):
        # print(i
        for j in range(min_str_length,max_str_length):
            if i+j<len(contents)+1:
                current_str = contents[i:i+j]
                if not current_str[0:1] in [' ', '\t', '\r', '\n']:
                    if current_str in counts:
                        counts[current_str]=counts[current_str]+1
                    else:
                        counts[current_str]=1
            else:
                break

    return counts

# Untar the files
def extractFileContent(file_object):
    bytes = io.BytesIO(file_object.get('Body').read())
    tar = tarfile.open(fileobj=bytes, mode='r:tar')
    content = ''
    for member in tar.getmembers():
        if '.metadata' not in member.name:
            f = tar.extractfile(member)
            # print(member, "   ", f)
            content = content + str(f.read())
    return content

def remove_control_characters(s):
    return s.replace("\\x00","").replace("\\x08","").replace("\\x01","").replace("\\x0","").replace("\\x14","").replace("\\x02","").replace("\\x1f","").replace("\\n","").replace("\\xe1Xt4","")
   # return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")