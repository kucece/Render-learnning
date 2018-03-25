#! /usr/bin/env python
# coding:utf-8


##            <!--有作用域问题-->
##            <!--注释无效-->
##            <!--<%  %>里面的脚本内容有渲染的语言决定-->
##            <!--本质是字符串拼接，动态函数构造执行，将结果进行渲染-->


##// John Resig - http://ejohn.org/ - MIT Licensed
##借助js模板渲染引擎进行模板渲染（模板语言受制于模板引擎）
from js import execjs
str_js_render = "function tmpl(html,string){\n\
    eval(\"var data =\" + string);\n\
    var result=\"var p=[];with(data){p.push(\'\"\n\
        +html.replace(/[\\r\\n\\t]/g,\" \")\n\
        .replace(/<%=(.*?)%>/g,\"\');p.push($1);p.push(\'\")\n\
        .replace(/<%/g,\"\');\")\n\
        .replace(/%>/g,\"p.push(\'\")\n\
        +\"\');}return p.join(\'\');\";\n\
    var fn=new Function(\"data\",result);	\n\
    return fn(data);\n\
}"

Render = execjs.compile(str_js_render.encode("utf-8"))

def render(content,str_data):
    return Render.call('tmpl',html,str(data))


if __name__ == "__main__":
    html = '<ul><% for ( var i = 0; i < data.users.length; i++ ) { %><li><a href="<%=data.users[i]%>"><%=data.users[i]%></a></li><% } %>        </ul>'
    data={}
    data["users"]=["Byron",            "Casper",            "Frank"]
    print(render(html,data))
