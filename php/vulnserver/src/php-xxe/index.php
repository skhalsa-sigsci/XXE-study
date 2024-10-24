<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>XML POST Form</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style type="text/css">
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            padding: 20px;
        }
        #xmlForm {
            background: #2d2d2d;
            padding: 20px;
            border-radius: 10px;
            max-width: 600px;
            margin: 0 auto;
            color: #fff;
        }
        textarea {
            width: 100%;
            height: 200px;
            border-radius: 10px;
            margin: 0 auto;
            font-family: monospace;
        }
        button {
            padding: 10px 20px;
            background: #8c910b;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #6c730b;
        }
        #output {
            background: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
            max-width: 600px;
            margin: 0 auto;
            color: #000;
        }
    </style>
    <script type="text/javascript" src="scripts/jquery.min.js"></script>
    <script type="text/javascript">
        function XMLFunction(){
            var xml = $('#xmlInput').val();
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if(xmlhttp.readyState == 4){
                    console.log(xmlhttp.readyState);
                    console.log(xmlhttp.responseText);
                    document.getElementById('output').innerHTML = xmlhttp.responseText;
                }
            }
            xmlhttp.open("POST","xxe.php",true);
            xmlhttp.setRequestHeader("Content-Type", "application/xml");
            xmlhttp.send(xml);
        };
    </script>
</head>
<body>
    <div id="xmlForm">
        <h2>Submit XML</h2>
        <div>
            <textarea id="xmlInput" name="xmlInput" placeholder="Paste your XML here..."></textarea>
            <p>
            <button id="submit" onclick="XMLFunction()">Submit</button>
        </div>
    </div>
    <div id="output"></div>
</body>
</html>
