import csv
import datetime
import json
import numpy as np
import uuid

from classes.top_level import Phenopacket, Cohort
from classes.building_blocks import Age, OntologyClass, Sex, Disease, PhenotypicFeature, Biosample, Individual

'''
Include metadata
'''
diseases = {'DOID:3429': 'inclusion body myositis'}
phenotypic_features = {'HP:0003805': 'Rimmed vacuoles'}
severity_levels = {'HP:0012826': 'Moderate', 'HP:0012828': 'Severe', 'HP:0012829': 'Profound'} 
taxonomies = {'NCBITaxon:9606': 'Homo sapiens'}
tissues = {'FMA:22431': 'Vastus lateralis', 'FMA:22532': 'Tibialis anterior'} 

resources = [{'id': "doid",
			  'name': "Human Disease Ontology",
			  'namespace_prefix': "DOID",
			  'url': "http://purl.obolibrary.org/obo/doid.owl",
			  'version': "2019-11-20",
			  'iri_prefix': "http://purl.obolibrary.org/obo/DOID_"},
			  {'id': "fma",
			  'name': "Foundational Model of Anatomy Ontology (subset)",
			  'namespace_prefix': "FMA",
			  'url': "http://purl.obolibrary.org/obo/fma.owl",
			  'version': "2019-11-21",
			  'iri_prefix': "http://purl.obolibrary.org/obo/FMA_"},
			  {'id': "hp",
			  'name': "Human Phenotype Ontology",
			  'namespace_prefix': "HP",
			  'url': "http://purl.obolibrary.org/obo/hp.owl",
			  'version': "2019-11-08",
			  'iri_prefix': "http://purl.obolibrary.org/obo/HP_"},
			  {'id': "ncbitaxon",
			  'name': "NCBI organismal classification",
			  'namespace_prefix': "NCBITaxon",
			  'url': "http://purl.obolibrary.org/obo/ncbitaxon.owl",
			  'version': "2018-07-27",
			  'iri_prefix': "http://purl.obolibrary.org/obo/NCBITaxon_"}]

metadata = {'created': str(datetime.datetime.today()),
			 'created_by': 'Jon Garrido-Aguirre',
			 'resources': resources} 

'''
Create {column_1_key: [column_1_values], ..., column_n_key: [column_n_values]} dict
'''
data_dict = dict()
with open("../../../data/sample-sheets/dummy_metadata-phenopacket_transform.csv", 'r') as f:
	csv_reader = csv.reader(f, delimiter=',')
	for i, line in enumerate(csv_reader):
		if i == 0:
			keys = line
			for item in keys:
				data_dict[item] = []
		else:
			for j, item in enumerate(line):
				data_dict[keys[j]].append(item)

'''
Create cohort phenopackets
'''
for cohort in list(np.unique(data_dict['cohort_id'])):

	cohort_ = Cohort(cohort_id=cohort, metadata=metadata)
	
	cohort_member_ids = [k for k, item in enumerate(data_dict['cohort_id']) if item == cohort]

	cohort_subjects = {x: None for x in list(np.unique([data_dict['subject_id'][i] for i in cohort_member_ids]))}

	for subject in list(cohort_subjects.keys()):
		subject_ids = [k for k, item in enumerate(data_dict['subject_id']) if item == subject]

		cohort_subjects[subject] = subject_ids

	for key, value in cohort_subjects.items():
		phenopacket = Phenopacket(phenopacket_id=uuid.uuid4().hex, metadata=metadata)

		for idx in value:
			biosample = Biosample(biosample_id=data_dict['sample_id'][idx], individual_id=key, tissue_id=data_dict['sample_tissue'][idx], tissue_label=tissues[data_dict['sample_tissue'][idx]], age_at_collection=data_dict['individual_age_at_collection'][idx], is_control_sample=data_dict['is_control_sample'][idx])

			phenotypic_feature = PhenotypicFeature(type_id=data_dict['phenotypic_feature'][idx], type_label=phenotypic_features[data_dict['phenotypic_feature'][idx]], severity_id=data_dict['phenotypic_feature'][idx], severity_label=severity_levels[data_dict['severity'][idx]])

			biosample.phenotypic_features.append(phenotypic_feature.as_dict())

			phenopacket.biosamples.append(biosample.as_dict())

		individual = Individual(individual_id=key, sex=data_dict['sex'][idx], taxon_id=data_dict['taxonomy'][idx], taxon_label=taxonomies[data_dict['taxonomy'][idx]])

		phenopacket.subject = individual.as_dict()

		disease = Disease(disease_id=data_dict['disease'][idx], disease_label=diseases[data_dict['disease'][idx]], age_of_onset=data_dict['onset'][idx])

		phenopacket.diseases.append(disease.as_dict())

		cohort_.members.append(phenopacket.as_dict())

	with open('../../../data/phenopackets/{}.json'.format(cohort), 'w') as file:
		json.dump(cohort_.as_dict(), file, indent=4)
