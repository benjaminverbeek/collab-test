html = f'''\
<html>
  <head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>


    <p>Hi,<br>
       Changes in availability were detected at ({time}), see below:<br>
    </p>
    <table>

    </table>
</html>
'''




# create html alternative...

htmlText = ''
for product in products:
    if product['discount'] != '-0 %':
        htmlText += '<p>'
        for k, v in product.items():
            htmlText += (k + ': ' + str(v) + '    ')
        htmlText += '</p>'

html = f'''\
<html>
  <body>
    <p>Hi,<br>
       Changes in availability were detected at {time}, see below:<br>
    </p>
    {htmlText}
  </body>
</html>
'''