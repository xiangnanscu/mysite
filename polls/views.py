from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    Question.objects.get_or_create(title="foo")
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged