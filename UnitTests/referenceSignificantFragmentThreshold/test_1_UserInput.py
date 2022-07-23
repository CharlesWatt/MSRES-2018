referencePatternsFileNamesList = ['reference_measured_EthyleneExtracted.csv']
referencePatternsFormsList = 'xyyy'
dataToAnalyzeFileName = 'Ethylene.csv'
referencePatternTimeRanges = []
ionizationDataFileName = '181017ProvidedIonizationData.csv'
iterativeAnalysis = False
iterationNumber = None
iterationSuffix = ''
unusedMolecules = ''
oldReferenceFileName = []
oldDataToAnalyzeFileName = ''
nextRefFileName = []
nextExpFileName = ''
preProcessing = 'yes'
dataAnalysis = 'yes'
dataSimulation = 'no'
grapher = 'no'
stopAtGraphs = False
timeRangeLimit = 'yes'
timeRangeStart = 6000.0
timeRangeFinish = 6200.0
specificMolecules = 'yes'
chosenMoleculesNames = ['Acetylene', 'Ethane', 'Ethylene']
specificMassFragments = 'yes'
chosenMassFragments = [2.0, 4.0, 14.0, 15.0, 16.0, 18.0, 25.0, 26.0, 27.0, 28.0, 30.0, 32.0, 40.0, 44.0]
moleculeLikelihoods = []
sensitivityValues = []
linearBaselineCorrectionSemiAutomatic = 'no'
baselineType = ['linear']
massesToBackgroundCorrect = [2.0, 4.0, 14.0, 15.0, 16.0, 18.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 32.0, 40.0, 44.0]
earlyBaselineTimes = [[6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0], [6133.0, 6160.0]]
lateBaselineTimes = [[0, 0]]
backgroundMassFragment = []
backgroundSlopes = [2, 5]
backgroundIntercepts = []
interpolateYorN = 'no'
marginalChangeRestriction = 2.0
ignorableDeltaYThreshold = 0.01
dataLowerBound = []
dataUpperBound = []
dataRangeSpecifierYorN = 'no'
signalOrConcentrationRange = 'signal'
csvFile = 'yes'
moleculesToRestrict = []
csvFileName = 'rangestemplate.csv'
bruteIncrements = []
permutationNum = 1000
maxPermutations = 100001
scaleRawDataOption = 'manual'
scaleRawDataFactor = 1
tuningCorrection = 'no'
referenceFileStandardTuningAndForm =[]
referenceFileExistingTuningAndForm = 'AcetaldehydeMeasuredRef.csv'
referenceFileDesiredTuningAndForm = 'AcetaldehydeOnlyNISTRef.csv'
referenceCorrectionCoefficients = {'A': 0.0, 'B': 0.0, 'C': 1.0}
extractReferencePatternFromDataOption = 'no'
rpcMoleculesToChange = ['Ethylene']
rpcMoleculesToChangeMF = [[2, 4, 14, 15, 16, 18, 25, 26, 27, 28, 29, 30, 32, 44]]
rpcTimeRanges = [[6745.0, 8000]]
minimalReferenceValue = 'yes'
referenceValueThreshold = [1.0]
referenceSignificantFragmentThresholds = [3.0]
lowerBoundThresholdChooser = 'no'
massesToLowerBoundThresholdFilter = []
lowerBoundThresholdPercentage = [0.25]
lowerBoundThresholdAbsolute = []
dataSmootherYorN = 'no'
dataSmootherChoice = 'pointrange'
dataSmootherTimeRadius = 7.0
dataSmootherPointRadius = 7.0
dataSmootherHeadersToConfineTo = []
polynomialOrder = 1
rawSignalThresholdMethod = 'no'
rawSignalThresholdValue = [1e-07]
sensitivityThresholdValue = [0.05]
rawSignalThresholdDivider = []
rawSignalThresholdLimit = 'no'
rawSignalThresholdLimitPercent = []
negativeAnalyzerYorN = 'no'
NegativeAnalyzerTopNContributors = 5
NegativeAnalyzerBaseNumberOfGridIntervals = 5
answer = 'sls'
uniqueOrCommon = 'unique'
slsWeighting = [0,0,1,0]
slsFinish = 'inverse'
objectiveFunctionType = 'ssr'
distinguished = 'yes'
fullBrute = 'no'
SLSUniqueExport = 'yes'
implicitSLScorrection = False
slsUniquePositiveConcentrationsOnly = False
collectedFileUncertainties = None
finalOptimization = 'None'
concentrationFinder = 'yes'
moleculesTSC_List = ['Acetylene', 'Ethane', 'Ethylene']
TSC_List_Type = 'SeparateMolecularFactors'
moleculeSignalTSC_List = [1e-08, 3e-09, 3e-09]
massNumberTSC_List = [18, 25, 25]
moleculeConcentrationTSC_List = [1, 1, 1]
unitsTSC = 'bar'
preProcessedDataOutputName = 'PreProcessedData.csv'
resolvedScaledConcentrationsOutputName = 'ScaledConcentrations.csv'
scaledConcentrationsPercentages = 'ScaledConcentrationPercentages.csv'
concentrationsOutputName = 'ResolvedConcentrations.csv'
simulatedSignalsOutputName = 'SimulatedRawSignals.csv'
TotalConcentrationsOutputName = 'TotalConcentrations.csv'
ExportAtEachStep = 'yes'
generatePercentages = 'no'
checkpoint = ''
start = ''
timeSinceLastCheckpoint = ''
iterationNumber = None

