import requests
from newspaper import Article
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

article_urls = [
    "https://www.alfatah.com.pk/about/",
    "https://www.alfatah.com.pk/warranty-policy/",
    "https://www.alfatah.com.pk/return-refund-policy/",
    "https://www.alfatah.com.pk/faq/"
]


session = requests.Session()
pages_content = []

for url in article_urls:
    try:
        time.sleep(2)
        response = session.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            article = Article(url)
            article.download()
            article.parse()
            pages_content.append({ "url": url, "text": article.text })
        else:
            print(f"Failed to fetch article at {url}")
    except Exception as e:
        print(f"Error occurred while fetching article at {url}: {e}")

print(pages_content)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=0)

all_texts, all_metadatas = [], []
for d in pages_content:
    chunks = text_splitter.split_text(d["text"])
    for chunk in chunks:
        all_texts.append(chunk)
        all_metadatas.append({ "source": d["url"] })

print(all_texts)

# save all_text in text file
with open("all_text.txt", "w") as f:
    for text in all_texts:
        f.write(text)
