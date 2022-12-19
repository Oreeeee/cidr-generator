import ipaddress
import argparse
import csv


START_IP = 0
END_IP = 1
TWO_LETTER_CODE = 2
FULL_COUNTRY_NAME = 3
REGION = 4
CITY = 5
ZIP_CODE = 8
TIMEZONE = 9


def range_to_cidr(start_ip, end_ip):
    return [ipaddr for ipaddr in ipaddress.summarize_address_range(start_ip, end_ip)]


def main():
    # Load IP2Location DB
    with open(args.ip2location_db, "r", newline="") as f:
        ip2location_db = list(csv.reader(f))

    # Generate CIDRs
    # TODO: Make this DRY
    cidr_list = []
    if args.two_letter_codes:
        for two_letter_code in args.two_letter_codes:
            for i in ip2location_db:
                if i[TWO_LETTER_CODE] == two_letter_code:
                    # Convert string IP numbers to IPv4 Objects
                    start_ip = ipaddress.ip_address(int(i[START_IP]))
                    end_ip = ipaddress.ip_address(int(i[END_IP]))

                    ipv4obj_cidrs = range_to_cidr(start_ip, end_ip)
                    for ipv4obj in ipv4obj_cidrs:
                        cidr_list.append(format(ipv4obj))

    if args.countries:
        for country in args.countries:
            for i in ip2location_db:
                if i[FULL_COUNTRY_NAME] == country:
                    # Convert string IP numbers to IPv4 Objects
                    start_ip = ipaddress.ip_address(int(i[START_IP]))
                    end_ip = ipaddress.ip_address(int(i[END_IP]))

                    ipv4obj_cidrs = range_to_cidr(start_ip, end_ip)
                    for ipv4obj in ipv4obj_cidrs:
                        cidr_list.append(format(ipv4obj))

    if args.regions:
        for region in args.regions:
            for i in ip2location_db:
                if i[REGION] == region:
                    # Convert string IP numbers to IPv4 Objects
                    start_ip = ipaddress.ip_address(int(i[START_IP]))
                    end_ip = ipaddress.ip_address(int(i[END_IP]))

                    ipv4obj_cidrs = range_to_cidr(start_ip, end_ip)
                    for ipv4obj in ipv4obj_cidrs:
                        cidr_list.append(format(ipv4obj))

    if args.cities:
        for city in args.cities:
            for i in ip2location_db:
                if i[CITY] == city:
                    # Convert string IP numbers to IPv4 Objects
                    start_ip = ipaddress.ip_address(int(i[START_IP]))
                    end_ip = ipaddress.ip_address(int(i[END_IP]))

                    ipv4obj_cidrs = range_to_cidr(start_ip, end_ip)
                    for ipv4obj in ipv4obj_cidrs:
                        cidr_list.append(format(ipv4obj))

    if args.zip_codes:
        for zip_code in args.zip_codes:
            for i in ip2location_db:
                if i[ZIP_CODE] == zip_code:
                    # Convert string IP numbers to IPv4 Objects
                    start_ip = ipaddress.ip_address(int(i[START_IP]))
                    end_ip = ipaddress.ip_address(int(i[END_IP]))

                    ipv4obj_cidrs = range_to_cidr(start_ip, end_ip)
                    for ipv4obj in ipv4obj_cidrs:
                        cidr_list.append(format(ipv4obj))

    if args.timezones:
        for timezone in args.timezones:
            for i in ip2location_db:
                if i[TIMEZONE] == timezone:
                    # Convert string IP numbers to IPv4 Objects
                    start_ip = ipaddress.ip_address(int(i[START_IP]))
                    end_ip = ipaddress.ip_address(int(i[END_IP]))

                    ipv4obj_cidrs = range_to_cidr(start_ip, end_ip)
                    for ipv4obj in ipv4obj_cidrs:
                        cidr_list.append(format(ipv4obj))

    # Remove dupes
    cidr_list = list(set(cidr_list))

    print(cidr_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--ip2location-db",
        dest="ip2location_db",
        help="Location to IP2Location CSV Database",
        required=True,
    )
    parser.add_argument(
        "--2-letter-codes",
        dest="two_letter_codes",
        help="2 Letter Code of the countries",
        nargs="+",
    )
    parser.add_argument(
        "--countries", dest="countries", help="List of countries", nargs="+"
    )
    parser.add_argument("--regions", dest="regions", help="List of Regions", nargs="+")
    parser.add_argument("--cities", dest="cities", help="List of Cities", nargs="+")
    parser.add_argument(
        "--zip-codes", dest="zip_codes", help="List of ZIP Codes", nargs="+"
    )
    parser.add_argument(
        "--timezones", dest="timezones", help="List of Timezones", nargs="+"
    )

    args = parser.parse_args()

    main()
