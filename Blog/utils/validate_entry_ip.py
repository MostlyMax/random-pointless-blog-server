from ..models import Entry
from datetime import datetime


def validate_entry_ip(ip):
    filter_entries = Entry.objects.filter(submitted_date__lte=datetime.today())
    filter_entries = filter_entries.filter(ip__iexact=ip)

    print(filter_entries)
    if filter_entries: return False
    else: return True

