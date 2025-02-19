import gzip
import numpy as np
import csv
import json

data_path = 'cb513_sequence_MASK.npy.gz'

f = gzip.GzipFile(data_path, "r")
CullPDB_sequence = np.load(f)
f.close()

# Define the array of characters
array = [
    '_', 'A', 'C', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'M', 'L', 'N', 'Q', 'P',
    'S', 'R', 'T', 'W', 'V', 'Y', 'X'
]

# Function to convert one-hot encoded sequence to string and clean trailing underscores


def convert_to_string(sequence):
    indices = np.argmax(sequence, axis=-1)
    sequence = ''.join([array[i] for i in indices])
    sequence = sequence.rstrip('_')  # Remove trailing underscores
    return sequence


# Apply the function to each sequence in CullPDB_sequence
cleaned_sequences = [convert_to_string(seq) for seq in CullPDB_sequence]

# Store the cleaned sequences and their lengths in a CSV file
# with open('cleaned_sequences.csv', 'w', newline='') as csvfile:
    # csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(['Index', 'Sequence', 'Length'])
    # for index, seq in enumerate(cleaned_sequences):
    #     # Count the length of the string that is not "_"
    #     length = len(seq.replace('_', ''))
    #     csvwriter.writerow([index, seq, length])

# print("Sequences have been stored in cleaned_sequences.csv")

# Create a job list for Alphafold Server (20 sequences per job)
# n from 59-513: 514 sequences
n_end = 513
n_start = 59

def create_joblist_batches(n_start, n_end, batch_size=20):
    joblist = []
    batch_counter = 4
    for n in range(n_start, n_end+1):
        seq = cleaned_sequences[n]
        job = {
            "name": f"Cb513_{n}",
            "modelSeeds": ["1"],
            "sequences": [
                {
                    "proteinChain": {
                        "sequence": seq,
                        "count": 1
                    }
                }
            ]
        }
        joblist.append(job)
        
        if len(joblist) == batch_size or n == n_end:
            filename = f'joblist_{batch_counter}.json'
            with open(filename, 'w') as f:
                json.dump(joblist, f, indent=4)
            print(f"Joblist batch {batch_counter} created")
            joblist = []
            batch_counter += 1

create_joblist_batches(n_start, n_end)
