<!DOCTYPE html>
<html>
<head>
    <title>MyDaily Version4.0</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
    <h1 style="left:3px;text-align:center;">MyDaily Version 4.0 </h1>
    <form action="/mydaily" method="post", style="left:3px;text-align:center;">
        日记: <input name ="content" type="text" />
        <input value ="保存" type="submit" />
    </form>
    <h1 style="left:3px;text-align:center;"> Previous diary </h1>
    <textarea row = "40" style="left:3px;text-align:center;"> {{ rows }} </textarea>
</body>
</html>