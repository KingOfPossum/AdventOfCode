package Challenge3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Challenge3 {

	public static char[][] textChars;
	
	public static void main(String[] args)
	{				
		textChars = FillCharArray();
		
		int sum = 0;
		
		for(int i = 0;i < textChars.length;i++)
		{
			boolean isNumber = false;
			boolean hasSymbol = false;
			
			List<Integer> num = new ArrayList<Integer>();			
			
			for(int j = 0;j < textChars[i].length;j++)
			{							
				if(Character.getNumericValue(textChars[i][j]) >= 0)
				{					
					isNumber = true;
					num.add(Character.getNumericValue(textChars[i][j]));
					if(!hasSymbol)
					{
						hasSymbol = SearchForSymbol(i,j);
					}
				}
				else
				{
					if(isNumber == true && hasSymbol)
					{
						System.out.println(Combine(num));
						sum += Combine(num);
						num.clear();
					}
					isNumber = false;
					hasSymbol = false;
					num.clear();
				}
				
				if(j == textChars[i].length - 1)
				{
					if(hasSymbol)
					{
						System.out.println(Combine(num));
						sum += Combine(num);
						num.clear();
					}
					hasSymbol = false;
				}
			}
		}
		
		System.out.println(sum);
	}

	public static boolean SearchForSymbol(int i,int j)
	{
		//Check if char under this char is a special
		if(i >= 0 && i < textChars.length-1)
		{					
			if(IsSpecial(textChars[i+1][j]))
			{				
				return true;
			}
		}
		
		//Check if char above this char is a special
		if(i > 0 && i <= textChars.length-1)
		{
			if(IsSpecial(textChars[i-1][j]))
			{				
				return true;
			}
		}
		
		//Check if char to the right is a special
		if(j >= 0 && j < textChars[i].length - 1)
		{
			if(IsSpecial(textChars[i][j+1]))
			{				
				return true;
			}
		}
		
		//Check if char to the left is a special
		if(j > 0 && j <= textChars[i].length - 1)
		{
			if(IsSpecial(textChars[i][j-1]))
			{						
				return true;
			}
		}
			
		//Check if char downright to this char is a special
		if(j >= 0 && j < textChars[i].length - 1 && i >= 0 && i < textChars.length - 1)
		{
			if(IsSpecial(textChars[i+1][j+1]))
			{				
				return true;
			}
		}
		
		//Check if char upright to this char is a special
		if(j >= 0 && j < textChars[i].length - 1 && i > 0 && i <= textChars.length - 1)
		{
			if(IsSpecial(textChars[i-1][j+1]))
			{				
				return true;
			}
		}
		
		//Check if char downleft to this char is a special
		if(j > 0 && j <= textChars[i].length - 1 && i >= 0 && i < textChars.length - 1)
		{
			if(IsSpecial(textChars[i+1][j-1]))
			{				
				return true;				
			}
		}
		
		//Check if char upleft to this char is a special
		if(j > 0 && j <= textChars[i].length - 1 && i > 0 && i <= textChars.length - 1)
		{
			if(IsSpecial(textChars[i-1][j-1]))
			{				
				return true;				
			}
		}
				
		return false;
	}
		
	//Checks if char is a special Character
	public static boolean IsSpecial(char symbol)
	{
		char[] specialCharacters = {'%','$','§','&','/','\\','#','+','-','*','@','=','<','>'};
		
		for(int i = 0;i < specialCharacters.length;i++)
		{
			if(symbol == specialCharacters[i])
			{
				return true;
			}
		}
		return false;
	}
	
	//Combine numbers
	public static int Combine(List<Integer> num)
	{
		int sum = 0;
		
		for(int i = 0;i < num.size();i++)
		{
			sum += Math.pow(10, num.size()- i -1 ) * num.get(i);
		}
		
		return sum;
	}
	
	public static char[][] FillCharArray()
	{
		try
		{
			//Get Ammount of lines in textfile
			Scanner scanner_length = new Scanner(new File("D:\\GameDev\\Java\\UNI\\AdventOfCode\\src\\Challenge3\\input.txt"));
			
			int textLines = 0;
			
			while(scanner_length.hasNextLine())
			{
				scanner_length.nextLine();
				textLines++;
			}
			
			scanner_length.close();
			
			//Fill Char Array with the text of the textfile
			Scanner scanner = new Scanner(new File("D:\\GameDev\\Java\\UNI\\AdventOfCode\\src\\Challenge3\\input.txt"));
			
			char[][] textChars = new char[textLines][140];
			
			for(int i = 0;i < textLines;i++)
			{
				String line = scanner.nextLine();
				for(int j = 0;j < 140;j++)
				{
					textChars[i][j] = line.charAt(j);
				}
			}
			
			scanner.close();	
			
			return textChars;
		}
		catch (FileNotFoundException e)
		{			
			e.printStackTrace();
			return null;
		}		
	}	
}
