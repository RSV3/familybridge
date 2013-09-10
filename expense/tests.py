from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from datetime import date
from django.contrib.auth.models import Group
from core.models import EmailUser
# Create your tests here.

from expense.models import Expense, Contribution


class ExpenseTestCase(TestCase):

  def setUp(self):

    self.client = Client()

    # create users
    pam_johnson = EmailUser(email='pam.johnson@gmail.com', first_name='Pam', last_name='Johnson')
    pam_johnson.save()
    pam_johnson.set_password('hello')
    pam_johnson.save()
    sue_johnson = EmailUser(email='sue.johnson@gmail.com', first_name='Sue', last_name='Johnson')
    sue_johnson.save()
    sue_johnson.set_password('hello')
    sue_johnson.save()
    jason_johnson = EmailUser(email='jason.johnson@gmail.com', first_name='Jason', last_name='Johnson')
    jason_johnson.save()
    jason_johnson.set_password('hello')
    jason_johnson.save()

    g = Group(name='johnson_family')
    g.save()

    pam_johnson.groups.add(g)
    sue_johnson.member_groups.add(g)
    jason_johnson.member_groups.add(g)

    # create expenses by users
    # and add contributions 
    purchase_date = date(2013, 8, 5)
    cake = Expense(owner=pam_johnson, title='Cake', description='70th Birthday Cake', amount=50.00,
                  category=1, date=purchase_date, contribution_requested=True)
    cake.save()

    contrib = Contribution(contributor=jason_johnson, expense=cake, percentage=20, amount=cake.amount*0.20)
    contrib.save()

    purchase_date = date(2013, 8, 7)
    car_fix = Expense(owner=pam_johnson, title='Car Fix', description='Muffler had to be fixed',
                    amount=120.00, category=5, date=purchase_date)

    purchase_date = date(2013, 8, 16)
    grip_bars = Expense(owner=jason_johnson, title='Grip Bars', description="Mom's stairs updates", 
                  amount=89.99, category=4, date=purchase_date, contribution_requested=True)
    grip_bars.save()


    contrib = Contribution(contributor=pam_johnson, expense=grip_bars, percentage=30, amount=grip_bars.amount*0.30)
    contrib.save()
    contrib = Contribution(contributor=sue_johnson, expense=grip_bars, percentage=30, amount=grip_bars.amount*0.30)
    contrib.save()

    purchase_date = date(2013, 8, 17)
    june_lee_gift = Expense(owner=sue_johnson, title='June Lee Gift', 
                    description="Flowers for Ms. Lee for help", amount=35.35, category=3,
                    date=purchase_date, contribution_requested=True)
    june_lee_gift.save()

    contrib = Contribution(contributor=pam_johnson, expense=june_lee_gift, percentage=50, amount=june_lee_gift.amount*0.50)
    contrib.save()


  def runTest(self):
    pass


  def test_add_expenses(self):
    """
      Adding a single expense
    """

    self.assertEquals(EmailUser.objects.get(email='pam.johnson@gmail.com').email, 'pam.johnson@gmail.com')
    # login
    response = self.client.post(reverse('login'), {'username': 'pam.johnson@gmail.com',
                                                    'password': 'hello' })

    self.assertRedirects(response, reverse('core:home'))

    # add an expense with no receipt
    self.client.post(reverse('expense:add_expense'), {
        'date': '8/27/2013',
        'amount': 73.00,
        'title': 'Dinner with Mom',
        'description': 'Wednesday regular dinners',
        'category': 5,
    })

    # add an expense with receipt


    # add an expense with a contributor


    # add an expense with more than one contributor


  def test_add_multiple_expenses(self):

    # add multiple expenses with no receipts

    # add multiple expenses with receipts 


    # add multiple expenses with few receipts


    # add multiple expenses with split contributors


    # add multiple expenses in different categories


    pass


  def test_add_bank_card(self):

    pass


  def test_add_contributors(self):

    # add contributor

    # check email sends

    pass


  def test_contribute(self):

    # load contribute page 

    # click contribute
    pass

