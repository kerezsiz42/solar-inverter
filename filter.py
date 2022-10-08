with open("filtered.txt", "w") as filtered:
    with open("output.txt", "r") as output:
        for line in output.readlines():
            if "01-03-20-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-92-7a" not in line:
                filtered.write(line)
                filtered.flush()
