#!/usr/bin/env python
__author__ = "hloverflow"
__credits__ = ["stephenbradshaw"]

from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto import Random
from flask import Flask, request, redirect
from lxml import etree
import html
import traceback

app = Flask(__name__)

# Config stuff
KEY = Random.new().read(32)  # 256-bit key for extra security
BLOCKSIZE = AES.block_size
ADMIN_SECRET = Random.new().read(32)  # need to keep this secret
APP_NAME = 'Flask XXE demo - Python etree parser'
APP_VERSION = '0.1 pre pre pre alpha'

CONFIG = {
    'encrypto_key': b64encode(KEY).decode('utf-8'),
    'secret_admin_value': b64encode(ADMIN_SECRET).decode('utf-8'),
    'app_name': APP_NAME,
}

@app.route('/python-xxe', methods=['POST', 'GET'], strict_slashes=False)
def xml():
    parsed_xml = None
    errormsg = ''
    xml_data = ''
    
    if request.method == 'POST':
        xml_data = request.form['xml']
        parser = etree.XMLParser(resolve_entities=True, no_network=False)
        try:
            doc = etree.fromstring(xml_data.encode('utf-8'), parser)
            parsed_xml = etree.tostring(doc).decode('utf-8')
            print(repr(parsed_xml))
        except etree.XMLSyntaxError:
            print("Cannot parse the XML")
            html_content += "Error:\n<br>\n" + html.escape(traceback.format_exc())
    
    html_content = f"""
    <html>
      <body>
        <form action="/python-xxe" method="POST">
            <p><h3>Enter XML to parse</h3></p>
            <textarea class="input" name="xml" cols="40" rows="5" placeholder="Paste your XML here...">{html.escape(xml_data)}</textarea>
            <p><input type='submit' value='Parse'/></p>
        </form>
    """

    if errormsg:
        html_content += errormsg
    elif parsed_xml:
        html_content += "Result:\n<br>\n" + html.escape(parsed_xml)

    html_content += """
      </body>
    </html>
    """
    return html_content

@app.route('/python-xxe/blindxml', methods=['POST', 'GET'])
def blindxml():
    parsed_xml = None
    
    html_content = """
    <html>
      <body>
    """
    
    if request.method == 'POST':
        xml_data = request.form['xml']
        parser = etree.XMLParser(no_network=True)  # Disable external entities for security
        try:
            doc = etree.fromstring(xml_data.encode('utf-8'), parser)
            parsed_xml = etree.tostring(doc).decode('utf-8')
            print(repr(parsed_xml))
        except etree.XMLSyntaxError:
            print("Cannot parse the XML")
            # Do not reveal internal errors to the user

    if parsed_xml:
        html_content += "Result:\n<br>\n" + html.escape(parsed_xml)
    else:
        html_content += """
          <form action="/python-xxe/blindxml" method="POST">
             <p><h3>Enter XML to parse</h3></p>
             <textarea class="input" name="xml" cols="40" rows="5"></textarea>
             <p><input type='submit' value='Parse'/></p>
          </form>
        """
    html_content += """
      </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)
