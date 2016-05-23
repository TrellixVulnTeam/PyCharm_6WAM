"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       return isinstance(self, int)


   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       if self.isInteger():
           return self
       else:
           return None

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       if self.isInteger():
           return None
       else:
           return self


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nested_list = nestedList
        self.nl_len = len(nestedList)
        self.cursor = 0

    def next(self):
        """
        :rtype: int
        """
        self.cursor += 1
        if self.nested_list.isInteger():
            return self.nested_list.getInteger()
        else:
            new_nested_list = self.nested_list.getList()
            return new_nested_list.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cursor == self.nl_len:
            return False
        else:
            return True


i, v = NestedIterator([1, 2]), []
while i.hasNext():
    v.append(i.next())
print(v)
