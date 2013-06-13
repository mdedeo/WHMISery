WHMISery
========

Process WHMIS chemical classification data from the [Service du répertoire toxicologique](http://www.reptox.csst.qc.ca/Documents/SIMDUT/FichierTxt/Htm/FichierTxt.htm) de la Commission de la santé et de la sécurité du travail (CSST) du Québec.

Here is a Python script which transforms the data as follows:
* Each different classification for each chemical is listed in a separate row in the main output file, WHMIS\_output.csv.
* Solutions, mixtures, or variants of a pure substance that have the same overall classification as the pure substance are dumped in an 'omit' list, WHMIS_omitted.csv.
* Alphanumeric WHMIS classification codes are replaced with with full English titles.


### Files ###

* DateMaj.txt - Downloaded from above webpage. Contains the date of last update and indicates the number of products listed.
* SIMDUT.txt - Input for the Python script. CSST database export, downloaded from the above webpage. It is a semicolon-separated CSV file (encoding: Windows Latin-1).
* WHMIS_output.csv - Output from the Python script.
* whmisery.py - The Python script.
