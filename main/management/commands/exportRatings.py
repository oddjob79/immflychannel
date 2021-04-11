from django.core.management.base import BaseCommand, CommandError
from ._private import calcAvgRatings, Channel
import csv

# export list of channels and average ratings to csv file
class Command(BaseCommand):
    def handle(self, *args, **options):
        dataset = []
        # retrieve all channels
        channels = Channel.objects.all()
        for chan in channels:
            # calculate average rating
            avg = calcAvgRatings(chan)
            # populate dictionary
            if avg:
                avg = round(avg,2)
                dataset.append({"channel title":chan.title, "average rating":avg})

        # sort dictionary before export
        dataset=sorted(dataset, key=lambda x:x['average rating'], reverse=True)

        # generate csv
        with open('avgratings.csv', 'w') as f:
            w = csv.DictWriter(f, fieldnames=["channel title", "average rating"])
            w.writeheader()
            for d in dataset:
                w.writerow(d)
