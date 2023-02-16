with open("file1.txt") as f:
    content_list=f.readlines()
content_list=[x.strip() for x in content_list]
print(content_list)