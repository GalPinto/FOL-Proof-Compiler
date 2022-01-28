import re
from typing import List, Callable

class Rule:
    # apply function signature: apply(knowns: List[Proposition], conclusion: Proposition) -> bool
    def __init__(self, text: str, apply: Callable = None):
        self.text = text
        self.apply = apply
        if(apply is None):
            for rule in global_rules:
                if(text == rule.text):
                    self.apply = rule.apply
        
    def __str__(self):
        return self.text
    def __eq__(self, other):
        return self.text == other.text and self.apply == other.apply

class Proposition:
    def __init__(self, text :str):
        self.text = text
    def __str__(self):
        return self.text
    def __eq__(self, other):
        return self.text == other.text

class ProofRow:
    def __init__(self,knowns: List[Proposition], rule: Rule, conclusion: Proposition):
        self.knowns = knowns
        self.rule = rule
        self.conclusion = conclusion
    def __str__(self):
        return f"Knowns: {' ,'.join(map(str, self.knowns))}, Rule: {self.rule}, Destination: {self.conclusion}"


#########
# Rules #
#########

def set_def_rule(knowns: List[Proposition], conclusion: Proposition) -> bool:
    if(len(knowns) == 0):
        conclusion_element, conclusion_set = re.compile(r"^(\w)\s*in\s*{(.*)}$").findall(conclusion.text)[0]
        return conclusion_element in conclusion_set.split(',')
    elif(len(knowns) == 1):
        set_name = re.compile(r"^(\w)\s*=\s*{.*}$").findall(knowns[0].text)[0]
        elements = re.compile(r"^\w\s*=\s*{(.*)}$").findall(knowns[0].text)[0].split(',')
        conclusion_element, conclusion_set = re.compile(r"^(\w)\s*in\s*(\w)$").findall(conclusion.text)[0]
        return set_name == conclusion_set and conclusion_element in elements
    else:
        return False

def set_diff_rule(knowns: List[Proposition], conclusion: Proposition) -> bool:
    if(len(knowns) == 0):
        r = re.compile(r"^{(.*)}\\{(.*)}\s*=\s*{(.*)}$").findall(conclusion.text)
        if(len(r) == 0):
            return False
        conclusion_elements1, conclusion_elements2, conclusion_elements = r[0]
        if(len(conclusion_elements1) == 0):
            conclusion_elements1 = set()
        else:
            conclusion_elements1 = conclusion_elements1.split(',')
        if(len(conclusion_elements2) == 0):
            conclusion_elements2 = set()
        else:
            conclusion_elements2 = conclusion_elements2.split(',')
        if(len(conclusion_elements) == 0):
            conclusion_elements = set()
        else:
            conclusion_elements = conclusion_elements.split(',')
        set_diff = set(conclusion_elements1) - set(conclusion_elements2)
        return set_diff == set(conclusion_elements)
    if(len(knowns) == 1):
        set_name = re.compile(r"^(\w)\s*=\s*{.*}$").findall(knowns[0].text)[0]
        elements = re.compile(r"^\w\s*=\s*{(.*)}$").findall(knowns[0].text)[0]
        if(len(elements) == 0):
            elements = set()
        else:
            elements = elements.split(',')
        r = re.compile(r"^(\w)\\{(.*)}\s*=\s*{(.*)}$").findall(conclusion.text)
        if(len(r) == 0):
            r = re.compile(r"^{(.*)}\\(\w)\s*=\s*{(.*)}$").findall(conclusion.text)
        if(len(r) == 0):
            return False
        conclusion_set1, conclusion_set2, conclusion_elements = r[0]
        if(len(conclusion_elements) == 0):
            conclusion_elements = set()
        else:
            conclusion_elements = conclusion_elements.split(',')
        if(conclusion_set1 == set_name):
            if(len(conclusion_set2) == 0):
                conclusion_set2 = set()
            else:
                elements2 = conclusion_set2.split(',')
            set_diff = set(elements) - set(elements2)
        elif(conclusion_set2 == set_name):
            if(len(conclusion_set1) == 0):
                elements2 = set()
            else:
                elements2 = conclusion_set1.split(',')
            set_diff = set(elements2) - set(elements)
        return set_diff == set(conclusion_elements)
    elif(len(knowns) == 2):
        set_name1 = re.compile(r"^(\w)\s*=\s*{.*}$").findall(knowns[0].text)[0]
        elements1 = re.compile(r"^\w\s*=\s*{(.*)}$").findall(knowns[0].text)[0]
        if(len(elements1) == 0):
            elements1 = set()
        else:
            elements1 = elements1.split(',')
        set_name2 = re.compile(r"^(\w)\s*=\s*{.*}$").findall(knowns[1].text)[0]
        elements2 = re.compile(r"^\w\s*=\s*{(.*)}$").findall(knowns[1].text)[0]
        if(len(elements2) == 0):
            elements2 = set()
        else:
            elements2 = elements2.split(',')
        conclusion_set1, conclusion_set2, conclusion_elements = re.compile(r"^(\w)\\(\w)\s*=\s*{(.*)}$").findall(conclusion.text)[0]
        if(len(conclusion_elements) == 0):
            conclusion_elements = set()
        else:
            conclusion_elements = conclusion_elements.split(',')
        if(conclusion_set1 == set_name1 and conclusion_set2 == set_name2):
            set_diff = set(elements1) - set(elements2)
            return set_diff == set(conclusion_elements)
        elif(conclusion_set1 == set_name2 and conclusion_set1 == set_name2):
            set_diff = set(elements2) - set(elements1)
            return set_diff == set(conclusion_elements)
        else:
            return False
    else:
        return False

