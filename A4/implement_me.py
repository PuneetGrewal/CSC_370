# Implementation of B+-tree functionality.

from index import *

# You should implement all of the static functions declared
# in the ImplementMe class and submit this (and only this!) file.
class ImplementMe:

    # Returns a B+-tree obtained by inserting a key into a pre-existing
    # B+-tree index if the key is not already there. If it already exists,
    # the return value is equivalent to the original, input tree.
    #
    # Complexity: Guaranteed to be asymptotically linear in the height of the tree
    # Because the tree is balanced, it is also asymptotically logarithmic in the
    # number of keys that already exist in the index.
    @staticmethod
    def InsertIntoIndex( index, key ):

        try:
            for i in range(100):

                if key == index.nodes[i].keys.keys[0] or key == index.nodes[i].keys.keys[1]:
                    return index

                if index.nodes[i].keys.keys[1] == -1:
                    index.nodes[i] = Node(KeySet((index.nodes[i].keys.keys[0], key)), PointerSet((0,0,0)))
                    return index

                if index.nodes[i].keys.keys[0] != -1 and index.nodes[i].keys.keys[1] != -1:

                    if key < index.nodes[i].keys.keys[1]:

                        if key < index.nodes[i].keys.keys[0]:

                            temp1 = (index.nodes[i].keys.keys[0])
                            temp2 = (index.nodes[i].keys.keys[1])

                            index = Index([Node()]*4)

                            index.nodes[0] = Node(KeySet((temp1,-1)), PointerSet((1,2,0)))
                            index.nodes[1] = Node(KeySet((key,-1)), PointerSet((0,0,2)))
                            index.nodes[2] = Node(KeySet((temp1,temp2)), PointerSet((0,0,0)))
                            return index


                        if key > index.nodes[i].keys.keys[0]:

                            temp1 = (index.nodes[i].keys.keys[0])
                            temp2 = (index.nodes[i].keys.keys[1])

                            index = Index([Node()]*4)

                            index.nodes[0] = Node(KeySet((temp1,-1)), PointerSet((1,2,0)))
                            index.nodes[1] = Node(KeySet((temp2,-1)), PointerSet((0,0,2)))
                            index.nodes[2] = Node(KeySet((temp1,key)), PointerSet((0,0,0)))
                            return index



# If the index is empty, initialize it

        except IndexError:

            index = Index([Node()]*1)
            index.nodes[0] = Node(KeySet((key,-1)), PointerSet((0,0,0)))
            return index

        return index

    # Returns a boolean that indicates whether a given key
    # is found among the leaves of a B+-tree index.
    #
    # Complexity: Guaranteed not to touch more nodes than the
    # height of the tree
    @staticmethod
    def LookupKeyInIndex( index, key ):

        try:
            for i in range(100):

                if (index.nodes[i].keys.keys[0] != -1) and (index.nodes[i].keys.keys[1] != -1):

                    if key == index.nodes[i].keys.keys[0] or key == index.nodes[i].keys.keys[1]:
                        return True

                else:

                     if key == index.nodes[i].keys.keys[0] or key == index.nodes[i].keys.keys[1]:
                        return True

        except IndexError:
            return False




    # Returns a list of keys in a B+-tree index within the half-open
    # interval [lower_bound, upper_bound)
    #
    # Complexity: Guaranteed not to touch more nodes than the height
    # of the tree and the number of leaves overlapping the interval.
    @staticmethod
    def RangeSearchInIndex( index, lower_bound, upper_bound ):

        temp = []

        try:
            for i in range(100):

                if index.nodes[i].keys.keys[0] >= lower_bound and index.nodes[i].keys.keys[0] < upper_bound:
                    temp.append(index.nodes[i].keys.keys[0])

                if index.nodes[i].keys.keys[1] >= lower_bound and index.nodes[i].keys.keys[1] < upper_bound:
                    temp.append(index.nodes[i].keys.keys[1])

        except IndexError:
            final = list(set(temp))
            try:
                final.remove(-1)
            except ValueError:
                pass
            final.sort()
            return final
