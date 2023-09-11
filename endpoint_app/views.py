from django.shortcuts import render
from django.http import JsonResponse
import datetime
import pytz

def endpoint(request):
    slack_name = request.GET.get('slack_name', 'owolabi_caleb')
    track = request.GET.get('track', 'backend')

    # getting current date and time
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.now(pytz.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')


    github_source_url = 'https://github.com/calebayobami/endpoint'
    github_repo_url = 'https://github.com/calebayobami/endpoint'


    data = {
        'slack_name': slack_name,
        'track':track,
        'current_day': current_day,
        'utc_time': utc_time,
        'github_repo_url': github_repo_url,
        'github_source_url':github_source_url,
        'status_code': 200
    }

    return JsonResponse(data)
