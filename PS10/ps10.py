# Problem Set 10
# Name:
# Collaborators:
# Time:

#Code shared across examples
import pylab, random, string, copy, math
import numpy as np
class Root(object):
    def __init__(self, name, originalAttrs, normalizedAttrs = None, itemWO=2, test=2):
        pass

class Point(Root):
    def __init__(self, name, originalAttrs, normalizedAttrs = None, itemWO=2, holder=None, **kwargs):
        """normalizedAttrs and originalAttrs are both arrays"""
        self.name = name
        self.unNormalized = originalAttrs
        self.attrs = normalizedAttrs
    def dimensionality(self):
        return len(self.attrs)
    def getAttrs(self):
        return self.attrs
    def getOriginalAttrs(self):
        return self.unNormalized
    def distance(self, other):
        #Euclidean distance metric
        difference = self.attrs - other.attrs
        return sum(difference * difference) ** 0.5
    def getName(self):
        return self.name
    def toStr(self):
        return self.name + str(self.attrs)
    def __str__(self):
        return self.name

# def call_log(function):
#     print(function.__name__ + " called")
#     fValue = function()
#     print(function.__name__ + " ended and returns " + str(fValue))
#
# def multTwo(num = 2):
#     return num * 2

# call_log(multTwo)
# exit()

class County(Point):
    weights = pylab.array([1.0] * 14)

    # Override Point.distance to use County.weights to decide the
    # significance of each dimension
    def distance(self, other):
        self.weights = pylab.array([1.0] * 14)
        difference = self.getAttrs() - other.getAttrs()
        # print("County.weights * difference * difference:", County.weights * difference * difference)
        # print("County.weights:", County.weights)
        # print("difference:", difference)
        return sum(County.weights * difference * difference) ** 0.5

def adjustWeights(weightAt=40):
    "docstring for adjustWeightsBeforeRun"
    # weights = [[0.0]*13]
    weights = pylab.array([0.0]*(weightAt-1) + [1.0] + [0.0]*(13-weightAt-1))
    return weights

class CountyWO(County):
    """docstring for CountyWO"""
    # weights = pylab.array([0.0]*8 + [1.0] + [0.0]*5)
    weights = adjustWeights(weightAt=6)

    def __init__(self, name, originalAttrs, normalizedAttrs = None, itemWO=3, test=2):
        super(County, self).__init__(name, originalAttrs, normalizedAttrs, itemWO, test)
        # weights = pylab.array([1.0] * itemWO + [0.0] + [1.0] * (13-itemWO))

    def distance(self, other):
        difference = self.getAttrs() - other.getAttrs()
        # print("County.weights * difference * difference:", County.weights * difference * difference)
        # print("County.weights:", CountyWO.weights)
        # print("difference:", difference)
        return sum(CountyWO.weights * difference * difference) ** 0.5




class Cluster(object):
    def __init__(self, points, pointType):
        self.points = points
        self.pointType = pointType
        self.centroid = self.computeCentroid()
    def getCentroid(self):
        return self.centroid
    def computeCentroid(self):
        dim = self.points[0].dimensionality()
        totVals = pylab.array([0.0]*dim)
        for p in self.points:
            totVals += p.getAttrs()
        meanPoint = self.pointType('mean',
                                   totVals/float(len(self.points)),
                                   totVals/float(len(self.points)))
        return meanPoint
    def update(self, points):
        oldCentroid = self.centroid
        self.points = points
        if len(points) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0
    def setPoints(self, points):
        self.points = points
    def getPoints(self):
        return self.points
    def contains(self, name):
        for p in self.points:
            if p.getName() == name:
                return True
        return False
    def toStr(self):
        result = ''
        for p in self.points:
            result = result + p.toStr() + ', '
        return result[:-2]
    def __str__(self):
        result = ''
        for p in self.points:
            result = result + str(p) + ', '
        return result[:-2]

