import csv

with open('cleaned_response_data_4_13_17.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    row_num = 0
    results = {}
    for row in readCSV:
        row_num = row_num + 1
        if row_num == 1:
            print "HEaders: {}".format(row)
            headers = row
            next
        else:
            for i in range(len(headers)):
                if not results.has_key(headers[i]):
                    results[headers[i]] = []
                results[headers[i]].append(row[i] or None)

    print "Here are the first 5 responses for each question:"
    for question_id, response_values in results.iteritems():
        print "  {}: {}".format(question_id, response_values[0:5])
