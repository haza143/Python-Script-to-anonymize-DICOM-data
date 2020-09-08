TO_ANOMIZE = [
    "PN",
]

REPLACE_WITH = "Anonymized"


import os, sys, glob
import pydicom



if len(sys.argv) > 1:
    directory = sys.argv[1]
else:
    exit()


def person_names_callback(dataset, data_element):
    if data_element.VR in TO_ANOMIZE:
        data_element.value = REPLACE_WITH
        print(data_element)


for dcm_file in glob.iglob(directory + '**/**', recursive=True):
    if dcm_file.endswith(".dcm"):
        print(dcm_file)
        dataset = pydicom.dcmread(dcm_file)
        dataset.walk(person_names_callback)
        dataset.save_as(dcm_file)