from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import EntrySerializer, FeatureSerializer
from .models import Entry, Feature
from .utils.validate import valid_recaptcha


@csrf_exempt
def entries(request):
    if request.method == 'GET':
        print(request.GET)
        all_entries = Entry.objects.all()
        serializer = EntrySerializer(all_entries, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = EntrySerializer(data=data)

        if not valid_recaptcha(request, data.get("recaptcha_token", 0)): return JsonResponse({"error": "invalid recaptcha"}, status=405)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


def entry_detail(request, pk):
    if request.method == 'GET':
        entry = Entry.objects.get(pk=pk)
        serializer = EntrySerializer(instance=entry, data=request.data)

        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def featured(request):
    if request.method == 'GET':
        featured_entries = Feature.objects.all()
        amount = int(request.GET.get('amount', 0))

        print(request.GET)
        if amount: featured_entries = featured_entries[amount:]
        print(featured_entries)

        serializer = FeatureSerializer(featured_entries, many=True, context={'request': request})

        return JsonResponse(serializer.data, safe=False)

