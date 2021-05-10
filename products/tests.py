from django.test import TestCase
from .forms import *


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Products.objects.create(name='book1', description='sharbhrbhbh', category='Books/Notes', price=100)

    def test_name_label(self):
        product = Products.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        product = Products.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        product = Products.objects.get(id=1)
        max_length = product._meta.get_field('description').max_length
        self.assertEqual(max_length, 2083)


class WishlistModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Wishlist.objects.create(username='abcd', pid=1)

    def test_username_label(self):
        wishlist = Wishlist.objects.get(id=1)
        field_label = wishlist._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_pid_label(self):
        wishlist = Wishlist.objects.get(id=1)
        field_label = wishlist._meta.get_field('pid').verbose_name
        self.assertEqual(field_label, 'pid')

    def test_username_max_length(self):
        wishlist = Wishlist.objects.get(id=1)
        max_length = wishlist._meta.get_field('username').max_length
        self.assertEqual(max_length, 255)


class TransactionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Transaction.objects.create(buyer='abcd', seller='wxyz', pid=1, pname='pqr')

    def test_buyer_label(self):
        transaction = Transaction.objects.get(id=1)
        field_label = transaction._meta.get_field('buyer').verbose_name
        self.assertEqual(field_label, 'buyer')

    def test_pid_label(self):
        transaction = Transaction.objects.get(id=1)
        field_label = transaction._meta.get_field('pid').verbose_name
        self.assertEqual(field_label, 'pid')

    def test_buyer_max_length(self):
        transaction = Transaction.objects.get(id=1)
        max_length = transaction._meta.get_field('buyer').max_length
        self.assertEqual(max_length, 255)


class RequestModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Requests.objects.create(buyer='abcd', seller='wxyz', pid=1)

    def test_buyer_label(self):
        requests = Requests.objects.get(id=1)
        field_label = requests._meta.get_field('buyer').verbose_name
        self.assertEqual(field_label, 'buyer')

    def test_pid_label(self):
        requests = Requests.objects.get(id=1)
        field_label = requests._meta.get_field('pid').verbose_name
        self.assertEqual(field_label, 'pid')

    def test_buyer_max_length(self):
        requests = Requests.objects.get(id=1)
        max_length = requests._meta.get_field('buyer').max_length
        self.assertEqual(max_length, 255)


class ItemFormTest(TestCase):
    def test_name_field_label(self):
        form = Item()
        self.assertTrue(form.fields['name'].label is None or form.fields['name'].label == 'Product Title')

    def test_description_field_label(self):
        form = Item()
        self.assertTrue(form.fields['description'].label is None or form.fields['description'].label == 'Product Description')

    def test_sell_field_choices(self):
        form = Item()
        self.assertEqual(form.fields['sell'].choices, SELL_CHOICES)


class EditItemFormTest(TestCase):
    def test_name_field_label(self):
        form = Edit_Item()
        self.assertTrue(form.fields['name'].label is None or form.fields['name'].label == 'Edit Name')

    def test_description_field_label(self):
        form = Edit_Item()
        self.assertTrue(form.fields['description'].label is None or form.fields['description'].label == 'Edit Description')

    def test_sell_field_choices(self):
        form = Edit_Item()
        self.assertEqual(form.fields['sell'].choices, SELL_CHOICES)
