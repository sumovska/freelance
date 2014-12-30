<?php 

if($_POST) {
	// $_POST['title'] содержит данные из поля "Тема", trim() - убираем все лишние пробелы и переносы строк, htmlspecialchars() - преобразует специальные символы в HTML сущности, будем считать для того, чтобы простейшие попытки взломать наш сайт обломались, ну и  substr($_POST['title'], 0, 1000) - урезаем текст до 1000 символов. Для переменной $_POST['mess'] все аналогично 
	$title = htmlspecialchars($_POST['name']);
	$email = htmlspecialchars($_POST['email']);
	$theme = htmlspecialchars($_POST['phone']);
	
	$message = '<p>Имя: '.$title.'</p><p>Почта: '.$email.'</p><p>Телефон: '.$theme.'</p>';
        // $to - кому отправляем 
        $to = 'banisaenergy.ua@gmail.com, yiiframe@yandex.ru'; 
        // $from - от кого 
        $headers  = 'MIME-Version: 1.0' . "\r\n";
		$headers .= 'Content-type: text/html; charset=utf-8' . "\r\n";
        // функция, которая отправляет наше письмо. 
       // mail($to, $title, $message,$headers); 
        mail($to, 'Banisa Energy Ukraine - заявка с сайта', $message, $headers); 
        echo 'Спасибо! Ваше письмо отправлено.'; 
}