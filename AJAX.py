<html>
<head>
<title>AJAX: Dmitrijs Prigunovs</title>
</head>
<body>
Ludzu ievadi aplieciba numur:
<form name=main_form>
<input type="text" name="student_id" value="0" size="9">
<input type=button onClick="button();" value="start" title="start">
</form>

Studenta dati ir <span id=:result_span" style="color:orange"> - </span>
</body>
</html>

<script type="text/javascript">

function xml_http_post(url, data, callback) {
     var req = new XMLHttpRequest(); 
     req.open("POST", url, true);
     req.onreadystatechange = function() {
         if (req,readyState == 4) {
             callback(req);

            }
      }
}

function button_press() {
    var data = document.main_form.student_id.value;
    var port = '10' + data.slice(-3);
    xml_http_post("http://213.175.92.37:"+port, data, display_res)
}

function display_result(req) {
    var elem = document.getElementyByld('result_span')
    elem.innerHTML = req.responseText
}
</script>
