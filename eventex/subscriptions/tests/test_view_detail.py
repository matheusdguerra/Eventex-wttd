from importlib.resources import contents
from django.test import TestCase
import uuid
from django.shortcuts import resolve_url as r

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):

    def setUp(self):
        self.obj = Subscription.objects.create(name='Matheus Guerra',
                                               cpf='12345678901',
                                               email='matheusguerra@outlook.com',
                                               phone='51-99237-7111')
        self.resp = self.client.get(r('subscriptions:detail', self.obj.hashid))

    def teste_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        context = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for expected in context:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('{}{}/'.format(r('subscriptions:new'), uuid.uuid4()))
        self.assertEqual(404, resp.status_code)
