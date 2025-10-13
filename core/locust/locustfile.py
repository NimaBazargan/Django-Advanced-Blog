from locust import HttpUser, task

class QuickstartUSer(HttpUser):

    def on_start(self):
        response = self.client.post('/accounts/api/v1/jwt/create/',data={
        "email": "nima.kazemzadeh.bazargan@gmail.com",
        "password": "nimrimah"
        }).json()
        self.client.headers = {'Authorization': f'Bearer {response.get("access",None)}'}
    
    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/")

    @task
    def category_list(self):
        self.client.get("/blog/api/v1/category/")