# #
# def cluster_points(X, mu):
#     clusters = {}
#     for x in X:
#         bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
#                     for i in enumerate(mu)], key=lambda t:t[1])[0]
#         try:
#             clusters[bestmukey].append(x)
#         except KeyError:
#             clusters[bestmukey] = [x]
#     return clusters


def kmeans(points, k, cutoff, pointType, minIters = 3, maxIters = 100, toPrint = False):
    """ Returns (Cluster list, max dist of any point to its cluster) """
    #Uses random initial centroids
    initialCentroids = random.sample(points,k)
    clusters = []
    for p in initialCentroids:
        clusters.append(Cluster([p], pointType))
    numIters = 0
    biggestChange = cutoff
    while (biggestChange >= cutoff and numIters < maxIters) or numIters < minIters:
        print "Starting iteration " + str(numIters)
        newClusters = []

        for c in clusters:
            newClusters.append([])
        for p in points:
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0
            for i in range(len(clusters)):
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            newClusters[index].append(p)
        biggestChange = 0.0
        for i in range(len(clusters)):
            change = clusters[i].update(newClusters[i])
            #print "Cluster " + str(i) + ": " + str(len(clusters[i].points))
            biggestChange = max(biggestChange, change)
        numIters += 1
        if toPrint:
            print 'Iteration count =', numIters
    maxDist = 0.0
    for c in clusters:
        for p in c.getPoints():
            if p.distance(c.getCentroid()) > maxDist:
                maxDist = p.distance(c.getCentroid())
    print 'Total Number of iterations =', numIters, 'Max Diameter =', maxDist
    print biggestChange
    return clusters, maxDist

#US Counties example
def readCountyData(fName, numEntries = 14):
    dataFile = open(fName, 'r')
    dataList = []
    nameList = []
    maxVals = pylab.array([0.0]*numEntries)
    #Build unnormalized feature vector
    for line in dataFile:
        if len(line) == 0 or line[0] == '#':
            continue
        dataLine = string.split(line)
        name = dataLine[0] + dataLine[1]
        features = []
        #Build vector with numEntries features
        for f in dataLine[2:]:
            try:
                f = float(f)
                features.append(f)
                if f > maxVals[len(features)-1]:
                    maxVals[len(features)-1] = f
            except ValueError:
                name = name + f
        if len(features) != numEntries:
            continue
        dataList.append(features)
        nameList.append(name)
    # longestName = 0
    # for each in nameList:
    #     if len(each) > longestName:
    #         longestName = len(each)
    # print("Longest name at {} characters".format(longestName))
    # # exit()
    # print("|          Name          |   Home Value   |     Income     |    Poverty     |  Pop Density   |   Pop Change   |")
    # feat = dataList[0]
    # print "|", nameList[0], " "*(21-len(str(nameList[0]))), "|", \
    #         feat[0], " "*(13-len(str(feat[0]))), "|", \
    #         feat[1], " "*(13-len(str(feat[1]))), "|", \
    #         feat[2], " "*(13-len(str(feat[2]))), "|", \
    #         feat[3], " "*(13-len(str(feat[3]))), "|", \
    #         feat[4], " "*(13-len(str(feat[4]))), "|", \
    #
    # exit()
    # for feat in dataList[0]:
    #     print "|", feat, " "*(21-len(str(feat))), "|",

    # from pandas import *
    # displayAttrs = {nameList[0]:dataList[0]}
    # display(DataFrame(displayAttrs))
    # return
    return nameList, dataList, maxVals

def buildCountyPoints(fName):
    """
    Given an input filename, reads County values from the file and returns
    them all in a list.
    """
    nameList, featureList, maxVals = readCountyData(fName)
    points = []
    for i in range(len(nameList)):
        originalAttrs = pylab.array(featureList[i])
        normalizedAttrs = originalAttrs/pylab.array(maxVals)
        points.append(CountyWO(nameList[i], originalAttrs, normalizedAttrs))
    return points

