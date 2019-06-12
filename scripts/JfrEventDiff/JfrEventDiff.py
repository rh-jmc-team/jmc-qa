#!/usr/bin/env python3

import os, sys, xmltodict

# Reads the raw XML file into a variable
def downloadMetadata():
  cmd1 = cmd2 = None
  if len(sys.argv) != 2: # Display an example if the number of arguments aren't met
    print('**Displaying Example of jdk11u-defe40e29642 against jdk12u-b58f3dee17d1**')
    cmd1 = 'curl http://hg.openjdk.java.net/jdk-updates/jdk11u/raw-file/defe40e29642/src/hotspot/share/jfr/metadata/metadata.xml'
    cmd2 = 'curl http://hg.openjdk.java.net/jdk-updates/jdk12u/raw-file/b58f3dee17d1/src/hotspot/share/jfr/metadata/metadata.xml'
  else:
    cmd1 = 'curl ' + sys.argv[1]
    cmd2 = 'curl ' + sys.argv[2]
  metadata1 = os.popen(cmd1).read()
  metadata2 = os.popen(cmd2).read()
  return metadata1, metadata2

# Converts the raw XML to a Dictionary
def convertXmlToDict(metadata1, metadata2):
  return xmltodict.parse(metadata1), xmltodict.parse(metadata2)

# Returns a dictionary where the index is the event name and the value is a dictionary of the xml values
def createDiff(xml1, xml2):
  diff_dict = {}
  for event in list_diff(xml1['Metadata']['Event'], xml2['Metadata']['Event']):
    diff_dict[event['@name']] = event
  return diff_dict

# Find the difference between two lists
def list_diff(list1, list2):
  # Source: https://stackoverflow.com/a/6489180
  fn = lambda first, second: [x for x in first if x not in second]
  return fn(list1, list2)

# Find the difference between two dictionaries
def dict_diff(dict1, dict2):
  # Source: https://stackoverflow.com/a/32815681
  fn = lambda first, second: [k for k in set(dict1) - set(dict2)]
  return fn(dict1, dict2)

# Given an Event dictionary, return the number of Fields in the event
def countNumOfFields(event):
  return len(event['Field'])

# Ensure that the fields are in list format for comparison
def convertFieldsToList(fields):
  if (isinstance(fields, list)):
    return fields
  else:
    return [fields]

# Returns the longer of two lists
def findLonger(list1, list2):
  if len(list1) > len(list2):
    return list1
  else:
    return list2

# Returns the short of two lists
def findShorter(list1, list2):
  if len(list1) < len(list2):
    return list1
  else:
    return list2

# Given two XML dictionaries, find where the Event fields differ
def compareEvents(diff1, diff2):
  print('---Metadata Diff Report---\n')
  for event in diff1:
    if event in diff2:
      # locate the differences within the matching event fields
      compareFields(diff1[event], diff2[event])
    else: # if the event is in file 1 but not file 2 -> it was removed
      incrementNumTransplantEvents()
      numFieldChanges = countNumOfFields(diff1[event])
      incrementNumTransplantFields(numFieldChanges)
      print('Event:', event)
      print('File 1: Event -', event)
      print('File 2: DNE')
      print('Removal of', numFieldChanges, 'fields\n')
  # if the event is in file 2 but not file 1 -> it was added
  new_events = dict_diff(diff2, diff1)
  if new_events:
    for event in new_events:
      incrementNumTransplantEvents()
      numFieldChanges = countNumOfFields(diff2[event])
      incrementNumTransplantFields(numFieldChanges)
      print('Event:', event)
      print('File 1: DNE')
      print('File 2: New Event -', event)
      print('Addition of', numFieldChanges, 'fields\n')

# Given two matching events, find the differences between their fields
def compareFields(event1, event2):
  print('Event:', event1['@name'])
  for attr in event1:
    if attr.startswith('@'): # Check Event Attributes - Already covered by compareEvents
      continue
    else: # Check the Fields
      fields1 = convertFieldsToList(event1[attr])
      fields2 = convertFieldsToList(event2[attr])
      diff1 = list_diff(fields1, fields2)
      diff2 = list_diff(fields2, fields1)
      if len(diff1) != len(diff2): # align the two sequences
        longer = findLonger(diff1, diff2)
        shorter = findShorter(diff1, diff2)
        i = 0
        for field1 in longer:
          found = 0
          j = 0
          for field2 in shorter:
            if found == 0 and field2 != [] and field1['@name'] != field2['@name']:
              found = 1
            j = j + 1
          if found == 0: # if the field isn't in the other event, then fill the gap with empty space
            shorter.insert(i, [])
            found = 1
          i = i + 1
      # once the sequencnes are aligned, compare the diffs
      k = 0
      for field in diff1:
        if field == []: # new field in diff2
          incrementNumTransplantFields()
          print('File 1: Field DNE')
          print('File 2: New Field @name =', diff2[k]['@name'], '\n')
        elif diff2[k] == []: # field from diff1 was removed
          incrementNumTransplantFields()
          print('File 1: Removed Field @name =', field['@name'])
          print('File 2: Field DNE\n')
        else:
          for field_attr in field:
            if field[field_attr] != diff2[k][field_attr]:
              incrementNumModifications()
              print('File 1:', attr, field['@name'], field_attr, '=', field[field_attr])
              print('File 2:', attr, field['@name'], field_attr, '=', diff2[k][field_attr], '\n')
          k = k + 1

# Report the tallied totals to the console
def reportResults():
  print('---Results---')
  print('Number of changes:', numModifications)
  print('Number of Event additions/removals:', numTransplantEvents)
  print('Number of Event Field addition/removals:', numTransplantFields)
  print('Total number of changes:', numModifications + numTransplantEvents + numTransplantFields)

# Increment the global counters
def incrementNumModifications():
  global numModifications
  numModifications = numModifications + 1

def incrementNumTransplantEvents():
  global numTransplantEvents
  numTransplantEvents = numTransplantEvents + 1

def incrementNumTransplantFields(num = 1):
  global numTransplantFields
  numTransplantFields = numTransplantFields + num

def main():
  # Retrieve the XML contents from the provided links
  metadata1, metadata2 = downloadMetadata()

  # Convert the XML to python dictionaries
  xml1, xml2 = convertXmlToDict(metadata1, metadata2)

  # Find the differences between the metadata
  diff1 = createDiff(xml1, xml2)
  diff2 = createDiff(xml2, xml1)

  # Find the differences between the events
  compareEvents(diff1, diff2)

  # Print results
  reportResults()

# Define the global counters
numModifications = 0
numTransplantEvents = 0
numTransplantFields = 0

main()