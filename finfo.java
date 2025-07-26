import java.io.*;
class finfo
{
	public static void main(String[] args)
	{
		File f=new File("C:\\Users\\harje\\OneDrive\\Desktop\\abc.txt");
		if(f.exists())
		{
			System.out.println(" File name is "+f.getName());
			System.out.println(" File Location is "+f.getAbsolutePath());
			System.out.println(" File Writable is "+f.canWrite());
			System.out.println(" File Readable is "+f.canRead());
			System.out.println(" File Size is "+f.length());
			System.out.println(" File Removed "+f.delete());
			
		}
		else
		{
			System.out.println(" File doesn't exists ");
		}
	}
}