def set_union_rule(knowns: List[Proposition], conclusion: Proposition) -> bool:
    if(len(knowns) == 0):
        r = re.compile(r"^{(.*)}\s*union\s*{(.*)}\s*=\s*{(.*)}$").findall(conclusion.text)
        if(len(r) == 0):
            return False
        conclusion_elements1, conclusion_elements2, conclusion_elements = r[0]
        if(len(conclusion_elements1) == 0):
            conclusion_elements1 = set()
        else:
            conclusion_elements1 = conclusion_elements1.split(',')
        if(len(conclusion_elements2) == 0):
            conclusion_elements2 = set()
        else:
            conclusion_elements2 = conclusion_elements2.split(',')
        if(len(conclusion_elements) == 0):
            conclusion_elements = set()
        else:
            conclusion_elements = conclusion_elements.split(',')
        set_union = set(conclusion_elements1) | set(conclusion_elements2)
        return set_union == set(conclusion_elements)
    if(len(knowns) == 1):
        set_name = re.compile(r"^(\w)\s*=\s*{.*}$").findall(knowns[0].text)[0]
        elements = re.compile(r"^\w\s*=\s*{(.*)}$").findall(knowns[0].text)[0]
        if(len(elements) == 0):
            elements = set()
        else:
            elements = elements.split(',')
        r = re.compile(r"^(\w)\s*union\s*{(.*)}\s*=\s*{(.*)}$").findall(conclusion.text)
        if(len(r) == 0):
            r = re.compile(r"^{(.*)}\s*union\s*(\w)\s*=\s*{(.*)}$").findall(conclusion.text)
        if(len(r) == 0):
            return False
        conclusion_set1, conclusion_set2, conclusion_elements = r[0]
        if(len(conclusion_elements) == 0):
            conclusion_elements = set()
        else:
            conclusion_elements = conclusion_elements.split(',')
        if(conclusion_set1 == set_name):
            if(len(conclusion_set2) == 0):
                elements2 = set()
            else:
                elements2 = conclusion_set2.split(',')
            set_union = set(elements) | set(elements2)
        elif(conclusion_set2 == set_name):
            if(len(conclusion_set1) == 0):
                elements2 = set()
            else:
                elements2 = conclusion_set1.split(',')
            set_union = set(elements2) | set(elements)
        return set_union == set(conclusion_elements)
    elif(len(knowns) == 2):
        set_name1 = re.compile(r"^(\w)\s*=\s*{.*}$").findall(knowns[0].text)[0]
        elements1 = re.compile(r"^\w\s*=\s*{(.*)}$").findall(knowns[0].text)[0]
        if(len(elements1) == 0):
            elements1 = set()
        else:
            elements1 = elements1.split(',')
        set_name2 = re.compile(r"^(\w)\s*=\s*{.*}$").findall(knowns[1].text)[0]
        elements2 = re.compile(r"^\w\s*=\s*{(.*)}$").findall(knowns[1].text)[0]
        if(len(elements2) == 0):
            elements2 = set()
        else:
            elements2 = elements2.split(',')
        conclusion_set1, conclusion_set2, conclusion_elements = re.compile(r"^(\w)\s*union\s*(\w)\s*=\s*{(.*)}$").findall(conclusion.text)[0]
        if(len(conclusion_elements) == 0):
            conclusion_elements = set()
        else:
            conclusion_elements = conclusion_elements.split(',')
        if(conclusion_set1 == set_name1 and conclusion_set2 == set_name2):
            set_union = set(elements1) | set(elements2)
            return set_union == set(conclusion_elements)
        elif(conclusion_set1 == set_name2 and conclusion_set1 == set_name2):
            set_union = set(elements2) | set(elements1)
            return set_union == set(conclusion_elements)
        else:
            return False
    else:
        return False

