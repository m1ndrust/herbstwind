<?php

// NOTE: <?php    recursively scanning a dir
// function getDirContents($dir, &$results = array()){
//     $files = scandir($dir);
//
//     foreach($files as $key => $value){
//         $path = realpath($dir.DIRECTORY_SEPARATOR.$value);
//         if(!is_dir($path)) {
//             $results[] = $path;
//         } else if($value != "." && $value != "..") {
//             getDirContents($path, $results);
//             $results[] = $path;
//         }
//     }
//
//     return $results;
// }

// $files = scandir("./");
// $scanned_directory = array_diff($files, array('..', '.'));
// sort($files);
// foreach ($scanned_directory as $file) {
//
//   $test = pathinfo($file);
//   echo $test['extension'];
//
//   echo'<a href="./'.$file.'">'.$file.'</a><br>';
//
// }
$iterator = new FilesystemIterator('./');
foreach($iterator as $fileInfo){
    if($fileInfo->isFile()){
        $cTime = new DateTime();
        $cTime->setTimestamp($fileInfo->getCTime());
        echo $fileInfo->getFileName() . " file Created " . $cTime->format('Y-m-d h:i:s') .  "<br/>\n";
        echo'<a href="./'.$fileInfo->getFileName().'">'.$fileInfo->getFileName().'</a><br>';
    }
    if($fileInfo->isDir()){
        $cTime = new DateTime();
        $cTime->setTimestamp($fileInfo->getMTime());
        echo $fileInfo->getFileName() . " dir Modified " . $cTime->format('Y-m-d h:i:s') . "<br/>\n";
    }
}
?>
