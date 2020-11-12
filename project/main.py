import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

def get_data():
    df = pd.read_csv("data.csv")
    print(df)
    print('')
    input = df.drop('hired', axis='columns')
    target = df['hired']
    return input, target

def get_unique_values(lst):
    return {key: value for (key, value) in zip(list(lst),range(0,len(list(lst))))}

def main():

    input, target = get_data()
    le_education = LabelEncoder()
    le_english = LabelEncoder()
    le_experience = LabelEncoder()
    le_interview = LabelEncoder()
    le_target = LabelEncoder()

    # Unique values
    le_education.fit(input['education'])
    le_english.fit(input['english'])
    le_experience.fit(input['experience'])
    le_interview.fit(input['interview'])
    le_target.fit(target)

    u_education = get_unique_values(list(le_education.classes_))
    u_english = get_unique_values(list(le_english.classes_))
    u_experience = get_unique_values(list(le_experience.classes_))
    u_interview = get_unique_values(list(le_interview.classes_))
    u_target = get_unique_values(list(le_target.classes_))

    print(u_education)
    print(u_english)
    print(u_experience)
    print(u_interview)
    print(u_target)
    print('')

    # Converting words to numbers
    input['education_n'] = le_education.fit_transform(input['education'])
    input['english_n'] = le_english.fit_transform(input['english'])
    input['experience_n'] = le_experience.fit_transform(input['experience'])
    input['interview_n'] = le_interview.fit_transform(input['interview'])

    n_input = input.drop(['education','english','experience','interview'], axis='columns')

    print(n_input)
    print('')

    # ML
    tree = DecisionTreeClassifier()
    tree.fit(n_input, target)

    # Making decision to new data

    new_data = [
        u_education['Student'],
        u_english['Intermediate'],
        u_experience['1 year'],
        u_interview['neutral']
    ]

    decision = tree.predict([new_data])
    print(decision)

if __name__ == "__main__":
    main()
