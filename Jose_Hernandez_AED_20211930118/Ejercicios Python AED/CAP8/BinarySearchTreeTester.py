class BinarySearchTreeTester:
    def test_bst(self):
        t = BinarySearchTree()
        for x in [4, 2, 6, 1, 3, 5, 7]:
            t.add(x)
        assert 4 in t
        assert 2 in t
        assert 5 in t
        assert len(t) == 7
        assert sorted(list(t)) == [1, 2, 3, 4, 5, 6, 7]
        t.delete(2)
        assert 2 not in t
        assert len(t) == 6
        assert sorted(list(t)) == [1, 3, 4, 5, 6, 7]
        t.delete(4)
        assert 4 not in t
        assert len(t) == 5
        assert sorted(list(t)) == [1, 3, 5, 6, 7]
        t.add(0)
        assert 0 in t
        assert len(t) == 6
        assert sorted(list(t)) == [0, 1, 3, 5, 6, 7]
        t.delete(5)
        assert 5 not in t
        assert len(t) == 5
        assert sorted(list(t)) == [0, 1, 3, 6, 7]

    def run_tests(self):
        self.test_bst()
        print('All tests passed.')
