except ImportError:
	from distutils.core import setup
config = {
	'description': 'A game of Tic-Tac-Toe',
	'author': 'Aditya Chincholi',
	'url': 'https://github.com/adch99/TicTacToe.git',
	'download_url': 'Where to download it',
	'author_email': 'adityachincholi@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['TicTacToe'],
	'scripts': ['engine.py', 'player.py', "Comp.py", "main.py", "Compmain.py"],
	'name': 'TicTacToe'
}

setup(**config)
