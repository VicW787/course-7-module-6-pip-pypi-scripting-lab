import csv
import requests


def fetch_data(post_id=1):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}", timeout=10
    )
    if response.status_code == 200:
        return response.json()
    return {}


def write_csv(post, filename="post_output.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerow({k: post.get(k, "") for k in ["id", "title", "body"]})
    return filename


if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    if post:
        print(f"Saved to {write_csv(post)}")

