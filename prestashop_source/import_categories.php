<?php
//ID,Aktywny,Nazwa,Kategoria nadrzędna
require_once('PrestaShop-webservice-lib-master/PSWebServiceLibrary.php');

$cat_map = array();
$prod_map = array();

class Cat{
    public int $ID;
    public string $name;
    public int $active;
    public string $parent_cat;
    public function __construct(int $ID, int $active, string $name, string $parent_cat ){
        $this->ID = $ID;
        $this->active = $active;
        $this->name = $name;
        $this->parent_cat = $parent_cat;
    }
    
    public function getID(): int{
        return $this->ID;
    }
    public function getName(): string{
        return $this->name;
    }
    public function isActive(): int{
        return $this->active;
    }
    public function getParentCat(): string{
        return $this->parent_cat;
    }
    
    public function add_cat():void{        
        try{
            $webservice = new PrestaShopWebservice('http://localhost','9ATPLJ9QZXTEJQQWDWPRF2TVGWZ2A3HU ', false);
            
            $blankXml = $webservice->get(['url' => 'http://localhost/api/categories?schema=blank']);

            $category_fields = $blankXml->category->children();
            $category_fields->name->language = $this->name;
            $category_fields->link_rewrite->language = $this->name;
            $category_fields->active = $this->active;
            $category_fields->id_parent = "2";

            $createdXml = $webservice->add([
                'resource' => 'categories',
                'postXml' => $blankXml->asXML()
            ]);
            global $cat_map;
            $newCategoryFields = $createdXml->category->children();
            $cat_map[(string)$newCategoryFields->name->language]= (string)$newCategoryFields->id;
            echo 'Utworzona kategoria o ID: ' . (string)$newCategoryFields->id ."\n";
        }catch(PrestaShopWebserviceException $e){
            echo 'Błąd API: ' . $e->getMessage();
        }
        // Pamiętaj, aby dodać obsługę innych błędów, np. błędów sieci
        catch(Exception $e) {
            echo 'Błąd ogólny (może być błąd połączenia): ' . $e->getMessage();
        }     
    }
}



class Prod_temp{
    private int $id;
    private string $name;
    private int $active;
    private int $category;
    private string $description;
    private float $net;
    private float $gross;
    private float $weight;
    private int $available;

    // public function __construct(int $id, string $name, int $active, string $category, string $description,float $net,float $gross, float $weight, int $available){
    //     $this->id = $id;
    //     $this->name = $name;
    //     $this->active = $active;
    //     $this->category = $category;
    //     $this->description = $description;
    //     $this->net = $net;
    //     $this->gross = $gross;
    //     $this->weight = $weight;
    //     $this->available = $available;
    // }
    public function __construct(int $id, string $name, int $active, int $category){
        $this->id = $id;
        $this->name = $name;
        $this->active = $active;
        $this->category = $category;
    }
    public function getId(): int{
        return $this->id;
    }
    public function getName(): string{
        return $this->name;
    }
    public function isActive(): int{
        return $this->active;
    }
    public function getCategory(): int{
        return $this->category;
    }
    public function getDescription(): string{
        return $this->description;
    }
    public function getNet(): float{
        return $this->net;
    }
    public function getGross(): float{
        return $this->gross;
    }
    public function getWeight(): float{
        return $this->weight;
    }
    public function getAvailable(): int{
        return $this->available;
    }
    public function add_product() : void{
        try{
            $webservice = new PrestaShopWebservice('http://localhost','9ATPLJ9QZXTEJQQWDWPRF2TVGWZ2A3HU ', false);
            
            $blankXml = $webservice->get(['url' => 'http://localhost/api/products?schema=blank']);
            
            $product_fields = $blankXml->product->children();

            $product_fields->name->language = $this->name;
            $product_fields->link_rewrite->language = $this->name;
            $product_fields->description->language = "OPIS";
            $product_fields->active = 1;
            $product_fields->stock_availables->stock_available->id = 4;
            $product_fields->minimal_quantity = 1;
            if($this->category > 0){
                $product_fields->id_category_default = 2;
                $product_fields->associations->categories->category->id = 2;
            }else{
                $product_fields->id_category_default = 2;
                $product_fields->associations->categories->category->id = 2;
            }
            $product_fields->price = 10.0;
            $product_fields->id_tax_rules_group = 1;
            global $prod_map;
            $createdProdXml = $webservice->add([
                'resource' => 'products',
                'postXml' => $blankXml->asXML()
            ]);
            $newProductFields = $createdProdXml->product->children();
            $prod_map[$newProductFields->id] = $this->id;
            echo 'Utworzony Produkt o ID: ' . (string)$newProductFields->id;
   
        }catch(PrestaShopWebserviceException $e){
            echo 'Błąd API: ' . $e->getMessage();
        }
        // Pamiętaj, aby dodać obsługę innych błędów, np. błędów sieci
        catch(\Exception $e) {
            echo 'Błąd ogólny (może być błąd połączenia): ' . $e->getMessage();
        }
    }
}

