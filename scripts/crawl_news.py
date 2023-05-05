from korea_news_crawler.articlecrawler import ArticleCrawler

if __name__ == "__main__":
    crawler = ArticleCrawler()
    crawler.set_category("오피니언")
    #crawler.set_category("정치", "경제", "사회", "생활문화", "IT과학", "세계", "오피니언")
    crawler.set_date_range("2023-01-01", "2023-01-01")
    crawler.start()