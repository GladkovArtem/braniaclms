from django.core.management import BaseCommand

from mainapp.models import News

class Command(BaseCommand):

    def handle(self, *args, **options):
        news_objects =[]
        for i in range(100):
            news_objects.append(
                News(
                    title=f'news#{i}',
                    preamble=f'preamble#{i}',
                    body=f'this is body for news{i}'
                )
            )
        News.objects.bulk_create(news_objects)