//adding categories
if (($handle = fopen("cateogries.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, null, ",")) !== FALSE) {
        $num = count($data);
        if(array_key_exists($data[3],$cat_map)){
            continue;
        }
        $curr_cat = new Cat($data[0], $data[1], $data[2],$data[3]);
        $curr_cat->add_cat();
    }
    echo "POZDRO\n";
    fclose($handle);
}

// //adding subcategories
if (($handle = fopen("subcategories.csv", "r")) !== FALSE) {
    while (($data2 = fgetcsv($handle, null, ",")) !== FALSE) {
        $num = count($data2);
        $parent_cat = 2;
        try{
            $parent_cat = $cat_map[$data2[3]];
        }catch(Exception $e){
            echo "Błąd ładowania podkategori\n". $e->getMessage();
        }
        $curr_cat = new Cat($data2[0], $data2[1], $data2[2],$parent_cat);
        $curr_cat->add_cat();
    }
    foreach($cat_map as $cat_id => $cat_name){
        echo "ID->". $cat_id ." NAZWA->". $cat_name ."\n";
    }
    fclose($handle);
}

//adding products
//id,name,active,category
if (($handle = fopen("products2.csv", "r")) !== FALSE) {
    while (($data3 = fgetcsv($handle, null, ",")) !== FALSE) {
        $num = count($data3);
        $prod_cat = 2;
        try{
            $prod_cat =(string)$cat_map[$data3[3]];
            echo "OTO ID KATEGORI -> \n". $prod_cat;
        }catch(Exception $e){
            echo "Kategoria nie istnieje\n". $e->getMessage();
        }
        $curr_cat = new Prod_temp($data3[0], $data3[1], $data3[2], $prod_cat);
        $curr_cat->add_product();
    }
    fclose($handle);
}


//adding product image

// $urlImage ='http://127.0.0.1/api/products';
// $key  = '9ATPLJ9QZXTEJQQWDWPRF2TVGWZ2A3HU';
// $image_mime = 'image/jpg';

// $ch = curl_init();
// curl_setopt($ch, CURLOPT_HEADER, 1);
// curl_setopt($ch, CURLINFO_HEADER_OUT, 1);
// curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
// curl_setopt($ch, CURLOPT_URL, $urlImage);
// curl_setopt($ch, CURLOPT_HTTPGET, 1);
// curl_setopt($ch, CURLOPT_USERPWD, $key.':');
// curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
// curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
// curl_setopt($ch, CURLOPT_HTTPHEADER, array(
//         // Nakazuje Apache i PrestaShopowi, aby myślał, że żądanie przyszło na ten adres:
//         'Host: localhost:8080', 
//         'Content-Type: multipart/form-data' // Upewnij się, że Content-Type jest poprawny
//     ));

// $result = curl_exec($ch);
// list($header, $body) = explode("\r\n\r\n", $result, 2);;
// $dom = new DOMDocument();
// $dom->loadXML($body);
// $xpath = new DOMXPath($dom);

// $nodes = $xpath->query('//product');
// foreach( $nodes as $node ){
//     $prod_id = $node->getAttribute('id');
//     $mapped_prod_id = $prod_map[$prod_id];
//     $urlImage ="http://127.0.0.1/api/images/products/{$mapped_prod_id}/";
//     $image_path = "/var/www/html/images/{$prod_id}/1.jpg";
//     $processed_path = compress_image( $image_path, $mapped_prod_id );
//     $args['image'] = new CurlFile($processed_path, $image_mime);
//     $ch = curl_init();
//     curl_setopt($ch, CURLOPT_HEADER, 1);
//     curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
//     curl_setopt($ch, CURLINFO_HEADER_OUT, 1);
//     curl_setopt($ch, CURLOPT_URL, $urlImage);
//     curl_setopt($ch, CURLOPT_POST, 1);
//     curl_setopt($ch, CURLOPT_USERPWD, $key.':');
//     curl_setopt($ch, CURLOPT_POSTFIELDS, $args);
//     curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
//     curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
//     curl_setopt($ch, CURLOPT_HTTPHEADER, array(
//         // Nakazuje Apache i PrestaShopowi, aby myślał, że żądanie przyszło na ten adres:
//         'Host: localhost', 
//         'Content-Type: multipart/form-data' // Upewnij się, że Content-Type jest poprawny
//     ));
//     $result = curl_exec($ch);
//     $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
//     if ($result === false) {
//         echo "--- BŁĄD CURL ---\n";
//         echo "cURL error number: " . curl_errno($ch) . "\n";
//         echo "cURL error: " . curl_error($ch) . "\n"; 
//     }
//     curl_close($ch);
// }

// function compress_image($image_path, $mapped_prod_id):String{
//     if(file_exists((string)$image_path)) {
//         $size_kB = filesize((string)$image_path)/1024;
//         if($size_kB >= 100){
//             $image_info = getimagesize($image_path);
//             $mime_type = $image_info['mime'];
//             $image_resource = false;
//             switch ($mime_type) {
//                 case 'image/jpeg':
//                     $image_resource = imagecreatefromjpeg($image_path);
//                     break;
//                 case 'image/png':
//                     $image_resource = imagecreatefrompng($image_path);
//                     break;
//                 case 'image/gif':
//                     $image_resource = imagecreatefromgif($image_path);
//                     break;
//                 case 'image/webp':
//                     $image_resource = imagecreatefromwebp($image_path);
//                     break;
//                 default:
//                     echo "Nieobsługiwany format pliku: $mime_type";
//             }
//             if($image_resource !== false){    
//                 $compressed_path = "/var/www/html/images/{$mapped_prod_id}/1C.jpg";
//                 $quality = 60;
//                 imagejpeg($image_resource, $compressed_path, $quality);
//                 imagedestroy($image_resource);
//                 $size_kB = filesize((string)$compressed_path)/1024;
//                 echo "Rozmiar po kompresji -> {$size_kB}";
//                 return $compressed_path;
//             }else{
//             return $image_path;
//         } 
//         }else{
//             return $image_path;
//         }        
//     }else{
//         return $image_path;
//     }
// }