<?php
  //Debes trabajar sobre el mismo namespace
  namespace PhpXmlRpc;
  //incluyes los archivos para que los puedas utilizar
  include 'src/Autoloader.php';
  include 'src/Client.php';
  include 'src/Encoder.php';
  include 'src/PhpXmlRpc.php';
  include 'src/Request.php';
  include 'src/Response.php';
  include 'src/Server.php';
  include 'src/Value.php';
  include 'src/Wrapper.php';
  include 'src/Helper/Charset.php';
  include 'src/Helper/Date.php';
  include 'src/Helper/Http.php';
  include 'src/Helper/Logger.php';
  include 'src/Helper/XMLParser.php';

  /* ********************** */
  // Variables Principales para generar las conexiones y consultas al webservice

  $server_url = 'http://localhost:8069'; // url del servidor
  $client = new Client($server_url.'/xmlrpc/common');// common cambia dependiendo que metodo vamos a llamar
  $db_odoo = "ODOO_QX";
  $user_odoo = "admin";
  $password_user_odoo = "admin";
  $id_user_odoo = 1;

  //La clase Cleinte puede recivir diferentes parametros, revisar aqui: http://gggeek.github.io/phpxmlrpc/doc-4/api/PhpXmlRpc/Client.html
  echo "ok<br><br>";
  //El objeto Request es el que recive el nombre del metodo y sus parametros.
  //Puede recivirlos en el constructor o por medio del metodo addParam(value,tipo)
  //tipos: string, int, boolean, struct y otros
  $msg=new Request("login",array(new Value($db_odoo, "string"),new Value($user_odoo, "string"),new Value($password_user_odoo, "string")));
  //EL metodo send de la clase Client recive como parametro un objeto de tipo Request y devuelve un objeto de tipo Response
  $send_msg= $client->send($msg);
  echo $send_msg->value()->scalarval();
  $uid = $msg->serialize();
  echo $uid."<br>";
  echo "<br><h3>Request Login </h3><br>";
  print_r($msg);

  echo "<br><br><br>";

     /* ********************************************* */
     /* ********************************************* */
     /* ********************************************* */
     // Creacion de Registro 

  //Ejemplo para crear un registro en res.partner
  $client_obj = new Client($server_url.'/xmlrpc/object');
  $client_obj->setSSLVerifyPeer(0);

  $val = array ( 
    "name"    => new Value("German PD PHP", "string"),
    "city" => new Value("Orizaba", "string"),
    "zip" => new Value("94300", "string"),
    "website" => new Value("http://poncesoft.blogspot.com", "string"),
    "vat"   => new Value("MXPODG890612987", "string"),
    );

  $r = new Request("execute");
  $r->addParam(new Value($db_odoo,"string")); // Esta es la base de datos
  $r->addParam(new Value($id_user_odoo,"int")); // Este es el ID del Usuario
  $r->addParam(new Value($password_user_odoo,"string")); // Esta es la contraseña nuevamente
  $r->addParam(new Value("res.partner","string"));
  $r->addParam(new Value("create","string"));
  $r->addParam(new Value($val,"struct"));

  $response = $client_obj->send($r);

  echo 'Partner created - partner_id = ' . $response->value()->scalarval();

  echo "<br><br>";

  //Descargar la libreria de php en: http://gggeek.github.io/phpxmlrpc/.
  //Utilizar los archivos que vienen en src
 ?>