def set_intersection_rule(knowns: List[Proposition], conclusion: Proposition) -> bool:
    if(len(knowns) == 0):
        r = re.compile(r"^{(.*)}\s*intersection\s*{(.*)}\s*=\s*{(.*)}$").findall(conclusion.text)
        if(len(r) == 0):
            return False
        conclusion_elements1, conclusion_elements2, conclusion_elements = r[0]
        if(len(conclusion_elements1) == 0):
            conclusion_elements1 = set()
        else:
            conclusion_elements1 = conclusion_elements1.split(',')
        if(len(conclusion_elements2) == 0):
            conclusion_elements2 = set()
        else:
            conclusion_elements2 = conclusion_elements2.split(',')
        if(len(conclusion_elements) == 0):
            conclusion_elements = set()
        else:
            conclusion_elements = conclusion_elements.split(',')
        set_intersection = set(conclusion_elements1) & set(conclusion_elements2)
        return set_intersection == set(conclusion_elements)
    if(len(knowns) == 1):
        set_name = re.compile(r"^(\w)\s*=\s*{.*}$").findall(knowns[0].text)[0]
        elements = re.compile(r"^\w\s*=\s*{(.*)}$").findall(knowns[0].text)[0]
        if(len(elements) == 0):
            elements = set()
        else:
            elements = elements.split(',')
        r = re.compile(r"^(\w)\s*intersection\s*{(.*)}\s*=\s*{(.*)}$").findall(conclusion.text)
        if(len(r) == 0):
            r = re.compile(r"^{(.*)}\s*intersection\s*(\w)\s*=\s*{(.*)}$").findall(conclusion.text)
        if(len(r) == 0):
            return False
        conclusion_set1, conclusion_set2, conclusion_elements = r[0]
        if(len(conclusion_elements) == 0):
            conclusion_elements = set()
        else:
            conclusion_elements = conclusion_elements.split(',')
        if(conclusion_set1 == set_name):
            if(len(conclusion_set2) == 0):
                elements2 = set()
            else:
                elements2 = conclusion_set2.split(',')
            set_intersection = set(elements) & set(elements2)
        elif(conclusion_set2 == set_name):
            if(len(conclusion_set1) == 0):
                elements2 = set()
            else:
                elements2 = conclusion_set1.split(',')
            set_intersection = set(elements2) & set(elements)
        return set_intersection == set(conclusion_elements)
    elif(len(knowns) == 2):
        set_name1 = re.compile(r"^(\w)\s*=\s*{.*}$").findall(knowns[0].text)[0]
        elements1 = re.compile(r"^\w\s*=\s*{(.*)}$").findall(knowns[0].text)[0]
        if(len(elements1) == 0):
            elements1 = set()
        else:
            elements1 = elements1.split(',')
        set_name2 = re.compile(r"^(\w)\s*=\s*{.*}$").findall(knowns[1].text)[0]
        elements2 = re.compile(r"^\w\s*=\s*{(.*)}$").findall(knowns[1].text)[0]
        if(len(elements2) == 0):
            elements2 = set()
        else:
            elements2 = elements2.split(',')
        conclusion_set1, conclusion_set2, conclusion_elements = re.compile(r"^(\w)\s*intersection\s*(\w)\s*=\s*{(.*)}$").findall(conclusion.text)[0]
        if(len(conclusion_elements) == 0):
            conclusion_elements = set()
        else:
            conclusion_elements = conclusion_elements.split(',')
        if(conclusion_set1 == set_name1 and conclusion_set2 == set_name2):
            set_intersection = set(elements1) & set(elements2)
            return set_intersection == set(conclusion_elements)
        elif(conclusion_set1 == set_name2 and conclusion_set1 == set_name2):
            set_intersection = set(elements2) & set(elements1)
            return set_intersection == set(conclusion_elements)
        else:
            return False
    else:
        return False

# TODO: Currently sub_rule only works with 1 substitution every time, starting from the left of the string, with no parentheses
def sub_rule(knowns: List[Proposition], conclusion: Proposition) -> bool:
    r = re.compile(r"^(.*)=(.*)$")
    conclusion_eq = r.findall(conclusion.text)[0]
    conclusion_eq = [str(conclusion_eq[0]).strip(),str(conclusion_eq[1]).strip()]
    if(conclusion_eq[0] == conclusion_eq[1]):
        return True
    elif(len(knowns) == 2):
        known1, known2 = r.findall(knowns[0].text)[0], r.findall(knowns[1].text)[0]
        known1, known2 = [str(known1[0]).strip(),str(known1[1]).strip()], [str(known2[0]).strip(),str(known2[1]).strip()]
        known = [known1, known2]
        for i in range(2):
            for j in range(2):
                sub1 = known[i][j].replace(known[(i+1)%2][0],known[(i+1)%2][1],1)
                sub2 = known[i][j].replace(known[(i+1)%2][1],known[(i+1)%2][0],1)
                if((sub1 == conclusion_eq[0] and known[i][(j+1)%2] == conclusion_eq[1])
                or (sub1 == conclusion_eq[1] and known[i][(j+1)%2] == conclusion_eq[0])
                or (sub2 == conclusion_eq[0] and known[i][(j+1)%2] == conclusion_eq[1])
                or (sub2 == conclusion_eq[1] and known[i][(j+1)%2] == conclusion_eq[0])):
                    return True
    else:
        return False

global_rules = [Rule("Set",set_def_rule), Rule("A\B",set_diff_rule) , Rule("A union B",set_union_rule), Rule("A intersection B",set_intersection_rule) , Rule("= Sub",sub_rule)]