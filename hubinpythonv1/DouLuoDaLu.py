import os
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}

# for i in range(1, 595):
#     for j in range(1, 20):
#         comicPicUrl = "http://mhpic.mh51.com/comic/D%2F%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%E6%8B%86%E5%88%86%E7%89%88%2F"+str(i)+"%E8%AF%9D%2F"+str(j)+".jpg-mht.middle"
#         html = requests.get(comicPicUrl)
#         if html.status_code == 200:
#             print("下载第"+str(i)+"话，第"+str(j)+"页。。。")
#             os.chdir("C:/Users/admin/Desktop/DouLuoDaLu")
#             comicTitle = str(i)+"-"+str(j)+".jpg"
#             with open(comicTitle, "wb") as f:
#                 f.write(html.content)
#         else:
#             break


