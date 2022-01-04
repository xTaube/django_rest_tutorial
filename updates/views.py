import json
from django.core.serializers import serialize
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from .models import Update
from django_rest_tutorial.mixin import JsonReponseMixin


def json_example_view(request):
    '''
    URI -- for a REST API
    GET -- Retrive
    '''
    data = {
        "count": 12,
        "content": "new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type="application/json")


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        '''
        URI -- for a REST API
        GET -- Retrive
        '''
        data = {
            "count": 12,
            "content": "new content"
        }

        return JsonResponse(data)


class JsonCBV2(JsonReponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 12,
            "content": "new content"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")