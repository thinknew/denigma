import os
import fileinput

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.db import connection
from django.db.models import Q

from data import get
from data.filters import TableFilter
from utils import is_int

from models import Interaction
from tables import InteractionTable
from filters import InteractionFilterSet
from integrator import main


def index(request, template='interactions/index.html'):
    entry = get("Interactions")
    return render(request, template, {'entry': entry})


class InteractionList(TableFilter):
    model = Interaction
    table_class = InteractionTable
    queryset = Interaction.objects.all()
    success_url = '/interactions/table/'

    def get_queryset(self):
        qs = self.queryset
        if InteractionList.query:
            terms = InteractionList.query.split(None)
            for term in terms:
                if is_int(term):
                    qs = qs.filter(Q(id_a=term) | Q(id_b=term))
                else:
                    qs = qs.filter(Q(alias_a__icontains=term) |
                                   Q(alias_b__icontains=term))
        self.filterset = InteractionFilterSet(qs, self.request.GET)
        return self.filterset.qs




def update(request, db="BioGRID"):
    exec("from %s import main" % db)
    main()
    return redirect('/interactions/')

def integrator(request, memory=True, header=False):

    main(memory=memory, header=header)
    pathToFile = os.path.join(settings.PROJECT_ROOT, 'apps', 'interactions', 'merged.txt')
    fields = ('id_a', 'id_b',
              'alias_a', 'alias_b',
              'system', 'type', 'method', 'modification',
              'taxid_a', 'taxid_b',
              'pmid', 'source', 'score')

    # Raw sql triggered direct insertion of the file:
    sql = "load data infile '%s' into table %s_%s columns terminated by '\t'"\
     "lines terminated by '\n'(%s);"\
          % (pathToFile,'interactions','interaction'"", ", ".join(fields))


#234567891123456789212345678931234567894123456789512345678961234567897123456789

    cursor = connection.cursor()
    cursor.execute('TRUNCATE TABLE interactions_interaction;')
    cursor.execute(sql)
    #row = cursor.fetchone()
    #print row

    print sql
    query = Interaction.objects.raw(sql)
    #    print query


    # Reading and inserting via Django ORM (works, but is too slow):
#    f = fileinput.input(os.path.join(settings.PROJECT_ROOT, 'apps', 'interactions', 'merged.txt'))
#    interactions = []
#    for line in f:
#        if header:
#            header = False
#            continue
#        values = line.replace('\n', '').split('\t')
#        #print values
#        input = dict(zip(fields, values))
#        interaction = Interaction()
#        interaction.__dict__.update(input)
#        #interaction.save()
#        interactions.append(interaction)
#    f.close()
#    Interaction.objects.bulk_create(interactions)





     # Alternative direct insertion via python-MySQLdb:
#    import MySQLdb as mysql
#    mydb = mysql.connect(user='root', db='denigma')
#    cursor = mydb.cursor()
#    handle = cursor.execute(sql)
#    print handle

    msg = "Successfully integrated interactions"
    messages.add_message(request, messages.SUCCESS, msg)
    return redirect('/interactions/')
#234567891123456789212345678931234567893