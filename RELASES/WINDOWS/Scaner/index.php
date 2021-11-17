<?php
    function getIp() {
        $ip = $_SERVER['REMOTE_ADDR'];
        if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
            $ip = $_SERVER['HTTP_CLIENT_IP'];
        } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
            $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
        }
        return $ip;
    }

    $myObj = new \stdClass();
    $myObj->Version = "1.2";
    $myObj->PC = "";
    $myObj->Phone = getIp();
    $myObj->PHP = "C:/Users/Shx32/Desktop/LiUpload/Ice/php-8.0";
    $myJSON = json_encode($myObj);
    $file = fopen("C:/Users/Shx32/Desktop/LiUpload/Ice/config.json","w");
    fwrite($file, $myJSON);
    fclose($file);
    header("Location: index.html")
?>