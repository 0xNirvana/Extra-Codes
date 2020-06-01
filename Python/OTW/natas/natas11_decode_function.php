#!/usr/bin/php

<?php

$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
// $cookie = hex2bin("0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c");


function xor_encrypt($in) {
    $key = "qw8J";
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$output = xor_encrypt(json_encode($defaultdata), $cookie);
echo base64_encode($output);
?>