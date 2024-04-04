RNA_sequence_1 = open("C:/Users/Lorenz/Machine Learning/Interactive-learning/RNA_sequence_1.fasta", "r")
RNA_sequence_2 = open("C:/Users/Lorenz/Machine Learning/Interactive-learning/RNA_sequence_2.fasta", "r")
RNA_sequence_1 = RNA_sequence_1.read()              # read the file
RNA_sequence_2 = RNA_sequence_2.read()              # read the file
RNA_sequence_1 = RNA_sequence_1.replace("\n", "")   # remove newline characters
RNA_sequence_2 = RNA_sequence_2.replace("\n", "")   # remove newline characters 
RNA_sequence_1 = RNA_sequence_1.split('[ARN]')[1]   # remove the first part of the sequence
RNA_sequence_2 = RNA_sequence_2.split('[ARN]')[1]   # remove the first part of the sequence