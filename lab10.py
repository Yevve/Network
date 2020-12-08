import re

#task1

#mtxt="jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."
#email = re.findall(r"\s\w+(?:\.\w+)*@\w+\.\w+",mtxt)
#print(email)

#task2

#htmltxt= """bla bla bla 
#<h1>My Rubric</h1>
#bla bla bla."""
#print(re.findall(r"<h1>\s*(.*?)\s*</h1>",htmltxt))

#task3
f=open("tabla.html",encoding="utf-8")
txt=f.read()
#print(txt)
serie=re.findall(r'''<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>\s*
<div class="svtJsStopPropagation">\s*
<div class="svtTablaTitleInfo svtHide-Js">\s*
<div class="svtTablaContent-Description">\s*
<p class="svtXMargin-Bottom-10px">\s*Amerikansk animerad komediserie från\s*\d+(?:\-*\d+)*. 
Säsong\s*(\d+)\.\s*Del\s*(\d+)\s*\w+\s*(\d+)\.\s*(.+?) Simpsons bor i Springfield.''', txt)

for i in range(len(serie)):
    print("Tid:      ",serie[i][0])
    print("Säsong:   ",serie[i][1])
    print("Avsnitt:  ",serie[i][2],"/",serie[i][3])
    print("Handling: ",serie[i][4],"\n")

