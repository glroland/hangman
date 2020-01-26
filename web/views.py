from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from .forms import NewGameForm
import urllib
from .game_factory import GameFactory
from .hangman_game import HangmanGame
from .difficulty_profiles import EasyDifficultyProfile
from .difficulty_profiles import MediumDifficultyProfile
from .difficulty_profiles import HardDifficultyProfile

def index(request):
    context = {}

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

    #return render(request, 'web/templates/index.html', context)

def game(request):
    if not request.session.get('game', None):
        return redirect(reverse('new_game'))
    game = request.session['game']

    if request.method == 'POST':
        if 'letter_A' in request.POST:
            game.guessLetter("A")
        if 'letter_B' in request.POST:
            game.guessLetter("B")
        if 'letter_C' in request.POST:
            game.guessLetter("C")
        if 'letter_D' in request.POST:
            game.guessLetter("D")
        if 'letter_E' in request.POST:
            game.guessLetter("E")
        if 'letter_F' in request.POST:
            game.guessLetter("F")
        if 'letter_G' in request.POST:
            game.guessLetter("G")
        if 'letter_H' in request.POST:
            game.guessLetter("H")
        if 'letter_I' in request.POST:
            game.guessLetter("I")
        if 'letter_J' in request.POST:
            game.guessLetter("J")
        if 'letter_K' in request.POST:
            game.guessLetter("K")
        if 'letter_L' in request.POST:
            game.guessLetter("L")
        if 'letter_M' in request.POST:
            game.guessLetter("M")
        if 'letter_N' in request.POST:
            game.guessLetter("N")
        if 'letter_O' in request.POST:
            game.guessLetter("O")
        if 'letter_P' in request.POST:
            game.guessLetter("P")
        if 'letter_Q' in request.POST:
            game.guessLetter("Q")
        if 'letter_R' in request.POST:
            game.guessLetter("R")
        if 'letter_S' in request.POST:
            game.guessLetter("S")
        if 'letter_T' in request.POST:
            game.guessLetter("T")
        if 'letter_U' in request.POST:
            game.guessLetter("U")
        if 'letter_V' in request.POST:
            game.guessLetter("V")
        if 'letter_W' in request.POST:
            game.guessLetter("W")
        if 'letter_X' in request.POST:
            game.guessLetter("X")
        if 'letter_Y' in request.POST:
            game.guessLetter("Y")
        if 'letter_Z' in request.POST:
            game.guessLetter("Z")

    context = {
        'solution': game.solution,
        'gameBoard': game.getGameBoardAsString(),
        'incorrectGuessCounter': str(game.incorrectGuessCounter)
    }

    request.session.modified = True
    template = loader.get_template('game.html')
    return HttpResponse(template.render(context, request))

def new_game(request):
    if request.method == 'POST':
        form = NewGameForm(request.POST)
        if form.is_valid():
            difficultyProfile = MediumDifficultyProfile()
            if form.getDifficultyLevel() == "Easy":
                difficultyProfile = EasyDifficultyProfile()
            elif form.getDifficultyLevel() == "Hard":
                difficultyProfile = HardDifficultyProfile()
            game = GameFactory.createGame(difficultyProfile)
            request.session['game'] = game
            return redirect(reverse('game'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewGameForm()
        request.session['game'] = {}
        request.session.modified = True

    return render(request, 'new_game.html', {'form': form})


