from head.mouth import speak
import requests
def news():
    """Fetch and speak the latest news headlines."""
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bbbcd7faf4104396a4a1bcffd58164c3"
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    for i, article in enumerate(articles[:2], 1):
        speak(f"Today's {i}th news is: {article['title']}")
        print(f"Today's {i}th news is: {article['title']}")

