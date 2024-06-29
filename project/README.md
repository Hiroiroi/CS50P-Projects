# MEAL CALORIE TRACKER
#### Video Demo: <https://youtu.be/hdtBQl8dbE8>
#### Description: 
I have coded a single meal calorie tracker for personal use. 
In designing this project, 
my main considerations were to ensure that I can get a total calories consumer output after entering the foods that I consumed after eating my meal. The reason I wanted this feature was because it would save me having to do the arithmetic in my head as well as googling each time the calories that are in the various foods that I might be consuming. 

I opted to go for a dict to store the calories for each food that I regularly consume. 
I considered initially, including the macros as well like protein, carbohydrate, 
and fat content of the foods and presenting those totals. It wouldn't be too much hassle to add, and I thought that calorie counting was enough for my needs in this case.

I will give a brief description of each of my functions in this project. 
get_calories is my dict which stores the foods and their calorie number. Also included
in this function is food_lower which removes case sensitivity for
the user input and an if else statement that check the dict for the food the user inputs,
otherwise will return 0. This is one aspect I would like to improve on in future, where 
if the user inputs a food that is not in the dict, they can either
add that food and its calorie number or ensure the user knows
that the food is not located in the dict and so no calculation can be made.

calculate_total_calories is as it reads, the total_calories is calculated for each food item that is input by the user (quantity is also part of the calculation).
Quantity was made to be equivalent to one serving size. So 1 would output the calorie number for one serving of 'x' food. This was a purposeful design choice also
where I was conscious that I tend to consume somewhere around 1 serving size or so when I eat some food item. Using serving size as the 
benchmark was far more enticing than using 1 as being equivalent to 100g for example. My calculations are aimed to be approximate
calculations, and measuring out 100g each time seemed a lot more inconvenient.

get_user_input prompts the user for food item eaten or if they are 'done' each food item they consumed and after each food item input
they will be prompted with the quantity of that food item. 'food' will take user_input that the user has eaten and .strip() will allow for
input with random whitespace to still be interpreted by the program without error. 
Line 36-37 allows for the user to be in control of when they are done entering their meal and is a key feature of my program where
total calories may be calculated instead of a bare-bones program which may only output the calorie information of one food item 
at a time which would be less than ideal.

main() will greets the user asking what they ate, retrieve user_input() and print total_calories to the user.