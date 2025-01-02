import re

from rest_framework.serializers import ValidationError

word = "youtube"
link_words = ["www", "http"]


def validate_source(value):
    value_list = re.split(r"[. :/]+", value)
    if "youtube" not in value_list:
        for v in value_list:
            if v in link_words:
                raise ValidationError(
                    "Материал не может содержать ссылку на сторонние сайты, кроме youtube.com."
                )
