<!DOCTYPE html>
<html>
<head>
    <title>极简日记</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>

    <h1 style="left:3px;text-align:center;">极简日记</h1>
    <form action="/mydaily" method="post", style="left:3px;text-align:center;">
        <textarea name= "content" type="text" rows="2" cols="30" > 
        </textarea>
        Tag: <input name ="tag" type="text" />
        <input value ="保存" type="submit" />
    </form>
    <hr>
    <table broder= "1px" width="500" border="0">
        <tr>
            <td style="background-color:#F5FFFA;width:100px;">
                <h1 style="left:3px;text-align:center;"> Previous diary </h1>
                <p style="left:3px;text-align:center;">
                {% for item in rows %}
                    <div style="border: 1px dashed black;background:white">
                    </br>
                    Tag:{{ item[0] }}
                    </br>
                    {{ item[1]['time']}}:{{item[1]['daily_content']}}
                    </br>
                    </div>
                    </br>
                {% endfor %}
                </p>
            </td>
        </tr>
    </table>
</body>
</html>