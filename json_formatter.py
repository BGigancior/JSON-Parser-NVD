import json
from collections import defaultdict

# available categories:
#   attackVector
#   attackComplexity
#   privilegesRequired
#   userInteraction
#   confidentialityImpact
#   integrityImpact
#   availabilityImpact
#   scope

# available vectors(impact): PHYSICAL, LOCAL, ADJACENT, NETWORK

def filter_json(inputFileName, outputFileName, category, impact):
    outputFile = []
    with open(inputFileName) as inputFile:
        oldData = json.load(inputFile)
        for item in range(len(oldData["CVE_Items"])):
            try:
                if isBaseMetricV3(oldData, item):
                    if oldData["CVE_Items"][item]["impact"]["baseMetricV3"]["cvssV3"][category] == impact:
                        outputFile.append(oldData["CVE_Items"][item])
            except IndexError:
                pass

        with open(outputFileName, "w") as output_file:
            json.dump(outputFile, output_file, indent=4)


def isBaseMetricV3(oldData, item):
    return list(oldData["CVE_Items"][item]["impact"].keys())[0] == "baseMetricV3"