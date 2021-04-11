from django.test import TestCase
from django.core.management import call_command
from io import StringIO
from main.models import *
from main.management.commands._private import calcAvgRatings
from decimal import Decimal

class AlgoTestCase(TestCase):
    def setUp(self):
        chan1 = Channel.objects.create(title='Childrens', language='en', picture='pic1.png')
        chan2 = Channel.objects.create(title='Movies', language='en', picture='pic1.png')
        chan3 = Channel.objects.create(title='TV Series', language='en', picture='pic1.png')
        chan4 = Channel.objects.create(title='Sports', language='en', picture='pic1.png')
        chan5 = Channel.objects.create(title='Comedy', language='en', picture='pic1.png', parent_channel=chan3)
        chan6 = Channel.objects.create(title='Drama', language='en', picture='pic1.png', parent_channel=chan3)
        chan7 = Channel.objects.create(title='Romantic', language='en', picture='pic1.png', parent_channel=chan3)
        chan8 = Channel.objects.create(title='Thriller', language='en', picture='pic1.png', parent_channel=chan2)
        chan9 = Channel.objects.create(title='SciFi', language='en', picture='pic1.png', parent_channel=chan2)
        chan10 = Channel.objects.create(title='Horror', language='en', picture='pic1.png', parent_channel=chan2)
        chan11 = Channel.objects.create(title='Family Guy', language='en', picture='pic1.png', parent_channel=chan5)
        chan12 = Channel.objects.create(title='South Park', language='en', picture='pic1.png', parent_channel=chan5)
        chan13 = Channel.objects.create(title='The Simpsons', language='en', picture='pic1.png', parent_channel=chan5)
        chan14 = Channel.objects.create(title='SP-Series 1', language='en', picture='pic1.png', parent_channel=chan12)
        chan15 = Channel.objects.create(title='SP-Series 2', language='en', picture='pic1.png', parent_channel=chan12)
        chan16 = Channel.objects.create(title='SP-Series 3', language='en', picture='pic1.png', parent_channel=chan12)

        cont1 = Content.objects.create(name='SP - S1E1', content='SPS1E1.mp4', rating=Decimal(9.0), channel=chan14)  # av 8.5
        cont1.save()
        cont2 = Content.objects.create(name='SP - S1E2', content='SPS1E2.mp4', rating=Decimal(8.0), channel=chan14)
        cont2.save()
        cont3 = Content.objects.create(name='SP - S1E3', content='SPS1E3.mp4', rating=Decimal(9.0), channel=chan14)
        cont3.save()
        cont4 = Content.objects.create(name='SP - S1E4', content='SPS1E4.mp4', rating=Decimal(8.0), channel=chan14)
        cont4.save()
        cont5 = Content(name='FG - S1E1', content='FGS1E1.mp4', rating=Decimal(8.5), channel=chan11)  # av 8.25
        cont5.save()
        cont6 = Content(name='FG - S1E2', content='FGS1E2.mp4', rating=Decimal(8.0), channel=chan11)
        cont6.save()
        cont7 = Content(name='FG - S1E3', content='FGS1E3.mp4', rating=Decimal(8.5), channel=chan11)
        cont7.save()
        cont8 = Content(name='FG - S1E4', content='FGS1E4.mp4', rating=Decimal(8.0), channel=chan11)
        cont8.save()
        cont9 = Content(name='2001', content='2001.mp4', rating=Decimal(9.5), channel=chan9) # av ~9.1
        cont9.save()
        cont10 = Content(name='Blade Runner', content='bladerunner.mp4', rating=Decimal(9.2), channel=chan9)
        cont10.save()
        cont11 = Content(name='Star Wars', content='starwars.mp4', rating=Decimal(8.5), channel=chan9)
        cont11.save()
        cont12 = Content(name='Alien', content='alien.mp4', rating=Decimal(9.0), channel=chan9)
        cont12.save()
        cont13 = Content(name='SP - S2E1', content='SPS2E1.mp4', rating=Decimal(9.0), channel=chan15)  # av 9.0
        cont13.save()
        cont14 = Content(name='SP - S2E2', content='SPS2E2.mp4', rating=Decimal(9.0), channel=chan15)
        cont14.save()
        cont15 = Content(name='Ths Shining', content='theshining.mp4', rating=Decimal(9.0), channel=chan10)  # av 8.0
        cont15.save()
        cont16 = Content(name='IT', content='it.mp4', rating=Decimal(7.0), channel=chan10)
        cont16.save()
        cont17 = Content(name='Luther', content='luther.mp4', rating=Decimal(8.5), channel=chan6)  # av 8.8
        cont17.save()
        cont18 = Content(name='Cracker', content='cracker.mp4', rating=Decimal(9.1), channel=chan6)
        cont18.save()
        pass

    def tearDown(self):
        pass


    def test_average_ratings_1(self):
        channel = Channel.objects.get(title__exact='SP-Series 1')
        self.assertEqual(round(calcAvgRatings(channel), 2), round(Decimal(8.50), 2))

    def test_average_ratings_2(self):
        channel = Channel.objects.get(title__exact='SP-Series 2')
        self.assertEqual(round(calcAvgRatings(channel), 2), round(Decimal(9.00), 2))

    def test_average_ratings_3(self):
        channel = Channel.objects.get(title__exact='South Park')
        self.assertEqual(round(calcAvgRatings(channel), 2), round(Decimal(8.67), 2))

    def test_average_ratings_4(self):
        channel = Channel.objects.get(title__exact='Family Guy')
        self.assertEqual(round(calcAvgRatings(channel), 2), round(Decimal(8.25), 2))

    def test_average_ratings_5(self):
        channel = Channel.objects.get(title__exact='SciFi')
        self.assertEqual(round(calcAvgRatings(channel), 2), round(Decimal(9.05), 2))

    def test_average_ratings_6(self):
        channel = Channel.objects.get(title__exact='Horror')
        self.assertEqual(round(calcAvgRatings(channel), 2), round(Decimal(8.00), 2))

    def test_average_ratings_7(self):
        channel = Channel.objects.get(title__exact='Movies')
        self.assertEqual(round(calcAvgRatings(channel), 2), round(Decimal(8.70), 2))

    def test_average_ratings_8(self):
        channel = Channel.objects.get(title__exact='Drama')
        self.assertEqual(round(calcAvgRatings(channel), 2), round(Decimal(8.80), 2))

    def test_average_ratings_9(self):
        channel = Channel.objects.get(title__exact='TV Series')
        self.assertEqual(round(calcAvgRatings(channel), 2), round(Decimal(8.55), 2))
