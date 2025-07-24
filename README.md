# higher-order-interactions-eeg
Under the supervision of Professor Mohammad Reza Rahimi Tabar, a leading researcher in complex systems and
 time series analysis, I analyzed a large set of EEG signals recorded from 109 subjects during simple cognitive
 tasks(for further references see PhysioNet). The goal was to identify causal and asymmetric connections between
 seven key brain regions. To achieve this, we applied an advanced method that captures higher-order interactions
 between different time series. As a result, we reconstructed not only a first-order graph but also a hypergraph, both
 comprising the seven brain regions.
 
## ⚠️ Important Note

To run `main_eeg_analysis.ipynb`, a large EEG dataset must be downloaded in advance.

- **Database source:**  
  [https://physionet.org/content/eegmmidb/1.0.0/](https://physionet.org/content/eegmmidb/1.0.0/)

- **Direct download link (ZIP):**  
  [https://physionet.org/content/eegmmidb/get-zip/1.0.0/](https://physionet.org/content/eegmmidb/get-zip/1.0.0/)

Moreover, mne and hints package need to be installed:

## HiNTS Package Installation(Higher-Order Interactions in N-Dimensional Time Series):

To install **HiNTS**, you can either use `pip` or install it directly from the source.

Option 1: Install via pip
```bash
pip install hints-kmcs
```

Option 2: Install from source
```bash
git clone https://github.com/aminakhshi/hints.git
cd hints
python setup.py install
```

For more information, please refer to the full documentation by the authors:
https://github.com/aminakhshi/hints.git
