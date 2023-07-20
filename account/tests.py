from rest_framework.test import APITestCase, APIClient
from django.urls import reverse_lazy
from rest_framework import status


class RegisterAndProfileViewTest(APITestCase):

    register_view_url = reverse_lazy("register-view")
    profile_view_url = reverse_lazy("profile-view")
    change_password_view_url = reverse_lazy("change-password")
    login_view_url = reverse_lazy("token_obtain_pair")
    refresh_view_url = reverse_lazy("token_refresh")

    create_user_data = {
            "username": "some",
            "email": "some@gmail.com",
            "bio": "some bio",
            "password": "password123",
            "password2": "password123"
        }
    
    valid_update_user_data = {
        "username": "some-updated",
        "email": "some-updated@gmail.com",
        "bio": "some bio updated"
    }

    invalid_update_user_data = {
        "email": "some-updated@gmail.com",
        "bio": "some bio updated"
    }

    valid_change_password_data = {
        "current_password": "password123",
        "new_password": "updatepassword123",
        "new_password2": "updatepassword123"
    }

    invalid_change_password_data = {
        "current_password": "password1234",
        "new_password": "updatepassword1235",
        "new_password2": "updatepassword123"
    }
 

    def setUp(self):
        response = self.client.post(self.register_view_url, self.create_user_data, format="json")
        self.access_token = response.data["access"]
        self.refresh_token = response.data["refresh"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_valid_profile_get(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.get(self.profile_view_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_profile_get(self):
        response = self.client.get(self.profile_view_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_profile_put(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.put(self.profile_view_url, data=self.valid_update_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_profile_put(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.put(self.profile_view_url, data=self.invalid_update_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_invalid_profile_put(self):
        response = self.client.put(self.profile_view_url, data=self.valid_update_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_profile_patch(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.patch(self.profile_view_url, data=self.valid_update_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_profile_patch(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.patch(self.profile_view_url, data=self.invalid_update_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_invalid_profile_patch(self):
        response = self.client.patch(self.profile_view_url, data=self.valid_update_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)    

    def test_profile_delete(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.delete(self.profile_view_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_valid_change_password(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.put(self.change_password_view_url, data=self.valid_change_password_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_invalid_change_password(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.put(self.change_password_view_url, data=self.invalid_change_password_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
     
    def test_login(self):
        data = {"username": "some", "password": "password123"}  
        response = self.client.post(self.login_view_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)  

    def test_refresh(self):
        data = {"refresh": self.refresh_token}
        response = self.client.post(self.refresh_view_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
