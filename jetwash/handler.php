<?php
function CheckCurlResponse($code)
{
  $code=(int)$code;
  $errors=array(
    301=>'Moved permanently',
    400=>'Bad request',
    401=>'Unauthorized',
    403=>'Forbidden',
    404=>'Not found',
    500=>'Internal server error',
    502=>'Bad gateway',
    503=>'Service unavailable'
  );
  try
  {    
    if($code!=200 && $code!=204)
      throw new Exception(isset($errors[$code]) ? $errors[$code] : 'Undescribed error',$code);
  }
  catch(Exception $E)
  {
    die('Ошибка: '.$E->getMessage().PHP_EOL.'Код ошибки: '.$E->getCode());
  }
}

$date = date("Y-m-d H:s");
$name = isset($_POST["name"]) ? $_POST["name"] : '';
$phone = isset($_POST["phone"]) ? $_POST["phone"] : '';

$to = "gqkish@gmail.com";
$headers  = "Content-type: text/html; charset=utf-8 \r\n";
$subject = "Заказ ";

if ($name !='' && $phone !='') {

$message = "
<h3>$subject</h3><br>
Имя: <b>$name</b><br>
Контактный телефон: <b>$phone</b><br>
Дата: <b>$date</b><br>\n ";
$send = mail($to, $subject, $message, $headers);

//amo crm
$user=array(
  'USER_LOGIN'=>'gqkish@gmail.com', #Ваш логин (электронная почта)
  'USER_HASH'=>'a7c693c24d850f6b631ea7942eecd482' #Хэш для доступа к API (смотрите в профиле пользователя)
);
 
$subdomain='new54946be20d570'; 
$link='https://'.$subdomain.'.amocrm.ru/private/api/auth.php?type=json';
$curl=curl_init(); 
curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);
curl_setopt($curl,CURLOPT_USERAGENT,'amoCRM-API-client/1.0');
curl_setopt($curl,CURLOPT_URL,$link);
curl_setopt($curl,CURLOPT_POST,true);
curl_setopt($curl,CURLOPT_POSTFIELDS,http_build_query($user));
curl_setopt($curl,CURLOPT_HEADER,false);
curl_setopt($curl,CURLOPT_COOKIEFILE,dirname(__FILE__).'/cookie.txt'); #PHP>5.3.6 dirname(__FILE__) -> __DIR__
curl_setopt($curl,CURLOPT_COOKIEJAR,dirname(__FILE__).'/cookie.txt'); #PHP>5.3.6 dirname(__FILE__) -> __DIR__
curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);
curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);
 
$out=curl_exec($curl); 
$code=curl_getinfo($curl,CURLINFO_HTTP_CODE);
curl_close($curl);
CheckCurlResponse($code);

