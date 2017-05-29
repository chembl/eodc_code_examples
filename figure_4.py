# Snippet 4.
# Using Python API client to filter molecules.

from chembl_webresource_client.new_client import new_client
molecule = new_client.molecule
mols=molecule.filter(molecule_properties__acd_logp__lte=5.0).filter(molecule_properties__aromatic_rings__lte=3).order_by('-max_phase')