def randomPartition(l, p):
    """
    Splits the input list into two partitions, where each element of l is
    in the first partition with probability p and the second one with
    probability (1.0 - p).

    l: The list to split
    p: The probability that an element of l will be in the first partition

    Returns: a tuple of lists, containing the elements of the first and
    second partitions.
    """
    l1 = []
    l2 = []
    for x in l:
        if random.random() < p:
            l1.append(x)
        else:
            l2.append(x)
    return (l1,l2)

def getAve(cluster, index=1):
    """
    Given a Cluster object, finds the average income field over the members
    of that cluster.

    cluster: the Cluster object to check

    Returns: a float representing the computed average income value
    """
    tot = 0.0
    numElems = 0
    for c in cluster.getPoints():
        tot += c.getOriginalAttrs()[index]

    return float(tot) / len(cluster.getPoints())

def getAveIncome(cluster):
    """
    Given a Cluster object, finds the average income field over the members
    of that cluster.

    cluster: the Cluster object to check

    Returns: a float representing the computed average income value
    """
    tot = 0.0
    numElems = 0
    for c in cluster.getPoints():
        tot += c.getOriginalAttrs()[1]

    return float(tot) / len(cluster.getPoints())


def test(points, k = 200, cutoff = 0.1):
    """
    A sample function to show you how to do a simple kmeans run and graph
    the results.
    """
    incomes = []
    print ''
    clusters, maxSmallest = kmeans(points, k, cutoff, County)

    for i in range(len(clusters)):
        if len(clusters[i].points) == 0: continue
        incomes.append(getAveIncome(clusters[i]))

    pylab.hist(incomes)
    pylab.xlabel('Ave. Income')
    pylab.ylabel('Number of Clusters')
    pylab.show()
# points = buildCountyPoints('counties.txt')
# random.seed(123)
# testPoints = random.sample(points, len(points)/10)
# test(points)

