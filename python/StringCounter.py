import tarfile
import io


def countContent(contents : str, min_str_length : int = 8, max_str_length : int = 40):
    splitContents = contents.split("\\r\\n")
    totalCounts = {}
    for content in splitContents:
        cnts = countStrings(content,min_str_length,max_str_length)
        totalCounts.update(cnts)
    return totalCounts

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

