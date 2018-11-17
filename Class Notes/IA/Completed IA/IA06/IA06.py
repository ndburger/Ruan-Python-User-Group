import sqlite3
import sys
import math
import Levenshtein as le

input = sys.argv[1]

# Define help function
def get_help():
    print ("Enter any university name from ia05 database table and \n \
            get its most similar and least similar university from  \n \
            rest of the universities\n \
            Type -l for list of universities")

if input == "-h":
    get_help()
else:
    conn = sqlite3.connect("ia06.sqlite")
    c = conn.cursor()
    # fetch all required column data
    university_data = c.execute('''SELECT School,  Median_SAT_std,
                                   Acceptance_Rate_Perc_std,
                                   Expenditures_per_student_std,
                                   Graduation_perc_std
                                  FROM universities''').fetchall()

    schools_list = []
    for i in range (0, len(university_data)):
        schools_list.append(university_data[i][0])

    # Print list of schools when input = -l
    if input == "-l":
        for school in schools_list:
            print(school)
    else:
        if input in schools_list:
            index = schools_list.index(input)
            median = university_data[index][1]
            acc_rate = university_data[index][2]
            exp_per_student = university_data[index][3]
            grad_perc = university_data[index][4]
            s1 = []
            s2 = []

            j = 0
            levdist = 10000
            levindex = 0

        for school in schools_list:
            currentSchoolName = school
            ldist = le.distance(input, currentSchoolName)
            if levdist > ldist:
                levindex = j
                levdist = ldist
            j+=1


            for i in range(0, len(university_data)):
                if i != index:
                    score = (median - university_data[i][1])**2 + \
                            (acc_rate - university_data[i][2])**2 +\
                            (exp_per_student - university_data[i][3])**2 +\
                            (grad_perc - university_data[i][4])**2
                    score = math.sqrt(score)
                    if len(s1) is 0:
                        s1.append(university_data[i][0])
                        s1.append(score)
                        s2.append(university_data[i][0])
                        s2.append(score)
                    # Compare and move
                    else:
                        if score < s1[1]:
                            s1[0] = university_data[i][0]
                            s1[1] = score
                        if score > s2[1]:
                            s2[0] = university_data[i][0]
                            s2[1] = score

        print ("Based on our calculation, a most similar University to"
                "{0} is {1} (Euclidean distance {2}), while the least "
                "similar is {3}(Euclidean distance of {4})"
               .format(input, s1[0], s1[1], s2[0], s2[1]))
        print ("The lowest Levenshtein is: " + schools_list[levindex])
