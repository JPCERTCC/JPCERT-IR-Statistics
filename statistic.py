#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, csv

FPATH = os.path.dirname(os.path.abspath(__file__))

FILE_LIST = ["incident-reports.csv", "incident-cases-coordinated.csv", "phishing.csv", "web-defacement.csv",
             "malware.csv", "scan.csv", "dos.csv", "apt.csv", "other.csv"]

with open(os.path.join(FPATH, "template.html"), "r", encoding="utf-8") as f:
    HTML_DATA = f.read()


def main():
    data_dict = {}
    for file_name in FILE_LIST:
        with open(os.path.join(FPATH, file_name), "r") as f:
            line_data = []
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                try:
                    value_data = int(row[1])
                except:
                    value_data = row[1]

                line_dict = {'date': row[0], 'value': value_data}
                line_data.append(line_dict)
        data_dict[file_name] = line_data

    # create result page
    with open(os.path.join(FPATH, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML_DATA.format(**{"data_report": data_dict["incident-reports.csv"],
                                    "data_coordinate": data_dict["incident-cases-coordinated.csv"],
                                    "data_phishing": data_dict["phishing.csv"],
                                    "data_web": data_dict["web-defacement.csv"],
                                    "data_malware": data_dict["malware.csv"],
                                    "data_scan": data_dict["scan.csv"],
                                    "data_dos": data_dict["dos.csv"],
                                    "data_apt": data_dict["apt.csv"],
                                    "data_other": data_dict["other.csv"],
                                    }))


if __name__ == "__main__":
    main()