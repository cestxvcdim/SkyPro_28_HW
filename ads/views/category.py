from django.views import View
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from ads.models import Category

import json
from configuration import config


class CategoryDataView(View):
    def get(self, request):
        with open(config.CATEGORY_ROOT_JSON, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                categories = Category(name=item.get("name"))
                categories.save()

        return JsonResponse({"message": "Categories completed"}, status=200)


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by('name')

        categories = []
        for category in self.object_list:
            categories.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(categories, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except:
            return JsonResponse({"message": "Not found"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category.objects.create(name=category_data.get("name"))

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)

        if (item := category_data.get("name")) is not None:
            self.object.name = item

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"message": "Deleted successfully"}, status=204)
