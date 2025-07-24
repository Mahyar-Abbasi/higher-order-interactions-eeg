# %%
import numpy as np
import mne

edf = mne.io.read_raw_edf(r"eeg-motor-movementimagery-dataset-1.0.0\files\S001\S001R11.edf")
header = ','.join(edf.ch_names)
np.savetxt('S001R11.csv', edf.get_data().T, delimiter=',', header=header)


