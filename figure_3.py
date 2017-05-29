# Snippet 3.
# Fetching SMILES identifiers for compounds tested for activity against a given target.  

from chembl_webresource_client.new_client import new_client
# UniProt ID for erbB-2, a target of Lapatinib
uniprot_id = "P04626"
# Getting a target for the given accession:
targets = new_client.target.filter(target_components__accession=uniprot_id)
# Retrieving activities:
activities = new_client.activity.filter(target_chembl_id__in=[target['target_chembl_id'] for target in targets]).filter(pchembl_value__gt=7)
# Creating a set of unique SMILES:
smiles_set = set([activity['canonical_smiles'] for activity in activities])
