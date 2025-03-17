import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class NewServlet2 extends HttpServlet {
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            // Retrieve form data
            String name = request.getParameter("name");
            String address = request.getParameter("address");
            String mobile = request.getParameter("mobile");
            String email = request.getParameter("email");
            String utilities = request.getParameter("utilities");

            // HTML structure for response
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet NewServlet2</title>");
            out.println("</head>");
            out.println("<body>");
            out.println("<table border=solid cellpadding=10>");
            out.println("<tr>");
            out.println("<td>");
            out.println("<center><h1>GLOBAL Home Collections </h1>");
            out.println("<h4>23, Cap Road, Nagercoil-1.</h4></center>");
            out.println("<hr>");
            out.println("Customer Name       :" + name + "<br>");
            out.println("Customer Address    :" + address + "<br>");
            out.println("Customer Mobile     :" + mobile + "<br>");
            out.println("Customer Email      :" + email + "<br>");
            out.println("<hr>");
            out.println("Product Ordered      : " + utilities + " <br><br>");
            out.println("<a href='servconfirm.html'>Confirm Order</a>");
            out.println("</td></tr></table>");
            out.println("</body>");
            out.println("</html>");
        }
    }
}
