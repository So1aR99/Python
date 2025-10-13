#dna = "ctacaatgtcagtatacccattgcattagccgg"
dna = input("염기 서열을 입력해주세요: ")
# window method
codon_list = [] # empty list
codon_dict = {} # empty dictionary
for i in range(0, len(dna), 3): # windowing
    codon_list.append(dna[i:i+3])
print(codon_list)

for (affset, codon_dna) in enumerate(codon_list):
    if len(codon_list[affset]) != 3:
        continue
    else:
        codon_dict[codon_dna] = codon_list.count(codon_list[affset])

print(codon_dict)
