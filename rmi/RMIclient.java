import java.rmi.*;
public class RMIclient
{
public static void main(String args[])
{
try
{
Adder stub=(Adder)Naming.lookup("rmi://local host:5000/sonoo");
System.out.println(stub.add(34,4));
}
catch (Exception e)
{}
}
}
