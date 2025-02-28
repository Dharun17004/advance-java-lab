<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h3>
            <%@ page import= "java.io.*,java.util.*" %>
            <%
            String name=(String)session.getAttribute("sessname");
            out.print("Hello User!!! You set the Session Name as :" +name);
            %>
        </h3>
    </body>
</html>
