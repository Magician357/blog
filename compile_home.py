from minify_html import minify
import distutils.dir_util

with open("index.html","r") as f:
    html=f.read()

# print(html)
html_split=html.split("<br>")
# print(html_split)
html_split[1]='<link rel="stylesheet" href="main.css">'
html="".join(html_split)

html_split=html.split('<p style="display:none">for python js</p>')
html_split[1]='<script src="main.js"></script>'
html="".join(html_split)

html=minify(html)
print(html)

with open("actual-website/index.html","w") as f:
    f.write(html)
    
distutils.dir_util.copy_tree("./icons","./actual-website/icons/")