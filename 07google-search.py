from serpapi import GoogleSearch

api_key = input("Enter your SerpAPI key: ")  # Prompt for SerpAPI key

params = {
    "engine": "google",
    "q": "latest AI tools",
    "api_key": api_key
}

search = GoogleSearch(params)
results = search.get_dict()

for res in results.get("organic_results", []):
    print(res["title"])
    print(res["link"])
    print()
