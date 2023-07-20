import random
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

#Define the file names
fasta_file = "InovirusM13.fasta"  # Primary multi-fasta file
bed_file = "IVM13_roi.bed"  # BED file with at lest 3 coordinates
output_file = "new_file.fasta"  # Output fasta file


# Function to reverse complement a DNA sequence
def reverse_complement(sequence):
    return str(Seq(sequence).reverse_complement())

# Function to introduce a random single nucleotide change in the sequence
def introduce_random_mutation(sequence):
    random_index = random.randint(0, len(sequence)-1)
    random_base = random.choice('ATCG')
    mutated_sequence = sequence[:random_index] + random_base + sequence[random_index+1:]
    return mutated_sequence

# Function to process and insert the modified subsequence back into the primary sequence
def process_and_insert_subsequences(fasta_file, bed_file, output_file):
    sequences = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))
    processed_sequences = []

    with open(bed_file) as file:
        for line in file:
            chromosome, start, end = line.strip().split('\t')
            start,end=int(start),int(end)
            for ids in sequences:
                if chromosome in ids:
                    sequence = str(sequences[ids].seq)
                    subsequence = sequence[start-1:end]  # Extract the subsequence

                    revcomp_subsequence = reverse_complement(subsequence)  # Reverse complement the subsequence
                    processed_subsequence = introduce_random_mutation(revcomp_subsequence)  # Introduce a random mutation

                    processed_sequence = sequence[:start-1] + processed_subsequence + sequence[end:]  # Insert the processed subsequence back

                    processed_record = SeqRecord(Seq(processed_sequence), id=chromosome + "_processed", description="")
                    processed_sequences.append(processed_record)

    SeqIO.write(processed_sequences, output_file, "fasta")

# Call the function to process and insert the modified subsequences
process_and_insert_subsequences(fasta_file, bed_file, output_file)