$Response=json_decode($out,true);
$Response=$Response['response'];
if(isset($Response['auth'])) { 
  //echo 'Авторизация прошла успешно';  

  // создаем данные
  $contact_name = $name;
  $contact_phone = $phone;
  $lead_title = 'Заявка '.$date; 

  // создаем сделку
  		
		 $lead=array(
		  'name'=> $lead_title,
		  'status_id' => 8147204,
		  'responsible_user_id' => 328340,		 
		);   	
	
	
	$set['request']['leads']['add'][]=$lead;
	 
	#Формируем ссылку для запроса
	$link='https://'.$subdomain.'.amocrm.ru/private/api/v2/json/leads/set';
	$curl=curl_init(); #Сохраняем дескриптор сеанса cURL
	#Устанавливаем необходимые опции для сеанса cURL
	curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);
	curl_setopt($curl,CURLOPT_USERAGENT,'amoCRM-API-client/1.0');
	curl_setopt($curl,CURLOPT_URL,$link);
	curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'POST');
	curl_setopt($curl,CURLOPT_POSTFIELDS,json_encode($set));
	curl_setopt($curl,CURLOPT_HTTPHEADER,array('Content-Type: application/json'));
	curl_setopt($curl,CURLOPT_HEADER,false);
	curl_setopt($curl,CURLOPT_COOKIEFILE,dirname(__FILE__).'/cookie.txt'); #PHP>5.3.6 dirname(__FILE__) -> __DIR__
	curl_setopt($curl,CURLOPT_COOKIEJAR,dirname(__FILE__).'/cookie.txt'); #PHP>5.3.6 dirname(__FILE__) -> __DIR__
	curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);
	curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);
	 
	$out=curl_exec($curl); #Инициируем запрос к API и сохраняем ответ в переменную
	$code=curl_getinfo($curl,CURLINFO_HTTP_CODE);
	CheckCurlResponse($code);
	 
	/**
	 * Данные получаем в формате JSON, поэтому, для получения читаемых данных,
	 * нам придётся перевести ответ в формат, понятный PHP
	 */
	$Response=json_decode($out,true);
	$Response=$Response['response']['leads']['add'];
	 
	$output='ID добавленных сделок:'.PHP_EOL;
	foreach($Response as $v)
	  if(is_array($v))
		$output.=$v['id'].PHP_EOL;
		//echo $output; 
		$lead_id[0] = $v['id'];
  
  // создаем контакт
  
  $contact=array(
      'name'=>$contact_name,
	  'responsible_user_id' => 328340,
	  'linked_leads_id' => $lead_id,      
    );   	
	$contact['custom_fields'][]=array(
		'id'=> '1419582',
		'values'=>array(
		  array(
			'value'=> $contact_phone,
			'enum'=>'WORK'
		  )
		)
	);	
	
	$set['request']['contacts']['add'][]=$contact;
	 
	#Формируем ссылку для запроса
	$link='https://'.$subdomain.'.amocrm.ru/private/api/v2/json/contacts/set';
	$curl=curl_init(); #Сохраняем дескриптор сеанса cURL
	#Устанавливаем необходимые опции для сеанса cURL
	curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);
	curl_setopt($curl,CURLOPT_USERAGENT,'amoCRM-API-client/1.0');
	curl_setopt($curl,CURLOPT_URL,$link);
	curl_setopt($curl,CURLOPT_CUSTOMREQUEST,'POST');
	curl_setopt($curl,CURLOPT_POSTFIELDS,json_encode($set));
	curl_setopt($curl,CURLOPT_HTTPHEADER,array('Content-Type: application/json'));
	curl_setopt($curl,CURLOPT_HEADER,false);
	curl_setopt($curl,CURLOPT_COOKIEFILE,dirname(__FILE__).'/cookie.txt'); #PHP>5.3.6 dirname(__FILE__) -> __DIR__
	curl_setopt($curl,CURLOPT_COOKIEJAR,dirname(__FILE__).'/cookie.txt'); #PHP>5.3.6 dirname(__FILE__) -> __DIR__
	curl_setopt($curl,CURLOPT_SSL_VERIFYPEER,0);
	curl_setopt($curl,CURLOPT_SSL_VERIFYHOST,0);
	 
	$out=curl_exec($curl); #Инициируем запрос к API и сохраняем ответ в переменную
	$code=curl_getinfo($curl,CURLINFO_HTTP_CODE);
	CheckCurlResponse($code);
	 
	/**
	 * Данные получаем в формате JSON, поэтому, для получения читаемых данных,
	 * нам придётся перевести ответ в формат, понятный PHP
	 */
	$Response=json_decode($out,true);
	$Response=$Response['response']['contacts']['add'];
	 
	$output='ID добавленных контактов:'.PHP_EOL;
	foreach($Response as $v)
	  if(is_array($v))
		$output.=$v['id'].PHP_EOL;
		//echo $output; 
		$contact_id = $v['id'];		
    
  } else {
	return 'Авторизация не удалась';
  }


if ($send) {	
	echo 'ok';
} else {
	echo 'error';
}
} else {
	echo 'Заполните все поля';
}