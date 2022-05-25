from requests import get
import time
import csv


def main():
    domains_list = []
    with open("domains.txt", "r") as f:
        for line in f:
            domain_list = []
            domain = line.strip()
            try:
                json = get('http://ip-api.com/json/' + domain)
                data = json.json()
                print(data['query'], data['country'], data['city'], data['isp'], data['org'], data['as'])
                domain_list.append(domain)
                domain_list.append(data['query'])
                domain_list.append(data['country'])
                domain_list.append(data['city'])
                domain_list.append(data['isp'])
                domain_list.append(data['org'])
                domain_list.append(data['as'])
                domains_list.append(domain_list)
            except:
                print("Error:", domain)
            time.sleep(2)

    # Write domains_list to csv file
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    with open(f"domains_list_{timestamp}.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(domains_list)


if __name__ == '__main__':
    main()
