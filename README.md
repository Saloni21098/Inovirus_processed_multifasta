# Subsequence Processing with Python
This repository contains a Python script that performs subsequence extraction, removal, reverse complementation, and introduces random single nucleotide changes. The script works with the primary multi-FASTA file (InovirusM13.fasta) and a BED file (IVM13_roi.bed) to identify regions of interest.

## Requirements
- Python 3.10
  
## Usage
1. Download or clone this repository to your local machine.
2. Place the primary multi-FASTA file (InovirusM13.fasta) and the BED file (IVM13_roi.bed) in the repository's root directory.
3. Run the `New_code.py` script using Python:
   ```
   python New_code.py
   ```
4. The script will generate the following file:
   - `new_file.fasta`: New multi-FASTA file with extracted subsequences removed, reverse complemented, and with random mutations.

## File Descriptions
- `New_code.py`: Python script that processes the subsequences and creates the output files.
- `InovirusM13.fasta`: Primary multi-FASTA file containing nucleotide sequences of various organisms.
- `IVM13_roi.bed`: BED file containing coordinates for at least 3 scaffolds (regions of interest).
- `new_file.fasta`: Output multi-FASTA file containing processed subsequences.
