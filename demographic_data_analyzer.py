import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-demographic-data-analyzer/adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    ##Filter the DataFrame for male entries
    men_df = df[df['sex'] == 'Male']
    average_age_men = round(men_df['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    ## Calculate the total number of people
    total_people = len(df)
    ## Calculate the number of people with a Bachelor's degree
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    ## Filter the DataFrame for people with advanced education
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    ## Calculate the percentage of people with advanced education who make more than 50K
    higher_salary_adv_edu = advanced_education[advanced_education['salary'] == '>50K']
    percentage_higher_salary_adv_edu = (len(higher_salary_adv_edu) / len(advanced_education)) * 100

    # What percentage of people without advanced education make more than 50K?
    ## Filter the DataFrame for people without advanced education
    non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    ## Calculate the percentage of people without advanced education who make more than 50K
    higher_salary_non_adv_edu = non_advanced_education[non_advanced_education['salary'] == '>50K']
    percentage_higher_salary_non_adv_edu = (len(higher_salary_non_adv_edu) / len(non_advanced_education)) * 100

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = advanced_education
    lower_education = non_advanced_education

    # percentage with salary >50K
    higher_education_rich = round(percentage_higher_salary_adv_edu,1)
    lower_education_rich = round(percentage_higher_salary_non_adv_edu,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    ## Filter the DataFrame for people who work the minimum number of hours per week
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]

    ## Calculate the percentage of these people who have a salary of more than 50K
    higher_salary_min_hours = min_hours_workers[min_hours_workers['salary'] == '>50K']
    rich_percentage = (len(higher_salary_min_hours) / len(min_hours_workers)) * 100

    # What country has the highest percentage of people that earn >50K?
    ## Filter the DataFrame for people earning more than 50K
    higher_salary = df[df['salary'] == '>50K']
    ## Calculate the total number of people in each country
    total_people_per_country = df['native-country'].value_counts()
    ## Calculate the number of people earning more than 50K in each country
    higher_salary_per_country = higher_salary['native-country'].value_counts()
    ## Calculate the percentage of people earning more than 50K in each country
    percentage_higher_salary_per_country = (higher_salary_per_country / total_people_per_country) * 100
    ## Identify the country with the highest percentage
    highest_earning_country = percentage_higher_salary_per_country.idxmax()
    highest_earning_country_percentage = round(percentage_higher_salary_per_country.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    ## Filter the DataFrame for people from India earning more than 50K
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    ## Identify the most popular occupation among these people
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
