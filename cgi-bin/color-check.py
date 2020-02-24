#!/usr/bin/env python3
import cgi
form=cgi.FieldStorage()
ucolor=form.getvalue("color")
status = False
with open("colors.txt", "r") as reader:
  if ucolor in reader.read():
    status = True

if status == True:
  html = """
    <html lang="en"> 
      <body>
        <p>
         {} is a color.
        </p>
        <div style="background-color:{}; width:50px; height:50px">
        </div>
      </body>
    </html>""".format(ucolor, ucolor.lower())
else:
  html= """
    <html lang="en"> 
      <body>
        <p>
         %s is not a color
       </p>
      </body>
    </html>""" % ucolor

print(html)