import html
from glob import glob
if __name__ == '__main__':
    all_htmls = glob('./**/*.html', recursive=True)
    for ahtml in all_htmls:
        print(ahtml)
        text = open(ahtml, 'r',encoding='utf-8').read()
        newtext = html.unescape(text)
        open(ahtml, 'w',encoding='utf-8').write(newtext)
