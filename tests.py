from compiler import compile
from classes_and_rules import *

def test_set_def():
    print("Running test_set_def():")
    test_num = 1

    knowns = []
    destination = Proposition("1 in {1}")
    proof = [ProofRow(knowns,Rule("Set"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = []
    destination = Proposition("2 in {1,2,3}")
    proof = [ProofRow(knowns,Rule("Set"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = []
    destination = Proposition("0 in {1,2,3}")
    proof = [ProofRow(knowns,Rule("Set"),destination)]
    run_single_test(test_num,knowns,destination,proof,False)
    test_num = test_num + 1

    knowns = []
    destination = Proposition("2 in {}")
    proof = [ProofRow(knowns,Rule("Set"),destination)]
    run_single_test(test_num,knowns,destination,proof,False)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("2 in A")
    proof = [ProofRow(knowns,Rule("Set"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

def test_set_diff():
    print("Running test_set_diff():")
    test_num = 1

    knowns = []
    destination = Proposition("{1}\{1} = {}")
    proof = [ProofRow(knowns,Rule("A\B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = []
    destination = Proposition("{1,2}\{2} = {1}")
    proof = [ProofRow(knowns,Rule("A\B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = []
    destination = Proposition("{1,3}\{2} = {1}")
    proof = [ProofRow(knowns,Rule("A\B"),destination)]
    run_single_test(test_num,knowns,destination,proof,False)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("A\{1} = {2}")
    proof = [ProofRow(knowns,Rule("A\B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("{1,2,3}\A = {3}")
    proof = [ProofRow(knowns,Rule("A\B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("{1,2,3}\A = {2}")
    proof = [ProofRow(knowns,Rule("A\B"),destination)]
    run_single_test(test_num,knowns,destination,proof,False)
    test_num = test_num + 1

def test_set_union():
    print("Running test_set_union():")
    test_num = 1

    knowns = []
    destination = Proposition("{2} union {1} = {1,2}")
    proof = [ProofRow(knowns,Rule("A union B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = []
    destination = Proposition("{} union {} = {}")
    proof = [ProofRow(knowns,Rule("A union B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("A union {1} = {1,2}")
    proof = [ProofRow(knowns,Rule("A union B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("{3} union A = {1,3,2}")
    proof = [ProofRow(knowns,Rule("A union B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("{3} union A = {1,2}")
    proof = [ProofRow(knowns,Rule("A union B"),destination)]
    run_single_test(test_num,knowns,destination,proof,False)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("{} union A = {1,2}")
    proof = [ProofRow(knowns,Rule("A union B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

def test_set_intersection():
    print("Running test_set_intersection():")
    test_num = 1

    knowns = []
    destination = Proposition("{2} intersection {1} = {}")
    proof = [ProofRow(knowns,Rule("A intersection B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = []
    destination = Proposition("{} intersection {} = {1}")
    proof = [ProofRow(knowns,Rule("A intersection B"),destination)]
    run_single_test(test_num,knowns,destination,proof,False)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("A intersection {2,3} = {2}")
    proof = [ProofRow(knowns,Rule("A intersection B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("{1} intersection A = {2}")
    proof = [ProofRow(knowns,Rule("A intersection B"),destination)]
    run_single_test(test_num,knowns,destination,proof,False)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}"), Proposition("B = {1,3}")]
    destination = Proposition("A intersection B = {1}")
    proof = [ProofRow(knowns,Rule("A intersection B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}"), Proposition("B = {1,3}")]
    destination = Proposition("B intersection A = {1}")
    proof = [ProofRow(knowns,Rule("A intersection B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}"), Proposition("B = {1,3}")]
    destination = Proposition("B intersection A = {}")
    proof = [ProofRow(knowns,Rule("A intersection B"),destination)]
    run_single_test(test_num,knowns,destination,proof,False)
    test_num = test_num + 1

    knowns = [Proposition("A = {}")]
    destination = Proposition("A intersection {1,2,3} = {}")
    proof = [ProofRow(knowns,Rule("A intersection B"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

def test_sub_rule():
    print("Running test_sub_rule():")
    test_num = 1

    knowns = [Proposition("A = {1,2}"), Proposition("B = {1,2}")]
    destination = Proposition("A = B")
    proof = [ProofRow(knowns,Rule("= Sub"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,3}"), Proposition("B = {1,2}")]
    destination = Proposition("A = B")
    proof = [ProofRow(knowns,Rule("= Sub"),destination)]
    run_single_test(test_num,knowns,destination,proof,False)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,3}"), Proposition("B = {1,3}")]
    destination = Proposition("B = A")
    proof = [ProofRow(knowns,Rule("= Sub"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("{1,3} = A"), Proposition("B = {1,3}")]
    destination = Proposition("A = B")
    proof = [ProofRow(knowns,Rule("= Sub"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("{1,3} = A"), Proposition("{1,3} = B")]
    destination = Proposition("A = B")
    proof = [ProofRow(knowns,Rule("= Sub"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("A = A")
    proof = [ProofRow(knowns,Rule("= Sub"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = []
    destination = Proposition("1 = 1")
    proof = [ProofRow(knowns,Rule("= Sub"),destination)]
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}"), Proposition("A = {1,2}")]
    destination = Proposition("A = B")
    proof = [ProofRow(knowns,Rule("= Sub"),destination)]
    run_single_test(test_num,knowns,destination,proof,False)
    test_num = test_num + 1

    knowns = [Proposition("A = {1,2}")]
    destination = Proposition("A\{1} union {1} = A")
    proof = []
    proof.append(ProofRow(knowns,Rule("A\B"),Proposition("A\{1} = {2}")))
    proof.append(ProofRow([],Rule("A union B"),Proposition("{2} union {1} = {1,2}")))
    proof.append(ProofRow([Proposition("{2} union {1} = {1,2}"),Proposition("A\{1} = {2}")],Rule("= Sub"),Proposition("A\{1} union {1} = {1,2}")))
    proof.append(ProofRow([Proposition("A\{1} union {1} = {1,2}"), Proposition("A = {1,2}")],Rule("= Sub"),Proposition("A\{1} union {1} = A")))
    run_single_test(test_num,knowns,destination,proof,True)
    test_num = test_num + 1

def run_single_test(test_num: int, knowns: List[Proposition], destination: Proposition, proof: List[Proposition], expected: bool):
    if(compile(knowns, destination, proof, print_results=False) == expected):
        print(f"Test {test_num} Passed")
    else:
        print(f"Test {test_num} Failed")

def run_tests():
    test_set_def()
    test_set_diff()
    test_set_union()
    test_set_intersection()
    test_sub_rule()

if __name__ == "__main__":
    run_tests()