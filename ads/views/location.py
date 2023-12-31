from django.views import View
from django.http import JsonResponse

from ads.models import Location

import json
from configuration import config


class LocationDataView(View):
    def get(self, request):
        with open(config.LOCATION_ROOT_JSON, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                locations = Location(
                    name=item.get("name"),
                    lat=item.get("lat"),
                    lng=item.get("lng")
                )
                locations.save()

        return JsonResponse({"message": "Locations completed"}, status=200)
