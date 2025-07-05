import unittest
from datetime import date
from Dijkstra import JKUMap

maxPoints = 12.0  # defines the maximum achievable points for the example tested here
points = maxPoints  # stores the actually achieved points based on failed unit tests


class TestAssignment04Student(unittest.TestCase):
    undirected_graph_flag = True

    def setUp(self):
        pass

    def test_map_construction(self):
        warning = " MAKE SURE TO FIX THIS, OTHERWISE ALL OTHER TESTS CANNOT WORK!"
        jku_map = JKUMap()
        self.assertEqual(17, jku_map.get_number_of_nodes(),
                         ".get_number_of_vertices() did return a wrong count." + warning)
        self.assertIsNotNone(jku_map.find("SP3"), ".find() did not find SP3." + warning)
        self.assertIsNotNone(jku_map.find("SP1"), ".find() did not find SP1." + warning)
        self.assertIsNotNone(jku_map.find("Parking"), ".find() did not find Parking." + warning)
        self.assertIsNotNone(jku_map.find("LUI"), ".find() did not find LUI." + warning)
        self.assertIsNotNone(jku_map.find("Teichwerk"), ".find() did not find Teichwerk." + warning)
        self.assertIsNotNone(jku_map.find("Bella Casa"), ".find() did not find Bella Casa." + warning)
        self.assertIsNotNone(jku_map.find("Chat"), ".find() did not find Chat." + warning)
        self.assertIsNotNone(jku_map.find("Library"), ".find() did not find Library." + warning)
        self.assertIsNotNone(jku_map.find("Bank"), ".find() did not find Bank." + warning)
        self.assertIsNotNone(jku_map.find("KHG"), ".find() did not find SP3." + warning)
        self.assertIsNotNone(jku_map.find("Spar"), ".find() did not find Spar." + warning)
        self.assertIsNotNone(jku_map.find("Porter"), ".find() did not find Porter." + warning)
        self.assertIsNotNone(jku_map.find("Open Lab"), ".find() did not find Open Lab." + warning)
        self.assertIsNotNone(jku_map.find("LIT"), ".find() did not find LIT." + warning)
        self.assertIsNotNone(jku_map.find("Castle"), ".find() did not find Castle." + warning)
        self.assertIsNotNone(jku_map.find("Papaya"), ".find() did not find Papaya." + warning)
        self.assertIsNotNone(jku_map.find("JKH"), ".find() did not find JHK." + warning)

        self.assertEqual(19, jku_map.get_number_of_edges(),
                         ".get_number_of_edges() did return a wrong count." + warning)

        self.assertIsNotNone(jku_map.find_edge("SP1", "SP3"),
                             ".find_edge() did not find edge between SP1 and SP3." + warning)
        self.assertIsNotNone(jku_map.find_edge("SP3", "SP1"),
                             ".find_edge() did not find edge between SP3 and SP1." + warning)
        self.assertEqual(130, jku_map.find_edge("SP3", "SP1").weight,
                         ".find_edge() returned wrong edge weight for edge between SP3 and SP1." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("SP1", "LUI"),
                             ".find_edge() did not find edge between SP1 and LUI." + warning)
        self.assertIsNotNone(jku_map.find_edge("LUI", "SP1"),
                             ".find_edge() did not find edge between LUI and SP1." + warning)
        self.assertEqual(175, jku_map.find_edge("LUI", "SP1").weight,
                         ".find_edge() returned wrong edge weight for edge between LUI and SP1." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("SP1", "Parking"),
                             ".find_edge() did not find edge between SP1 and Parking." + warning)
        self.assertIsNotNone(jku_map.find_edge("Parking", "SP1"),
                             ".find_edge() did not find edge between Parking and SP1." + warning)
        self.assertEqual(240, jku_map.find_edge("Parking", "SP1").weight,
                         ".find_edge() returned wrong edge weight for edge between Parking and SP1." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("Bella Casa", "Parking"),
                             ".find_edge() did not find edge between Bella Casa and Parking." + warning)
        self.assertIsNotNone(jku_map.find_edge("Parking", "Bella Casa"),
                             ".find_edge() did not find edge between Parking and Bella Casa." + warning)
        self.assertEqual(145, jku_map.find_edge("Parking", "Bella Casa").weight,
                         ".find_edge() returned wrong edge weight for edge between Parking and Bella "
                         "Casa." + warning)

        self.assertIsNotNone(jku_map.find_edge("KHG", "Parking"),
                             ".find_edge() did not find edge between KHG and Parking." + warning)
        self.assertIsNotNone(jku_map.find_edge("Parking", "KHG"),
                             ".find_edge() did not find edge between Parking and KHG." + warning)
        self.assertEqual(190, jku_map.find_edge("Parking", "KHG").weight,
                         ".find_edge() returned wrong edge weight for edge between Parking and KHG." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("KHG", "Spar"),
                             ".find_edge() did not find edge between KHG and Spar." + warning)
        self.assertIsNotNone(jku_map.find_edge("Spar", "KHG"),
                             ".find_edge() did not find edge between Spar and KHG." + warning)
        self.assertEqual(165, jku_map.find_edge("Spar", "KHG").weight,
                         ".find_edge() returned wrong edge weight for edge between Spar and KHG." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("KHG", "Bank"),
                             ".find_edge() did not find edge between KHG and Bank." + warning)
        self.assertIsNotNone(jku_map.find_edge("Bank", "KHG"),
                             ".find_edge() did not find edge between Bank and KHG." + warning)
        self.assertEqual(150, jku_map.find_edge("Bank", "KHG").weight,
                         ".find_edge() returned wrong edge weight for edge between Bank and KHG." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("Porter", "Spar"),
                             ".find_edge() did not find edge between Porter and Spar." + warning)
        self.assertIsNotNone(jku_map.find_edge("Spar", "Porter"),
                             ".find_edge() did not find edge between Spar and Porter." + warning)
        self.assertEqual(103, jku_map.find_edge("Spar", "Porter").weight,
                         ".find_edge() returned wrong edge weight for edge between Spar and Porter." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("LIT", "Spar"),
                             ".find_edge() did not find edge between LIT and Spar." + warning)
        self.assertIsNotNone(jku_map.find_edge("Spar", "LIT"),
                             ".find_edge() did not find edge between Spar and LIT." + warning)
        self.assertEqual(50, jku_map.find_edge("Spar", "LIT").weight,
                         ".find_edge() returned wrong edge weight for edge between Spar and LIT." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("LIT", "Porter"),
                             ".find_edge() did not find edge between LIT and Porter." + warning)
        self.assertIsNotNone(jku_map.find_edge("Porter", "LIT"),
                             ".find_edge() did not find edge between Porter and LIT." + warning)
        self.assertEqual(80, jku_map.find_edge("Porter", "LIT").weight,
                         ".find_edge() returned wrong edge weight for edge between Porter and LIT." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("Open Lab", "Porter"),
                             ".find_edge() did not find edge between Open Lab and Porter." + warning)
        self.assertIsNotNone(jku_map.find_edge("Porter", "Open Lab"),
                             ".find_edge() did not find edge between Porter and Open Lab." + warning)
        self.assertEqual(70, jku_map.find_edge("Porter", "Open Lab").weight,
                         ".find_edge() returned wrong edge weight for edge between Porter and Open "
                         "Lab. " + warning)

        self.assertIsNotNone(jku_map.find_edge("Bank", "Porter"),
                             ".find_edge() did not find edge between Bank and Porter." + warning)
        self.assertIsNotNone(jku_map.find_edge("Porter", "Bank"),
                             ".find_edge() did not find edge between Porter and Bank." + warning)
        self.assertEqual(100, jku_map.find_edge("Porter", "Bank").weight,
                         ".find_edge() returned wrong edge weight for edge between Porter and Bank." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("Bank", "Chat"),
                             ".find_edge() did not find edge between Bank and Chat." + warning)
        self.assertIsNotNone(jku_map.find_edge("Chat", "Bank"),
                             ".find_edge() did not find edge between Chat and Bank." + warning)
        self.assertEqual(115, jku_map.find_edge("Chat", "Bank").weight,
                         ".find_edge() returned wrong edge weight for edge between Chat and Bank." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("Library", "Chat"),
                             ".find_edge() did not find edge between Library and Chat." + warning)
        self.assertIsNotNone(jku_map.find_edge("Chat", "Library"),
                             ".find_edge() did not find edge between Chat and Library." + warning)
        self.assertEqual(160, jku_map.find_edge("Chat", "Library").weight,
                         ".find_edge() returned wrong edge weight for edge between Chat and Library." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("LUI", "Chat"),
                             ".find_edge() did not find edge between LUI and Chat." + warning)
        self.assertIsNotNone(jku_map.find_edge("Chat", "LUI"),
                             ".find_edge() did not find edge between Chat and LUI." + warning)
        self.assertEqual(240, jku_map.find_edge("Chat", "LUI").weight,
                         ".find_edge() returned wrong edge weight for edge between Chat and LUI." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("Library", "LUI"),
                             ".find_edge() did not find edge between Library and LUI." + warning)
        self.assertIsNotNone(jku_map.find_edge("LUI", "Library"),
                             ".find_edge() did not find edge between LUI and Library." + warning)
        self.assertEqual(90, jku_map.find_edge("LUI", "Library").weight,
                         ".find_edge() returned wrong edge weight for edge between LUI and Library." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("Teichwerk", "LUI"),
                             ".find_edge() did not find edge between Teichwerk and LUI." + warning)
        self.assertIsNotNone(jku_map.find_edge("LUI", "Teichwerk"),
                             ".find_edge() did not find edge between LUI and Teichwerk." + warning)
        self.assertEqual(135, jku_map.find_edge("LUI", "Teichwerk").weight,
                         ".find_edge() returned wrong edge weight for edge between LUI and Teichwerk." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("Castle", "Papaya"),
                             ".find_edge() did not find edge between Castle and Papaya." + warning)
        self.assertIsNotNone(jku_map.find_edge("Papaya", "Castle"),
                             ".find_edge() did not find edge between Papaya and Castle." + warning)
        self.assertEqual(85, jku_map.find_edge("Papaya", "Castle").weight,
                         ".find_edge() returned wrong edge weight for edge between Papaya and Castle." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge("JKH", "Papaya"),
                             ".find_edge() did not find edge between JKH and Papaya." + warning)
        self.assertIsNotNone(jku_map.find_edge("Papaya", "JKH"),
                             ".find_edge() did not find edge between Papaya and JKH." + warning)
        self.assertEqual(80, jku_map.find_edge("Papaya", "JKH").weight,
                         ".find_edge() returned wrong edge weight for edge between Papaya and JKH." +
                         warning)

    def test_non_existing_shortest_path_from_JKH_to_KHG(self):
        jku_map = JKUMap()
        path = jku_map.get_shortest_path(jku_map.find("JKH"), jku_map.find("KHG"))
        self.assertIsNone(path,
                          ".get_shortest_path() did not return None for a non-existing way from JKH to KHG")

    def test_non_existing_shortest_path_from_KHG_to_JKH(self):
        jku_map = JKUMap()
        path = jku_map.get_shortest_path(jku_map.find("KHG"), jku_map.find("JKH"))
        self.assertIsNone(path,
                          ".get_shortest_path() did not return None for a non-existing way from KHG to JKH")

    def test_existing_shortest_path_from_castle_to_papaya(self):
        jku_map = JKUMap()
        path = jku_map.get_shortest_path(jku_map.find("Castle"), jku_map.find("Papaya"))
        self.assertIsNotNone(path,
                             ".get_shortest_path() did return None for an existing way from Castle to Papaya")
        self.assertEqual("Castle", path[0].point.name)
        self.assertEqual(0, path[0].covered_distance)
        self.assertEqual("Papaya", path[1].point.name)
        self.assertEqual(85, path[1].covered_distance)

    def test_existing_shortest_path_from_SP3_to_spar(self):
        jku_map = JKUMap()
        path = jku_map.get_shortest_path(jku_map.find("SP3"), jku_map.find("Spar"))
        self.assertIsNotNone(path, ".get_shortest_path() did return None for an existing way from SP3 to Spar")
        self.assertEqual("SP3", path[0].point.name)
        self.assertEqual(0, path[0].covered_distance)
        self.assertEqual("SP1", path[1].point.name)
        self.assertEqual(130, path[1].covered_distance)
        self.assertEqual("Parking", path[2].point.name)
        self.assertEqual(370, path[2].covered_distance)
        self.assertEqual("KHG", path[3].point.name)
        self.assertEqual(560, path[3].covered_distance)
        self.assertEqual("Spar", path[4].point.name)
        self.assertEqual(725, path[4].covered_distance)

    def test_shortest_distances_from_JKH(self):
        jku_map = JKUMap()
        result = jku_map.get_shortest_distances(jku_map.find("JKH"))
        if result is None:
            self.fail("The function returned None, which is not valid.")
        elif not isinstance(result, (dict)):
            self.fail(f"The function returned an invalid type: {type(result)}")
        self.assertEqual(17, len(result),
                         ".get_shortest_distances() returned a map with a wrong number of entries.")
        self.assertEqual(165, result.get("Castle"),
                         ".get_shortest_distances() did return wrong distance for reachable point")
        self.assertEqual(80, result.get("Papaya"),
                         ".get_shortest_distances() did return wrong distance for reachable point")

        self.assertEqual(0, result.get("JKH"), ".get_shortest_distances() did not return 0 for the start point")

        self.assertEqual(-1, result.get("LUI"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Library"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Chat"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Teichwerk"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("SP1"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("SP3"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Parking"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Bank"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Bella Casa"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("KHG"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Porter"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Spar"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("LIT"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Open Lab"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")

    def test_shortest_distances_from_LUI(self):
        jku_map = JKUMap()
        result = jku_map.get_shortest_distances(jku_map.find("LUI"))
        if result is None:
            self.fail("The function returned None, which is not valid.")
        elif not isinstance(result, (dict)):
            self.fail(f"The function returned an invalid type: {type(result)}")
        self.assertEqual(17, len(result),
                         ".get_shortest_distances() returned a map with a wrong number of entries.")
        self.assertEqual(-1, result.get("Castle"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Papaya"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("JKH"),
                         ".get_shortest_distances() did not return -1 for a non-reachable point")

        self.assertEqual(0, result.get("LUI"), ".get_shortest_distances() did not return 0 for the start point")

        self.assertEqual(90, result.get("Library"),
                         ".get_shortest_distances() did return a wrong distance for a direct neighbor")
        self.assertEqual(240, result.get("Chat"),
                         ".get_shortest_distances() did return a wrong distance for a direct neighbor")
        self.assertEqual(135, result.get("Teichwerk"),
                         ".get_shortest_distances() did return a wrong distance for a direct neighbor")
        self.assertEqual(175, result.get("SP1"),
                         ".get_shortest_distances() did return a wrong distance for a direct neighbor")

        self.assertEqual(305, result.get("SP3"),
                         ".get_shortest_distances() did return a wrong distance for a 2-step reachable point")
        self.assertEqual(415, result.get("Parking"),
                         ".get_shortest_distances() did return a wrong distance for a 2-step reachable point")
        self.assertEqual(355, result.get("Bank"),
                         ".get_shortest_distances() did return a wrong distance for a 2-step reachable point")

        self.assertEqual(560, result.get("Bella Casa"),
                         ".get_shortest_distances() did return a wrong distance for a 3-step reachable point")
        self.assertEqual(505, result.get("KHG"),
                         ".get_shortest_distances() did return a wrong distance for a 3-step reachable point")
        self.assertEqual(455, result.get("Porter"),
                         ".get_shortest_distances() did return a wrong distance for a 3-step reachable point")

        self.assertEqual(558, result.get("Spar"),
                         ".get_shortest_distances() did return a wrong distance for a 4-step reachable point")
        self.assertEqual(535, result.get("LIT"),
                         ".get_shortest_distances() did return a wrong distance for a 4-step reachable point")
        self.assertEqual(525, result.get("Open Lab"),
                         ".get_shortest_distances() did return a wrong distance for a 4-step reachable point")

    def test_shortest_path_from_to_none_parameter(self):
        jku_map = JKUMap()

        with self.assertRaises(ValueError) as cm:
            jku_map.get_shortest_path(None, jku_map.find("LUI"))
        self.assertTrue(isinstance(cm.exception, ValueError), ".get_shortest_path() did not throw an expected "
                                                              "ValueError when None was passed as parameter")

        with self.assertRaises(ValueError) as cm:
            jku_map.get_shortest_path(jku_map.find("LUI"), None)
        self.assertTrue(isinstance(cm.exception, ValueError), ".get_shortest_path() did not throw an expected "
                                                              "ValueError when None was passed as parameter")

        with self.assertRaises(ValueError) as cm:
            jku_map.get_shortest_path(None, None)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".get_shortest_path() did not throw an expected ValueError when None was passed as "
                        "parameter")

    def test_shortest_path_from_to_same_parameter(self):
        jku_map = JKUMap()

        with self.assertRaises(ValueError) as cm:
            jku_map.get_shortest_path(jku_map.find("LUI"), jku_map.find("LUI"))
        self.assertTrue(isinstance(cm.exception, ValueError), ".get_shortest_path() did not throw an expected "
                                                              "ValueError when the same node was passed for both "
                                                              "parameters")

    def test_shortest_distances_from_none_parameter(self):
        jku_map = JKUMap()

        with self.assertRaises(ValueError) as cm:
            jku_map.get_shortest_distances(None)
        self.assertTrue(isinstance(cm.exception, ValueError), ".get_shortest_distances() did not throw an "
                                                              "expected ValueError when None was passed as parameter")

    def test_reachable_castle_to_papaya(self):
        jku_map = JKUMap()
        try:
            self.assertTrue(jku_map.reachable(jku_map.find("Castle"), jku_map.find("Papaya")),
                            ".reachable() did not return true for a reachable point")
        except Exception as ex:
            self.fail("Could not test as an exception has been thrown: " + str(ex))

    def test_reachable_castle_to_lui(self):
        jku_map = JKUMap()
        try:
            self.assertFalse(jku_map.reachable(jku_map.find("Castle"), jku_map.find("LUI")),
                             ".reachable() did not return false for an unreachable point")
        except Exception as ex:
            self.fail("Could not test as an exception has been thrown: " + str(ex))

    def test_reachable_null_parameter(self):
        jku_map = JKUMap()
        try:
            with self.assertRaises(ValueError,
                                   msg=".reachable() did not throw an expected ValueError when None was passed as parameter"):
                jku_map.reachable(jku_map.find("LUI"), None)
            with self.assertRaises(ValueError,
                                   msg=".reachable() did not throw an expected ValueError when None was passed as parameter"):
                jku_map.reachable(None, jku_map.find("LUI"))
        except Exception as ex:
            self.fail("Could not test as an exception has been thrown: " + str(ex))



if __name__ == '__main__':
    unittest.main()
