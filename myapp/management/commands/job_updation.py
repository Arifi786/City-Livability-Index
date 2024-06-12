import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import City
import pandas as pd

# Read the CSV file
csv_file_path = '/Users/arif/Downloads/archive-2/census2011_modified.csv'
data = pd.read_csv(csv_file_path)

# Iterate over the rows and update the job column
for index, row in data.iterrows():
    # Assuming 'id' column is used for identifying the rows in the MySQL table
    record_id = row['District']

    # Split the job opportunities string into individual jobs
    job_opportunities = [job.strip() for job in row['Job_Opportunities'].split(',')]

    # Get the corresponding record from the MySQL table
    try:
        record = City.objects.get(city_name=row['District'], state=row['State'])

        # Update the job column with multiple job values
        record.Job = ', '.join(job_opportunities)
        record.save()
        print(f"Updated job for record with id {record_id}")
    except City.DoesNotExist:
        print(f"Record with id {record_id} does not exist in the database")

print("Job column update complete.")
