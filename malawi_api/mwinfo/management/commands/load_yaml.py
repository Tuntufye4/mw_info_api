from django.core.management.base import BaseCommand
from mwinfo.models import District
import yaml

class Command(BaseCommand):
    help = "Load district data from YAML"

    def handle(self, *args, **kwargs):
        with open("data/district_data.yml", "r") as f:
            data = yaml.safe_load(f)

        for d in data["districts"]:
            District.objects.update_or_create(
                name=d["district"],
                defaults={
                    "region": d["region"],
                    "latitude": d["latitude"],
                    "longitude": d["longitude"],
                    "capital": d.get("capital", ""),
                    "population_2023": d["population_2023"],
                    "area_km2": d["area_km2"],
                    "density": d["population_density"],
                    "elevation_m": d["elevation_m"],
                    "climate": d["climate"],
                    "timezone": d["timezone"]
                }
            )
        self.stdout.write(self.style.SUCCESS("Districts loaded successfully"))
