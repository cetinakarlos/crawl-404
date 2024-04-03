# Crawling Broken Links with 404 Error in Python
The sample demonstrates how to crawl website to find out 404 pages in Python.

## Installation

```bash
pip install beautifulsoup4
```

## How to Run
1. Run `404crawler.py` with the target page, the depth of crawling and link filter:

    For example, if you want to crawl the website `https://www.dynamsoft.com` with the depth of 1, you can run the following command:

    ```bash
    python 404crawler.py -l https://www.dynamsoft.com -d 1 -f dynamsoft.com
    ```

    The default depth is `0`, which means only the target page will be checked. If the depth is `-1`, it will crawl all the pages on the website. 

2. Press `ctrl+c` to stop the program.

## Blog
[How to Check Broken Links with 404 Error in Python][1]

[1]:https://www.dynamsoft.com/codepool/python-check-broken-links-404.html



## html in python:
https://stackoverflow.com/questions/41857610/use-a-variable-inside-html-email