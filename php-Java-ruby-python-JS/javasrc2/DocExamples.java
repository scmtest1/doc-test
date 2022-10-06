import java.io.*;


public class DocExamples
{

/*===========================
FORWARD_NULL - fixed
===========================*/

  public static Object callA() {
    return testA(new Object());
  }
  
  public static Object callB() {
    // No defect report 
    return testA(new Object());
  }
    
  public static String testA(Object o) {
    return o.toString();
  }


/*===========================
GUARDED_BY_VIOLATION
===========================*/

   int count;
    Object lock;

    public void increment() {
        synchronized(lock) { //  lock_event
            count++;         //  guarded_access event
        }
    }

    public void times_two() {
        synchronized(lock) { //  lock_event
            count *= 2;      //  guarded_access event
        }
    }

    public void square() {
        synchronized(lock) { //  lock_event
            count *= count;  //  guarded_access event
        }
    }

    public void decrement() {
        count--;             //  Defect: unguarded_access
    }


/*===========================
NULL_RETURN
===========================*/
    public static Object returnC() {
        return null;
    }

    public static Object returnD() {
        return new Object();
    }

    public static void testC() {
        // This demonstrates a very straightforward null-return bug
        returnC().toString();
    }

    public static void testD() {
        returnD().toString();
    }

/*===========================
RESOURCE_LEAK - fixed
===========================*/

    public void ResourceLeak()
    {
	try
	{
		FileInputStream fis = new FileInputStream("foo");  
		BufferedInputStream bis = new BufferedInputStream(fis);
		bis.close();
		fis.close(); 

	}
	catch(Exception e)
	{
		// ignore exception
	}
    }


/*===========================
REVERSE_INULL - fixed
===========================*/

   public static String ReverseINull(Object o) {
	
	if( o == null ) {
		System.out.println("It's null");
	}else{
		System.out.println(o.toString());
	}
	
	return "done";
   }

/*===========================
USE_AFTER_FREE
===========================*/

    public void UseAfterFree()
    {
	try
	{

		BufferedReader br = new BufferedReader(new FileReader("input.txt"));
		
		String line1 = br.readLine();
		br.close();
		System.out.println(br.readLine()); // defect
		
	}
	catch(Exception e)
	{
		// ignore exception
	}
    }






}

