import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import staff
from App.controllers import (
    create_staff,
    get_all_staffs_json,
    login,
    get_staff,
    get_staff_by_staffname,
    update_staff
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class staffUnitTests(unittest.TestCase):

    def test_new_staff(self):
        staff = staff("bob", "bobpass")
        assert staff.staffname == "bob"

    # pure function no side effects or integrations called
    def test_get_json(self):
        staff = staff("bob", "bobpass")
        staff_json = staff.get_json()
        self.assertDictEqual(staff_json, {"id":None, "staffname":"bob"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        staff = staff("bob", password)
        assert staff.password != password

    def test_check_password(self):
        password = "mypass"
        staff = staff("bob", password)
        assert staff.check_password(password)

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_authenticate():
    staff = create_staff("bob", "bobpass")
    assert login("bob", "bobpass") != None

class staffsIntegrationTests(unittest.TestCase):

    def test_create_staff(self):
        staff = create_staff("rick", "bobpass")
        assert staff.staffname == "rick"

    def test_get_all_staffs_json(self):
        staffs_json = get_all_staffs_json()
        self.assertListEqual([{"id":1, "staffname":"bob"}, {"id":2, "staffname":"rick"}], staffs_json)

    # Tests data changes in the database
    def test_update_staff(self):
        update_staff(1, "ronnie")
        staff = get_staff(1)
        assert staff.staffname == "ronnie"
        

