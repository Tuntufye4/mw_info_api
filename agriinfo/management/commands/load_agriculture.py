from django.core.management.base import BaseCommand
from agriinfo.models import Crop, Fish
import yaml
import os
  
class Command(BaseCommand):
    help = "Load agriculture crop and fish data from YAML"

    def handle(self, *args, **kwargs):
        file_path = os.path.join("data", "agriculture_data.yml")
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"{file_path} not found."))
            return

        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        crops = data.get("crops", [])
        fish_species = data.get("fish", [])

        for crop in crops:
            Crop.objects.update_or_create(
                english=crop["english"],
                defaults={
                    "chichewa": crop["chichewa"],
                    "scientific": crop["scientific"]
                }
            )

        for fish in fish_species:
            Fish.objects.update_or_create(
                english=fish["english"],
                defaults={
                    "chichewa": fish["chichewa"],
                    "scientific": fish["scientific"]
                }
            )

        self.stdout.write(self.style.SUCCESS("✅ Agriculture crops and fish data loaded successfully."))
