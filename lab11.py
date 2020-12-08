import sqlite3

conn=sqlite3.connect('mytest.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS people(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    firstName TEXT,
    lastName TEXT,
    UNIQUE (firstName,lastName)
)''')

c.execute('''CREATE TABLE IF NOT EXISTS scoreTable(
    personID INTEGER,
    task TEXT,
    score TEXT,
    FOREIGN KEY (personID) REFERENCES people(ID) ON DELETE CASCADE,
    UNIQUE(personID,task)
) ''')

with open("score2.txt","r") as f:
    for line in f.readlines():
        line=line.split()
        task = line[1]
        firstName = line[2]
        lastName = line[3]
        score = line[4]

        c.execute("INSERT OR IGNORE INTO people(firstName,lastName) VALUES(?,?)",[firstName,lastName])
        c.execute("INSERT OR IGNORE INTO scoreTable VALUES((SELECT ID FROM people WHERE firstName = ? AND lastName = ?),?,?)",[firstName,lastName,task,score])
#Top 10 best score
    #for i in c.execute("SELECT firstName,lastName,SUM(score) as s FROM people JOIN scoreTable on ID=personID GROUP BY firstName,lastName ORDER BY s DESC LIMIT 10"):
    #    print(i)
    #print("\n")
#Top 10 hard tasks
    #for i in c.execute("SELECT task,SUM(score) as s FROM scoreTable GROUP BY task ORDER BY s ASC limit 10"):
    #   print(i)
    #print("\n")

#People and score Print 
    for i in c.execute("SELECT * FROM people"):
        print(i)
    print("\n")

    #for i in c.execute("SELECT * FROM scoreTable"):
    #    print(i)
    #print("\n")


conn.commit()

conn.close()
