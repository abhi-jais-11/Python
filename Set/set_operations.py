one={1,2,3,4}
two={3,4,5,6}
three={1,2}

'''





'''


#union() Returns the union of sets in a new set
print(f"Union of the set is:{one.union(two)}")

#intersection() Returns the intersection of two sets as a new set
print(f"Intersection of the set is:{one.intersection(two)}")

#difference() Returns the difference of two or more sets as a new set
print(f"Difference of the set is:{one.difference(two)}")


#issubset() Returns True if another set contains this set
print(f"This is subset of the set or not: {three.issubset(one)}")



#issuperset() Returns True if this set contains another set
print(f"This is superset of the set or not: {two.issuperset(three)}")


#isdisjoint() Returns True if two sets have a null intersection

print(f"This is disjoint of the set or not: {two.isdisjoint(three)}")


#symmetric_difference() Returns the symmetric difference of two sets as a new set

print(f"Symmentric Difference of the set is:{one.symmetric_difference(two)}")