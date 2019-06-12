# JfrEventDiff

## Description

`JfrEventDiff.py` takes two URL paths (to raw-file xml data of JFR metadata files) and displays the differences & changes between the files in human readable format.

An example output has been supplied at `diff-example.txt`

## Dependencies

xmltodict is used to convert xml to python dictionaries.

Installation: `pip3 install xmltodict --user`

## Usage:

Example usage:

`python3 JfrEventDiff.py`

will display the difference between jdk11u-defe40e29642 against jdk12u-b58f3dee17d1 as an example. The URL paths could also be modified in the code to compare whatever files you want, but the intended behaviour is to supply two URLs to the raw-file xml data:

`python3 JfrEventDiff.py <URL-to-metadata1-raw-xml> <URL-to-metadata2-raw-xml>`

where an example URL could be: http://hg.openjdk.java.net/jdk-updates/jdk11u/raw-file/defe40e29642/src/hotspot/share/jfr/metadata/metadata.xml