def prepare_file(filename):
    file = open(f"./utils/{filename}.fasta", "r")
    file = file.read()              # read the file
    file = file.replace("\n", "")   # remove newline characters
    if '[ARN]' in file:
        file = file.split('[ARN]')[1]
    if '[ADN]' in file:
        file = file.split('[ADN]')[1]

    return file

ADN_sequence_1 = prepare_file("ADN_sequence_1")
ADN_sequence_2 = prepare_file("ADN_sequence_2")
ARN_sequence_1 = prepare_file("ARN_sequence_1")
ARN_sequence_2 = prepare_file("ARN_sequence_2")