package Challenge4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Challenge4_Part2 
{
	public static void main(String[] args)
	{	
		try
		{
			Scanner scanner = new Scanner(new File("D:\\GameDev\\Java\\UNI\\AdventOfCode\\src\\Challenge4\\input.txt"));
			Scanner scanner_length = new Scanner(new File("D:\\GameDev\\Java\\UNI\\AdventOfCode\\src\\Challenge4\\input.txt"));
			
			int sum = 0;			
			int lines = 0;
			
			while(scanner_length.hasNextLine())
			{
				lines++;
				scanner_length.nextLine();
			}
			scanner_length.close();
			
			int[] gameCount = new int[lines];
			
			for(int i = 0;i < gameCount.length;i++)
			{
				gameCount[i] = 1;
			}		
			
			int currentLine = -1;
			
			while(scanner.hasNextLine())
			{
				String line = scanner.nextLine();	
				currentLine++;
				
				String winningNumsTxt = line.split("\\|")[0].split("\\:")[1];
				String yourNumsTxt = line.split("\\|")[1];
				
				List<Integer> winningNums = new ArrayList<Integer>();
				List<Integer> yourNums = new ArrayList<Integer>();
				
				ConvertToList(winningNumsTxt,winningNums);
				ConvertToList(yourNumsTxt,yourNums);
				
				int correctNums = 0;
				
				for(int i = 0;i < winningNums.size();i++)
				{
					if(yourNums.contains(winningNums.get(i)))
					{
						correctNums++;
					}
				}
				
				//System.out.println(correctNums);
				
				int currentGameCountValue = gameCount[currentLine];
				for(int j = 0;j < currentGameCountValue;j++)
				{
					for(int i = 1;i <= correctNums;i++)
					{
						if(currentLine + i < gameCount.length)
						{
							gameCount[currentLine + i]++;							
						}
					}				
				}				
			}
			
			for(int i = 0;i < gameCount.length;i++)
			{
				sum += gameCount[i];
				System.out.println(sum);
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
