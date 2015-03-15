<?php

$post = (!empty($_POST)) ? true : false;

if($post)
{
$email = trim($_POST['email']);
$name = htmlspecialchars($_POST['name']);
$email = htmlspecialchars($_POST['email']);
$phone = htmlspecialchars($_POST['phone']);
$website = htmlspecialchars($_POST['website']);
$message = htmlspecialchars($_POST['message']);
$contacts = "\r\n\r\n".$phone."\r\n".$website;
$subject = "Сообщение с WebJav";
$error = '';

if(!$name)
{
$error .= 'Введите ваше имя.<br />';
}

// Check email
function ValidateEmail($value)
{
$regex = '|^[-0-9a-z_\.]+@[-0-9a-z_^\.]+\.[a-z]{2,6}$|i';

if($value == '') {
return false;
} else {
$string = preg_replace($regex, '', $value);
}

return empty($string) ? true : false;
}

if(!$email)
{
$error .= 'Введите e-mail.<br />';
}

if($email && !ValidateEmail($email))
{
$error .= 'Некорректный e-mail.<br />';
}


// Check message (length)

if(!$message || strlen($message) < 1) {
	$error .= "Введите сообщение.<br />";// В этой строчке ставиться минимальное ограничение на написание букв.
}
if(!$error) {
	$mail = mail("webjab@yandex.ru", $subject, $message.$contacts, "From: ".$name." <".$email.">\r\n"."Reply-To: ".$email."\r\n"."X-Mailer: PHP/".phpversion());
	if($mail) {
		echo 'OK';
	}
} else {
	echo '<div class="notification_error">'.$error.'</div>';
}

}
?>