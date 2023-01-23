import random as rd

def ranking_gen(number_of_students,number_of_activities):
    """
    Returns a random ranking matrix for a given number of student and activities
    This matrix is made with the README convention, so there is no need to sort it by activities
    """
    choices = [j + 1 for j in range(number_of_activities)]
    ranking=[]
    for i in range(number_of_students):
        rd.shuffle(choices)
        ranking.append(choices)
    return ranking

if __name__ == "__main__" :
    print(ranking_gen(10,5))