#!/usr/local/bin/python3

# whmisery.py
# See README.md for explanation.

import csv

def main():
    # We'll supply a descriptive English name for each class.
    classes = {
               'A': 'Class A - Compressed gases',
               'B': 'Class B - Flammable and combustible materials',
               'B1': 'Class B1 - Flammable gases',
               'B2': 'Class B2 - Flammable liquids',
               'B3': 'Class B3 - Combustible liquids',
               'B4': 'Class B4 - Flammable solids',
               'B5': 'Class B5 - Flammable aerosols',
               'B6': 'Class B6 - Reactive flammable materials',
               'C': 'Class C - Oxidizing materials',
               'D1': 'Class D1 - Materials causing immediate and serious toxic effects',
               'D1A': 'Class D1A - Very toxic material causing immediate and serious toxic effects',
               'D1B': 'Class D1B - Toxic material causing immediate and serious toxic effects',
               'D2': 'Class D2 - Materials causing other toxic effects',
               'D2A': 'Class D2A - Very toxic material causing other toxic effects',
               'D2B': 'Class D2B - Toxic material causing other toxic effects',
               'D3': 'Class D3 - Biohazard infectious materials',
               'E': 'Class E - Corrosive materials',
               'F': 'Class F - Dangerously reactive materials',
               'Produit non contrôlé': 'Not controlled product',
               'Classification non disponible': 'Classification not available',
               'Classification': 'Classification'   # For the header row
               }
    infile = open('SIMDUT.txt', newline='', encoding='latin-1')
    csvreader = csv.reader(infile, delimiter=';')
    outfile_yes = open('output/WHMIS_output.csv', 'w', newline='', encoding='utf-8')
    outfile_no = open('output/WHMIS_omitted.csv', 'w', newline='', encoding='utf-8')
    writer_yes = csv.writer(outfile_yes, dialect='excel', delimiter=';')
    writer_no = csv.writer(outfile_no, dialect='excel', delimiter=';')
    print('Processing SIMDUT.txt and writing output files.')
    # Fields in the CSV file:
    # 0: NomFrançais
    # 1: NomAnglais
    # 2: CAS
    # 3: NoUN
    # 4: Classification
    # 5: PourcentageDeDivulgation [Minimum percentage for ingredient disclosure]
    # 6: Commentaire [Comments]
    lastcasname = '@'
    lastcasclass = '@'
    for row in csvreader:
        # Filter out solutions/mixtures/variants... 
        # NOTE: This only works because the source list is sorted by name (fr),
        # and variants are given no CASRN, and they are called '<name>, x%'.
        if row[2] == '' and lastcasname in row[0] and row[4] == lastcasclass:
            writer_no.writerow(row)
        else:
            # Separate the lists of classifications:
            for c in row[4].split(','):
                writer_yes.writerow(row[:4] + [classes[c.strip()]] + row[5:])
        # Remember...
        if row[2] != '':
            lastcasname = row[0]
            lastcasclass = row[4]
    infile.close()
    outfile_yes.close()
    outfile_no.close()

if __name__ == '__main__':
    main()