def graphRemovedErr(points, kvals = [25, 50, 75, 100, 125, 150], cutoff = 0.1):
    """
    Should produce graphs of the error in training and holdout point sets, and
    the ratio of the error of the points, after clustering for the given values of k.
    For details see Problem 1.
    """


    # Helper functions.

    def calcTotalErr(clusters, pointType=County, name="Untitled"):
        """
        Should go through each point and aggregate up each squared distance
        to a running total. Then return the total error of the set.
        """
        total_error = 0.0
        for each_cluster in clusters:
            for each_county in each_cluster.getPoints():
                total_error += each_county.distance(each_cluster.getCentroid())**2
                # print(name + " total_error:", round(total_error, 5) )
        return round(total_error, 5)

    # Your Code Here
    training_errors = []
    holdout_errors = []
    for each_k in kvals:

        ### Groundwork

        trainingSet, holdoutSet = randomPartition(points, 0.8)
        trainingClusters, training_maxDist = kmeans(points, each_k, cutoff, County)

        ### Formulate the holdout set

        # Get the mean points from eachc cluster from the training set
        trained_centroids = [mean_point.getCentroid() for mean_point in trainingClusters]
        # For each mean_point, create a cluster with each as its only point... Set each of these mean points as a cluster
        holdout_clusters = []
        for p in trained_centroids:
            holdout_clusters.append(Cluster([p], County))

        # Add the rest of the points to each's closest cluster
        newClusters = []
        for c in holdout_clusters:
            newClusters.append([])
        for p in holdoutSet:
            smallestDistance = p.distance(holdout_clusters[0].getCentroid())
            index = 0
            for i in range(len(holdout_clusters)):
                distance = p.distance(holdout_clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            newClusters[index].append(p)
        for c in xrange(len(newClusters)):
            holdout_clusters[c].setPoints(newClusters[c])



        # Check the error at the end
        training_errors += [calcTotalErr(trainingClusters, name="Training")]
        holdout_errors += [calcTotalErr(holdout_clusters, name="Training")]

        # Graph the comparison.

    pylab.plot(kvals, training_errors, 'ro')
    pylab.plot(kvals, holdout_errors, 'bo')
    pylab.xlabel('K - # of Clusters')
    pylab.ylabel('Total Error of Cluster Set')
    pylab.figure()
    pylab.plot(kvals, [holdout_errors[i] / training_errors[i] for i in xrange(len(kvals))])
    pylab.xlabel('K - # of Clusters')
    pylab.ylabel('Ratio of Error of Cluster Sets (Holdout/Training)')
    # print([p for p in holdout_clusters[0].getPoints()])
    print("holdout_errors:", holdout_errors)
    print("training_errors:", training_errors)
    pylab.show()
# points = buildCountyPoints('counties.txt')
# # random.seed(123)
# # testPoints = random.sample(points, len(points)/10)
# graphRemovedErr(points)

def homeClusterAnalysis(points, k = 50, cutoff = 0.1):

    from pandas import *
    # x = [["A", "B"], ["C", "D"]]
    # print DataFrame(x)
    run = []
    for i in xrange(2):
        run.append(kmeans(points, k, cutoff, County))
        run_counter = 1
        for r in run:
            print("Run #", run_counter)
            run_counter += 1
            cluster_counter = 1
            for c in r[0]:
                print("Cluster #", cluster_counter)
                cluster_counter += 1
                cntyNames = [cnty.getName() for cnty in c.getPoints()]
                if "MIKalamazoo" in cntyNames:
                    maxIncome = 0
                    minIncome = c.getPoints()[0]
                    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
                    print("Kalamazoo cluster located...")

                    print("|          Name          |   Home Value   |     Income     |    Poverty     |  Pop Density   |   Pop Change   |")
                    for p in c.getPoints():
                        # print "p.getOriginalAttrs()..."
                        feat = p.getOriginalAttrs()
                        print "|", p.getName(), " "*(21-len(p.getName())), "|", \
                                feat[0], " "*(13-len(str(feat[0]))), "|", \
                                feat[1], " "*(13-len(str(feat[1]))), "|", \
                                feat[2], " "*(13-len(str(feat[2]))), "|", \
                                feat[3], " "*(13-len(str(feat[3]))), "|", \
                                feat[4], " "*(13-len(str(feat[4]))), "|"
                        if feat[1] > maxIncome:
                            maxIncome = feat[1]
                        if feat[1] < minIncome:
                            minIncome = feat[1]

                    print("|          Name          |    Prcnt65+    |     Below18    |PrcntFemale2000 |PrcntHSgrads2000|PrcntCollege2000|")
                    for p in c.getPoints():
                        # print "p.getOriginalAttrs()..."
                        feat = p.getOriginalAttrs()
                        print "|", p.getName(), " "*(21-len(p.getName())), "|", \
                                feat[5], " "*(13-len(str(feat[5]))), "|", \
                                feat[6], " "*(13-len(str(feat[6]))), "|", \
                                feat[7], " "*(13-len(str(feat[7]))), "|", \
                                feat[8], " "*(13-len(str(feat[8]))), "|", \
                                feat[9], " "*(13-len(str(feat[9]))), "|"

                    print("|          Name          |   Unemployed   | PrcntBelow18   | LifeExpectancy |   FarmAcres   |")
                    for p in c.getPoints():
                        # print "p.getOriginalAttrs()..."
                        feat = p.getOriginalAttrs()
                        print "|", p.getName(), " "*(21-len(p.getName())), "|", \
                                feat[10], " "*(11-len(str(feat[5]))), "|", \
                                feat[11], " "*(16-len(str(feat[6]))), "|", \
                                feat[12], " "*(13-len(str(feat[7]))), "|", \
                                feat[13], " "*(13-len(str(feat[8]))), "|"
                    print("maxIncome, minIncome:", maxIncome, minIncome)
                    exit()
                    # print(cntyNames)

                    # print(cnty.getOriginalAttrs())
                else:
                    print([cnty.getName() for cnty in c.getPoints()])

# points = buildCountyPoints('counties.txt')
# random.seed(123)
# testPoints = random.sample(points, len(points)/10)
# homeClusterAnalysis(points)

def graphPredictionErr(points, dimension, kvals = [25, 50, 75, 100, 125, 150], cutoff = 0.1):
    """
    Given input points and a dimension to predict, should cluster on the
    appropriate values of k and graph the error in the resulting predictions,
    as described in Problem 3.
    """

	# Your Code Here

    # 1. Set the weight of the Poverty feature to 0 and the weight of all other features to 1 in the weights array of the County class (we will examine the effect of changes to this weight vector later.) DONE


    def createClusterSetsFromTrainingData():
        # 2. Partition your data set into a training set and a holdout set, where the holdout set is 20% of all the data and is randomly chosen. DONE
        trainingSet, holdoutSet = randomPartition(points, 0.8)
        # 3. Using kmeans(...), cluster the training data into 25-150 clusters as in Problem 1.
        clusterSets = []
        for each_k in kvals:
            trainingClusters, training_max_dist = kmeans(trainingSet, each_k, cutoff, CountyWO)
            clusterSets += [trainingClusters]
        return clusterSets, holdoutSet

    clusterSetsFromTrainingData, holdoutSet = createClusterSetsFromTrainingData()

    def addPointToCluster(p, clusterSet):
        dist = 0.0
        index = 0
        for c in clusterSet:
            dist_to_c = p.distance(c.getCentroid())
            if dist_to_c > dist:
                index_of_cluster_to_add_point_to = index
                dist = dist_to_c
            index += 1
        points_for_new_clusters_by_index[index_of_cluster_to_add_point_to] += [p]

    def createNewClusters(arg):
        """

        """
        pass

    for p in holdoutSet:
        # find the cluster c that is closest to p.

        # What do I* need to track?
        # How do I* compute this?
        cs_ave_povs = []
        all_new_cluster_sets = []

        # How do I* compute this?
        for cs in clusterSetsFromTrainingData:

            # How do I recluster the holdout points using centroids from each of the current cluster sets?
            # How do I* recreate all clusters, at their same centroids, but with the holdout points instead of the training points
            # What are the methods I* need to consider to achieve this computation? Could create a method called setCentroid()
            new_clusters_without_training_points = []
            points_for_new_clusters_by_index = []
            for c in cs:
                new_clusters_without_training_points += [Cluster(points=[c.getCentroid()], pointType=County)]
                points_for_new_clusters_by_index += [[]]
                # c_ave_pov += getAve(c, index=2)

            for p in holdoutSet:
                addPointToCluster(p, new_clusters_without_training_points)

            for index in xrange(len(new_clusters_without_training_points)):
                cur_points = points_for_new_clusters_by_index[index]
                new_clusters_without_training_points[index].setPoints(cur_points)
            all_new_cluster_sets += [new_clusters_without_training_points]

    # The total error of each cluster at a given k
    # What will the x-axis be? | Cluster #
    # What will the y-axis be? | Total of squared difference between each point
        # and the mean point (centroidd)
    # Need to remember the error at each cluster
    cluster_set_error_list = []
    # Need each cluster set
    for cs in all_new_cluster_sets:
        # Need each cluster from the cluster set
        error_at_each_cluster = []
        for c in cs:
            # Need the total squared difference of all points and their distances to
            # the centroid
            tot = 0.0
            for p in c.getPoints():
                tot += (p.getOriginalAttrs()[2] - getAve(c, index=2))**2
            error_at_each_cluster += [tot]
        cluster_set_error_list += [error_at_each_cluster] #####################################################
    # For each k in kvals, graph the error of each cluster of the cluster #
    # i = 0
    # for each in kvals:
    #     pylab.plot(range(len(cluster_set_error_list[i])), cluster_set_error_list[i], 'ro')
    #     pylab.title("Total error of each cluster")
    #     pylab.xlabel('Cluster #')
    #     pylab.ylabel('Total error of each cluster')
    #     pylab.figure()
    #         # Need each point from the cluster set
    #     i += 1

    # The total error of each point given a cluster
    def checkWeights():
        print("CountyWO.weights", CountyWO.weights)

    def checkErrors():
        counter = 0
        for eachTotalError in cluster_set_error_list:
            print("For K at {}, the error is:".format(kvals[counter]), sum(eachTotalError)) # Need a way to handle the parenthesis cluster fuck.
            counter += 1

    checkWeights()
    checkErrors()

    def plotAndShowGraph(x, y, ymin=1000, ymax=2500, hist=False):
        if hist == False:
            pylab.plot(x, y, "go")
        else:
            pass
        # pylab.hist([sum(cs) for cs in cluster_set_error_list], bins=kvals)
        pylab.xticks(np.arange(min(kvals), max(kvals) + 25.0, 25.0))
        pylab.yticks(np.arange(1000, 2500, 200))
        pylab.title("Total error of each cluster set over K")
        pylab.xlabel("K #")
        pylab.ylabel("Total error at each cluster set")
        pylab.show()

    plotAndShowGraph(x=kvals, y=[sum(cs) for cs in cluster_set_error_list])

def setWeightValues(HomeValue2000 = 1.0, Income1999 = 1.0, Poverty1999 = 1.0, PopDensity2000 = 1.0, PopChange = 1.0, \
	       PrcntAbove65 = 1.0, Below18 = 1.0, PrcntFemale2000 = 1.0, PrcntHSgrads2000 = 1.0, PrcntCollege2000 = 1.0, \
           Unemployed = 1.0, PrcntBelow18 = 1.0, LifeExpectancy = 1.0, FarmAcres = 1.0):
    """
    Accepts weight values for each data column. Default weights at 1.0.

    Returns a list of 14 weights, with each value in the list representing the
    column via the index.
    """

    weights = [HomeValue2000, Income1999, Poverty1999, PopDensity2000, PopChange, \
    	       PrcntAbove65, Below18, PrcntFemale2000, PrcntHSgrads2000, PrcntCollege2000, \
               Unemployed, PrcntBelow18, LifeExpectancy, FarmAcres]
    return weights

def setWeightValuesDefZero(HomeValue2000 = 0.0, Income1999 = 0.0, Poverty1999 = 0.0, PopDensity2000 = 0.0, PopChange = 0.0, \
	       PrcntAbove65 = 0.0, Below18 = 0.0, PrcntFemale2000 = 0.0, PrcntHSgrads2000 = 0.0, PrcntCollege2000 = 0.0, \0
           Unemployed = 0.0, PrcntBelow18 = 0.0, LifeExpectancy = 0.0, FarmAcres = 0.0):
    """
    Accepts weight values for each data column. Default weights at 1.0.

    Returns a list of 14 weights, with each value in the list representing the
    column via the index.
    """

    weights = [HomeValue2000, Income1999, Poverty1999, PopDensity2000, PopChange, \
    	       PrcntAbove65, Below18, PrcntFemale2000, PrcntHSgrads2000, PrcntCollege2000, \
               Unemployed, PrcntBelow18, LifeExpectancy, FarmAcres]
    return weights

def setSingleWeight(weightAt=4):
    weights = [0.0]*13
    weights[weightAt:weightAt] = [1.0]

def adjustWeightsThenRun(weights, points=None, dim=1):
    "docstring for adjustWeightsBeforeRun"

    weights = pylab.array(weights)
    print("adjustWeightsBeforeRun() weights len:", len(weights))
    CountyWO.weights = weights
    graphPredictionErr(points, 1)


points = buildCountyPoints('counties.txt')
random.seed(123)
testPoints = random.sample(points, len(points)/10)
# graphPredictionErr(testPoints, 1)
adjustWeightsThenRun(setWeightValuesDefZero(Income1999 = 1.0, PrcntCollege2000 = 1.0), points=points, dim=1)
