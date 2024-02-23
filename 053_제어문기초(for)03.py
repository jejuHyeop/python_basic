from bs4 import BeautifulSoup

st = """<html>
<body>
    123
    <div id='hello1'>123</div>
    <div class='hello2'>123</div>
    <div>
        <span>Here</span>
    </div>
</body>
</html>"""
soup = BeautifulSoup(st, 'html.parser')
print(soup.select('body'))
print(soup.select('div#hello1'))
print(soup.select('div.hello2'))
print(soup.select('div > span'))
