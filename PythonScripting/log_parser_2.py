#!/usr/bin/env python3

import csv
import collections
import sys

time_program_table = collections.OrderedDict()
all_programs = set()
in_name = sys.argv[1]
out_name = sys.argv[2]

with open(in_name, "r") as in_file:
    for row in in_file:
        fields = row.split(sep=" ", maxsplit=5)
        timestamp = " ".join(fields[:3])
        timestamp = timestamp[:timestamp.rfind(":")]
        program = fields[4][:fields[4].find("[")]

        if timestamp not in time_program_table :
            time_program_table[timestamp] = {}
            
        time_program_table[timestamp][program] = time_program_table[timestamp].setdefault(program, 0) + 1
              
        all_programs.add(program)
                
with open(out_name, "w+") as out_file:
    csvwriter = csv.writer(out_file, delimiter=',')
    csvwriter.writerow(["minute", "total_count"] + list(all_programs))
    for timestamp in time_program_table.keys():
        res = []
        for program in all_programs:
            if program in time_program_table[timestamp]:
                res.append(time_program_table[timestamp][program])
            else:
                res .append(0)
        csvwriter.writerow([timestamp, sum(res)] + res)