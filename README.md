# Sample-Data-Projects
The folder contains several sample ETL data projects 


**1. Project name: Gym - Membership management and marketing**

**Usecase:** In a local gym, every month there is a need to find out the list of members who are currently active and
enrolled for the "Gold", "Silver" and "Bronze" memberships. This will help the gym's marketing team to plan for targeted
promotions of various services offered at the gym to selected group of members.

**Problem statement:** Currently, someone have to manually evaluate the "current members.txt" file to address the above usecase. It would be great,
if this process can be automated with python program

**Note:** for illustration purposes of this project, we are going to generate some sample data and then process it to address the usecase listed above.
    Input:
    "MonthlyFile" --> File that contains the list of all members (including active/inactive and all membership categories) at the end of each month.
    Output:
    "GoldMonthlyFile" --> File that contains the list of all members who have "Gold" membership
    "SilverMonthlyFile" --> File that contains the list of all members who have "Silver" membership
    "BronzeMonthlyFile" --> that contains the list of all members who have "Bronze" membership

**How to run this program:** please install a python IDE, download the "gym_MemberManagement.py" and the "data" folders to your local and then run the python code.



**2. Project name (CourseEra practice project): ETL - Automated extraction of GDP's of all countires**
**Usecase** An international firm that is looking to expand its business in different countries across the world wants an automated script that can extract the list of all countries in order of 
their GDPs in billion USDs (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF). 
Since IMF releases this evaluation twice a year, this code will be used by the organization to extract the information as it is updated.

**Data Location** 
You can find the required data on this webpage (https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29).

**Requirements**
1. The required information needs to be made accessible as a JSON file 'Countries_by_GDP.json' as well as 
a table 'Countries_by_GDP' in a database file 'World_Economies.db' with attributes 'Country' and 'GDP_USD_billion.'

2. To demonstrate the success of this code: run a query on the database table to display only the entries with more 
than a 100 billion USD economy. Also, log the entire process of execution in a file named 'etl_project_log.txt'.

**Code** The Python code for this project can be found in 'etl_project_gdp.py' that performs all the required tasks.
