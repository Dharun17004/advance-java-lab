<%@page import="java.util.Date"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
            <% String Username=request.getParameter("inputname");
                   out.print("Welcome"+Username); %>
            </b><br><br>
            <b>
            <% Date createTime=new Date(session.getCreationTime());
            out.println("Session Created Time is:"+createTime);%>
            </b><br><br>
            <b>
            <% out.print("Session Id is:"+session.getId()); %>
           </b><br><br>
           <% session.setAttribute("sessname",Username); %>
           <br><br>
           <h2> <a href="session2.jsp">Set Session name and check it</a> </h2>   
    </body>
</html>
