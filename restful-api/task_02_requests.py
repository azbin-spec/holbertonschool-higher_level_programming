#!./venv/bin/python3
"""
Module containing functions fetching and printing or saving posts from JSONPlaceholder.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches and prints all post titles from JSONPlaceholder.
    """
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        obj = r.json()
        for item in obj:
            print(item["title"])


def fetch_and_save_posts():
    """
    Fetches and saves in CSV format all posts from JSONPlaceholder.
    """
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        obj = r.json()
        result = []
        for i in range(len(obj)):
            result.append({
                "id": obj[i]["id"],
                "title": obj[i]["title"],
                "body": obj[i]["body"].replace("\n", " ")
            })

        with open("posts.csv", "w", newline="") as f:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(result)
