from models.player import Player
from models.tournament import Tournament


class HomeMenuView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        """Print each key - entry of menu.items()"""
        for key, entry in self.menu.items():
            print(f"{key} : {entry.option}")

    def get_user_choice(self):
        """Return user choice of menu."""
        while True:
            self._display_menu()
            choice = input(">>")
            if choice in self.menu:
                return self.menu[choice]


class CreatePlayerView:
    def get_player_informations(self, key):
        """Return user's inputs as value for key."""
        value = input(f"{key} ?")
        return value

    def confirm_fields(self, fields):
        """Return True if user confirms informations - False if not."""
        for field in fields:
            print(field)
        confirm = input("Confirm new player y/n ?")
        if confirm == "y":
            return True
        else:
            print("Creation of new player cancelled")
            return False

    def player_saved(self, player):
        """Print confirmation of saving profil of a player in database."""
        print(
            f"Profil de {player.firstname.capitalize()} sauvegardé - ID : {player.id}"
        )

    def invalid_value(self):
        """Inform user that input is a not in a valid format."""
        print(f"Value invalid - Please respect format")


class CreateTournamentView:
    def get_tournament_informations(self, key):
        """Return user's inputs as value for key."""
        value = input(f"{key} ?")
        return value

    def confirm_fields(self, fields):
        """Return True if user confirms informations - False if not."""
        for field in fields:
            print(field)
        confirm = input("Confirm new tournament y/n ?")
        if confirm == "y":
            return True
        else:
            print("Creation of new tournament cancelled")
            return False

    def add_player_to_tournament(self):
        """Return player's id gave by user."""
        player_id = input("Player ID ?")
        return player_id

    def new_tournament_created(self, new_tournament):
        """Print confirmation of saving tournament in database."""
        print(
            f"{new_tournament.name} is now saved in database - ID = {new_tournament.id}"
        )

    def invalid_value(self):
        """Inform user that input is a not in a valid format."""
        print(f"Value invalid - Please respect format")


class PlayTournamentView:
    def get_tournament(self):
        """Return Id of tournament to be played gaved by user."""
        return input("ID of tournament to be played ?")

    def present_matches(self, round):
        """Print matches of round."""
        print(f"Matches round n°{round.number}")
        for match in round.matches:
            print(match)
        print("\n")

    def play_match(self, match):
        """Return input of user 0 or 1 or 2."""
        winner = input(
            f"Who is the winner : 1- {match.player_1.firstname} | 2 - {match.player_2.firstname} | 0 - Draw ?"
        )
        while int(winner) not in [0, 1, 2]:
            print(f"Value invalid - Please respect format")
            winner = input(
                f"Who is the winner : 1- {match.player_1.firstname} | 2 - {match.player_2.firstname} | 0 - Draw ?"
            )
        return int(winner)

    def update_classment(self, players):
        """Print each player of players."""
        print(f"\nClassement actuel :")
        for player in players:
            print(
                f"{player.firstname.capitalize()} avec {player.tournament_point} points - Ranking = {player.ranking}"
            )
        print("\n")

    def waiting_screen(self):
        """Waiting screen."""
        input(
            "--- Waiting screen --- Press ENTER to finish Round and update scores --- Waiting screen ---"
        )

    def get_new_ranking(self, player):
    	"""Return new ranking of player."""
    	print(f"{player.firstname.capitalize()} {player.lastname.capitalize()}")
    	print(f"Player ID : {player.id}")
    	print(f"Actual ranking : {player.ranking}")
    	new_rank = input (f"New rank ? >>")
    	return new_rank

class UpdateRankingView:
	pass
