import numpy as np
import os
from alabtools.imaging.ctfile import CtFile
from alabtools.imaging.phasing import WSPhaser

# print working directory and file directory
print('Current working directory:\n{}\n\n'.format(os.getcwd()))
print('File directory:\n{}\n\n'.format(os.path.dirname(os.path.realpath(__file__))))

# change working directory to file directory
print('Changing working directory to file directory...\n\n')
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# print working directory and file directory
print('Current working directory:\n{}\n\n'.format(os.getcwd()))
print('File directory:\n{}\n\n'.format(os.path.dirname(os.path.realpath(__file__))))

# Set the configuration for phasing
ct_name = 'takei_1Mb_comb_no-out.ct'
ct_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), ct_name)
config = {'ct_name': ct_name,
          'parallel': {'controller': 'ipyparallel'},
          'ncluster': {'#': 2, 'chrX': 1},
          'additional_parameters': {'st': 1.2, 'ot': 2.5}}

# Run phasing
phaser = WSPhaser(config)
ct_phased = phaser.run()

# Print the Attributes and Datasets of the CtFile
print('Results:')
print('ncell =', ct_phased.ncell)
print('ndomain =', ct_phased.ndomain)
print('nspot_tot =', ct_phased.nspot_tot)
print('ntrace_tot =', ct_phased.ntrace_tot)
print('nspot_max =', ct_phased.nspot_max)
print('ncopy_max =', ct_phased.ncopy_max)
print('cell_labels.shape =', ct_phased.cell_labels.shape)
print('ncopy.shape =', ct_phased.ncopy.shape)
print('nspot.shape =', ct_phased.nspot.shape)
print('coordinates.shape =', ct_phased.coordinates.shape)
print('coordinates[0, 0, 0, 0, 0] =', ct_phased.coordinates[0, 0, 0, 0, 0])
print('is np.max(ct_phased.nspot) == ct_phased.nspot_max?')
print(np.max(ct_phased.nspot) == ct_phased.nspot_max)
print('is np.max(ct_phased.ncopy) == ct_phased.ncopy_max?')
print(np.max(ct_phased.ncopy) == ct_phased.ncopy_max)

ct_phased.close()
