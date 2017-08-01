<!doctype html>
<html lang="">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Library of the Void</title>

    <!-- Disable tap highlight on IE -->
    <meta name="msapplication-tap-highlight" content="no">

    <!-- Web Application Manifest -->
    <link rel="manifest" href="manifest.json">

    <!-- Add to homescreen for Chrome on Android -->
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="application-name" content="Web Starter Kit">
    <link rel="icon" sizes="192x192" href="images/touch/chrome-touch-icon-192x192.png">

    <!-- Add to homescreen for Safari on iOS -->
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <link rel="apple-touch-icon" href="images/touch/apple-touch-icon.png">
    <meta name="apple-mobile-web-app-title" content="Web Starter Kit">

    <!-- Tile icon for Win8 (144x144 + tile color) -->
    <meta name="msapplication-TileImage" content="images/touch/ms-touch-icon-144x144-precomposed.png">
    <meta name="msapplication-TileColor" content="#2F3BA2">

    <!-- Color the status bar on mobile devices -->
    <meta name="theme-color" content="#2F3BA2">

    <!-- SEO: If your mobile URL is different from the desktop URL, add a canonical link to the desktop page https://developers.google.com/webmasters/smartphone-sites/feature-phones -->
    <!--
    <link rel="canonical" href="http://www.example.com/">
    -->

    <!-- Material Design icons -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">


    <!-- Material Design Lite page styles:
    You can choose other color schemes from the CDN, more info here http://www.getmdl.io/customize/index.html
    Format: material.color1-color2.min.css, some examples:
    material.red-teal.min.css
    material.blue-orange.min.css
    material.purple-indigo.min.css
    -->
    <link rel="stylesheet" href="https://code.getmdl.io/1.2.1/material.indigo-pink.min.css">

    <!-- Your styles -->
    <link rel="stylesheet" href="styles/main.css">
  </head>
  <body id="body_wrap">
    <header>  <!--Header start -->
      <div id="wrap_header">
      <div id="header_content">
        <div id="website_title">
          0xdeadbeef
        </div>
      </div>

      </div>
    </header> <!--Header end -->
    <div id="header_sidebar"> <!-- NOTE: Searchbar -->
      <form id="searchbar" action="index.html" method="post">
        <input type="search">
        <button>Go</button>

        </style>
      </form>
    </div>
    <br>
    <br>
    <div id="wrap_main"> <!--main start-->

      <div id="main_navbar">
        <div id="navbar_title">
          [ 0xdeadbeef ]
        </div>
          <nav>
          <ul>
           <li><a href="/html/"> 0x01 code</a> </li>
           <li><a href="observer.html">  0x02 d1sgusted observer </a> </li>
           <li><a href="radio.html">  0x03 cyberia[radio]</a> <br> </li>
           <li><a href="vault.php">  0x05 wisd0m vaul7</a> <br> </li>
           <li><a href="contact.html">  [0x06] /query</a> <br> </li>
           <li><a href="index.html"> cd ~ </a> </li>
          </ul>
        </nav>
       <div id="sidebar_twitter_feed">
         Twitter feed
       </div>
      </div>

      <div id="main_content_wrapper">

        <div id="page_title">
          [ library ]
        </div>
        <div id="content">
          <div id="content_text_vault">
            <table>
              <tr>
              <th>[name]</th>
              <th>[type]</th>
              <th>[size]</th>
              <th>[date]</th>
              <th>[description]</th>
            </tr>

            <?php
            $iterator = new RecursiveDirectoryIterator('./knowledgev1');

            foreach($iterator as $fileInfo){
              if($fileInfo->isFile()){
                  $cTime = new DateTime();
                  $cTime->setTimestamp($fileInfo->getCTime());

                  echo'<tr><td><a href="./'.$fileInfo->getFileName().'">'.$fileInfo->getFileName().'</a></td><td>'.$fileInfo->getType().'</td><td>'.$fileInfo->getSize().'</td><td>'.$cTime->format('Y-m-d').'</td><td>desc</td></tr>';
                    }
              if($fileInfo->isDir()){
                $cTime = new DateTime();
                $cTime->setTimestamp($fileInfo->getMTime());
                echo'<tr><td><a href="./'.$fileInfo->getFileName().'">'.$fileInfo->getFileName().'</a></td><td>'.$fileInfo->getType().'</td><td>'.$fileInfo->getSize().'</td><td>'.$cTime->format('Y-m-d').'</td></tr>';
                }
              }

                      ?>
          </table>

            </div>
          </div>


        </div>

      </div>
    </div> <!--main end-->
    <br>
    <br>
    <footer><!-- Footer start -->
    <div id="wrap_footer">
      <div id="footer_content">
         馬鹿は死ななきゃ治らない。
      </div>
    </div>
  </footer> <!-- Footer end -->

  </body>
</html>
