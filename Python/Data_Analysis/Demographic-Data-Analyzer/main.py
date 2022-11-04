import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = df['race'].unique()
    race_count = pd.Series(
        map(lambda race: (df['race'] == race).sum() , races), 
        index=races)
    

    # What is the average age of men?
    age = df.loc[df['sex'] == 'Male', ['sex', 'age']]  
    average_age_men = age['age'].mean().round(1)   

    # What is the percentage of people who have a Bachelor's degree?
    educ = df['education'].count() # n of all people in education row
    bach = (df['education'] == 'Bachelors').sum() # n of all with bach degree
    percentage_bachelors = ((bach / educ) * 100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    higher_education = (df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'), ['salary']])
    
    lower_education = (df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'), ['salary']]) # n of people w lower educatio

    # percentage with salary >50K
    higher_education_rich = float((((higher_education['salary'] == '>50K').sum() / higher_education.count()) * 100).round(1))
    lower_education_rich = float((((lower_education['salary'] == '>50K').sum() / lower_education.count()) * 100).round(1))

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_people = df.loc[df['hours-per-week'] == df['hours-per-week'].min(),['salary']] 
    all_min_work_people = min_work_people.count()# n of people working min num of hours
    rich_min_work = (min_work_people['salary'] == '>50K').sum() # n of ppl w min work hours and 50+ k
    
    num_min_workers = all_min_work_people

    rich_percentage = float(((rich_min_work / num_min_workers) * 100).round(1))

    # What country has the highest percentage of people that earn >50K?
    all_workers = df['native-country'].unique()# all people per country
    
    worker_per_country = pd.Series(
        map(lambda worker: (df['native-country'] == worker).sum() , all_workers), 
        index=all_workers)
    
    rich_worker_per_country = pd.Series(
        map(lambda worker:  ( (df['native-country'] == worker) & (df['salary'] == '>50K') ).sum() , all_workers) , 
        index=all_workers)                        # all people per country that make over 50 k
    
    percentage_of_rich_workers = pd.Series( ((rich_worker_per_country / worker_per_country) * 100).round(1) , index=all_workers) # percentage of richest workers from all countries
    
    highest_earning_country = str(percentage_of_rich_workers.idxmax())
    
    highest_earning_country_percentage = float(percentage_of_rich_workers.max())

    # Identify the most popular occupation for those who earn >50K in India.
    job_india_50k = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    
    top_IN_occupation = str(job_india_50k['occupation'].value_counts().idxmax())

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


calculate_demographic_data()