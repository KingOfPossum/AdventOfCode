package Challenge4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Challenge4 
{
	public static void main(String[] args)
	{	
		try
		{
			Scanner scanner = new Scanner(new File("D:\\GameDev\\Java\\UNI\\AdventOfCode\\src\\Challenge4\\input.txt"));
			int sum = 0;			
			
			while(scanner.hasNextLine())
			{
				String line = scanner.nextLine();	
				
				String winningNumsTxt = line.split("\\|")[0].split("\\:")[1];
				String yourNumsTxt = line.split("\\|")[1];
				
				List<Integer> winningNums = new ArrayList<Integer>();
				List<Integer> yourNums = new ArrayList<Integer>();
				
				ConvertToList(winningNumsTxt,winningNums);
				ConvertToList(yourNumsTxt,yourNums);
				
				int correctNums = -1;
				
				for(int i = 0;i < winningNums.size();i++)
				{
					if(yourNums.contains(winningNums.get(i)))
					{
						correctNums++;
					}
				}
				
				sum += Math.pow(2, correctNums);
						
				System.out.println(sum);
				System.out.println("------------");
			}			
		} 
		catch (FileNotFoundException e)
		{			
			e.printStackTrace();
		}		
	}
	
	public static void ConvertToList(String txt,List<Integer> list)
	{
		for(int i = 0; i < txt.length();i++)
		{
			if(Character.getNumericValue(txt.charAt(i)) >= 0)
			{
				if(i < txt.length()-1 &&Character.getNumericValue(txt.charAt(i+1)) >= 0)
				{
					list.add(Combine( Character.getNumericValue(txt.charAt(i)), Character.getNumericValue(txt.charAt(i+1))));
				}
				else
				{
					list.add(Character.getNumericValue(txt.charAt(i)));
				}
				i++;
			}
		}
	}
	
	public static int Combine(int num1,int num2)
	{
		return num1*10+num2;
	}
}
