from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Wait time between tasks (in seconds)
    wait_time = between(1, 3)

    @task(1)
    def load_homepage(self):
        self.client.get("/")

    @task(2)
    def load_about_page(self):
        self.client.get("/about")

    @task(3)
    def submit_form(self):
        self.client.post("/submit", json={
            "name": "Arshia",
            "email": "test@example.com",
            "message": "This is a performance test example."
        })
