from django.shortcuts import render
from .models import Board

# Create your views here.
def home(request):
    boards = Board.objects.all()
    # boards_names = list()

    # for board in boards:
    #     boards_names.append(board.name)

    # response_html = '<br>'.join(boards_names)

    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
