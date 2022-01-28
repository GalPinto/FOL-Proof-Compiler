import re
from typing import List, Callable
from classes_and_rules import *
from knowns import global_knowns

def compile(knowns: List[Proposition], destination: Proposition, proof: List[ProofRow], print_results: bool = True) -> bool:
    if(print_results):
        print("Compiling proof:")
    global_knowns.extend(knowns) # Check syntax (?)
    for row in proof:
        if(not compileRow(row,print_results)):
            return False
    if(destination in global_knowns):
        if(print_results):
            print("Compilation succeeded.")
        return True
    if(print_results):
        print(f"Compilation failed.\nSpecified destination doesn't follow from the proofs.")
    return False

def compileRow(row: ProofRow, print_results: bool = True) -> bool:
    # Check knowns
    for known in row.knowns:
        if(known not in global_knowns):
            if(print_results):
                print(f"Compilation failed in row: {row}.\nSpecified known: {known} hasn't been proven as true proposition.")
            return False
    
    # Check Rule
    if(row.rule not in global_rules):
        if(print_results):
            print(f"Compilation failed in row: {row}.\nSpecified rule: {row.rule} is not a valid rule")
        return False

    # Check validity
    if(row.rule.apply(row.knowns, row.conclusion)):
        global_knowns.append(row.conclusion)
        return True
    else:
        if(print_results):
            print(f"Compilation failed in row: {row}.\nSpecified conclusion doesn't follow from the specified knowns and rule.")
        return False

def main() -> None:
    # TODO: Parse input instead of manual preparation of proof.

    knowns = []
    knowns.append(Proposition("A = {1,2}"))

    destination = Proposition("A\{1} union {1} = A")

    proof = []
    proof.append(ProofRow(knowns,Rule("A\B"),Proposition("A\{1} = {2}")))
    proof.append(ProofRow([],Rule("A union B"),Proposition("{2} union {1} = {1,2}")))
    proof.append(ProofRow([Proposition("{2} union {1} = {1,2}"),Proposition("A\{1} = {2}")],Rule("= Sub"),Proposition("A\{1} union {1} = {1,2}")))
    proof.append(ProofRow([Proposition("A\{1} union {1} = {1,2}"), Proposition("A = {1,2}")],Rule("= Sub"),Proposition("A\{1} union {1} = A")))
    
    compile(knowns, destination, proof)

if __name__ == "__main__":
    main()