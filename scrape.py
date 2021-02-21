
import urllib3
http = urllib3.PoolManager()

def url2content(url):
    r = http.request('GET',url)
    return r.data

skey = '<meta name="citation_pdf_url" content="'
ekey = '">'

def content2pdf(content):
    sidx,eidx=-1,-1

    try:
        sidx = content.index(skey) + len(skey)
    except:
        sidx = -2

    if sidx > 0:
        try:
            eidx = content[sidx:].index(ekey)
        except:
            eidx = -2
        if eidx > 0:
            return content[sidx:sidx+eidx]
    return ""

if __name__ == "__main__":
    lst = open('cdbc.filtered.lst', 'r')
    Lines = lst.readlines()
    for line in Lines:
        content = url2content(line.strip())
        # if wrong url or 
        if content == "": continue
        pdf = content2pdf(content)
        # if no support for pdf download
        if pdf == "": continue
        import wget
        filename = wget.download(pdf)