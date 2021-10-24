import urllib.request

if __name__ == '__main__':
    LINKS = [
        'https://stackoverflow.com/',
        'https://www.w3schools.com/',
        'https://www.centos.org/',
        'https://www.bloomberg.com/',
        'https://www.geeksforgeeks.org/',
        'https://hackr.io/',
        'https://www.computerscience.org/',
        'https://www.agileventures.org/',
        'https://www.snhu.edu/',
        'https://cscircles.cemc.uwaterloo.ca/'
    ]

    for link in LINKS:
        html_res = urllib.request.urlopen(link)
        html_content = html_res.read()
        with open(f"serverfile/{link[8:-1]}.html", 'w') as writer:
            writer.write(html_content.decode())
