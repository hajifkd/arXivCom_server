from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Comment, Article, User

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
@login_required
@require_POST
def comment(request, arXiv_id):
    user = request.user
    data = json.loads(request.body)
    article, _ = Article.objects.get_or_create(arXiv_id=arXiv_id)

    comment = Comment()
    comment.text = data['text']
    comment.user = user
    comment.article = article
    comment.save()

    return JsonResponse({'success': True})

@csrf_exempt
@login_required
@require_GET
def list(request, arXiv_id):
    user = request.user
    article, f = Article.objects.get_or_create(arXiv_id=arXiv_id)

    if f:
        return JsonResponse([], safe=False)

    comments = []
    for i, comment in enumerate(article.comment_set.all()):
        # We assume that all the user account have their own ORCIDs.
        uid = comment.user.socialaccount_set.all()[0].uid
        text = comment.text
        created_at = comment.created_at
        comments.append({'uid': uid, 'text': text, 
                         'created_at': created_at, 'cid': i})

    return JsonResponse(comments, safe=False)


@csrf_exempt
@login_required
@require_POST
def user_info(request):
    data = json.loads(request.body)
    query = User.objects.filter(socialaccount__uid__in=data['uids'])\
                        .values('first_name', 
                                'last_name', 
                                'socialaccount__uid')

    result = {d['socialaccount__uid']: {'first_name': d['first_name'],
                                        'last_name': d['last_name']}
              for d in query}
    return JsonResponse(result)


@csrf_exempt
@login_required
@require_POST
def count_comments(request):
    data = json.loads(request.body)
    query = Article.objects.filter(arXiv_id__in=data['aids'])

    result = {a.arXiv_id: a.comment_set.count() for a in query}
    return JsonResponse(result)


