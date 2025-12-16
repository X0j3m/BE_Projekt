<?php
$urlImage ='http://127.0.0.1/api/products';
$key  = 'INACQCW9UIC7794GLQQVALVDXG91QBQA';
$image_mime = 'image/jpg';

$ch = curl_init();
curl_setopt($ch, CURLOPT_HEADER, 1);
curl_setopt($ch, CURLINFO_HEADER_OUT, 1);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_URL, $urlImage);
curl_setopt($ch, CURLOPT_HTTPGET, 1);
curl_setopt($ch, CURLOPT_USERPWD, $key.':');
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        // Nakazuje Apache i PrestaShopowi, aby myślał, że żądanie przyszło na ten adres:
        'Host: localhost:8080', 
        'Content-Type: multipart/form-data' // Upewnij się, że Content-Type jest poprawny
    ));

$result = curl_exec($ch);
list($header, $body) = explode("\r\n\r\n", $result, 2);;
$dom = new DOMDocument();
$dom->loadXML($body);
$xpath = new DOMXPath($dom);

$nodes = $xpath->query('//product');
foreach( $nodes as $node ){
    $prod_id = $node->getAttribute('id');
    $urlImage ="http://127.0.0.1/api/images/products/{$prod_id}/";
    $image_path = "/var/www/html/images/{$prod_id}/2.jpg";
    $processed_path = compress_image( $image_path, $prod_id );
    $args['image'] = new CurlFile($processed_path, $image_mime);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_HEADER, 1);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLINFO_HEADER_OUT, 1);
    curl_setopt($ch, CURLOPT_URL, $urlImage);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_USERPWD, $key.':');
    curl_setopt($ch, CURLOPT_POSTFIELDS, $args);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        // Nakazuje Apache i PrestaShopowi, aby myślał, że żądanie przyszło na ten adres:
        'Host: localhost', 
        'Content-Type: multipart/form-data' // Upewnij się, że Content-Type jest poprawny
    ));
    $result = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($result === false) {
        echo "--- BŁĄD CURL ---\n";
        echo "cURL error number: " . curl_errno($ch) . "\n";
        echo "cURL error: " . curl_error($ch) . "\n"; 
    }
    curl_close($ch);
}


function compress_image($image_path, $prod_id):String{
    if(file_exists((string)$image_path)) {
        $size_kB = filesize((string)$image_path)/1024;
        if($size_kB >= 100){
            $image_info = getimagesize($image_path);
            $mime_type = $image_info['mime'];
            $image_resource = false;
            switch ($mime_type) {
                case 'image/jpeg':
                    $image_resource = imagecreatefromjpeg($image_path);
                    break;
                case 'image/png':
                    $image_resource = imagecreatefrompng($image_path);
                    break;
                case 'image/gif':
                    $image_resource = imagecreatefromgif($image_path);
                    break;
                case 'image/webp':
                    $image_resource = imagecreatefromwebp($image_path);
                    break;
                default:
                    echo "Nieobsługiwany format pliku: $mime_type";
            }
            if($image_resource !== false){    
                $compressed_path = "/var/www/html/images/{$prod_id}/2C.jpg";
                $quality = 55;
                imagejpeg($image_resource, $compressed_path, $quality);
                imagedestroy($image_resource);
                $size_kB = filesize((string)$compressed_path)/1024;
                echo "Rozmiar po kompresji -> {$size_kB}";
                return $compressed_path;
            }else{
            return $image_path;
        } 
        }else{
            return $image_path;
        }        
    }else{
        return $image_path;
    }
}