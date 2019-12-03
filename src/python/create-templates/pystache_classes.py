class Disease:
	def get_disease(disease):
		disease_dict = {'DOID:3429': "http://purl.obolibrary.org/obo/DOID_3429"}
		return disease_dict[disease]

class Person:
	def get_taxonomy(taxonomy):
		taxonomy_dict = {'NCBITaxon:9606': "http://purl.obolibrary.org/obo/NCBITaxon_9606"}
		return taxonomy_dict[taxonomy]

	def get_sex(sex):
		sex_dict = {'0': "http://purl.obolibrary.org/obo/NCIT_C17998", 
					'1': "http://purl.obolibrary.org/obo/NCIT_C46113",
					'2': "http://purl.obolibrary.org/obo/NCIT_C46112",
					'3': "http://purl.obolibrary.org/obo/NCIT_C45908"}
		return sex_dict[sex]

