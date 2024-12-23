import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

def plotRunningAverage(array):
    numericArray = np.array(array).astype(int) * 100
    runningAverage = np.cumsum(numericArray) / np.arange(1, len(numericArray) + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(range(len(runningAverage)), runningAverage, '-', label='Running Average')

    margin = (runningAverage.max() - runningAverage.min()) * 0.15
    plt.ylim(runningAverage.min() - margin, runningAverage.max() + margin)
    plt.show()

if __name__ == "__main__":
    url = "https://www.rottentomatoes.com/m/a_complete_unknown"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    emsID = soup.find(lambda tag: tag.get("data-ems-id"))["data-ems-id"]

    baseURL = f"https://www.rottentomatoes.com/napi/movie/{emsID}/reviews/all"
    cursor = None
    reviews = []
    while True:
        if cursor:
            url = baseURL + f"?after={cursor}"
        else:
            url = baseURL
        print(url)
        r = requests.get(url).json()
        reviews.extend([review["isFresh"] for review in r["reviews"]])
        if r["pageInfo"]["hasNextPage"]:
            cursor = r["pageInfo"]["endCursor"]
        else:
            break


    plotRunningAverage(reviews)



