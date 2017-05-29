# Snippet 2.
# Retrieving protein target information via API using Python client.  

from chembl_webresource_client.new_client import new_client
target = new_client.target
hits = target.filter(target_synonym__exact='TSHR', organism='Homo sapiens')
