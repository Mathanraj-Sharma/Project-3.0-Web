from django.shortcuts import render
from reviews.models import review

# Create your views here.

def get_question_totals(hotel_id, question):
    """
    this function will get a hotel id and question as input and return the list of answers
    for that question in all reviews for that hotel
    """
    reviews  = review.objects.filter(hotel = hotel_id).values('qa')
    answers = []
    for rev in reviews:
        rev_list = ast.literal_eval(rev['qa'])
        for dic in rev_list:
            if dic['question'] == question:
               answers.append(dic["answer"])

    return answers