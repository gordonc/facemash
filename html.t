<html>
  <head>
    <title>facemash</title>
    <style type="text/css">
      body { font-family:sans-serif; }
      td { text-align:center; }
      td.pic { background-color:#b0c4de; }
      td.pic:hover { background-color:#4682b4; }
    </style>
  </head>
  <body>
    <form action="" method="post">
      <table cellpadding="10" cellspacing="5">
        <tr>
          <input type="hidden" name="name1" value="%(name1)s"/>
          <td class="pic"><input type="image" src="%(pic1)s" width=400 height=300 name="winner" value="face1"/></td>
          <td rowspan="2"><h3>V</h3></td>
          <input type="hidden" name="name2" value="%(name2)s"/>
          <td class="pic"><input type="image" src="%(pic2)s" width=400 height=300 name="winner" value="face2"/></td>
        </tr>
        </tr>
          <td>Rank: %(rank1)d</td>
          <td>Rank: %(rank2)d</td>
        </tr>
      </table>
    </form>
  </body>
</html>
