import webbrowser
import urllib.parse

def search_in_google():
    search = input("What do you want to search? ")
    keyword = urllib.parse.quote(search)
    url = f"https://www.google.com/search?q={keyword}"
    webbrowser.open(url)

def search_in_bing():
    search = input("What do you want to search? ")
    keyword = urllib.parse.quote(search)
    url = f"https://www.bing.com/search?q={keyword}"
    webbrowser.open(url)

def search_in_youtube():
    search = input("What do you want to search? ")
    keyword = urllib.parse.quote(search)
    url = f"https://www.youtube.com/results?search_query={keyword}"
    webbrowser.open(url)

def search_in_bilibili():
    search = input("What do you want to search? ")
    keyword = urllib.parse.quote(search)
    url = f"https://search.bilibili.com/all?keyword={keyword}"
    webbrowser.open(url)

def search_in_taobao():
    search = input("What do you want to search? ")
    keyword = urllib.parse.quote(search)
    url = f"https://s.taobao.com/search?q={keyword}"
    webbrowser.open(url)

def search_in_amazon():
    search = input("What do you want to search? ")
    keyword = urllib.parse.quote(search)
    url = f"https://www.amazon.com/s?k={keyword}"
    webbrowser.open(url)

def search_in_wikipedia():
    search = input("What do you want to search? ")
    keyword = urllib.parse.quote(search)
    url = f"https://zh.wikipedia.org/wiki/Special:Search?search={keyword}"
    webbrowser.open(url)

def search_in_reddit():
    search = input("What do you want to search? ")
    keyword = urllib.parse.quote(search)
    url = f"https://www.reddit.com/search/?q={keyword}"
    webbrowser.open(url)

def search_in_twitter():
    search = input("What do you want to search? ")
    keyword = urllib.parse.quote(search)
    url = f"https://twitter.com/search?q={keyword}"
    webbrowser.open(url)


while True:
    website = input("Choose website: 1.google 2.bing 3.youtube 4.bilibili 5.taobao 6.amazon 7.wikipedia 8.reddit 9.twitter 10.exit")

    if website == "google" or website == "1":
        search_in_google()
    elif website == "bing" or website == "2":
        search_in_bing()
    elif website == "youtube" or website == "3":
        search_in_youtube()
    elif website == "bilibili" or website == "4":
        search_in_bilibili()
    elif website == "taobao" or website == "5":
        search_in_taobao()
    elif website == "amazon" or website == "6":
        search_in_amazon()
    elif website == "wikipedia" or website == "7":
        search_in_wikipedia()
    elif website == "reddit" or website == "8":
        search_in_reddit()
    elif website == "twitter" or website == "9":
        search_in_twitter()
    elif website == "exit" or website == "10":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
