package Challenge5;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;


public class Challenge5 {

	public static void main(String[] args)
	{		
		try 
		{
			Scanner scanner = new Scanner(new File("D:\\GameDev\\Java\\UNI\\AdventOfCode\\src\\Challenge5\\input.txt"));
			
			String line = scanner.nextLine();
			
			int[] seeds = getSeeds(line);
			
			scanner.nextLine();
			scanner.nextLine();
			line = scanner.nextLine();
			
			int[][] seedToSoil = new int[9][3];
			
		} 
		catch (FileNotFoundException e)
		{			
			e.printStackTrace();
		}		
	}
	
	public static int ConvertToInt(String txt)
	{	
		List<Integer> list = new ArrayList<Integer>();
		for(int i = 0;i < txt.length();i++)
		{
			if(Character.getNumericValue(txt.charAt(i)) >= 0)
			{
				list.add(Character.getNumericValue(txt.charAt(i)));				
			}
		}
		
		int num = 0;
		
		for(int i = 0;i < list.size();i++)
		{
			num += Math.pow(10, list.size()- i -1 ) * list.get(i);
		}
		
		return num;
	}
	
	public static int[] getSeeds(String line)
	{		
		String[] seedsTxt = line.split("\\:")[1].split("\s");

		int[] seeds = new int[seedsTxt.length-1];
		
		for(int i = 0;i < seeds.length;i++)
		{
			seeds[i] = ConvertToInt(seedsTxt[i+1]);
		}
		
		return seeds;
	}
}
