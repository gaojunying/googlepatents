# googlepatents
Download pdf download using patents ID in google patents
## Scraping Scenario
- to get web content from url
- to get pdf url
```
 <meta name="citation_pdf_url" content="https://patentimages.storage.googleapis.com/21/d9/64/29c8a1118dbbac/US20190034917A1.pdf">
```
- to download pdf file using wget
## USAGE
x.lst's format
```
https://patents.google.com/patent/US8985442B1/en
https://patents.google.com/patent/AT521455A2/en
https://patents.google.com/patent/CN108292330A/en
https://patents.google.com/patent/US20130086389A1/en
https://patents.google.com/patent/US20190034917A1/en
....
```
#### Download
```
$ python scrape.py
$ mv *pdf results
```
#### Exception
*when downloading failed due to network connection time out or some other reasons*

- to filter already downloaded files in lst
```
$ python filter.py
```
- to trigger downloading again with filtered list.
```
$ python scrape.py
$ mv *pdf results
```
*cautions: change the x.lst as x.filtered.lst before triggering scraping.*