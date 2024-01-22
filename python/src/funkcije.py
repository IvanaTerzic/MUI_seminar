import sys
sys.path.append('../src')
from modules import *



def calculate_fingerprint(smiles):
    """
    izračunava otisak (fingerprint) molekule iz SMILES zapisa
    ulaz:
    - `smiles` (str): SMILES zapis molekule koja se pretvara u otisak
    izlaz:    
    - Numpy niz cijelih brojeva (int) koji predstavlja otisak molekule

    Ako SMILES zapis nije valjan ili se ne može pretvoriti u molekulu, funkcija vraća None."""
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
        return np.array(list(fp.ToBitString()), dtype=int)
    return None
