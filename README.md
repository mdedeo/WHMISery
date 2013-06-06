WHMIS
=====

Process WHMIS chemical classification data from the [Service du répertoire toxicologique](http://www.reptox.csst.qc.ca/Documents/SIMDUT/FichierTxt/Htm/FichierTxt.htm) de la Commission de la santé et de la sécurité du travail (CSST) du Québec.

Here is a Python script which transforms the data so that each different classification for each chemical is listed in a separate row, and it also replaces the alphanumeric WHMIS classification codes with full English titles.

Files:
------
* DateMaj.txt - Downloaded from above webpage. Contains the date of last update and indicates the number of products listed.
* SIMDUT.txt - Input for the Python script. CSST database export, downloaded from the above webpage. It is a semicolon-separated CSV file (encoding: Windows Latin-1).
* WHMIS_output.csv - Output from the Python script.
* whmiscrunch.py - The Python script.
