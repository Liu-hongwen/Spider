# coding:utf-8

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 待爬取的URL列表
        self.old_urls = set()  # 爬取过的URL列表

    def add_new_url(self, url):  # 添加新的URL(一个)
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):  # 添加新的URL(多个)
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):  # 判断是否有URL
        return len(self.new_urls) != 0

    def get_new_url(self):  # 获取新的URL
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

