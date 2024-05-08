from locust import HttpUser, task, between
from bs4 import BeautifulSoup
class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def extract_csrf_token(self, response_text):
        soup = BeautifulSoup(response_text, "html.parser")
        csrf_token_input = soup.find("input", {"name": "csrf_token"})
        if csrf_token_input:
            return csrf_token_input["value"]
        return None

    def on_start(self):
        # Wywołaj GET na stronie zawierającej formularz, aby uzyskać token CSRF
        response = self.client.get("/posts")
        self.csrf_token = self.extract_csrf_token(response.text)
    @task
    def view_posts(self):
        self.client.get("/posts")

    @task
    def view_comments(self):
        self.client.get("/comments")

    @task
    def view_photos(self):
        self.client.get("/photos")

    @task
    def view_albums(self):
        self.client.get("/albums")

    @task
    def search_number(self):
        data = {
            "top": "100",
            "bottom": "50",
            "csrf_token": self.csrf_token  # Przekaż token CSRF w danych formularza
        }
        response = self.client.post("/posts", data=data)


