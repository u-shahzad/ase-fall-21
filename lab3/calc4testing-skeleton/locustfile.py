import time
from locust import HttpUser, task, between


# http://localhost:8089
class QuickstartUser(HttpUser):
    wait_time = between(1, 2) # 1-2 seconds between simulated events

    @task # defines a user task, asssociated to a microthread by locust
    def index_page(self):
        self.client.get("/") # get home page

    @task(3) # this task is 3 times likelier than the previous!
    def sum(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.client.get(f"/calc/sum?m={i}&n={j}", name="/calc/sum")
    
    @task(3)
    def divide(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.client.get(f"/calc/div?m={i}&n={j}", name="/calc/div")

    @task(3)
    def multiply(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.client.get(f"/calc/mul?m={i}&n={j}", name="/calc/mul")
    
    def on_start(self): # init for each virtual user
        pass