# __var_list__ = ['referencePatternsFileNamesList','referencePatternsFormsList','dataToAnalyzeFileName','referencePatternTimeRanges','ionizationDataFileName','iterativeAnalysis','iterationNumber','iterationSuffix','unusedMolecules','oldReferenceFileName','oldDataToAnalyzeFileName','nextRefFileName','nextExpFileName','preProcessing','dataAnalysis','dataSimulation','grapher','timeRangeLimit','timeRangeStart','timeRangeFinish','specificMolecules','chosenMoleculesNames','specificMassFragments','chosenMassFragments','moleculeLikelihoods','sensitivityValues','linearBaselineCorrectionSemiAutomatic','baselineType','massesToBackgroundCorrect','earlyBaselineTimes','lateBaselineTimes','backgroundMassFragment','backgroundSlopes','backgroundIntercepts','interpolateYorN','marginalChangeRestriction','ignorableDeltaYThreshold','dataLowerBound','dataUpperBound','dataRangeSpecifierYorN','signalOrConcentrationRange','csvFile','moleculesToRestrict','csvFileName','bruteIncrements','permutationNum','maxPermutations','scaleRawDataOption','scaleRawDataFactor','tuningCorrection','referenceFileExistingTuningAndForm','referenceFileDesiredTuningAndForm','referenceCorrectionCoefficients','extractReferencePatternFromDataOption','rpcMoleculesToChange','rpcMoleculesToChangeMF','rpcTimeRanges','minimalReferenceValue','referenceValueThreshold','referenceSignificantFragmentThresholds','lowerBoundThresholdChooser','massesToLowerBoundThresholdFilter','lowerBoundThresholdPercentage','lowerBoundThresholdAbsolute','dataSmootherYorN','dataSmootherChoice','dataSmootherTimeRadius','dataSmootherPointRadius','dataSmootherHeadersToConfineTo','polynomialOrder','rawSignalThresholdMethod','rawSignalThresholdValue','sensitivityThresholdValue','rawSignalThresholdDivider','rawSignalThresholdLimit','rawSignalThresholdLimitPercent','negativeAnalyzerYorN','answer','uniqueOrCommon','slsFinish','objectiveFunctionType','distinguished','fullBrute','SLSUniqueExport','concentrationFinder','moleculesTSC_List','TSC_List_Type','moleculeSignalTSC_List','massNumberTSC_List','moleculeConcentrationTSC_List','unitsTSC','preProcessedDataOutputName','resolvedScaledConcentrationsOutputName','scaledConcentrationsPercentages','concentrationsOutputName','simulatedSignalsOutputName','TotalConcentrationsOutputName','ExportAtEachStep','generatePercentages','checkpoint','start','timeSinceLastCheckpoint','iterationNumber']