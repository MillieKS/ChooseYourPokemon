# ChooseYourPokemon/tests/unit/test_game.py

from game.game import TopTrumps
from unittest.mock import patch
import pytest

def test_successful_greeting(capsys):
    with patch("builtins.input", side_effect=["John", "yes"]):
        game = TopTrumps()
        game.greet_player()
        captured = capsys.readouterr()
        assert "Let's go!" in captured.out

def test_empty_name(capsys):
    with patch("builtins.input", side_effect=["", "John", "yes"]):
        game = TopTrumps()
        game.greet_player()
        captured = capsys.readouterr()
        assert "You need to enter a name." in captured.out
        assert "Let's go!" in captured.out

def test_maximum_retries(capsys):
    with patch("builtins.input", side_effect=["", "", "", "", "", "yes"]):
        game = TopTrumps()
        game.greet_player()
        captured = capsys.readouterr()
        assert "Maximum number of retries reached. Exiting." in captured.out

def test_not_ready(capsys):
    with patch("builtins.input", side_effect=["John", "no", "no", "yes"]):
        game = TopTrumps()
        game.greet_player()
        captured = capsys.readouterr()
        assert "Not ready. Let's ask again." in captured.out
        assert "Let's go!" in captured.out
