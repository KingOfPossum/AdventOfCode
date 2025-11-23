package Challenge2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Challenge2 {

	public static void main(String[] args)
	{
		int maxRed = 12;
		int maxGreen = 13;
		int maxBlue = 14;
		
		int sum = 0;
		
		try 
		{
			Scanner scanner = new Scanner(new File("D:\\GameDev\\Java\\UNI\\AdventOfCode\\src\\Challenge2\\input.txt"));
			List<Integer> gameNum = new ArrayList<Integer>();						
			
			while(scanner.hasNextLine())
			{			
				System.out.println("Next Line: ");
				System.out.println();
				
				String line = scanner.nextLine();				
				boolean isFine = true;
				
				String[] parts = line.split(";");
				
				for(int i = 0;i < parts.length;i++)
				{
					int red = getColorAmmount(parts[i],"red");
					int green = getColorAmmount(parts[i],"green");
					int blue = getColorAmmount(parts[i],"blue");
					
					System.out.println("red : " + red);
					System.out.println("green : " + green);
					System.out.println("blue : " + blue);
					
					if(!(red <= maxRed && green <= maxGreen && blue <= maxBlue))
					{
						isFine = false;									
					}				
					
					System.out.println();					
				}
				
				if(isFine)
				{
					gameNum.add(getGameNum(line));
					System.out.println("Game : " + gameNum.get(gameNum.size()-1));
				}	
				
				System.out.println("---------------");				
			}			
			
			for(int i = 0;i < gameNum.size();i++)
			{
				sum += gameNum.get(i);
			}
			System.out.println(sum);
		}
		catch (FileNotFoundException e)
		{			
			e.printStackTrace();
		}
		
	}

	public static int Combine(int num1,int num2 , int num3)
	{
		if(num2 >= 0 && num3 < 0)
		{			
			return num1 * 10 + num2;
		}
		else if(num2 == 0 && num3 == 0)
		{
			return num1 * 100 + num2 * 10 + num3;
		}
		else
		{
			return num1;
		}
	}
	
	public static int Combine(int num1,int num2)
	{
		if(num1 >=0 )
		{
			return num1 * 10 + num2;
		}
		else
		{
			return num2;
		}
	}
	
	public static int getGameNum(String line)
	{
		int gameNum1 = Character.getNumericValue(line.charAt(5));
		int gameNum2 = 0;
		int gameNum3 = 0;
	
		if(line.charAt(6) != ':')
		{
			gameNum2 = Character.getNumericValue(line.charAt(6));				
		}
		else
		{
			gameNum2 = -1;
		}
		
		if(!Character.isWhitespace(line.charAt(7)) && !(line.charAt(7) == ':'))
		{
			gameNum3 = Character.getNumericValue(line.charAt(7));
		}
		else
		{
			gameNum3 = -1;
		}
		
		return Combine(gameNum1,gameNum2,gameNum3);
	}
	
	public static int getColorAmmount(String line ,String color)
	{
		int ammount = 0;
		
		if(!line.contains(color))
		{
			ammount = 0;
		}
		else
		{
			int num_1 = 0;
			int num_2 = Character.getNumericValue(line.charAt(line.indexOf(color) - 2));
			
			if(!Character.isWhitespace(line.charAt(line.indexOf(color) - 3)))
			{
				num_1 = Character.getNumericValue(line.charAt(line.indexOf(color) - 3));		
			}
			
			ammount += Combine(num_1,num_2);
			
			int i = line.indexOf(color);
			for(int j = i + 1;j < line.length();j++)
			{
				if(line.indexOf(color,j) > 0)
				{							
					int num1 = 0;
					int num2 = Character.getNumericValue(line.charAt(line.indexOf(color,j) - 2));
					
					if(!Character.isWhitespace(line.charAt(line.indexOf(color,j) - 3)))
					{
						num1 = Character.getNumericValue(line.charAt(line.indexOf(color,j) - 3));
					}						
					
					ammount += Combine(num1,num2);
					
					j = line.indexOf(color,j) + color.length() + 1;
				}
			}					
		}
		
		return ammount;
	}	
}