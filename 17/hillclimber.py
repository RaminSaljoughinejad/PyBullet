from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(self.Spawn(), self.Mutate(), self.child.Evaluate("DIRECT"), self.Select(), currentGeneration+1)
        

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness<self.child.fitness:
            self.parent = self.child
    
    def Evolve_For_One_Generation(self,sp,mu,ev,se,itr):
        self.child.Evaluate("DIRECT")
        self.Print(itr)

    def Print(self, itr):
        print("\n",itr,self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")
