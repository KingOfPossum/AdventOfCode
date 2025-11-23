package Challenge1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Challenge1 {

	public static void main(String[] args)
	{	
		char[] numbers = {'0','1','2','3','4','5','6','7','8','9'};
		String[] numbers2 = {"one","two","three","four","five","six","seven","eight","nine"};
		int sum = 0;		
		
		try 
		{
			Scanner scanner = new Scanner(new File("D:\\GameDev\\Java\\UNI\\AdventOfCode\\src\\Challenge1\\input.txt"));
			while(scanner.hasNextLine())
			{
				String line = scanner.nextLine();
				System.out.println(line);				
				
				List<Integer> numbersInText = new ArrayList<Integer>();
				
				List<Integer> index = new ArrayList<Integer>();
				List<Character> indexNumbers = new ArrayList<Character>();
				
				for(int i = 0;i < numbers2.length;i++)
				{
					if(line.contains(numbers2[i]))
					{
						index.add(line.indexOf(numbers2[i]));	
						indexNumbers.add(numbers[i + 1]);
						for(int j = line.indexOf(numbers2[i]) + 1;j < line.length();j++)
						{
							if(line.indexOf(numbers2[i], j) > 0)
							{
								index.add(line.indexOf(numbers2[i], j));
								indexNumbers.add(numbers[i + 1]);								
							}
							j += numbers2[i].length() + 1;
						}
					}					
				}
				
				System.out.println(index.size());
				
				for(int k = 0;k < index.size();k++)
				{
					System.out.println(indexNumbers.get(k) + ": " + index.get(k));
				}
				
				for(int i = 0;i < line.length();i++)
				{
					for(int k = 0;k < index.size();k++)
					{
						if(index.get(k) == i)
						{
							System.out.println("i : " + i + " ; index[k] : " + index.get(k));
							numbersInText.add(Character.getNumericValue(indexNumbers.get(k)));
						}
					}
					
					for(int j = 0;j < numbers.length;j++)
					{						
						if(line.charAt(i) == numbers[j])
						{
							numbersInText.add(Character.getNumericValue(numbers[j]));
							break;
						}
					}
				}	
				
				if(numbersInText.size() > 0)
				{					
					for(int i = 0;i < numbersInText.size();i++)
					{
						System.out.print(numbersInText.get(i) +  "  ,  ");
					}
				}
				
				System.out.println();
				
				int num1;
				
				if(numbersInText.size() > 0)
				{
					num1 = numbersInText.get(0);
				}
				else
				{
					num1 = 0;					
				}
				
				int num2;
				
				if(numbersInText.size() <= 1)
				{
					num2 = num1;
				}
				else
				{
					num2 = numbersInText.get(numbersInText.size() -1);					
				}
				
				System.out.println("Num1 : " + num1);
				System.out.println("Num2 : " + num2);
				
				int combinedNum;
				
				if(num2 == 0)
				{
					combinedNum = num1;
				}
				else
				{
					combinedNum = num1 * 10 + num2;					
				}
				
				System.out.println("CombinedNum : " + combinedNum);
				System.out.println();
				
				sum += combinedNum;		
			}
			scanner.close();
		} catch (FileNotFoundException e)
		{			
			e.printStackTrace();
		}		
				
		System.out.println();
		System.out.println("Sum : " + sum);
	}

}
