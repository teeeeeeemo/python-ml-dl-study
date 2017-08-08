import csv, codecs

with codecs.open("test.csv", "w", "euc_kr") as fp:
	writer = csv.writer(fp, delimiter=",", quotechar='"')
	writer.writerow(["ID", "이름", "가격"])
	writer.writerow(["1000", "아이폰", "100"])
	writer.writerow(["1001", "맥북", "1000"])
	writer.writerow(["1002", "아이맥", "10000"])
