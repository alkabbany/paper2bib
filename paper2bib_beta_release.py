import requests
import time


def fetch_metadata_crossref(title):
    """
    Fetch metadata of a scientific article from CrossRef based on its title.
    """
    search_url = "https://api.crossref.org/works"
    params = {"query": title, "rows": 1}  # Fetch the top result
    headers = {"User-Agent": "Python Script (mailto:your_email@example.com)"}

    response = requests.get(search_url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch results for: {title}")
        return None

    data = response.json()

    # Check if any results were found
    if "message" not in data or "items" not in data["message"] or len(data["message"]["items"]) == 0:
        print(f"No results found for: {title}")
        return None

    return data["message"]["items"][0]  # Return the first result


def construct_bibtex(metadata):
    """
    Construct a BibTeX entry from CrossRef metadata.
    """
    if not metadata:
        return None

    # Extract metadata fields
    doi = metadata.get("DOI", "")
    title = metadata.get("title", [""])[0]
    author_list = metadata.get("author", [])
    authors = " and ".join(
        [
            f"{author.get('given', '')} {author.get('family', '')}".strip()
            for author in author_list
        ]
    )
    year = metadata.get("published-print", {}).get("date-parts", [[None]])[0][0] or metadata.get("published-online", {}).get("date-parts", [[None]])[0][0]
    journal = metadata.get("container-title", [""])[0]
    volume = metadata.get("volume", "")
    issue = metadata.get("issue", "")
    pages = metadata.get("page", "")

    # Generate BibTeX entry
    bibtex = f"@article{{{doi},\n"
    bibtex += f"  title = {{{title}}},\n"
    if authors:
        bibtex += f"  author = {{{authors}}},\n"
    if journal:
        bibtex += f"  journal = {{{journal}}},\n"
    if year:
        bibtex += f"  year = {{{year}}},\n"
    if volume:
        bibtex += f"  volume = {{{volume}}},\n"
    if issue:
        bibtex += f"  number = {{{issue}}},\n"
    if pages:
        bibtex += f"  pages = {{{pages}}},\n"
    if doi:
        bibtex += f"  doi = {{{doi}}},\n"
    bibtex += "}"
    return bibtex


def process_titles_file(file_path):
    """
    Process the titles in the given txt file, fetch metadata, and construct BibTeX records.
    """
    try:
        with open(file_path, "r") as file:
            titles = file.read().split(";")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    output_file = file_path.replace(".txt", ".bib")
    with open(output_file, "w") as bib_file:
        for title in titles:
            title = title.strip()
            if not title:
                continue

            print(f"Fetching metadata for: {title}")
            metadata = fetch_metadata_crossref(title)

            if metadata:
                bibtex_record = construct_bibtex(metadata)
                if bibtex_record:
                    bib_file.write(bibtex_record + "\n\n")
                else:
                    bib_file.write(f"% Failed to construct BibTeX for: {title}\n\n")
            else:
                bib_file.write(f"% Failed to fetch metadata for: {title}\n\n")

            # Respect API rate limits
            time.sleep(1)

    print(f"BibTeX records saved to: {output_file}")


if __name__ == "__main__":
    # Replace 'titles.txt' with the name of your input file
    input_file = "titles.txt"
    process_titles_file(input_file)