import base64
import cherrypy
from cherrypy.lib.static import serve_file

class base64Decoder(object):
	def index(self):
		return """
		<html>
		<head><title>Base 64 Decoder</title></head>
		<body>
			<h2>Base 64 Decoder</h2> 
			<a href="encoder">Switch to Encoder</a>
			<h2>Paste in the base 64 encoded string</h2>
			<form action="decode" method="post" enctype="multipart/form-data" target="_blank">
			<textarea id="textToDecode" name="textToDecode" rows="5" cols="40"></textarea>
			Name of output file: 
			<input type="text" id="fileName" name="fileName" />
			<input type="submit" value="decode"/>
			</form>
		</body></html>
		"""
	index.exposed = True

	def encoder(self):
		return """
		<html>
		<head><title>Base 64 Encoder</title></head>
		<body>
			<h2>Base 64 Encoder</h2> 
			<a href="decoder">Switch to Decoder</a>
			<h2>Upload a file to encode</h2>
			<form action="encode" method="post" enctype="multipart/form-data" target="_blank">
			filename: <input type="file" name="myFile" />
			<input type="submit" value="encode"/>
			</form>
		</body></html>
		"""
	encoder.exposed = True

	def encode(self, myFile):
		cherrypy.response.headers['Content-Type'] = 'text/plain'
		data = myFile.file.read()
		return base64.encodestring(data)
	encode.exposed = True

	def decode(self, textToDecode, fileName):
		cherrypy.response.headers['Content-Type'] = 'application/octet-stream'
		dis = 'attachment; filename="%s"' % fileName
		cherrypy.response.headers['Content-Disposition'] = dis
		outstr = base64.decodestring(textToDecode)
		return outstr
	decode.exposed = True

	decoder = index

cherrypy.server.socket_port = 8064
cherrypy.quickstart(base64Decoder(), '/')
