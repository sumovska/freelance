<?php

$final = 'Name: ' . $_POST['name'] . "\r\n" .
         'Company: ' . $_POST['company'] . "\r\n" .
         'E-mail: ' . $_POST['email'] . "\r\n" .
         'Phone: ' . $_POST['phone'] . "\r\n" . "\r\n" .
         'Message: ' . "\r\n" . $_POST['message'] . "\r\n";

$to      = 'info@symmetrymedia.com';
$subject = 'New contact request on Symmetry Media';
$headers = 'From: webmaster@symmetrymedia.com' . "\r\n" .
    'Reply-To: webmaster@symmetrymedia.com' . "\r\n" .
    'X-Mailer: PHP/' . phpversion();

mail($to, $subject, $final, $headers);
?>