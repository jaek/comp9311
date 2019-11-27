#!/usr/bin/python3

class Relation:
    def __init__(self, name, attributes=None):
        if attributes is not None:
            self.attributes = attributes
        else:
            self.attributes = set()
        self.name = name
        self.closures = {}
        self.superkeys = []

    def add_attribute(self, name):
        '''check if an attribute is part of a relation. if not, create it'''
        for a in self.attributes:
            if name == a.name:
                return a
        n = Attribute(name)
        self.attributes.add(n)
        print("added attribute " + n.name + " to relation " + self.name)
        return n

    def get_attribute(self, name):
        ''' Check whether an attribute exists and return it '''
        for a in self.attributes:
            if name == a.name:
                return a
        print("no attribute " + name + " found")
        return False

    def parse_fd(self, input):
        ''' Take user input and covert it into a relation'''
        print("Parsing input " + input)
        t = self.tokenize(input)
        for attrib in t:
            RHS = []
            for a in attrib[1]:
                n = self.add_attribute(a)
                RHS.append(n)
            for a in attrib[0]:
                n = self.add_attribute(a)
                if n:
                    n.add_dependencies(RHS)

    def tokenize(self, input):
        ''' Split a sequence of characters up for consumption by parse_fd'''
        t = []
        relationships = input.split(';')
        print(relationships)
        for r in relationships:
            r = r.split('->')
            lhs = r[0].split(',')
            rhs = r[1].split(',')
            t.append((lhs, rhs))
        return t

    def show_relation(self):
        ''' Print the contents of a relation to the screen'''
        for d in self.attributes:
            d.show_dependencies()

    def show_closures(self):
        ''' Print all closures to the screen'''
        for c in self.closures:
            print(f"closure of {c} is {list(x.name for x in self.closures[c])}")

    def compute_closure(self, a, closure, to_check, checked):
        ''' calculate the closure of an attribute with regards to its FD set'''
        if closure == set():
            closure.add(a)
        d = a.dependencies
        closure.update(d)
        to_check.update(d.difference(checked))
        #see if we have dependencies to check
        if len(to_check) == 0:
            return closure
        else:
            checked.add(a)
            b = to_check.pop()
            return(self.compute_closure(b, closure, to_check, checked))

    def compute_all_closures(self):
        '''find the closures of all members of R and store them'''
        for a in self.attributes:
            c = self.compute_closure(a, set(), set(), set())
            self.closures[a.name] = c
        self.show_closures()

    def check_if_key(self, k):
        if k == self.attributes:
            return True
        return False

    def closure_of_set(self, s):
        ''''given a set of attributes, compute the closure of that set'''
        r = set()
        for a in s:
            try:
                r.update(self.closures[a.name])
            except:
                print(f"no closure found for {a}")
        return r

    def compute_super_keys(self):
        sk = []
        sk.append(self.attributes)
        i = 0
        print("searching for superkeys:")
        while i < 20:
            l = list(sk[i])
            for a in l:
                tmp = set()
                tmp.add(a)
                t = sk[i].remove(a)
                c = self.closure_of_set(t)
                if self.check_if_key(c):
                    print(f"Found superkey: {list(a.name for a in c)}")
                    sk.append(c)
            i = i + 1

class Attribute:
    # an attribute is a relation that consists of one identifier and
    # a set of atomic dependencies
    def __init__(self, name):
        self.name = name
        self.dependencies = set()

    def __str__(self):
        return(self.name)

    def add_dependencies(self, dependencies):
        if isinstance(dependencies, list):
            for d in dependencies:
                self.dependencies.add(d)
                print(f"added dependency {d.name} to attribute {self.name}")
        else:
            self.dependencies.add(dependencies)
            print(f"added dependency {dependencies.name} to attribute {self.name}")

    def show_dependencies(self):
        if len(self.dependencies) is not 0:
            o = ""
            for d in self.dependencies:
                o = o + d.name
            print(self.name + "->" + str(o))



def test(input):
    print("Creating a new relation R\n")
    print("*"*20)
    r = Relation('R')
    r.parse_fd(input)
    print("*"*20)
    print("Dependencies:")
    r.show_relation()
    print("*"*20)
    print("Computing all closures:")
    r.compute_all_closures()
    print("*"*20)
    r.compute_super_keys()
    print("Finished\n\n")
    del r
    return True

if __name__ == '__main__':
    F1 = "C->D,E;A,B->C,F;D->G;G->A;L->M"
    F2 = "A->B;B->C;A->C"

    test(F2)
    test(F1)
