<!DOCTYPE html>
<html lang="en">
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
    <table>
    <p>
    Previous content:
    %for row in {{rows}}:
        <tr>    
        % for col in row:
            <td>{{col}}</td>
        %end
        </tr>
    %end
    </p>
    </table>
</body>
</html>