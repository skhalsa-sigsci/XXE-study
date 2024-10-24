<?php
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
$dom = new DOMDocument();
$dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
$info = simplexml_import_dom($dom);

// Convert the entire XML back to a string to return it.
$xmlString = $info->asXML();

echo $xmlString;
?>
