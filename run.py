from handle_data_values import HandleDataValues

population = HandleDataValues('population')
life_expectancy = HandleDataValues('lifeexpectancy')

# with missing values
population.with_missing_values()
life_expectancy.with_missing_values()

# without missing values
population.without_missing_values()
life_expectancy.without_missing_values()