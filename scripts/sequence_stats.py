import sys
from pathlib import Path
input_file = Path(sys.argv[1])
output_file = Path(sys.argv[2])
sequences = []
with open(input_file) as handle:
	for line in handle:
		line = line.strip()
		if line and not line.startswith(">"):
			sequences.append(line.upper())

sequence = "".join(sequences)
length = len(sequence)

if length == 0:
	raise ValueError(f"No sequence found in {input_file}")

gc = 100 * (sequence.count("G") + sequence.count("C")) / length

with open(output_file, "w") as handle:
	handle.write(f"{input_file.stem}\t{length}\t{gc:.2f}\n")
