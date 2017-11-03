function clickAction() {
	textField = document.getElementById("search");
	appendImage(textField.value);
}
function appendImage(tag) {
       
        imageUrl = httpPost(getServerlessApiUrl(), JSON.stringify({"giphy_request": tag}));
        var marq = document.createElement("MARQUEE");
        var img = document.createElement("IMG");
        img.src = imageUrl;
        marq.appendChild(img)
        document.body.appendChild(marq)
    }


    function getServerlessApiUrl(tag) {
	return "http://localhost:9999"
    }

    function httpPost(theUrl, query)
    {
        var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "POST", theUrl, false);
	xmlHttp.setRequestHeader('Content-type', 'application/json');
        xmlHttp.send(query);
	return xmlHttp.responseText
    }


    function httpGet(theUrl)  
    {  
      //Note: Sync version for demo purposes

        var xmlHttp = new XMLHttpRequest();  
        xmlHttp.open( "GET", theUrl, false ); // false for synchronous request  
        xmlHttp.send( null );  
        return JSON.parse(xmlHttp.responseText);  
    }  
    
function clickReset() {
	var elems = document.getElementsByTagName("marquee");
	  var list = []
	  for (element in elems) {
	    list.push(elems[element]);
	  }
	  
	  for (item in list) {
	    document.body.removeChild(list[item])
	  }

}



