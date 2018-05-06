import html_downloader
import html_outputer
import html_parser
import url_manager

# canbe reference https://github.com/codeboywang/SpiderMan
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outpter = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while (self.urls.has_new_url()):
            new_url = self.urls.get_new_url()
            print 'craw count : %d,url: %s' % (count, new_url)
            html_content = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_content)
            self.urls.add_new_urls(new_urls)
            self.outpter.collect_data(new_data)

            if count == 10:
                break
            count = count + 1



        self.outpter.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)