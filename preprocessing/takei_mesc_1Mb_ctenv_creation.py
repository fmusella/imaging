import os
from alabtools.imaging import CtEnvelope

# print working directory and file directory
print('Current working directory:\n{}\n\n'.format(os.getcwd()))
print('File directory:\n{}\n\n'.format(os.path.dirname(os.path.realpath(__file__))))

# change working directory to file directory
print('Changing working directory to file directory...\n\n')
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# print working directory and file directory
print('Current working directory:\n{}\n\n'.format(os.getcwd()))
print('File directory:\n{}\n\n'.format(os.path.dirname(os.path.realpath(__file__))))

# Initialize the CtEnvelope object
ctenv_name = 'takei_1Mb_comb.ctenv'
ctenv_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), ctenv_name)
ctenv = CtEnvelope(ctenv_name, 'w')

# Create configuration dictionary for the fitting
ct_name = 'takei_1Mb_comb.ct'
ct_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), ct_name)
cfg = {'ct_name': ct_name,  
       'parallel': {'controller': 'ipyparallel'},
       'fit parameters': {'alpha': 0.0005,
                          'force': False,
                          'delta_alpha': 0.0001,
                          'thresh': 1100,
                          'min_neigh': 20}}

# Fit the CtEnvelope
ctenv.run(cfg)

# Print attributes of the CtEnvelope
print('Attributes and Datasets:')
print('ncell =', ctenv.ncell)
print('fitted =', ctenv.fitted)
print('ct_fit =', ctenv.ct_fit)
print('cell_labels.shape =', ctenv.cell_labels.shape)
print('alpha.shape =', ctenv.alpha.shape)
print('len(mesh) =', len(ctenv.mesh))
print('volume.shape =', ctenv.volume.shape)
print('alpha:')
print(ctenv.alpha)
print('volume:')
print(ctenv.volume)

# save the ctenv file
ctenv.save()
