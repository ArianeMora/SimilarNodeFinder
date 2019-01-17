import unittest
from tree_object import TreeObject
from tree_controller import TreeController

class TestStringMethods(unittest.TestCase):

    def test_same_tree(self):
        t1 = TreeObject("/Users/ariane/PycharmProjects/SimilarNodeFinder/data/0_10_dhad_28102018.nwk")
        t2 = TreeObject("/Users/ariane/PycharmProjects/SimilarNodeFinder/data/0_10_dhad_28102018.nwk")

        tc = TreeController()
        node_macthing = tc.get_similar_nodes_between_trees(t1, t2, True)

        for label_original, label_match in node_macthing.items():
            self.assertEqual(label_match.get_label(), label_original)


    def test_not_same_tree(self):
        t1 = TreeObject("/Users/ariane/PycharmProjects/SimilarNodeFinder/data/0_10_dhad_28102018.nwk")
        t2 = TreeObject("/Users/ariane/PycharmProjects/SimilarNodeFinder/data/20_40_dhad_28102018.nwk")

        tc = TreeController()
        node_macthing = tc.get_similar_nodes_between_trees(t1, t2, True)

        self.assertEqual(node_macthing["N0"].get_label(), "N0")
        self.assertEqual(node_macthing["N35_0.126"].get_label(), "N26_0.907")
        self.assertEqual(node_macthing["N16_0.993"].get_label(), "N16_0.993")
        self.assertEqual(node_macthing["N3"].get_label(), "N1_0.749")


if __name__ == '__main__':
    unittest.main()