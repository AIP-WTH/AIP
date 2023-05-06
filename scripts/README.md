# Utility files

## Getting started

### Prerequisites

- Python 3.11 or above
- (`gen_chatgpt_news.py`) OpenAI API Key

### Installation

```bash
pip install -r requirements.txt
```

### Scripts

1. News Crawler: `crawl_news.py`

   - korea_news_crawler는 [https://github.com/lumyjuwon/KoreaNewsCrawler](https://github.com/lumyjuwon/KoreaNewsCrawler) 고쳐서 만든 내용
   - 실행하면 `../output` 폴더에 파일 생김
   - Output CSV
     |Column|Content|
     |:-:|:--|
     |0|작성 일시|
     |1|카테고리|
     |2|작성자|
     |3|제목|
     |4|본문|
     |5|기사 원본 링크|

2. ChatGPT News Generator: `gen_chatgpt_news.py`

   - News Crawler로 크롤링한 뉴스 데이터 csv를 받아 ChatGPT에게 같은 주제로 재작성하도록 하는 스크립트
   - ChatGPT API key 필요
   - backup 디렉토리 및 output 디렉토리 미리 생성해둬야함
   - Output CSV
     |Column|Content|
     |:-:|:--|
     |0|변환 전 데이터 인덱스|
     |1|작성 일시|
     |2|카테고리|
     |3|작성자|
     |4|제목|
     |5|본문|
     |6|기사 원본 링크|
