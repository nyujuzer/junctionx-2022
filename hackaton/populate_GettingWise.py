import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackaton.settings')

import django
import json
django.setup()

from GettingWise.models import known_vendors, item

def populate():
        python_pages = [
                {'': ''},
        ]
        django_pages = [
                {'': ''},
        ]
        other_pages = [
                {'': ''},
        ]
        cats = {'Python': {'pages': python_pages},
                'Django': {'pages': django_pages},
                'Other Frameworks': {'pages': other_pages},
        }

        for cat, cat_data in cats.items():
                c = add_cat(cat)
                for p in cat_data['pages']:
                        add_page(c, p['title'], p['url'])

        for c in known_vendors.objects.all():
                for p in item.objects.filter(category=c):
                        print(f'- {c}: {p}')
              
        return 0
def add_page(cat, title, url, views=0):
        p = item.objects.get_or_create(category=cat, title=title)[0]
        p.url=url
        p.views=views
        p.save()
        return p

def add_cat(name):
        c = known_vendors.objects.get_or_create(name=name)[0]
        c.save()
        return c

if __name__ == '__main__':
    print("Starting GettingWise population script...")
    populate()
    print("Done!")
