# Half Life
## Description

Radioactive materials decay over time and turn into other substances. For example, Carbon-14 decays into Nitrogen-14 through beta decay. 

The rate of radioactive decay of a material is measured in terms of its half-life. The half-life of a material is defined to be the amount of time it takes for half of the material to undergo radioactive decay. Let m be the initial mass in grams of some material and let h be the material’s half-life in days. Then the remaining mass of the material on day t, denoted m(t), is given by the formula:

![image](https://user-images.githubusercontent.com/86201781/128746882-d53d5c1e-c893-493b-b4ff-fb146cea3aa0.png)

## Problem description

To write a program which does the following:
- Prompt the user to enter the initial mass of the material (in grams). You must make sure that the user enters a positive number. If they do not enter a positive number, print a message informing them so, and prompt them to enter the initial amount of material again. Keep doing this until they enter a positive number.
- Prompt the user to enter the half-life of the material (in days). As above, make sure that the user enters a positive number, and if they don’t, keep asking until they do.
- Starting from day 0, output the amount of the material remaining at one-day intervals. Thus, for day 0, day 1, day 2, etc., you should print out the amount of remaining mass according to the above formula. Your program should stop on the first day on which remaining mass is less than 1% of the initial mass.

![image](https://user-images.githubusercontent.com/86201781/128747135-a9218167-ed7a-4914-87bf-2e99428c1d2f.png)

## How to use
Here are the steps for how to open, use and utilize the program:

- First, download all of the files listed above;
- Put all the files in one folder;
- Open the file Projec_half_life.py;
- The program will open a command console which will ask you to input the initial mass of the material and then its half life.
