package Challenge3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Challenge3_Part2 {

	public static char[][] textChars;
	
	public static void main(String[] args)
	{				
		textChars = FillCharArray();
		
		int sum = 0;
		
		for(int i = 0;i < textChars.length;i++)
		{			
			List<Integer> num = new ArrayList<Integer>();			
			
			for(int j = 0;j < textChars[i].length;j++)
			{							
				if(textChars[i][j] == '*')					
				{					
					if(SearchForNumbers(i,j) >= 0)
					{
						sum += SearchForNumbers(i,j);
					}
				}								
			}
		}
		
		System.out.println(sum);
	}

	public static int SearchForNumbers(int i,int j)
	{
		int foundNums = 0;		
		int num1 = -1;
		int num2 = -1;
		//Check if char under this char is a special
		if(i >= 0 && i < textChars.length-1)
		{					
			if(Character.getNumericValue(textChars[i+1][j]) >= 0)
			{		
				if(foundNums == 0)
				{
					num1 = getNumber(i+1, j);
					foundNums++;
				}
				else
				{					
					num2 = getNumber(i+1,j);
					if(num1 == num2)
					{
						num2 = -1;
					}
					else
					{						
						foundNums++;
					}
				}
			}
		}
		
		//Check if char above this char is a special
		if(i > 0 && i <= textChars.length-1)
		{
			if(Character.getNumericValue(textChars[i-1][j]) >= 0)
			{				
				if(foundNums == 0)
				{
					num1 = getNumber(i-1, j);
					foundNums++;
				}
				else
				{					
					num2 = getNumber(i-1,j);
					if(num1 == num2)
					{
						num2 = -1;
					}
					else
					{						
						foundNums++;
					}
				}
			}
		}
		
		//Check if char to the right is a special
		if(j >= 0 && j < textChars[i].length - 1)
		{
			if(Character.getNumericValue(textChars[i][j+1]) >= 0)
			{				
				if(foundNums == 0)
				{
					num1 = getNumber(i, j+1);
					foundNums++;
				}
				else
				{					
					num2 = getNumber(i,j+1);
					if(num1 == num2)
					{
						num2 = -1;
					}
					else
					{						
						foundNums++;
					}
				}
			}
		}
		
		//Check if char to the left is a special
		if(j > 0 && j <= textChars[i].length - 1)
		{
			if(Character.getNumericValue(textChars[i][j-1]) >= 0)
			{						
				if(foundNums == 0)
				{
					num1 = getNumber(i, j-1);
					foundNums++;
				}
				else
				{					
					num2 = getNumber(i,j-1);
					if(num1 == num2)
					{
						num2 = -1;
					}
					else
					{						
						foundNums++;
					}
				}
			}
		}
			
		//Check if char downright to this char is a special
		if(j >= 0 && j < textChars[i].length - 1 && i >= 0 && i < textChars.length - 1)
		{
			if(Character.getNumericValue(textChars[i+1][j+1]) >= 0)
			{				
				if(foundNums == 0)
				{
					num1 = getNumber(i+1, j+1);
					foundNums++;
				}
				else
				{					
					num2 = getNumber(i+1,j+1);
					if(num1 == num2)
					{
						num2 = -1;
					}
					else
					{						
						foundNums++;
					}
				}
			}
		}
		
		//Check if char upright to this char is a special
		if(j >= 0 && j < textChars[i].length - 1 && i > 0 && i <= textChars.length - 1)
		{
			if(Character.getNumericValue(textChars[i-1][j+1]) >= 0)
			{				
				if(foundNums == 0)
				{
					num1 = getNumber(i-1, j+1);
					foundNums++;
				}
				else
				{					
					num2 = getNumber(i-1,j+1);
					if(num1 == num2)
					{
						num2 = -1;
					}
					else
					{						
						foundNums++;
					}
				}
			}
		}
		
		//Check if char downleft to this char is a special
		if(j > 0 && j <= textChars[i].length - 1 && i >= 0 && i < textChars.length - 1)
		{
			if(Character.getNumericValue(textChars[i+1][j-1]) >= 0)
			{				
				if(foundNums == 0)
				{
					num1 = getNumber(i+1, j-1);
					foundNums++;
				}
				else
				{					
					num2 = getNumber(i+1,j-1);
					if(num1 == num2)
					{
						num2 = -1;
					}
					else
					{						
						foundNums++;
					}
				}				
			}
		}
		
		//Check if char upleft to this char is a special
		if(j > 0 && j <= textChars[i].length - 1 && i > 0 && i <= textChars.length - 1)
		{
			if(Character.getNumericValue(textChars[i-1][j-1]) >= 0)
			{				
				if(foundNums == 0)
				{
					num1 = getNumber(i-1, j-1);
					foundNums++;
				}
				else
				{					
					num2 = getNumber(i-1,j-1);
					if(num1 == num2)
					{
						num2 = -1;
					}
					else
					{						
						foundNums++;
					}
				}			
			}
		}
				
		if(foundNums == 2)
		{
			return num1*num2;
		}
		else
		{
			return -1;
		}
	}
	
	public static int getNumber(int i,int j)
	{
		int startOfNumber = -1;
		int currentIndex = j;		
		
		List<Integer> nums = new ArrayList<Integer>();
		
		while(startOfNumber == -1)
		{
			if(currentIndex == 0)
			{
				startOfNumber = currentIndex;
			}
			else
			{
				if(Character.getNumericValue(textChars[i][currentIndex - 1]) > 0)
				{
					currentIndex--;
				}				
				else
				{
					startOfNumber = currentIndex;
				}
			}
		}
		
		currentIndex = startOfNumber;
		
		while(Character.getNumericValue(textChars[i][currentIndex]) > 0)
		{
			nums.add(Character.getNumericValue(textChars[i][currentIndex]));
			currentIndex++;
		}
		
		return Combine(nums);
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
