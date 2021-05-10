from django.test import TestCase

from .forms import *


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        CustomUser.objects.create(full_name='Sponge Bob', phone_no='1234567890', email='abc@xyz.com')

    def test_full_name_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('full_name').verbose_name
        self.assertEqual(field_label, 'full name')

    def test_phone_no_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('phone_no').verbose_name
        self.assertEqual(field_label, 'phone no')

    def test_full_name_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 100)


class SignUpFormTest(TestCase):
    def test_full_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['full_name'].label is None or form.fields['full_name'].label == 'full name')

    def test_full_name_field_help_text(self):
        form = SignUpForm()
        self.assertEqual(form.fields['full_name'].help_text, 'Required. 100 characters or fewer.')

    def test_email_field_validity(self):
        email = 'abcdefg'
        form = SignUpForm(data={'email': email})
        self.assertFalse(form.is_valid())

    def test_phone_no_max(self):
        phoneno = 'asiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvrrsdfssf'
        form = SignUpForm(data={'phone_no': phoneno})
        self.assertFalse(form.is_valid())


class ContactFormTest(TestCase):
    def test_name_field_label(self):
        form = ContactForm()
        self.assertTrue(form.fields['name'].label is None or form.fields['name'].label == 'Name')

    def test_name_field_max_length(self):
        form = ContactForm()
        self.assertEqual(form.fields['name'].max_length, 500)

    def test_messaage_field_validity(self):
        message = 'abcdefg'
        form = ContactForm(data={'message': message})
        self.assertFalse(form.is_valid())


class EditFormTest(TestCase):
    def test_full_name_field_label(self):
        form = EditForm()
        self.assertTrue(form.fields['full_name'].label is None or form.fields['full_name'].label == 'full name')

    def test_email_field_validity(self):
        email = 'abcdefg'
        form = EditForm(data={'email': email})
        self.assertFalse(form.is_valid())

    def test_phone_no_max(self):
        phoneno = 'asiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvasiuhasjjvrrsdfssf'
        form = EditForm(data={'phone_no': phoneno})
        self.assertFalse(form.is_valid())

    def test_email_field_help_text(self):
        form = EditForm()
        self.assertEqual(form.fields['email'].help_text, 'Required.')