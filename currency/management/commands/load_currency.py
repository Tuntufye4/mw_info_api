from django.core.management.base import BaseCommand
from currency.models import CurrencyRate
import yaml
import os

class Command(BaseCommand):
    help = "Load currency exchange rates from YAML"

    def handle(self, *args, **kwargs):
        file_path = os.path.join("data", "currency_rates.yml")
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"{file_path} not found."))
            return

        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        rates = data.get("rates", {})

        for code, rate in rates.items():
            CurrencyRate.objects.update_or_create(
                code=code.upper(),
                defaults={"rate_to_mwk": rate}
            )

        self.stdout.write(self.style.SUCCESS("✅ Currency exchange rates loaded successfully."))
