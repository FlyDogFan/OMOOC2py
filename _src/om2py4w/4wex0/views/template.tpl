<!DOCTYPE html>
<html>
<head>
    <title>MyDaily Version4.0</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
    <h1>MyDaily Version 4.0 </h1>
    <form action="/mydaily" method="post">
        日记: <input name ="content" type="text" />
        <input value ="保存" type="submit" />
    </form>
    <h1>Previous diary:</h1>
    <textarea rows="35" cols= "100"> {{rows}} </textarea>
</body>
</html>