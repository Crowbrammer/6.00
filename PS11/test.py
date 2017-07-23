from graph import Digraph, Edge, Node
from ps11 import WeightedEdge

def buildNodes(mitMapLines = "mit_map.txt"):

    allNodes = set()
    testEdge = WeightedEdge("1", "2", "3", "4")
    allEdges = set(testEdge)

    # Nodes

    def nodeExists(name):
        return name in {node.getName() for node in allNodes}

    def addNodeToList(name):
        allNodes.add(Node(name))

    def checkThenAddNodeIfFalse(name):
        if nodeExists(name) == False:
            addNodeToList(Node(name))

    # Edges

    def edgeExists(src, dest):
        return (src, dest) in {(edge.getSource(), edge.getDestination()) for edge in allEdges}

    def getPaths(fileName = mitMapLines):

        def valWithoutNewline(val):
            return val.replace("\n", "")

        with open("mit_map.txt") as f:
            for line in f:
                splitLine = line.split(" ")
                splitLine[3] = valWithoutNewline(splitLine[3])
                yield splitLine

    def buildEach(splitLine):
        curPath = splitLine.next()
        counter = 0

        def buildEachNode():
            checkThenAddNodeIfFalse(str(curPath[0]))
            checkThenAddNodeIfFalse(str(curPath[1]))

        def buildEachEdge():
            pass

        while curPath != None and counter < 100:
            buildEachNode()
            curPath = splitLine.next()
            counter += 1


    def testFunction(func = None, params = None, allNodes = allNodes, valCheck = None):
        def buildAndExecuteFunc():
            pass
        def checkValues():
            pass
        print(valCheck)
        if params == None:
            buildEach(getPaths())
            # allNodes = addNodeToList(allNodes, 32)
        print(valCheck)
    testFunction(addNodeToList, valCheck = allNodes)
    # for splitLine in mitMapLines:
    #     node1, node2 = splitLine[0], splitLine[1]

buildNodes()

# How to get the name of the variable
# How to get the params of the function for use in executing another function.

# getPaths("mit_map.txt")
# Use this idea for creating log decorators
