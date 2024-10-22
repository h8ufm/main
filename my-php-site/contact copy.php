
// $post = (!empty($_POST)) ? true : false;

// if ($post) {
//     $name = ($_POST['name']);
//     $phone = ($_POST['phone']);
//     $colServer = ($_POST['col-server']);
//     $colStation = ($_POST['col-station']);
//     $messagess = ($_POST['messagess']);
//     $error = '';

//     if (!$name) {
//         $error .= '';
//     }



//     $error .= '';
// }



// if (!$phone || strlen($phone) < 1) {
//     $error .= "";
// }


// if (!$error) {
//     $subject = "Новый заказ с сайта ДедМорозка";
//     $mail = mail("alex_suschin@mail.ru", $name, $phone, $colServer, $colStation);
//     if ($mail) {
//         echo 'OK';
//     }

// }

// if ($_SERVER["REQUEST_METHOD"] == "POST") {
//     $name = htmlspecialchars($_POST['name']);
//     $phone = htmlspecialchars($_POST['tell']);
//     $error = '';

//     if (empty($name)) {
//         $error .= "Пожалуйста, введите имя.<br>";
//     }

//     if (empty($phone) || strlen($phone) < 11) {
//         $error .= "Пожалуйста, введите корректный номер телефона.<br>";
//     }

//     if (empty($error)) {
//         $to = "alex_suschin@mail.ru"; // Замените на ваш email
//         $subject = "Новый заказ с сайта ДедМорозка";
//         $message = "Имя: $name\nНомер телефона: $phone";
//         $headers = "From: no-reply@example.com"; // Замените на ваш домен

//         if (mail($to, $subject, $message, $headers)) {
//             echo 'OK';
//         } else {
//             echo 'Ошибка при отправке заявки.';
//         }
//     } else {
//         echo $error;
//     }
// } else {
//     echo 'Недопустимый метод запроса.';
// }

