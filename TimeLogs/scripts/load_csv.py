from TimeLogs.models import TimeLogs
from dateutil.parser import parse
from datetime import datetime
import csv

def run():
    def format_date(date_str):
        """
        It takes a string in the format of "dd/mm/yyyy" and returns a string in the format of
        "yyyy-mm-dd"
        
        Args:
          date_str: The date string to be formatted.
        
        Returns:
          A string in the format of YYYY-MM-DD
        """
        
        date_object = parse(date_str, tzinfos={"BST": 6 * 3600})
        date_object = date_object.strftime("%Y-%m-%d")
        return date_object

    def format_time(time_str):
        """
        If the time_str is empty, return 0.0, otherwise return the time_str rounded to 1 decimal place.
        
        Args:
          time_str: the time in seconds
        
        Returns:
          the time_str variable.
        """

        if time_str == "":
            time_str = None
        else:
            time_str = round(int(time_str) / 3600000, 1)
        return time_str
  
    # Reading the csv file and saving the data to the database.
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
