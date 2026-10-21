from datetime import datetime

from django.shortcuts import render, get_object_or_404

from books.models import Book


def books_view(request, pub_date=None):
    template = 'books/books_list.html'

    if pub_date:
        # pub_date приходит как datetime через DateConverter
        books = Book.objects.filter(pub_date=pub_date)

        # Получаем все уникальные даты
        dates = Book.objects.values_list('pub_date', flat=True).distinct().order_by('pub_date')

        # Определяем предыдущую и следующую даты
        prev_date = None
        for date in dates:
            if date < pub_date.date():
                prev_date = date
            else:
                break

        next_date = None
        for date in reversed(dates):
            if date > pub_date.date():
                next_date = date
            else:
                break

        context = {
            'books': books,
            'prev_date': prev_date,
            'next_date': next_date,
        }
    else:
        # Все книги, сортировка по дате (от новых к старым)
        books = Book.objects.all().order_by('-pub_date')
        context = {'books': books}

    return render(request, template, context)
