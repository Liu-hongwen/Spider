# coding:utf-8

import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  # URL管理器
        self.downloader = html_downloader.HtmlDownloader()  # HTML下载器
        self.parser = html_parser.HtmlParser()  # HTML解析器
        self.outputer = html_outputer.HtmlOutputer()  # HTML输出器

    def craw(self, root_url):  # 爬虫调度程序

        count = 1  # 计数URL的个数

        self.urls.add_new_url(root_url)  # 将根URL添加到URL管理器
        while self.urls.has_new_url():  # 如果有待爬取的URL
            try:
                new_url = self.urls.get_new_url()  # 获取新的URL
                print "craw %d : %s" % (count, new_url)
                html_cont = self.downloader.download(new_url)  # 下载新的URL页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析页面
                self.urls.add_new_urls(new_urls)  # 将解析出来的URL添加到URL管理器
                self.outputer.collect_data(new_data)  # 收集数据

                if count == 10:
                    break
                count += 1

            except:
                print "craw failed"  # 如果出现异常，爬取失败

        self.outputer.output_html()  # 输出收集好的数据


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

