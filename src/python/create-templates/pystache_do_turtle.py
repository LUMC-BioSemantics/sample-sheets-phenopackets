import json
import pystache
from pystache_classes import Disease, Person


def parse_template(filepath):
	file = open(filepath, 'r') 
	return file.read()

cohort_files = ["fIBM.json", "sIBM.json"]

for file in cohort_files:
	with open("../../../data/phenopackets/{}".format(file), 'r') as f:
		str_file = f.read()

	cohort_data = json.loads(str_file)

	for member in cohort_data['members']:
		subject_id = member['subject']['id']
		sex = Person.get_sex(member['subject']['sex']['sex'])

		output_file = open("../../../data/templates/subjects/subject_{}.ttl".format(subject_id), 'w')

		person_dict = {'personIri': "https://ejrd.hackathon.eu/person/{}".format(subject_id),
						'genderIri': "https://ejrd.hackathon.eu/gender/{}".format(subject_id),
						'sexIri': sex,
						'personIdIri': "https://ejrd.hackathon.eu/person/{}/identifier".format(subject_id),
						'personId': subject_id}

		output_file.write(pystache.render(parse_template("../../../data/templates/subject-rdf-turtle-template.ttl"), person_dict))

		output_file.close()

		disease = member['diseases'][0]['term']['id']

		diagnosis = Disease.get_disease(disease)

		output_file = open("../../../data/templates/diagnosis/diagnosis_{}.ttl".format(subject_id), 'w')

		disease_dict = {'personIri': "https://ejrd.hackathon.eu/person/{}".format(subject_id),
						'diagnosisIri': "https://ejrd.hackathon.eu/diagnosis/{}_{}".format(subject_id, diagnosis),
						'diseaseIri': "https://ejrd.hackathon.eu/disease/{}_{}".format(subject_id, diagnosis),
						'diseaseClassIri': diagnosis}

		output_file.write(pystache.render(parse_template("../../../data/templates/diagnosis-rdf-turtle-template.ttl"), disease_dict))

		output_file.close()
