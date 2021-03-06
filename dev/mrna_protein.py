rna_codons = {'F' : 2, 'L': 6, 'S': 6, 'Y': 2, 'Stop': 3, 'C': 2, 'W': 1,
                'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2,
                'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4}

data = """MFPQEWIATKTNCHFRTALDSRRPDWVPVIRHWLIDRGPHECWQDYHIGSHWPECQIAWVVQAVMAHKSYTSMHTYQPSYHGPMLWYTYNELDHMVMWFYRPMVGRSELKLIWCNMQNQMSKHFYFEEYAYITWYYTSPRRRHKVPDVEVIDPRMFCHMHYFRKEWCMHYHSIDTSPEKEAMTISLWVYTVMMQSYQYALMPPLTHYKWTKEEMIIEFIQCFFQDWSLYVALVLRPREIKYGMWADNMRISGQCVNITMCAGSTGVQLQCDYPNRHSQYEPMYFATLKHEQAPSCKIWWCPMGNHAWMDLNPSASVANYGMINAEHKSYNEVPVAAVEVFNPLVYTTGLNCMDFTLKSSAQHHEKMHKDNWPGDQDCNAIFYCHGSCSQDFEWLGDIENHCDHPKSKHHHTRALPMFIERAKCKCVHGCRFVILGYEVSQKMNFHNQHKCRTATDGRNRIYCGRKISDLSYCDMWFQCFKHGCGEYSRINVYHAPTRFCDQCTLCAKNWHAHASQINGNSMGVAYEQPLIFHCACMQCWTRRCMKLHQMHWNHFFFVHMAAPSFESLKDKWPLVSALHAQNFIHWHNQWEQYHMNQRVVTKDMQLGRSRWLWDSINEGYEMNAQPFPENSCFERIMERNAAICVKRVMEMKLFFEWETLVSDHRPEWSWHKNYMGPQHLIHDCSQMPLVSVNLFALWIGNAHFWSVHECPYLMCTDGPFIFSLIDPGIESHWEYSETHYKMCSVYNFIVPLSGPPEKTPYCMNRDARSPACYTNYNPGTWPDWHTIDKLPKVSDMEKQNHTDQNQRLFGSFNKWADNVASFCPTDCAEQTFIPYYDMRKHRCSNAYGWRVEKCQAIKKPHWVRISLYIINQLSTHHQQIWLLVCIWEILYHNLHAAMDFRNGHLPAELSDWKADEINTRIHQYFGMKCKYLEGECAWYVDVPGEFFQTRNETCMECFPVIHHESDMYTYWNHSDEQICNPFLIFCNCINPMEQTAQDFLN"""

total = 1
for aa in data:
    total *= rna_codons[aa]
    total %= 1000000
total *= rna_codons['Stop']
total %= 1000000
print(total)