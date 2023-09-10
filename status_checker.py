import requests

def check_http_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException:
        return "Error"

def read_urls_from_file(filename):
    with open(filename, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

def save_urls_with_200_status(urls, output_filename):
    with open(output_filename, 'w') as file:
        for url in urls:
            status = check_http_status(url)
            if status == 200:
                file.write(f"{url}\n")

def main():
    filename = input("Enter the name of the file containing URLs: ")
    output_filename = input("Enter the name of the output file: ")

    urls = read_urls_from_file(filename)
    save_urls_with_200_status(urls, output_filename)

if __name__ == "__main__":
    main()
