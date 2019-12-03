
'''
Define classes for the Phenopacket building blocks
'''
class Age:
	'''
	Data model for the 'Age' Phenopacket building block
	More info in https://phenopackets-schema.readthedocs.io/en/latest/age.html
	'''
	def __init__(self, age):
		self.age = age

	def as_dict(self):
		return dict(age=self.age)

class OntologyClass:
	'''
	Data model for the 'OntologyClass' Phenopacket building block
	More info in https://phenopackets-schema.readthedocs.io/en/latest/ontologyclass.html
	'''
	def __init__(self, ontology_id, label):
		self.id = ontology_id
		self.label = label

	def as_dict(self):
		return dict(id=self.id, label=self.label)

class Sex:
	'''
	Data model for the 'Sex' Phenopacket building block
	More info in https://phenopackets-schema.readthedocs.io/en/latest/sex.html
	'''
	def __init__(self, sex):
		self.sex = sex

	def as_dict(self):
		return dict(sex=self.sex)

class Disease:
	'''
	Data model for the 'Disease' Phenopacket building block
	More info in https://phenopackets-schema.readthedocs.io/en/latest/disease.html
	'''
	def __init__(self, disease_id, disease_label, age_of_onset):
		self.term = OntologyClass(ontology_id=disease_id, label=disease_label)
		self.onset = Age(age=age_of_onset)

	def as_dict(self):
		return dict(term=self.term.as_dict(), onset=self.onset.as_dict())

class PhenotypicFeature:
	'''
	Data model for the 'PhenotypicFeature' Phenopacket building block
	More info in https://phenopackets-schema.readthedocs.io/en/latest/phenotype.html
	'''
	def __init__(self, type_id, type_label, severity_id, severity_label):
		self.type = OntologyClass(ontology_id=type_id, label=type_label)
		self.severity = OntologyClass(ontology_id=severity_id, label=severity_label)

	def as_dict(self):
		return dict(type=self.type.as_dict(), severity=self.severity.as_dict())

class Biosample:
	'''
	Data model for the 'Biosample' Phenopacket building block
	More info in https://phenopackets-schema.readthedocs.io/en/latest/biosample.html
	'''
	def __init__(self, biosample_id, individual_id, tissue_id, tissue_label, age_at_collection, is_control_sample):
		self.id = biosample_id
		self.individual_id = individual_id
		self.sampled_tissue = OntologyClass(ontology_id=tissue_id, label=tissue_label)
		self.phenotypic_features = list()
		self.individual_age_at_collection = Age(age=age_at_collection)
		self.is_control_sample = is_control_sample

	def as_dict(self):
		return dict(id=self.id, 
			individual_id=self.individual_id, 
			sampled_tissue=self.sampled_tissue.as_dict(), 
			phenotypic_features=self.phenotypic_features,
			individual_age_at_collection=self.individual_age_at_collection.as_dict(),
			is_control_sample=self.is_control_sample)

class Individual:
	'''
	Data model for the 'Individual' Phenopacket building block
	More info in https://phenopackets-schema.readthedocs.io/en/latest/individual.html
	'''
	def __init__(self, individual_id, sex, taxon_id, taxon_label):
		self.id = individual_id
		self.sex = Sex(sex=sex)
		self.taxonomy = OntologyClass(ontology_id=taxon_id, label=taxon_label)

	def as_dict(self):
		return dict(id=self.id, sex=self.sex.as_dict(), taxonomy=self.taxonomy.as_dict())
