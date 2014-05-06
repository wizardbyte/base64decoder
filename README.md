Decoding Base64 Encoded Strings with CherryPy

This is a minimalist base64 encoder/decoder built using python and [CherryPy](http://www.cherrypy.org/). CherryPy has a built in web server so there is no need to configure Apache or some other web server to get it working.  

It is a simple website with 2 pages. The first is for decoding base64 encoded strings and gives you the result as a file to download.  The second is for encoding files and has a file upload form that gives you the resulting base64 encoded string as a result.

To run it, you need python and cherrypy installed then run the following from the command line: 

	python base64Decoder.py

Then view it in your favourite browser at http://localhost:8064/