from html.parser import HTMLParser
from bs4 import BeautifulSoup as soupify
import requests

class Story(object):
    def __init__(self, id):
        self.url = "https://www.literotica.com/s/%s" %(id)
        # first page, full of useful stuff yo
        self.fp = ""
        self.author = ""
        self.category = ""
        self.description = ""
        self.num_pages = 0
        self.text = []
        self.title = ""

    def cache_first_page(self):
        '''
        Caches the first page of a story.

        You don't even understand how fucking useful this is.

        :raises: IOError
        '''
        r = requests.get(self.url)
        status = r.status_code // 100
        if status == 2:
            self.fp = soupify(r.content, features="html.parser")
        elif status == 4:
            raise IOError("Client Error %s" %(r.status_code))
        elif status == 5:
            raise IOError("Server Error %s" %(r.status_code))
        else:
            raise IOError("Unidentified Error %s" %(r.status_code))

    def fill_metadata(self):
        if not self.fp:
            self.cache_first_page()

        # WARNING: hard coded class string
        tofind = "b-story-user-y x-r22"
        self.author = self.fp.find('span', {'class': tofind})
        self.author = self.author.getText()

        self.title = self.fp.find('title').getText()
        self.title = HTMLParser().unescape(self.title)
        # rip out " - Literotica.com"
        self.title, self.category = self.title[:-17].rsplit(' - ', 1)

        self.description = self.fp.find('meta', {'name': 'description'})
        self.description = self.description['content']
        
        # WARNING: hard coded search string
        tofind = 'b-pager-next'
        if tofind in self.fp.prettify():
            # assumes that the only <option> tags are page nums
            # findAll() -> find_all() in bs4
            self.num_pages = int(self.fp.findAll('option')[-1].text)
        else:
            self.num_pages = 1

    def get_author(self):
        if not self.author:
            self.fill_metadata()
        return self.author

    def get_category(self):
        if not self.category:
            self.fill_metadata()
        return self.category

    def get_description(self):
        if not self.description:
            self.fill_metadata()
        return self.description
    
    def get_num_pages(self):
        if not self.num_pages:
            self.fill_metadata()
        return self.num_pages

    def get_title(self):
        if not self.title:
            self.fill_metadata()
        return self.title

    def get_text(self):
        if not self.num_pages:
            self.fill_metadata()
        if not self.text:
            soups = []
            for x in range(1, self.num_pages+1):
                print("Handling (%s) page %d/%d" % (self.get_title(), x, self.num_pages))
                resp = requests.get("%s?page=%s" %(self.url, x))
                html = resp.content
                s = soupify(html, features="html.parser")
                soups.append(s)

            # WARNING: hard coded class name
            tofind = 'b-story-body-x x-r15'
            t = [soup.find('div', {'class': tofind}) for soup in soups]
            self.text = [str(s) for s in t]
        return self.text

    def writeToDisk(self):
        author = self.get_author()
        cat = self.get_category()
        desc = self.get_description()
        title = self.get_title()
        text = self.get_text()

        f = open( ("%s.html" % str(title)), "w")
        f.write( "Title: %s<br/>Author: %s<br/>Category: %s<br/>Description: %s<br/><hr/><br/>" % ( str(title), str(author), str(cat), str(desc) ) )
        for t in text:
            f.write(str(t))
        f.close()

