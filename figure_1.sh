#!/bin/sh

# Snippet 1.
# Example of fetching molecule data via REST using curl.

curl -H "X-HTTP-Method-Override: GET" -H "Content-Type: application/json" -d '{"molecule_chembl_id__in":["CHEMBL1200769","CHEMBL1200392"]}' https://www.ebi.ac.uk/chembl/api/data/molecule.json
