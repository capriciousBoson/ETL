from TimeLogs.models import TimeLogs
from dateutil.parser import parse
from datetime import datetime
import csv

def run():
    def format_date(date_str):
        date_object = parse(date_str, tzinfos={"BST": 6 * 3600})
        date_object = date_object.strftime("%Y-%m-%d")
        return date_object

    def format_time(time_str):
        if time_str == "":
            time_str = 0.0
        else:
            time_str = round(int(time_str) / 3600000, 1)
        return time_str

    with open('TimeLogs/data/TIME-LOGS-CHALLANGE.csv') as file:
        reader = csv.reader(file)

        # to skip the header
        next(reader)

        for row in reader:
            team_ = row[41]
            username_ = row[1]
            job_number_ = row[14]
            booking_codes_ = row[39]
            booking_date_ = format_date(row[8])
            time_tracked_ = format_time(row[9])
            task_estimate_ = format_time(row[23])

            timelog = TimeLogs(team=team_,
                               username=username_,
                               job_number=job_number_,
                               booking_codes=booking_codes_,
                               booking_date=booking_date_,
                               time_tracked=time_tracked_,
                               task_estimate=task_estimate_)
            timelog.save()
