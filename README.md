# higher-order-interactions-eeg
Under the supervision of Professor Mohammad Reza Rahimi Tabar, a leading researcher in complex systems and
 time series analysis, I analyzed a large set of EEG signals recorded from 109 subjects during simple cognitive
 tasks(for further references see PhysioNet). The goal was to identify causal and asymmetric connections between
 seven key brain regions. To achieve this, we applied an advanced method that captures higher-order interactions
 between different time series. As a result, we reconstructed not only a first-order graph but also a hypergraph, both
 comprising the seven brain regions.

<img width="1288" height="1008" alt="Nodes picture" src="https://github.com/user-attachments/assets/9d285d72-6640-4774-a7c1-2a23849752d3" />

<img width="952" height="790" alt="image" src="https://github.com/user-attachments/assets/9f7738ce-4df3-411e-9d8b-3719ae5ccfe9" />

 
## ⚠️ Important Note

To run `main_eeg_analysis.ipynb`, a large EEG dataset must be downloaded in advance.

- **Database source:**  
  [https://physionet.org/content/eegmmidb/1.0.0/](https://physionet.org/content/eegmmidb/1.0.0/)

- **Direct download link (ZIP):**  
  [https://physionet.org/content/eegmmidb/get-zip/1.0.0/](https://physionet.org/content/eegmmidb/get-zip/1.0.0/)

Moreover, mne and hints package need to be installed:

## HiNTS Package Installation(Higher-Order Interactions in N-Dimensional Time Series):

For more detailed examples and tutorials, please refer to authors' source [hints package](https://github.com/aminakhshi/hints/tree/main#) and the corresponding papers:  
- **Akhshi et al. (2024):** [GitHub Link](https://github.com/aminakhshi/hints/tree/main#)  
- **Tabar et al. (2024):** [PRX Paper](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.011050)

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

