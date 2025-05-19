import json

import django
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Item


@csrf_exempt
def get_data(request):
    items = Item.objects.all()
    data = {
        'items': [
            {'id': item.id, 'name': item.name}
            for item in items
        ]
    }
    return JsonResponse(data)

def create_item(request):
    if request.method == 'POST':
        try:
            try:
                data = json.loads(request.body)
            except django.http.request.RawPostDataException:
                # リクエストボディが既に読み込まれている場合
                data = request.POST.dict()

            name = data.get('name', '')

            if name:
                item = Item.objects.create(name=name)
                return JsonResponse({
                    'success': True,
                    'message': 'アイテムを作成しました',
                    'item': {'id': item.id, 'name': item.name}
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'アイテム名は必須です'
                }, status=400)

        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': '無効なJSONデータです'
            }, status=400)

    return JsonResponse({
        'success': False,
        'message': 'POSTリクエストが必要です'
    }, status=405)
