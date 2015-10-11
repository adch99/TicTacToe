except ImportError:
	from distutils.core import setup
config = {
	'description': 'A game of Tic-Tac-Toe',
	'author': 'Aditya',
	'url': 'url to get it at',
	'download_url': 'Where to download it',
	'author_email': 'adityachincholi@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['TicTacToe'],
	'scripts': ['game.py','player.py',"main.py"],
	'name': 'TicTacToe'
}

setup(**config)
