from django.core.management.base import BaseCommand
import json
from pathlib import Path
from api.models import Word, Group


class Command(BaseCommand):
    help = 'Seed database from JSON files in ../seed'

    def handle(self, *args, **options):
        base = Path(__file__).resolve().parents[4] / 'seed'
        self.stdout.write(f'Looking for seed files in {base}')
        if not base.exists():
            self.stdout.write('No seed directory found; skipping')
            return

        for f in sorted(base.glob('*.json')):
            self.stdout.write(f'Importing {f.name}...')
            try:
                data = json.loads(f.read_text(encoding='utf-8'))
            except Exception as e:
                self.stdout.write(f'  failed to read {f.name}: {e}')
                continue

            # allow either list or single object
            items = data if isinstance(data, list) else [data]

            # derive group name from filename
            group_name = f.stem.replace('_', ' ').title()
            group, _ = Group.objects.get_or_create(name=group_name)

            created = 0
            for it in items:
                kanji = it.get('kanji') or it.get('word') or it.get('kanji')
                romaji = it.get('romaji', '')
                english = it.get('english', '')
                parts = it.get('parts', [])
                if not kanji:
                    continue
                w, was = Word.objects.get_or_create(kanji=kanji, defaults={'romaji': romaji, 'english': english, 'parts': parts})
                if not was:
                    # update fields if missing
                    updated = False
                    if not w.romaji and romaji:
                        w.romaji = romaji
                        updated = True
                    if not w.english and english:
                        w.english = english
                        updated = True
                    if updated:
                        w.save()
                w.groups.add(group)
                created += 1

            self.stdout.write(f'  imported {created} items into group "{group.name}"')
