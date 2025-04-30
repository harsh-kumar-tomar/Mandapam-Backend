img_path = r"https://raw.githubusercontent.com/harsh-kumar-tomar/Mandapam-Images/main/img{}.jpg"
ls = []
for i in range(1,125):
    ls.append(img_path.format(i))
    
print(ls)
