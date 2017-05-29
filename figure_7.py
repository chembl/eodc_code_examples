# Snippet 5.
# Example of a simple Luigi Pipeline computing 3D coordinates for compounds from ChEMBL.

import os
import sys

import luigi
from chembl_webresource_client.utils import utils
from chembl_webresource_client.new_client import new_client

class GetCompoundsFromChEMBL(luigi.Task):
    """
    This task will retrieve compounds from ChEMBL and save them
    In the SDF format. Compounds will be prefiltered by:
     - logP (lower limit)
     - number of aromatic rings (upper limit)
     - chirality (exact value)
     - molecular weight (upper limit)
    """
    logP = luigi.FloatParameter(default=1.9)
    rings_number = luigi.IntParameter(default=3)
    chirality = luigi.IntParameter(default=(-1))
    mwt = luigi.FloatParameter(default=100.0)

    def requires(self):
        return []

    def run(self):
        molecule = new_client.molecule
        molecule.set_format('sdf')

        mols = molecule.filter(molecule_properties__acd_logp__gte=self.logP) \
                       .filter(molecule_properties__aromatic_rings__lte=self.rings_number) \
                       .filter(chirality=self.chirality) \
                       .filter(molecule_properties__full_mwt__lte=self.mwt)

        with self.output().open('w') as output:
            for mol in mols:
                output.write(mol)
                output.write('$$$$\n')    

    def output(self):
        return luigi.LocalTarget('mols_2D.sdf')

class Compute3DCoordinates(luigi.Task):
    """
    This task will take SDF file and comoute 3D coordinates
    for each molecule in the file.
    """
    def requires(self):
        return [GetCompoundsFromChEMBL()]

    def run(self):
        with self.output().open('w') as output:
            for input in self.input():
                mols = input.open('r').read().split('$$$$\n')
                for mol in mols:
                    mol_3D = utils.ctab23D(mol)
                    output.write(mol_3D)
                    output.write('$$$$\n')

    def output(self):
        return luigi.LocalTarget('mols_3D.sdf')
