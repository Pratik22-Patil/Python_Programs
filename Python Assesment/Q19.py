string = ["hello",""," ","world","","Python"]
for i in string:
    if not i.strip():
        continue
    print(i)