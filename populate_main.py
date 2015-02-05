import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTU.settings')

import django
django.setup()

from main.models import Study, Patient
from django.utils import timezone


def populate():
    python_study = addStudy('Alzheimer')

    addPatient(name="Cohen", surname="Wright",study=python_study)
    addPatient(name="Rice", surname="Healy",study=python_study)
    addPatient(name="Comeau", surname="Curiel",study=python_study)
    addPatient(name="Warwick", surname="Rosen",study=python_study)
    addPatient(name="Taguchi", surname="Shao",study=python_study)


    python_study2 = addStudy("Thyroid cancer")
    
    addPatient(name="Collis", surname="Benefiel",study=python_study2)
    addPatient(name="Dyky", surname="Trinchieri",study=python_study2)
    addPatient(name="Laird", surname="Robinson",study=python_study2)
    addPatient(name="Frechette", surname="Mink",study=python_study2)

   
    # Print out what we have added to the user.
    for s in Study.objects.all():
        for p in Patient.objects.filter(study=s):
            print "- {0} - {1}".format(str(s), str(p))

def addPatient(name, surname, study):
    p = Patient.objects.get_or_create(firstName=name,lastName=surname,study=study)[0]
    return p

def addStudy(name):
    s = Study.objects.get_or_create(name=name,startDate=timezone.now())[0]
    return s

# Start execution here!
if __name__ == '__main__':
    print "Starting CTU population script..."
    populate()