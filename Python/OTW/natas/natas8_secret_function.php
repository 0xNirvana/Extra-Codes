#!/usr/bin/php

<?php
	echo base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362")));
	echo "\n";
?>

<!-- hex2bin: Converts base16 values to binary (base2) values -->
<!-- strrev: Reverses the string
base64_decode: Decodes data that is encoded in base64 -->