from app import app
import unittest
import json
from testRequestData import get, successful_post, unsuccessful_post, delete, search_district_like,\
    search_name_equals, update, bad_update

class FlaskTestCase(unittest.TestCase):
    client = app.test_client()

    # Checking that the api main endpoint is working
    def test_0_get(self):
        response = self.client.get(get['url'], content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_1_post_new_market(self):
        response = self.client.post(
            '/api/feira',
            data=successful_post['data'],
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 201)

    def test_2_get_by_id(self):
        response = self.client.get(get['url']+'/-9999', content_type='application/json')
        self.assertIsNotNone(response.data)

    def test_3_post_new_market_bad_request(self):
        response = self.client.post(
            '/api/feira',
            data=unsuccessful_post['data'],
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 400)

    def test_4_search_by_name_equals(self):
        response = self.client.get(
            search_name_equals['url'],
            follow_redirects=True
        )

        data = json.loads(response.data.decode()).get('objects')
        nome_feira = ''

        if data:
            nome_feira = data[0]['nome_feira']

        self.assertEqual(nome_feira, "VILA MEDEIROS")

    def test_5_search_by_district_like(self):
        response = self.client.get(
            search_district_like['url'],
            content_type='application/json',
            follow_redirects=True
        )
        data = json.loads(response.data.decode()).get('objects')
        district = ''

        if data:
            district = data[0]['district']

        self.assertIn(district, "MADALENA")

    def test_6_update(self):
        response = self.client.patch(
            update['url'],
            data=update['data'],
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_7_bad_update(self):
        response = self.client.patch(
            update['url'],
            data=bad_update['data'],
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 400)

    def test_8_delete_by_id(self):
        response = self.client.delete(
            delete['url'],
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
