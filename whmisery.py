#!/usr/local/bin/python3

# whmisery.py
# See README.md for explanation.

# the classes have changed see http://www.csst.qc.ca/en/prevention/reptox/whmis-2015/Documents/Classification-Key-2015.txt

import csv

def main():
    # We'll supply a descriptive English name for each class.
    classes = {
'PH.2.1' : 'Flammable gases / Category 1',
'PH.2.2' : 'Flammable gases / Category 2',
'PH.3.1' : 'Flammable aerosols / Category 1',
'PH.3.2' : 'Flammable aerosols / Category 2',
'PH.4.1' : 'Oxidizing gases / Category 1',
'PH.5.1' : 'Gases under pressure / Compressed gas',
'PH.5.2' : 'Gases under pressure / Liquefied gas',
'PH.5.3' : 'Gases under pressure / Refrigirated liquefied gas',
'PH.5.4' : 'Gases under pressure / Dissolved gas',
'PH.6.1' : 'Flammable liquids / Category 1',
'PH.6.2' : 'Flammable liquids / Category 2',
'PH.6.3' : 'Flammable liquids / Category 3',
'PH.6.4' : 'Flammable liquids / Category 4',
'PH.7.1' : 'Flammable solids / Category 1',
'PH.7.2' : 'Flammable solids / Category 2',
'PH.8.A' : 'Self-reactive substances / Type A',
'PH.8.B' : 'Self-reactive substances / Type B',
'PH.8.C' : 'Self-reactive substances / Type C',
'PH.8.D' : 'Self-reactive substances / Type D',
'PH.8.E' : 'Self-reactive substances / Type E',
'PH.8.F' : 'Self-reactive substances / Type F',
'PH.8.G' : 'Self-reactive substances / Type G',
'PH.8.99' : 'Self-reactive substances / Undefined category',
'PH.9.1' : 'Pyrophoric liquids / Category 1',
'PH.10.1' : 'Pyrophoric solids / Category 1',
'PH.11.1' : 'Self-heating substances and mixtures / Category 1',
'PH.11.2' : 'Self-heating substances and mixtures / Category 2',
'PH.12.1' : 'Substances which, in contact with water, emit flammable gases / Category 1',
'PH.12.2' : 'Substances which, in contact with water, emit flammable gases / Category 2',
'PH.12.3' : 'Substances which, in contact with water, emit flammable gases / Category 3',
'PH.13.1' : 'Oxidizing liquids / Category 1',
'PH.13.2' : 'Oxidizing liquids / Category 2',
'PH.13.3' : 'Oxidizing liquids / Category 3',
'PH.14.1' : 'Oxidizing solids / Category 1',
'PH.14.2' : 'Oxidizing solids / Category 2',
'PH.14.3' : 'Oxidizing solids / Category 3',
'PH.15.A' : 'Organic peroxides / Type A',
'PH.15.B' : 'Organic peroxides / Type B',
'PH.15.C' : 'Organic peroxides / Type C',
'PH.15.D' : 'Organic peroxides / Type D',
'PH.15.E' : 'Organic peroxides / Type E',
'PH.15.F' : 'Organic peroxides / Type F',
'PH.15.G' : 'Organic peroxides / Type G',
'PH.15.99' : 'Organic peroxides / Undefined category',
'PH.16.1' : 'Corrosive to metals / Category 1',
'PH.17.1' : 'Combustible dusts / Category 1',
'PH.18.1' : 'Simple asphyxiants / Category 1',
'PH.19.1' : 'Pyrophoric gases / Category 1',
'PH.20exp.1' : 'Physical hazards not otherwise classified (exploding bomb) / Category 1',
'PH.20fl.1' : 'Physical hazards not otherwise classified (flame) / Category 1',
'PH.20ox.1' : 'Physical hazards not otherwise classified (flame over circle) / Category 1',
'PH.20ga.1' : 'Physical hazards not otherwise classified (gas cylinder) / Category 1',
'PH.20co.1' : 'Physical hazards not otherwise classified (corrosion) / Category 1',
'PH.20sk.1' : 'Physical hazards not otherwise classified (skull and crossbones) / Category 1',
'PH.20exc.1' : 'Physical hazards not otherwise classified (exclamation mark) / Category 1',
'HH.1d.1' : 'Acute toxicity - dermal / Category 1',
'HH.1d.2' : 'Acute toxicity - dermal / Category 2',
'HH.1d.3' : 'Acute toxicity - dermal / Category 3',
'HH.1d.4' : 'Acute toxicity - dermal / Category 4',
'HH.1d.99' : 'Acute toxicity - dermal / Not reviewed',
'HH.1i.1' : 'Acute toxicity - inhalation / Category 1',
'HH.1i.2' : 'Acute toxicity - inhalation / Category 2',
'HH.1i.3' : 'Acute toxicity - inhalation / Category 3',
'HH.1i.4' : 'Acute toxicity - inhalation / Category 4',
'HH.1i.99' : 'Acute toxicity - inhalation / Not reviewed',
'HH.1o.1' : 'Acute toxicity - oral / Category 1',
'HH.1o.2' : 'Acute toxicity - oral / Category 2',
'HH.1o.3' : 'Acute toxicity - oral / Category 3',
'HH.1o.4' : 'Acute toxicity - oral / Category 4',
'HH.1o.99' : 'Acute toxicity - oral / Not reviewed',
'HH.2.1' : 'Skin corrosion/irritation / Category 1',
'HH.2.1A' : 'Skin corrosion/irritation / Category 1A',
'HH.2.1B' : 'Skin corrosion/irritation / Category 1B',
'HH.2.1C' : 'Skin corrosion/irritation / Category 1C',
'HH.2.2' : 'Skin corrosion/irritation / Category 2',
'HH.2.99' : 'Skin corrosion/irritation / Not reviewed',
'HH.3.1' : 'Serious eye damage/eye irritation / Category 1',
'HH.3.2' : 'Serious eye damage/eye irritation / Category 2',
'HH.3.2A' : 'Serious eye damage/eye irritation / Category 2A',
'HH.3.2B' : 'Serious eye damage/eye irritation / Category 2B',
'HH.3.99' : 'Serious eye damage/eye irritation / Not reviewed',
'HH.4s.1' : 'Skin sensitization / Category 1',
'HH.4s.1A' : 'Skin sensitization / Category 1A',
'HH.4s.1B' : 'Skin sensitization / Category 1B',
'HH.4s.99' : 'Skin sensitization / Not reviewed',
'HH.4r.1' : 'Respiratory sensitization / Category 1',
'HH.4r.1A' : 'Respiratory sensitization / Category 1A',
'HH.4r.1B' : 'Respiratory sensitization / Category 1B',
'HH.4r.99' : 'Respiratory sensitization / Not reviewed',
'HH.5.1' : 'Germ cell mutagenicity / Category 1',
'HH.5.1A' : 'Germ cell mutagenicity / Category 1A',
'HH.5.1B' : 'Germ cell mutagenicity / Category 1B',
'HH.5.2' : 'Germ cell mutagenicity / Category 2',
'HH.5.99' : 'Germ cell mutagenicity / Not reviewed',
'HH.6.1' : 'Carcinogenicity / Category 1',
'HH.6.1A' : 'Carcinogenicity / Category 1A',
'HH.6.1B' : 'Carcinogenicity / Category 1B',
'HH.6.2' : 'Carcinogenicity / Category 2',
'HH.6.99' : 'Carcinogenicity / Not reviewed',
'HH.7.1' : 'Reproductive toxicity / Category 1',
'HH.7.1A' : 'Reproductive toxicity / Category 1',
'HH.7.1B' : 'Reproductive toxicity / Category 1',
'HH.7.2' : 'Reproductive toxicity / Category 2',
'HH.7.99' : 'Reproductive toxicity / Not reviewed',
'HH.7l.1' : 'Reproductive toxicity (lactation) / Effects on or via lactation',
'HH.7l.99' : 'Reproductive toxicity (lactation) / Effects on or via lactation : Not reviewed',
'HH.8.1' : 'Specific target organ toxicity - single exposure / Category 1',
'HH.8.2' : 'Specific target organ toxicity - single exposure / Category 2',
'HH.8.99' : 'Specific target organ toxicity - single exposure / Not reviewed',
'HH.8n.3' : 'Specific target organ toxicity - single exposure (narcotic effects) / Category 3 - Narcotic effect',
'HH.8i.3' : 'Specific target organ toxicity - single exposure (respiratory tract irritation) / Category 3 - Respiratory tract irritation',
'HH.9.1' : 'Specific target organ toxicity - repeated exposure / Category 1',
'HH.9.3' : 'Specific target organ toxicity - repeated exposure / Category 2',
'HH.9.99' : 'Specific target organ toxicity - repeated exposure / Not reviewed',
'HH.10.1' : 'Aspiration hazard / Category 1',
'HH.10.99' : 'Aspiration hazard / Not reviewed',
'HH.11.1' : 'Biohazardous infectious material / Category 1',
'HH.11.99' : 'Biohazardous infectious material / Not reviewed',
'HH.12co.1' : 'Health hazards not otherwise classified (corrosion) / Category 1',
'HH.12sk.1' : 'Health hazards not otherwise classified (skull and crossbones) / Category 1',
'HH.12exc.1' : 'Health hazards not otherwise classified (exclamation mark) / Category 1',
'HH.12hh.1' : 'Health hazards not otherwise classified (health hazard) / Category 1',
'HH.12bi.1' : 'Health hazards not otherwise classified (biohazardous infectious materials) / Category 1',
'Uncontrolled product' : 'Uncontrolled product',
'' : '',
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
    # 0: EnglishName
    # 1: FrenchName
    # 2: CAS
    # 3: NoUN
    # 4: Classification
    # 5: Remarks
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
                writer_yes.writerow(row[:4] + [classes[c.strip()]])
        # Remember...
        if row[2] != '':
            lastcasname = row[0]
            lastcasclass = row[4]
    infile.close()
    outfile_yes.close()
    outfile_no.close()

if __name__ == '__main__':
    main()
