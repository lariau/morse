# tests/test_game.py
import unittest
from morse import Morse

class TestMorse(unittest.TestCase):
    def test_empty_message(self):
        self.assertEqual(Morse().decode(""), "")

    def test_a(self):
        self.assertEqual(Morse().decode(".-"), "A")

    def test_b(self):
        self.assertEqual(Morse().decode("-..."), "B")

    def test_c(self):
        self.assertEqual(Morse().decode("-.-."), "C")

    def test_d(self):
        self.assertEqual(Morse().decode("-.."), "D")

    def test_e(self):
        self.assertEqual(Morse().decode("."), "E")

    def test_f(self):
        self.assertEqual(Morse().decode("..-."), "F")

    def test_g(self):
        self.assertEqual(Morse().decode("--."), "G")

    def test_h(self):
        self.assertEqual(Morse().decode("...."), "H")

    def test_i(self):
        self.assertEqual(Morse().decode(".."), "I")

    def test_j(self):
        self.assertEqual(Morse().decode(".---"), "J")

    def test_k(self):
        self.assertEqual(Morse().decode("-.-"), "K")

    def test_l(self):
        self.assertEqual(Morse().decode(".-.."), "L")

    def test_m(self):
        self.assertEqual(Morse().decode("--"), "M")

    def test_n(self):
        self.assertEqual(Morse().decode("-."), "N")

    def test_o(self):
        self.assertEqual(Morse().decode("---"), "O")

    def test_p(self):
        self.assertEqual(Morse().decode(".--."), "P")

    def test_q(self):
        self.assertEqual(Morse().decode("--.-"), "Q")

    def test_r(self):
        self.assertEqual(Morse().decode(".-."), "R")

    def test_s(self):
        self.assertEqual(Morse().decode("..."), "S")

    def test_t(self):
        self.assertEqual(Morse().decode("-"), "T")

    def test_u(self):
        self.assertEqual(Morse().decode("..-"), "U")

    def test_v(self):
        self.assertEqual(Morse().decode("...-"), "V")

    def test_w(self):
        self.assertEqual(Morse().decode(".--"), "W")

    def test_x(self):
        self.assertEqual(Morse().decode("-..-"), "X")

    def test_y(self):
        self.assertEqual(Morse().decode("-.--"), "Y")

    def test_z(self):
        self.assertEqual(Morse().decode("--.."), "Z")

    def test_sos(self):
        self.assertEqual(Morse().decode("... --- ..."), "SOS")

    def test_whole_sentence(self):
        message = Morse().decode(".- .-.. .-.. / -.-- --- ..- / -. . . -.. / .. ... / -.-. --- -.. .")
        self.assertEqual(message, "ALL YOU NEED IS CODE")

    # NOTE: we will add a test for *sentences* later
