'''
Definition of the top-level elements in the Phenopacket schema
'''
class Phenopacket:
	'''
	Definition of the Phenopacket top-level element
	More info in https://phenopackets-schema.readthedocs.io/en/latest/phenopacket.html
	'''
	def __init__(self, phenopacket_id, metadata):
		self.id = phenopacket_id
		self.subject = None  # Individual()
		self.phenotypic_features = list()
		self.biosamples = list()
		self.diseases = list()
		self.meta_data = metadata

	def as_dict(self):
		return dict(id=self.id, 
			subject=self.subject,
			phenotypic_features=self.phenotypic_features,
			biosamples=self.biosamples,
			diseases=self.diseases,
			meta_data=self.meta_data)

class Cohort:
	'''
	Definition of the Cohort top-level element
	More info in https://phenopackets-schema.readthedocs.io/en/latest/cohort.html
	'''
	def __init__(self, cohort_id, metadata):
		self.id = cohort_id
		self.members = list()
		self.meta_data = metadata

	def as_dict(self):
		return dict(id=self.id, 
			members=self.members,
			meta_data=self.meta_data)
